"""Converte as plantas validadas (ebook/plantas/projetos.py) em módulos para o motor 3D.

Para cada planta gera video/src/plantas/<ID>.js com o mesmo formato de video/src/planta.js,
já em coordenadas do mundo 3D: x espelhado (X = LARGURA - x, ver espelhar()), y igual (0 = frente)
(LARGURA, PROFUNDIDADE, ambientes, paredes com vãos de porta, janelas, portas) e mais
MOVEIS (posicionados pelas regras de projeto do X1-Plantas), ORDEM (sequência em que os cômodos ganham vida)
e META (nome, área, quartos, cotas).

Uso:
    python3 ferramentas/planta3d.py            todas as plantas
    python3 ferramentas/planta3d.py C01 E03    só estas
Depois: cd video && node render-planta.cjs --planta C01
"""
import json
import math
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ / "ferramentas"))
import plantas as PL  # noqa: E402

SAIDA = RAIZ / "video" / "src" / "plantas"
FECHADOS_NAO = PL.EXTERNOS | PL.SEMIEXTERNOS
PORTA = 0.8
PORTA_ENTRADA = 0.9
CORES_AMB = {"sala": "#E8D7BC", "estar": "#E8D7BC", "jantar": "#E8D7BC", "cozinha": "#D5E0CF",
             "dorm": "#EADCC6", "casal": "#EADCC6", "banho": "#D3E2E6", "lavabo": "#D3E2E6",
             "servico": "#D8E4D0", "circ": "#F1EBE0", "escritorio": "#E3DDF0", "varanda": "#DDD6CA",
             "garagem": "#CFCBC4", "patio": "#B9CFA0", "externo": "#B9CFA0", "deposito": "#E9E2D6"}
PISO = {"cozinha": "porcelanato", "banho": "porcelanato", "lavabo": "porcelanato", "servico": "porcelanato",
        "varanda": "cimento", "garagem": "cimento", "patio": "grama", "externo": "grama"}
R = lambda v: round(v, 3)


def fechado(c):
    return c["tipo"] not in FECHADOS_NAO and c["tipo"] != "futuro"


# ---------------------------------------------------------------- arestas e paredes
def arestas(c):
    """As 4 arestas de um cômodo: (lado, orientação, fixo, a, b)."""
    return [("frente", "h", c["y0"], c["x0"], c["x1"]), ("fundos", "h", c["y1"], c["x0"], c["x1"]),
            ("esq", "v", c["x0"], c["y0"], c["y1"]), ("dir", "v", c["x1"], c["y0"], c["y1"])]


def subtrair(intervalos, a, b):
    out = []
    for (p, q) in intervalos:
        if b <= p or a >= q:
            out.append((p, q))
            continue
        if a > p:
            out.append((p, a))
        if b < q:
            out.append((b, q))
    return [(p, q) for (p, q) in out if q - p > 0.005]


def unir(intervalos):
    out = []
    for p, q in sorted(intervalos):
        if out and p <= out[-1][1] + 1e-6:
            out[-1] = (out[-1][0], max(out[-1][1], q))
        else:
            out.append((p, q))
    return out


def trecho_livre(planta, c, lado):
    """Maior trecho contínuo da aresta 'lado' de c que dá para fora (ou para varanda/garagem/pátio)."""
    _, o, fixo, a, b = next(x for x in arestas(c) if x[0] == lado)
    d = {"frente": -0.05, "fundos": 0.05, "esq": -0.05, "dir": 0.05}[lado]
    pts = PL._passos(a, b, 0.05)
    livres = []
    for s in pts:
        x, y = (s, fixo + d) if o == "h" else (fixo + d, s)
        v = PL._dentro(planta, x, y, ignorar=(c["id"],))
        livres.append(v is None or not fechado(v))
    melhor, ini = (0, 0, 0), None
    passo = (b - a) / len(pts)
    for i, ok in enumerate(livres + [False]):
        if ok and ini is None:
            ini = i
        if not ok and ini is not None:
            if i - ini > melhor[0]:
                melhor = (i - ini, a + ini * passo, a + i * passo)
            ini = None
    return melhor[1], melhor[2]


def construir(planta):
    cs = planta["comodos"]
    por_id = {c["id"]: c for c in cs}
    # 1. Paredes: arestas de cômodos fechados, por linha (orientação, fixo) → intervalos unidos
    linhas = {}
    for c in cs:
        if not fechado(c):
            continue
        for (_, o, fixo, a, b) in arestas(c):
            linhas.setdefault((o, R(fixo)), []).append((a, b))
    for k in linhas:
        linhas[k] = unir(linhas[k])

    portas, vaos_por_comodo, vaos_ext = [], {}, {}

    def abrir(o, fixo, a, b):
        k = (o, R(fixo))
        if k in linhas:
            linhas[k] = subtrair(linhas[k], a, b)

    def registrar(cid, lado, a, b):
        vaos_por_comodo.setdefault(cid, []).append((lado, a, b))

    def lado_de(c, o, fixo):
        if o == "h":
            return "frente" if abs(c["y0"] - fixo) < 1e-6 else "fundos"
        return "esq" if abs(c["x0"] - fixo) < 1e-6 else "dir"

    def arco(o, fixo, a, larg, para_mais):
        """Dobradiça e ângulos (convenção de video/src/planta.js)."""
        if o == "h":
            return ({"x": R(a), "y": R(fixo), "r": larg, "a0": 0, "a1": math.pi / 2} if para_mais else
                    {"x": R(a + larg), "y": R(fixo), "r": larg, "a0": math.pi, "a1": 1.5 * math.pi})
        return ({"x": R(fixo), "y": R(a + larg), "r": larg, "a0": 1.5 * math.pi, "a1": 2 * math.pi} if para_mais else
                {"x": R(fixo), "y": R(a), "r": larg, "a0": math.pi / 2, "a1": math.pi})

    for porta in planta.get("portas", []):
        a_id, b_id = porta[0], porta[1]
        if a_id == "ext":
            c = por_id[b_id]
            lado = porta[2]
            _, o, fixo, ia, ib = next(x for x in arestas(c) if x[0] == lado)
            la, lb = trecho_livre(planta, c, lado)
            if lb - la < PORTA_ENTRADA:
                la, lb = ia, ib
            # Com janela no mesmo lado, a porta vai para perto do canto (sobra parede para a janela), como se faz em obra
            tem_janela = any(l == lado for (l, _) in planta.get("janelas", {}).get(b_id, []))
            padrao = la + PORTA_ENTRADA / 2 + 0.15 if tem_janela and lb - la > 2.4 else (la + lb) / 2
            centro = porta[3] if len(porta) > 3 else padrao
            centro = min(max(centro, la + PORTA_ENTRADA / 2 + 0.05), lb - PORTA_ENTRADA / 2 - 0.05)
            a, b = centro - PORTA_ENTRADA / 2, centro + PORTA_ENTRADA / 2
            if lado == "frente":
                planta["_entrada_x"] = centro  # o caminho do jardim chega aqui (varanda aberta não tem folha de porta)
            if fechado(c):
                abrir(o, fixo, a, b)
                para_mais = lado in ("frente", "esq")
                portas.append({"id": f"ext-{b_id}", **arco(o, fixo, a, PORTA_ENTRADA, para_mais)})
            registrar(b_id, lado, a, b)
            vaos_ext[(b_id, lado)] = (o, fixo, a, b)
            continue
        ca, cb = por_id[a_id], por_id[b_id]
        pc = PL.parede_comum(ca, cb)
        if not pc:
            continue
        o, fixo, i0, i1 = pc
        aberta = len(porta) > 2 and porta[2] == "aberto"
        if aberta:
            a, b = i0 + 0.08, i1 - 0.08
        else:
            centro = (i0 + i1) / 2
            # porta perto de um canto, como se faz em obra (sobra parede para móvel)
            centro = max(i0 + PORTA / 2 + 0.12, min(centro, i0 + PORTA / 2 + 0.25)) if i1 - i0 > 2.0 else centro
            a, b = centro - PORTA / 2, centro + PORTA / 2
        abrir(o, fixo, a, b)
        registrar(a_id, lado_de(ca, o, fixo), a, b)
        registrar(b_id, lado_de(cb, o, fixo), a, b)
        if not aberta and (fechado(ca) or fechado(cb)):
            # a folha abre para dentro do cômodo mais privado (b)
            para_mais = (cb["y0"] >= fixo - 1e-6) if o == "h" else (cb["x0"] >= fixo - 1e-6)
            portas.append({"id": f"{a_id}-{b_id}", **arco(o, fixo, a, PORTA, para_mais)})

    # 2. Janelas: no maior trecho livre do lado, centradas
    janelas = []
    jan_por_comodo = {}
    for cid, lista in planta.get("janelas", {}).items():
        c = por_id[cid]
        for (lado, larg) in lista:
            _, o, fixo, ia, ib = next(x for x in arestas(c) if x[0] == lado)
            la, lb = trecho_livre(planta, c, lado)
            # evita o vão da porta no mesmo lado
            vaos = [(a, b) for (l, a, b) in vaos_por_comodo.get(cid, []) if l == lado]
            livres = [(la, lb)]
            for (a, b) in vaos:
                livres = subtrair(livres, a - 0.1, b + 0.1)
            livres = sorted(livres, key=lambda t: -(t[1] - t[0]))
            if livres and livres[0][1] - livres[0][0] >= larg:
                la, lb = livres[0]
            m = (la + lb) / 2
            a, b = m - larg / 2, m + larg / 2
            tipo = c["tipo"]
            peitoril = 1.6 if tipo in ("banho", "lavabo") else (1.1 if tipo in ("cozinha", "servico") else 1.0)
            seg = [R(a), R(fixo), R(b), R(fixo)] if o == "h" else [R(fixo), R(a), R(fixo), R(b)]
            janelas.append({"seg": seg, "peitoril": peitoril, "verga": 2.2, "id": cid})
            jan_por_comodo.setdefault(cid, []).append((lado, a, b))
    # 2b. Veneziana em cima da porta de fora (F(..., veneziana_sobre_porta=lado)): no vão da porta, da verga dela até o topo
    # de PL.VENEZIANA_PORTA. Fica acima do corte da planta (1,1 m): o 3D cortado não a mostra; a planta 2D a desenha tracejada.
    for c in cs:
        vao = vaos_ext.get((c["id"], c.get("veneziana_sobre_porta")))
        if vao:
            o, fixo, a, b = vao
            m, meia = (a + b) / 2, PL.VENEZIANA_PORTA["largura"] / 2
            seg = [R(m - meia), R(fixo), R(m + meia), R(fixo)] if o == "h" else [R(fixo), R(m - meia), R(fixo), R(m + meia)]
            janelas.append({"seg": seg, "peitoril": PL.VENEZIANA_PORTA["base"], "verga": PL.VENEZIANA_PORTA["topo"],
                            "id": c["id"], "tipo": "veneziana"})

    paredes = []
    for (o, fixo), ivs in sorted(linhas.items()):
        for (a, b) in ivs:
            if b - a < 0.02:
                continue
            paredes.append([R(a), fixo, R(b), fixo] if o == "h" else [fixo, R(a), fixo, R(b)])

    moveis = mobiliar(planta, vaos_por_comodo, jan_por_comodo, paredes, portas)
    return paredes, janelas, portas, moveis


# ---------------------------------------------------------------- móveis
OPOSTO = {"frente": "fundos", "fundos": "frente", "esq": "dir", "dir": "esq"}
ROT = {"frente": 0.0, "fundos": math.pi, "esq": math.pi / 2, "dir": -math.pi / 2}


def _livre_no_lado(c, lado, vaos, w, margem=0.05, perto_passagem=False, ocupados=(), prof=None, no_canto=False):
    """Posição central (ao longo do lado) onde cabe uma peça de largura w sem bloquear porta nem outro móvel.

    Com prof (profundidade da peça), a porta de um lado perpendicular só tira lugar se o vão dela
    começar dentro da faixa que a peça ocupa junto da parede; sem prof, vale a regra antiga (0,95 m do canto)."""
    _, o, fixo, a, b = next(x for x in arestas(c) if x[0] == lado)
    livres = [(a + margem, b - margem)]
    for (oa, ob) in ocupados:
        livres = subtrair(livres, oa - 0.03, ob + 0.03)
    perto_canto = 0.95
    for (l, va, vb) in vaos:
        if l == lado:
            livres = subtrair(livres, va - 0.1, vb + 0.1)
        elif l != OPOSTO[lado]:
            # porta num lado perpendicular, perto do canto com este lado: a peça não pode ficar na frente dela
            canto = c["y0"] if lado == "frente" else c["y1"] if lado == "fundos" else c["x0"] if lado == "esq" else c["x1"]
            if prof is not None:
                faixa = (canto, canto + prof + 0.1) if lado in ("frente", "esq") else (canto - prof - 0.1, canto)
                bate = va < faixa[1] and vb > faixa[0]
            else:
                bate = min(abs(va - canto), abs(vb - canto)) < perto_canto
            if bate:
                ponta = c["x0"] if l == "esq" else c["x1"] if l == "dir" else c["y0"] if l == "frente" else c["y1"]
                # só o sofá pode chegar a 0,5 m de uma passagem aberta larga (ela não tem folha de porta)
                folga = 0.5 if perto_passagem and vb - va > 1.2 else (PORTA + 0.05 if prof is not None else 0.95)  # raio da folha da porta
                livres = subtrair(livres, ponta - folga, ponta + folga)
    cabe = [(p, q) for (p, q) in livres if q - p >= w]
    if not cabe:
        return None
    p, q = max(cabe, key=lambda t: t[1] - t[0])
    return p + w / 2 if no_canto else (p + q) / 2  # no canto: sobra o resto da parede para a peça seguinte


def _no_lado(c, lado, pos, d, folga=0.0):
    """Coordenadas (x, y) do centro de uma peça de profundidade d encostada no lado."""
    if lado == "frente":
        return pos, c["y0"] + d / 2 + folga
    if lado == "fundos":
        return pos, c["y1"] - d / 2 - folga
    if lado == "esq":
        return c["x0"] + d / 2 + folga, pos
    return c["x1"] - d / 2 - folga, pos




def _comp(c, lado):
    return (c["x1"] - c["x0"]) if lado in ("frente", "fundos") else (c["y1"] - c["y0"])


def _prof(c, lado):
    return (c["y1"] - c["y0"]) if lado in ("frente", "fundos") else (c["x1"] - c["x0"])


PEGADA = {"criado": (0.45, 0.4), "vaso": (0.4, 0.65), "cadeira": (0.45, 0.5)}
ESP_EXT, ESP_INT = PL.PAREDE_EXT, PL.PAREDE_INT  # as paredes do validador: externa de 15 cm para dentro, interna de 12 no eixo
FACE = ESP_EXT / 2  # o motor 3D desenha a parede externa com o eixo 7,5 cm para dentro da face de fora (paredes_reais)
CADEIRA_ZONA = (0.6, 0.75)  # largura x fundo livres na frente da escrivaninha para a cadeira e quem senta (Anexo G: 0,75 m da borda da mesa)


def recuado(c, paredes, planta=None):
    """O cômodo até a face de dentro das paredes de verdade: 15 cm na externa, 6 cm de cada lado da interna (PL._desconto).

    Até 24/11/2026 o motor 3D desenhava a parede externa sobre o eixo e o móvel parava a 7,5 cm do eixo, dentro da parede
    de verdade. Agora a parede do 3D (paredes_reais) e o móvel param na mesma face, a do validador (Arquiteto, 24/11/2026)."""
    r = dict(c)
    for lado, o, fixo, a, b in arestas(c):
        tem = any((p[1] == p[3]) == (o == "h") and abs((p[1] if o == "h" else p[0]) - fixo) < 1e-6
                  and min(max(p[0], p[2]) if o == "h" else max(p[1], p[3]), b) - max(min(p[0], p[2]) if o == "h" else min(p[1], p[3]), a) > 0.01
                  for p in paredes)
        if tem:
            k = {"frente": "y0", "fundos": "y1", "esq": "x0", "dir": "x1"}[lado]
            d = PL._desconto(planta, c, lado) if planta else FACE
            r[k] = c[k] + (d if lado in ("frente", "esq") else -d)
    return r


# ---------------------------------------------------------------- paredes de verdade (as do validador) para o desenho 3D
def _classe(planta, o, fixo, s):
    """Que parede é esta no ponto s da linha: +1/-1 externa (o cômodo fechado fica do lado de mais/de menos), 0 interna."""
    pts = [(s, fixo - 0.05), (s, fixo + 0.05)] if o == "h" else [(fixo - 0.05, s), (fixo + 0.05, s)]
    menos, mais = ((v := PL._dentro(planta, x, y)) is not None and fechado(v) for x, y in pts)
    return 0 if menos and mais else 1 if mais else -1 if menos else None


def paredes_reais(planta, paredes):
    """As paredes do eixo (construir) na posição de verdade: [(o, fixo_real, ini, fim, esp, classe, fixo_eixo)].

    Externa: 15 cm para dentro da face de fora (o eixo do desenho vai 7,5 cm para dentro); interna: 12 cm sobre o eixo.
    ini e fim são as pontas de verdade: no canto e no T a parede vai até a face de fora da parede que ela encontra; no vão de
    porta e na ponta solta, para no vão. Uma linha com trecho externo e trecho interno vira duas peças."""
    cortes = {"h": sorted({c[k] for c in planta["comodos"] for k in ("x0", "x1")}),
              "v": sorted({c[k] for c in planta["comodos"] for k in ("y0", "y1")})}
    pecas = []
    for p in paredes:
        o = "h" if p[1] == p[3] else "v"
        fixo = p[1] if o == "h" else p[0]
        a, b = (min(p[0], p[2]), max(p[0], p[2])) if o == "h" else (min(p[1], p[3]), max(p[1], p[3]))
        pts = [a] + [s for s in cortes[o] if a + 1e-6 < s < b - 1e-6] + [b]
        trechos = []
        for s0, s1 in zip(pts, pts[1:]):
            k = _classe(planta, o, fixo, (s0 + s1) / 2)
            if trechos and trechos[-1][2] == k:
                trechos[-1][1] = s1
            else:
                trechos.append([s0, s1, k])
        for i, (s0, s1, k) in enumerate(trechos):
            if k is None:
                continue
            esp = ESP_EXT if k else ESP_INT
            pecas.append({"o": o, "eixo": fixo, "fixo": fixo + k * FACE, "esp": esp, "classe": k, "a": s0, "b": s1,
                          "corte_a": i > 0, "corte_b": i < len(trechos) - 1})
    for q in pecas:
        corpo = (q["fixo"] - q["esp"] / 2, q["fixo"] + q["esp"] / 2)
        for ponta, sinal in (("a", -1), ("b", 1)):
            e = q[ponta]
            if q["corte_" + ponta]:  # a linha muda de externa para interna aqui: a externa avança a espessura dela
                if q["classe"]:
                    q[ponta] = e + sinal * ESP_EXT
                continue
            achadas = [r for r in pecas if r["o"] != q["o"] and abs(r["eixo"] - e) < 1e-6 and r["a"] - 1e-6 <= q["eixo"] <= r["b"] + 1e-6]
            if not achadas:
                continue  # vão de porta ou ponta solta: a parede para aí
            sobra = lambda r: min(corpo[1], r["b"] + (ESP_EXT if r["corte_b"] and r["classe"] else 0)) - max(corpo[0], r["a"] - (ESP_EXT if r["corte_a"] and r["classe"] else 0))
            r = max(achadas, key=sobra)
            q[ponta] = r["fixo"] + sinal * r["esp"] / 2  # até a face de fora da parede encontrada
    return [(q["o"], q["fixo"], q["a"], q["b"], q["esp"], q["classe"], q["eixo"]) for q in pecas]


def desloca(reais, o, eixo, s):
    """Quanto o eixo do desenho anda (para dentro da casa) no ponto s da parede de eixo (o, eixo): 0 na interna."""
    for (o2, fixo, a, b, esp, k, e2) in reais:
        if o2 == o and abs(e2 - eixo) < 1e-6 and a - 1e-6 <= s <= b + 1e-6:
            return fixo - e2
    return 0.0


def para_desenho(planta, paredes, janelas, portas):
    """Paredes, janelas e portas na posição de verdade, no formato de video/src/planta.js (antes de espelhar).

    Parede: [x0, y0, x1, y1, esp], com as pontas recolhidas ESPESSURA/2 (o motor e a vista da rua somam ESPESSURA/2 em
    cada ponta); a janela e a dobradiça da porta externa vão com a parede, 7,5 cm para dentro."""
    reais = paredes_reais(planta, paredes)
    caixa = lambda q: (q[2], q[1] - q[4] / 2, q[3], q[1] + q[4] / 2) if q[0] == "h" else (q[1] - q[4] / 2, q[2], q[1] + q[4] / 2, q[3])
    contida = lambda q: any(r is not q and all(abs(u - v) < 1e-6 or (u > v if i < 2 else u < v)
                                               for i, (u, v) in enumerate(zip(caixa(q), caixa(r)))) for r in reais)
    out = []
    for q in reais:
        o, fixo, a, b, esp = q[:5]
        if b - a < ESP_EXT and contida(q):
            continue  # toquinho de parede (ao lado de uma passagem) que já está dentro da parede do canto
        a2, b2 = a + ESP_EXT / 2, b - ESP_EXT / 2
        if b2 < a2:  # parede mais curta que 15 cm: fica com o comprimento de verdade em volta do meio
            a2 = b2 = (a + b) / 2
        out.append([R(a2), R(fixo), R(b2), R(fixo), esp] if o == "h" else [R(fixo), R(a2), R(fixo), R(b2), esp])
    jan = []
    for j in janelas:
        x0, y0, x1, y1 = j["seg"]
        if y0 == y1:
            dy = desloca(reais, "h", y0, (x0 + x1) / 2)
            jan.append({**j, "seg": [x0, R(y0 + dy), x1, R(y1 + dy)]})
        else:
            dx = desloca(reais, "v", x0, (y0 + y1) / 2)
            jan.append({**j, "seg": [R(x0 + dx), y0, R(x1 + dx), y1]})
    por = []
    for d in portas:
        horiz = abs(math.sin(d["a0"])) < 1e-6
        ponta = d["x"] + d["r"] * math.cos(d["a0"]) if horiz else d["y"] + d["r"] * math.sin(d["a0"])
        # o meio da porta cai no vão, onde não há parede: o deslocamento vem da parede que encosta numa das pontas do vão
        # (até 24/11/2026 media no meio, dava 0 e a porta externa ficava na face de fora; Designer, 24/11/2026)
        o, fixo, dob = ("h", d["y"], d["x"]) if horiz else ("v", d["x"], d["y"])
        dd = next((v for v in (desloca(reais, o, fixo, s) for s in (dob, ponta)) if v), 0.0)
        por.append({**d, "y": R(d["y"] + dd)} if horiz else {**d, "x": R(d["x"] + dd)})
    return out, jan, por


def cadeira_de(m):
    """A cadeira da escrivaninha, na frente dela (onde o motor 3D a desenhava até 23/11/2026, agora móvel próprio)."""
    sx, sy = math.sin(m.get("rot", 0.0)), math.cos(m.get("rot", 0.0))
    k = m["d"] / 2 + 0.25
    return {"tipo": "cadeira", "x": m["x"] + sx * k, "y": m["y"] + sy * k, "rot": m.get("rot", 0.0)}


def zona_da_cadeira(m):
    """Retângulo livre na frente da escrivaninha: a cadeira e o espaço de puxá-la (CADEIRA_ZONA)."""
    zw, zd = CADEIRA_ZONA
    sx, sy = math.sin(m.get("rot", 0.0)), math.cos(m.get("rot", 0.0))
    k = m["d"] / 2 + zd / 2
    cx, cy = m["x"] + sx * k, m["y"] + sy * k
    w, d = (zw, zd) if abs(sx) < 0.5 else (zd, zw)
    return (cx - w / 2, cy - d / 2, cx + w / 2, cy + d / 2)
NAO_COLIDE = ("tapete",)  # o tapete fica embaixo do sofá e da mesinha


def pegada(m):
    """Retângulo (x0, y0, x1, y1) que o móvel ocupa no chão; a mesa de jantar conta as cadeiras."""
    if m["tipo"] == "planta":
        w = d = 0.5 * m.get("s", 1)
    else:
        w, d = PEGADA.get(m["tipo"], (m.get("w", 0.4), m.get("d", 0.4)))
    if m["tipo"] == "mesaJantar":
        w += 0.9  # duas cadeiras de cada lado, 0,45 m para fora do tampo
    if abs(abs(m.get("rot", 0.0)) - math.pi / 2) < 1e-3:
        w, d = d, w
    return (m["x"] - w / 2, m["y"] - d / 2, m["x"] + w / 2, m["y"] + d / 2)


def sobrepoe(r1, r2, folga=0.0):
    return r1[0] < r2[2] + folga and r2[0] < r1[2] + folga and r1[1] < r2[3] + folga and r2[1] < r1[3] + folga


def sobrepostos(moveis):
    """Pares de móveis do mesmo cômodo que ocupam o mesmo chão (o tapete não conta). Lista vazia = tudo certo."""
    out = []
    for i, a in enumerate(moveis):
        for b in moveis[i + 1:]:
            if a["amb"] == b["amb"] and a["tipo"] not in NAO_COLIDE and b["tipo"] not in NAO_COLIDE \
                    and sobrepoe(pegada(a), pegada(b), -0.02):
                out.append((a["amb"], a["tipo"], b["tipo"]))
    return out


def moveis_na_parede(planta, tol=0.005):
    """Móveis que entram numa parede de verdade (a do desenho 3D, paredes_reais) mais que tol: [(amb, tipo, 'externa'|'interna', cm)].

    Desde 24/11/2026 a parede do 3D e a do validador são a mesma (externa de 15 cm para dentro, interna de 12 no eixo):
    móvel encostado para na face e a tolerância caiu de 2 cm para meio centímetro."""
    paredes, _, _, moveis = construir(planta)
    out = []
    for (o, fixo, a, b, esp, k, _) in paredes_reais(planta, paredes):
        caixa = (a, fixo - esp / 2, b, fixo + esp / 2) if o == "h" else (fixo - esp / 2, a, fixo + esp / 2, b)
        for m in moveis:
            r = pegada(m)
            dx, dy = min(r[2], caixa[2]) - max(r[0], caixa[0]), min(r[3], caixa[3]) - max(r[1], caixa[1])
            if dx > tol and dy > tol:
                out.append((m["amb"], m["tipo"], "externa" if k else "interna", round(100 * min(dx, dy))))
    return out


def cadeiras_sem_lugar(planta):
    """Cadeira de escrivaninha em cima de cama ou de outro móvel: [(amb, tipo de baixo)]. Lista vazia = tudo certo."""
    moveis = construir(planta)[3]
    out = []
    for c in (m for m in moveis if m["tipo"] == "cadeira"):
        for o in moveis:
            if o is not c and o["amb"] == c["amb"] and o["tipo"] not in NAO_COLIDE + ("escrivaninha",) and sobrepoe(pegada(c), pegada(o)):
                out.append((c["amb"], o["tipo"]))
    return out


ALTOS = ("geladeira", "armario", "estante")  # móvel que passa do peitoril: na frente da janela, tapa luz e ventilação
FRENTE_JANELA = 0.5  # faixa na frente da janela, a partir da face de dentro da parede, que móvel alto não pode ocupar
CADEIRA_PAREDE = 0.45  # da borda da mesa de jantar até a parede de verdade, para a cadeira e quem senta (Arquiteto, 24/11/2026)


def zonas_de_janela(janelas, cid):
    """Faixa de FRENTE_JANELA na frente de cada janela do cômodo (retângulos no chão, a partir da face do 3D)."""
    out = []
    for j in janelas:
        if j["id"] != cid:
            continue
        x0, y0, x1, y1 = j["seg"]
        out.append((j, min(x0, x1), y0, max(x0, x1), y0) if y0 == y1 else (j, x0, min(y0, y1), x0, max(y0, y1)))
    return out


def altos_na_janela(planta):
    """Geladeira, guarda-roupa ou estante na frente de janela: [(amb, tipo, cm na frente)]. Lista vazia = tudo certo."""
    _, janelas, _, moveis = construir(planta)
    por_id = {c["id"]: c for c in planta["comodos"]}
    out = []
    for m in (m for m in moveis if m["tipo"] in ALTOS):
        r = pegada(m)
        c = por_id[m["amb"]]
        for j, a0, b0, a1, b1 in zonas_de_janela(janelas, m["amb"]):
            if b0 == b1:  # janela na frente ou no fundo do cômodo (a faixa sai da face de verdade da parede)
                fundo = b0 + (PL._desconto(planta, c, "frente") if abs(b0 - c["y0"]) < 1e-6 else -PL._desconto(planta, c, "fundos"))
                z = (a0, fundo, a1, fundo + FRENTE_JANELA) if abs(b0 - c["y0"]) < 1e-6 else (a0, fundo - FRENTE_JANELA, a1, fundo)
                lap = min(r[2], z[2]) - max(r[0], z[0])
            else:
                fundo = a0 + (PL._desconto(planta, c, "esq") if abs(a0 - c["x0"]) < 1e-6 else -PL._desconto(planta, c, "dir"))
                z = (fundo, b0, fundo + FRENTE_JANELA, b1) if abs(a0 - c["x0"]) < 1e-6 else (fundo - FRENTE_JANELA, b0, fundo, b1)
                lap = min(r[3], z[3]) - max(r[1], z[1])
            if sobrepoe(r, z, -0.02):
                out.append((m["amb"], m["tipo"], round(100 * lap)))
    return out


def cadeiras_apertadas(planta, minimo=CADEIRA_PAREDE):
    """Mesa de jantar com cadeira a menos de 'minimo' da parede de verdade (15 cm externa, 6 cm de cada lado da interna).

    As cadeiras ficam nos dois lados compridos da mesa (pegada: +0,45 m de cada lado). [(amb, cm)]. Vazia = tudo certo."""
    moveis = construir(planta)[3]
    por_id = {c["id"]: c for c in planta["comodos"]}
    out = []
    for m in (m for m in moveis if m["tipo"] == "mesaJantar"):
        c = por_id[m["amb"]]
        faces = {"esq": c["x0"] + PL._desconto(planta, c, "esq"), "dir": c["x1"] - PL._desconto(planta, c, "dir"),
                 "frente": c["y0"] + PL._desconto(planta, c, "frente"), "fundos": c["y1"] - PL._desconto(planta, c, "fundos")}
        deitada = abs(abs(m.get("rot", 0.0)) - math.pi / 2) < 1e-3
        meia = m.get("w", 0.8) / 2  # metade do tampo no sentido das cadeiras
        if deitada:  # cadeiras para a frente e para o fundo
            folgas = (m["y"] - meia - faces["frente"], faces["fundos"] - (m["y"] + meia))
        else:  # cadeiras para a esquerda e para a direita
            folgas = (m["x"] - meia - faces["esq"], faces["dir"] - (m["x"] + meia))
        for f in folgas:
            if f < minimo - 0.005:
                out.append((m["amb"], round(100 * f)))
    return out


FRENTE_ARMARIO = 0.6  # livre na frente do guarda-roupa de porta de abrir: a folha (33 a 40 cm) abre e a pessoa fica na frente (24/11/2026)
FIXOS = ("tanque", "pia", "vaso", "bancada", "box", "maquina")  # o que não sai do lugar (água, esgoto, obra): a porta não pode bater


def armarios_sem_frente(planta, minimo=FRENTE_ARMARIO):
    """Guarda-roupa com menos de 'minimo' livres na frente, até a parede de verdade ou o primeiro móvel: [(amb, cm)].

    Achado do levantamento das 3 casas (24/11/2026): na C01 a cama ficava a 10 cm da frente do guarda-roupa."""
    paredes, _, _, moveis = construir(planta)
    por_id = {c["id"]: c for c in planta["comodos"]}
    out = []
    for m in (m for m in moveis if m["tipo"] == "armario"):
        c = recuado(por_id[m["amb"]], paredes, planta)
        r = pegada(m)
        sx, sy = round(math.sin(m.get("rot", 0.0))), round(math.cos(m.get("rot", 0.0)))  # para onde as portas abrem
        k = 0 if sx else 1  # eixo da frente: 0 = x, 1 = y
        sinal = sx or sy
        face = r[2 + k] if sinal > 0 else r[k]
        livre = (c["x1" if k == 0 else "y1"] - face) if sinal > 0 else (face - c["x0" if k == 0 else "y0"])
        for o in moveis:
            if o is m or o["amb"] != m["amb"] or o["tipo"] in NAO_COLIDE:
                continue
            q = pegada(o)
            j = 1 - k  # o eixo ao longo das portas
            lap = min(r[2 + j], q[2 + j]) - max(r[j], q[j])
            if lap <= 0.005:
                continue  # fora da faixa das portas
            perto, longe = (q[k], q[2 + k]) if sinal > 0 else (-q[2 + k], -q[k])
            f = face if sinal > 0 else -face
            if longe > f + 0.005:
                livre = min(livre, max(0.0, perto - f))
        if livre < minimo - 0.005:
            out.append((m["amb"], round(100 * livre)))
    return out


def giros_de_porta(planta, portas=None):
    """A folha de cada porta como no e-book (PL.porta_dobradica), com a dobradiça na face da parede do lado em que abre.

    [(id, cômodo, (hx, hy), raio, u, v)]: u aponta para onde a folha aberta fica, v para a folha fechada (ao longo da parede)."""
    if portas is None:
        portas = construir(planta)[2]
    out = []
    for d in portas:
        H, P, A = PL.porta_dobradica(planta, d)
        r = d["r"]
        u = (round((A[0] - H[0]) / r), round((A[1] - H[1]) / r))
        v = (round((P[0] - H[0]) / r), round((P[1] - H[1]) / r))
        c = PL._dentro(planta, H[0] + 0.3 * u[0] + 0.4 * v[0], H[1] + 0.3 * u[1] + 0.4 * v[1])
        if c is None:
            continue
        lado = {(0, 1): "frente", (0, -1): "fundos", (1, 0): "esq", (-1, 0): "dir"}[u]
        e = PL._desconto(planta, c, lado)
        out.append((d["id"], c["id"], (H[0] + e * u[0], H[1] + e * u[1]), r, u, v))
    return out


def bate_na_porta(giro, ret, tol=0.005):
    """Quanto (m) o retângulo entra no quarto de círculo que a folha varre; 0 se não entra."""
    _, _, (hx, hy), r, u, v = giro
    x0, y0, x1, y1 = ret
    for (dx, dy) in (u, v):  # o quarto de círculo fica do lado de u e de v da dobradiça
        if dx > 0: x0 = max(x0, hx)
        if dx < 0: x1 = min(x1, hx)
        if dy > 0: y0 = max(y0, hy)
        if dy < 0: y1 = min(y1, hy)
    if x1 - x0 <= tol or y1 - y0 <= tol:
        return 0.0
    dist = math.hypot(min(max(hx, x0), x1) - hx, min(max(hy, y0), y1) - hy)
    return max(0.0, r - dist) if dist < r - tol else 0.0


def portas_em_fixos(planta, fixos=FIXOS):
    """Porta que bate em tanque, pia, vaso, bancada, box ou máquina ao abrir: [(cômodo, porta, tipo, cm)]. Vazia = tudo certo.

    Achado do levantamento das 3 casas (24/11/2026): na C01 a folha da porta da cozinha batia no tanque."""
    moveis = construir(planta)[3]
    out = []
    for g in giros_de_porta(planta):
        for m in moveis:
            if m["amb"] == g[1] and m["tipo"] in fixos:
                cm = bate_na_porta(g, pegada(m))
                if cm:
                    out.append((g[1], g[0], m["tipo"], round(100 * cm, 1)))
    return out


def janelas_sobre_portas(planta):
    """Pares (porta, janela) em que a janela caiu em cima do vão da porta (parede curta demais para os dois).
    A veneziana declarada em cima da porta de fora (tipo "veneziana") fica de fora: ela é posta no vão da porta de propósito,
    e o validador dá erro se não houver porta embaixo dela."""
    _, janelas, portas, _ = construir(planta)
    out = []
    for d in portas:
        hx, hy = d["x"], d["y"]
        ex, ey = hx + d["r"] * math.cos(d["a0"]), hy + d["r"] * math.sin(d["a0"])
        for j in (j for j in janelas if j.get("tipo") != "veneziana"):
            x0, y0, x1, y1 = j["seg"]
            if abs(y0 - y1) < 1e-6 and abs(hy - ey) < 1e-6 and abs(hy - y0) < 1e-6 and min(hx, ex) < max(x0, x1) and max(hx, ex) > min(x0, x1):
                out.append((d["id"], j["id"]))
            if abs(x0 - x1) < 1e-6 and abs(hx - ex) < 1e-6 and abs(hx - x0) < 1e-6 and min(hy, ey) < max(y0, y1) and max(hy, ey) > min(y0, y1):
                out.append((d["id"], j["id"]))
    return out


def _lados_por_preferencia(c, vaos, janelas, quer_comprido=True):
    lados = ["frente", "fundos", "esq", "dir"]
    def nota(l):
        n = 0
        n -= 3 * sum(1 for (x, _, _) in vaos if x == l)
        n -= 1 * sum(1 for (x, _, _) in janelas if x == l)
        n += _comp(c, l) * (0.5 if quer_comprido else -0.5)
        return n
    return sorted(lados, key=nota, reverse=True)


def frente_do_armario(m):
    """Retângulo de FRENTE_ARMARIO na frente das portas do guarda-roupa (o chão que fica livre para abrir)."""
    r = pegada(m)
    sx, sy = round(math.sin(m.get("rot", 0.0))), round(math.cos(m.get("rot", 0.0)))
    f = FRENTE_ARMARIO
    return ((r[2], r[1], r[2] + f, r[3]) if sx > 0 else (r[0] - f, r[1], r[0], r[3]) if sx < 0 else
            (r[0], r[3], r[2], r[3] + f) if sy > 0 else (r[0], r[1] - f, r[2], r[1]))


def mobiliar(planta, vaos_por_comodo, jan_por_comodo, paredes=(), portas=()):
    """Móveis de cada cômodo pelas regras de projeto. Nenhum móvel ocupa o chão de outro nem entra na parede (checar.py)."""
    out = []
    por_id = {c["id"]: c for c in planta["comodos"]}
    for c0 in planta["comodos"]:
        t, cid = c0["tipo"], c0["id"]
        c = recuado(c0, paredes, planta)  # o arranjo automático usa o chão livre, da face de dentro das paredes de verdade
        vaos = vaos_por_comodo.get(cid, [])
        jans = jan_por_comodo.get(cid, [])
        w, d = c0["x1"] - c0["x0"], c0["y1"] - c0["y0"]  # as regras de tamanho (limiares) seguem a medida de eixo, como antes
        cx, cy = (c["x0"] + c["x1"]) / 2, (c["y0"] + c["y1"]) / 2
        aqui = []  # móveis já postos neste cômodo

        giros = [g for g in giros_de_porta(planta, portas) if g[1] == cid]  # a folha de cada porta que abre aqui (24/11/2026)

        def cabe(m, folga=0.0):
            r = pegada(m)
            dentro = r[0] >= c["x0"] - 1e-6 and r[1] >= c["y0"] - 1e-6 and r[2] <= c["x1"] + 1e-6 and r[3] <= c["y1"] + 1e-6
            return dentro and not any(o["tipo"] not in NAO_COLIDE and sobrepoe(r, pegada(o), folga) for o in aqui) \
                and (m["tipo"] in NAO_COLIDE or not any(bate_na_porta(g, r) for g in giros)) \
                and not any(o["tipo"] == "armario" and sobrepoe(r, frente_do_armario(o), -0.005) for o in aqui)

        def na_folha(lado, prof):
            """Trechos do lado em que uma peça de fundo prof, encostada nele, levaria a folha de uma porta ao abrir."""
            ini, fim = (c["x0"], c["x1"]) if lado in ("frente", "fundos") else (c["y0"], c["y1"])
            b0, b1 = {"frente": (c["y0"], c["y0"] + prof), "fundos": (c["y1"] - prof, c["y1"]),
                      "esq": (c["x0"], c["x0"] + prof), "dir": (c["x1"] - prof, c["x1"])}[lado]
            out_, s, passo = [], ini, 0.02
            while giros and s < fim - 1e-9:
                ret = (s, b0, s + passo, b1) if lado in ("frente", "fundos") else (b0, s, b1, s + passo)
                if any(bate_na_porta(g, ret) for g in giros):
                    out_.append((s, s + passo))
                s += passo
            return unir(out_)

        def add(**m):
            m = {"amb": cid, **{k: (R(v) if isinstance(v, float) else v) for k, v in m.items()}}
            out.append(m)
            aqui.append(m)
            return m

        if c0.get("moveis"):  # arranjo desenhado à mão pelo Arquiteto (PL.movel), com x e y a partir do canto do cômodo
            for m in c0["moveis"]:
                mm = add(**{**m, "x": c0["x0"] + m["x"], "y": c0["y0"] + m["y"]})
                if m["tipo"] == "escrivaninha":
                    add(**cadeira_de(mm))
            continue

        def ocupados(lado, prof):
            """Trechos do lado já tomados por móveis na faixa de profundidade prof junto da parede."""
            if lado in ("frente", "fundos"):
                faixa = (c["x0"], c["y0"], c["x1"], c["y0"] + prof) if lado == "frente" else (c["x0"], c["y1"] - prof, c["x1"], c["y1"])
                return [(r[0], r[2]) for r in (pegada(o) for o in aqui if o["tipo"] not in NAO_COLIDE) if sobrepoe(r, faixa)]
            faixa = (c["x0"], c["y0"], c["x0"] + prof, c["y1"]) if lado == "esq" else (c["x1"] - prof, c["y0"], c["x1"], c["y1"])
            return [(r[1], r[3]) for r in (pegada(o) for o in aqui if o["tipo"] not in NAO_COLIDE) if sobrepoe(r, faixa)]

        def na_janela(lado, prof):
            """Trechos do lado em que móvel alto taparia janela (24/11/2026): a janela da mesma parede e, no canto,
            a faixa de FRENTE_JANELA na frente da janela da parede do lado, se a peça de fundo prof chegar nela."""
            ini, fim = (c["x0"], c["x1"]) if lado in ("frente", "fundos") else (c["y0"], c["y1"])
            prof_ini, prof_fim = {"frente": (c["y0"], c["y0"] + prof), "fundos": (c["y1"] - prof, c["y1"]),
                                  "esq": (c["x0"], c["x0"] + prof), "dir": (c["x1"] - prof, c["x1"])}[lado]
            out_ = []
            for (l, ja, jb) in jans:
                if l == lado:
                    out_.append((ja, jb))
                elif l != OPOSTO[lado] and ja < prof_fim and jb > prof_ini:
                    out_.append((ini, ini + FRENTE_JANELA) if l in ("frente", "esq") else (fim - FRENTE_JANELA, fim))
            return out_

        def encostar(tipo, larg, prof, lados=None, folga=0.0, frente=0.5, no_canto=False, **extra):
            for lado in (lados or _lados_por_preferencia(c, vaos, jans)):
                if _prof(c0, lado) < prof + frente:
                    continue
                livre_frente = FRENTE_ARMARIO if tipo == "armario" else 0.0  # o guarda-roupa leva junto os 60 cm da frente
                if livre_frente and _prof(c, lado) < prof + folga + livre_frente:
                    continue
                tomados = ocupados(lado, prof + folga + livre_frente) + na_folha(lado, prof + folga) \
                    + (na_janela(lado, prof + folga) if tipo in ALTOS else [])
                pos = _livre_no_lado(c, lado, vaos, larg, perto_passagem=(tipo == "sofa"), ocupados=tomados,
                                     prof=prof + folga, no_canto=no_canto)
                if pos is None:
                    continue
                x, y = _no_lado(c, lado, pos, prof, folga)
                add(tipo=tipo, x=x, y=y, rot=ROT[lado], w=larg, d=prof, **extra)
                return lado, pos
            return None, None

        def escrivaninha(larguras, prof, lados):
            """Escrivaninha com a cadeira na frente: só fica onde a cadeira cabe sem cama, móvel ou porta na frente."""
            zonas_porta = [(va, c["y0"], vb, c["y0"] + 0.8) if l == "frente" else (va, c["y1"] - 0.8, vb, c["y1"]) if l == "fundos"
                           else (c["x0"], va, c["x0"] + 0.8, vb) if l == "esq" else (c["x1"] - 0.8, va, c["x1"], vb)
                           for (l, va, vb) in vaos]
            for l in (lados or _lados_por_preferencia(c, vaos, jans)):
                for larg in larguras:
                    for canto in (False, True):
                        if not encostar("escrivaninha", larg, prof, [l], no_canto=canto)[0]:
                            continue
                        z = zona_da_cadeira(aqui[-1])
                        dentro = z[0] >= c["x0"] - 1e-6 and z[1] >= c["y0"] - 1e-6 and z[2] <= c["x1"] + 1e-6 and z[3] <= c["y1"] + 1e-6
                        livre = not any(o["tipo"] not in NAO_COLIDE and sobrepoe(z, pegada(o)) for o in aqui[:-1])
                        arm = [frente_do_armario(o) for o in aqui[:-1] if o["tipo"] == "armario"]
                        if dentro and livre and not any(sobrepoe(z, zp) for zp in zonas_porta) \
                                and not any(sobrepoe(z, fa, -0.005) or sobrepoe(pegada(aqui[-1]), fa, -0.005) for fa in arm):
                            add(**cadeira_de(aqui[-1]))
                            return True
                        out.remove(aqui.pop())
            return False  # sem lugar com a cadeira: o quarto fica sem escrivaninha

        def mesa_de_jantar():
            """Mesa de 4 lugares (0,80 x 1,20 m) no canto livre mais perto da cozinha, fora da frente das portas."""
            cozinhas = [c] if t == "cozinha" else [o for o in por_id.values() if o["tipo"] == "cozinha" and PL.parede_comum(c0, o)]
            alvo = ((cozinhas[0]["x0"] + cozinhas[0]["x1"]) / 2, (cozinhas[0]["y0"] + cozinhas[0]["y1"]) / 2) if cozinhas else (cx, cy)
            portas_zona = []
            for (l, va, vb) in vaos:  # 0,80 m livres na frente de cada porta ou passagem, medidos do eixo da parede
                if l == "frente":
                    portas_zona.append((va, c0["y0"], vb, c0["y0"] + 0.8))
                elif l == "fundos":
                    portas_zona.append((va, c0["y1"] - 0.8, vb, c0["y1"]))
                elif l == "esq":
                    portas_zona.append((c0["x0"], va, c0["x0"] + 0.8, vb))
                else:
                    portas_zona.append((c0["x1"] - 0.8, va, c0["x1"], vb))
            melhor = None
            for rot in (0.0, math.pi / 2):
                for i in range(int(w / 0.025) + 1):
                    for j in range(int(d / 0.025) + 1):
                        m = {"tipo": "mesaJantar", "x": c["x0"] + i * 0.025, "y": c["y0"] + j * 0.025, "w": 0.8, "d": 1.2, "rot": rot}
                        r = pegada(m)
                        if not cabe(m, 0.1) or r[0] < c["x0"] or r[1] < c["y0"] or r[2] > c["x1"] or r[3] > c["y1"]:  # c já vai até a face da parede
                            continue
                        if any(sobrepoe(r, z) for z in portas_zona) or any(bate_na_porta(g, r) for g in giros):
                            continue
                        dist = math.hypot(m["x"] - alvo[0], m["y"] - alvo[1])
                        if melhor is None or dist < melhor[0]:
                            melhor = (dist, m)
            if melhor:
                m = melhor[1]
                add(tipo="mesaJantar", x=m["x"], y=m["y"], rot=m["rot"], w=0.8, d=1.2)
                return True
            return False

        if t in ("casal", "dorm"):
            casal = t == "casal"
            bw, bd = (1.38, 1.88) if casal else (0.88, 1.88)  # colchão de casal e de solteiro padrão (24/11/2026: era queen, 1,60 x 2,00)
            lados = [l for l in _lados_por_preferencia(c, vaos, jans) if _prof(c0, l) >= bd + 0.6]

            def cama_e_armario(lados_cama, canto):
                """Cama, criados e o maior guarda-roupa com 60 cm na frente; devolve (lado da cama, tem guarda-roupa)."""
                lado, pos = encostar("camaCasal" if casal else "camaSolteiro", bw, bd, lados_cama, no_canto=canto,
                                     manta="#B9C7D6" if casal else "#E3B9A4")
                if not lado:
                    return None, False
                for s in (-1, 1):
                    p = pos + s * (bw / 2 + 0.28)  # criado de 0,45 m ao lado da cama, sem entrar nela
                    a, b = (c["x0"], c["x1"]) if lado in ("frente", "fundos") else (c["y0"], c["y1"])
                    livre = all(not (l == lado and va - 0.1 < p < vb + 0.1) for (l, va, vb) in vaos)
                    x, y = _no_lado(c, lado, p, 0.4)
                    if a + 0.25 < p < b - 0.25 and livre and cabe({"tipo": "criado", "x": x, "y": y, "rot": ROT[lado]}):
                        add(tipo="criado", x=x, y=y, rot=ROT[lado])
                    if not casal:
                        break
                for arm in ((2.0, 1.6, 1.2) if casal else (1.5, 1.2, 1.0)):  # o maior guarda-roupa que couber, com 60 cm na frente
                    if encostar("armario", arm, 0.5, [l for l in _lados_por_preferencia(c, vaos, jans) if l != lado])[0]:
                        return lado, True  # 0,50 de fundo, o da Portaria MCID 725 (24/11/2026: era 0,60)
                return lado, False

            # a cama do lugar de sempre; se ali o guarda-roupa não tiver os 60 cm na frente, a cama tenta outra parede ou o canto
            lado, com_armario = cama_e_armario(lados, False)
            for l, canto in [(l, k) for l in lados for k in (False, True)]:
                if com_armario or not lado:
                    break
                ate = [m for m in aqui]
                while aqui:
                    out.remove(aqui.pop())
                lado2, ok = cama_e_armario([l], canto)
                if ok:
                    lado, com_armario = lado2, True
                    break
                while aqui:
                    out.remove(aqui.pop())
                for m in ate:
                    out.append(m)
                    aqui.append(m)
            if lado:
                restantes = [l for l in _lados_por_preferencia(c, vaos, jans) if l != lado]
                if not casal:
                    escrivaninha((1.0, 0.8), 0.5, restantes)
        elif t in ("sala", "estar"):
            jantar = t == "sala" and "jantar" in c["nome"].lower()
            if jantar:
                mesa_de_jantar()  # primeiro a mesa, perto da cozinha; o estar se arruma no que sobra
            lados = [l for l in _lados_por_preferencia(c, vaos, jans) if _prof(c0, l) >= 2.6]
            lado = pos = None
            # sofá de 3, de 2 e meio e de 2 lugares: o maior que couber sem tapar porta, medido na parede em que encosta,
            # de preferência com a TV (rack) na parede da frente dele; sem par, o sofá fica sozinho
            p_op = None
            for com_tv in (True, False):
                for larg in (2.1, 1.8, 1.5, 1.4):
                    for l in (lados or _lados_por_preferencia(c, vaos, jans)):
                        lado, pos = encostar("sofa", min(larg, _comp(c, l) - 0.6), 0.88, [l], cor="#8A9A86")
                        if not lado:
                            continue
                        p_op = _livre_no_lado(c, OPOSTO[lado], vaos, 1.6, ocupados=ocupados(OPOSTO[lado], 0.4) + na_folha(OPOSTO[lado], 0.4), prof=0.4)
                        if p_op is not None or not com_tv:
                            break
                        out.remove(aqui.pop())
                        lado = None
                    if lado:
                        break
                if lado:
                    break
            if lado:
                op = OPOSTO[lado]
                x, y = _no_lado(c, op, pos, 0.4)
                if p_op is not None:
                    x, y = _no_lado(c, op, p_op, 0.4)
                    add(tipo="rack", x=x, y=y, rot=ROT[op], w=1.6, d=0.4)
                sx, sy = _no_lado(c, lado, pos, 0.88)
                mx, my = (sx + x) / 2, (sy + y) / 2
                vertical = lado in ("esq", "dir")
                centro = {"tipo": "mesaCentro", "x": mx, "y": my, "w": 1.0 if not vertical else 0.6, "d": 0.6 if not vertical else 1.0}
                if cabe(centro, 0.25):
                    tw, td = (2.0, 2.2) if vertical else (2.2, 2.0)
                    for k in (1.0, 0.85, 0.7):  # tapete menor se a mesa de jantar estiver perto
                        tap = {"tipo": "tapete", "x": mx, "y": my, "w": tw * k, "d": td * k}
                        r = pegada(tap)
                        dentro = r[0] >= c["x0"] - 1e-6 and r[1] >= c["y0"] - 1e-6 and r[2] <= c["x1"] + 1e-6 and r[3] <= c["y1"] + 1e-6
                        if dentro and not any(o["tipo"] == "mesaJantar" and sobrepoe(r, pegada(o)) for o in aqui):
                            add(tipo="tapete", x=mx, y=my, w=tw * k, d=td * k, cor="#D9CBB4", borda="#B49D7C")
                            break
                    add(**centro)
            if t == "estar" and w * d > 14:
                encostar("camaCasal", 1.4, 1.9, None, manta="#C9B59A")
            for (px, py) in ((c["x0"] + 0.4, c["y0"] + 0.4), (c["x1"] - 0.4, c["y0"] + 0.4), (c["x0"] + 0.4, c["y1"] - 0.4)):
                if cabe({"tipo": "planta", "x": px, "y": py, "s": 0.9}, 0.05) and \
                        all(not (abs(px - (va + vb) / 2) < 1.0 and l in ("frente", "fundos")) for (l, va, vb) in vaos):
                    add(tipo="planta", x=px, y=py, s=0.9)
                    break
        elif t == "jantar":
            add(tipo="mesaJantar", x=cx, y=cy, w=0.85 if w < d else 1.3, d=1.3 if w < d else 0.85)
        elif t == "cozinha":
            comp_max = 0
            lado, pos = None, None
            for l in _lados_por_preferencia(c, vaos, [], True):
                if _prof(c0, l) < 1.5:
                    continue
                larg = min(3.0, _comp(c, l) - 0.2)
                while larg >= 1.2:
                    p = _livre_no_lado(c, l, vaos, larg)
                    if p is not None:
                        break
                    larg = round(larg - 0.1, 2)
                if larg >= 1.2 and p is not None and larg > comp_max:
                    comp_max, lado, pos = larg, l, p
            if lado:
                x, y = _no_lado(c, lado, pos, 0.62)
                add(tipo="bancada", x=x, y=y, rot=ROT[lado], w=comp_max, d=0.62)
                restantes = [l for l in _lados_por_preferencia(c, vaos, []) if l != lado]

                def geladeira():
                    if encostar("geladeira", 0.72, 0.7, restantes)[0] or comp_max - 0.8 < 1.0:  # bancada curta (1 m, pia e fogão) antes de cozinha sem geladeira
                        return
                    # sem outra parede livre, a geladeira fica na ponta da bancada, na mesma parede
                    banc = next(m for m in aqui if m["tipo"] == "bancada")
                    aqui.remove(banc)
                    out.remove(banc)
                    ini = pos - comp_max / 2
                    for desloc in (0.0, 0.8):  # a geladeira na ponta de lá da bancada ou, se ali taparia a janela, na de cá
                        x, y = _no_lado(c, lado, ini + desloc + (comp_max - 0.8) / 2, 0.62)
                        curta = add(tipo="bancada", x=x, y=y, rot=ROT[lado], w=comp_max - 0.8, d=0.62)
                        if encostar("geladeira", 0.72, 0.7, [lado])[0]:
                            return
                        aqui.remove(curta)
                        out.remove(curta)
                    add(**{k: v for k, v in banc.items() if k != "amb"})
                geladeira()
            if w * d >= 8.5 and min(w, d) >= 2.6 and not mesa_de_jantar() and lado:
                # a geladeira (fora da janela, 24/11/2026) tomou o lugar da mesa: a mesa primeiro, a geladeira no que sobrar
                antes = list(aqui)
                while aqui:  # recomeça: bancada inteira, mesa, geladeira
                    out.remove(aqui.pop())
                x, y = _no_lado(c, lado, pos, 0.62)
                add(tipo="bancada", x=x, y=y, rot=ROT[lado], w=comp_max, d=0.62)
                if mesa_de_jantar():
                    geladeira()
                else:  # nem assim: volta o arranjo de antes, sem mesa
                    while aqui:
                        out.remove(aqui.pop())
                    for m in antes:
                        out.append(m)
                        aqui.append(m)
        elif t in ("banho", "lavabo"):
            lados = _lados_por_preferencia(c, vaos, jans)
            # o box primeiro (é o maior); se ele tirar o lugar do vaso ou da pia, tenta o box em outra parede
            opcoes = sorted((l for l in lados if _comp(c0, l) >= 0.9), key=lambda l: _comp(c0, l) < 1.6) if min(w, d) >= 1.2 and t == "banho" else []
            def tirar(ate):
                while len(aqui) > ate:
                    out.remove(aqui.pop())

            def vaso_e_pia():
                """Procura parede e ponta para o vaso e a pia juntos (com a parede de verdade, o primeiro lugar nem sempre serve)."""
                ate = len(aqui)
                for vl in lados:
                    for vc in (False, True):
                        if not encostar("vaso", 0.4, 0.65, [vl], frente=0.3, no_canto=vc)[0]:
                            continue
                        for pl in reversed(lados):
                            for pc in (False, True):
                                if encostar("pia", 0.6, 0.42, [pl], frente=0.3, no_canto=pc)[0]:
                                    return True
                        tirar(ate)
                return False

            feito = False
            # box de 0,90 x 0,95 (Portaria MCID 725, Anexo, item 2.I.c.v) nos dois sentidos; o de 0,80 x 0,85 só se o maior não couber
            for bw_, bd_ in ((0.95, 0.9), (0.9, 0.95), (0.8, 0.85)):
                for box_lado in opcoes:
                    for bc in (True, False):  # o box vai no canto (duas paredes), não solto no meio da parede
                        antes = len(aqui)
                        if encostar("box", bw_, bd_, [box_lado], frente=0.3, no_canto=bc)[0] and vaso_e_pia():
                            feito = True
                            break
                        tirar(antes)
                    if feito:
                        break
                if feito:
                    break
            if not feito and not vaso_e_pia():  # sem box: o vaso e a pia juntos ou, se não der, o que couber
                encostar("vaso", 0.4, 0.65, lados, frente=0.3)[0] and encostar("pia", 0.6, 0.42, list(reversed(lados)), frente=0.3)
        elif t == "servico":
            encostar("tanque", 0.6, 0.5, None, frente=0.4, no_canto=True)  # tanque no canto, máquina ao lado
            if not (encostar("maquina", 0.6, 0.6, None, frente=0.4)[0] or encostar("maquina", 0.6, 0.6, None, frente=0.3)[0]):
                # sem lugar para a máquina (a folha da porta tomou o canto): o tanque procura outra parede (24/11/2026)
                for l in _lados_por_preferencia(c, vaos, jans):
                    for canto in (True, False):
                        while aqui:
                            out.remove(aqui.pop())
                        if encostar("tanque", 0.6, 0.5, [l], frente=0.4, no_canto=canto)[0] and \
                                encostar("maquina", 0.6, 0.6, None, frente=0.3)[0]:
                            break
                    else:
                        continue
                    break
                else:  # nem assim: fica só o tanque, no canto
                    while aqui:
                        out.remove(aqui.pop())
                    encostar("tanque", 0.6, 0.5, None, frente=0.4, no_canto=True)
        elif t == "escritorio":
            escrivaninha((1.2, 1.0), 0.6, None)
            encostar("armario", 1.2, 0.45, None)
        elif t == "garagem":
            add(tipo="carro", x=cx, y=cy, rot=0.0, w=1.75, d=min(4.2, d - 0.6))
        elif t == "varanda":
            if c["nome"].lower().startswith("área gourmet"):
                add(tipo="mesaJantar", x=cx, y=cy, w=1.3 if w > d else 0.85, d=0.85 if w > d else 1.3)
                encostar("bancada", min(2.0, max(w, d) - 1.0), 0.6, None)
            elif min(w, d) >= 1.5:
                add(tipo="planta", x=c["x0"] + 0.4, y=c["y0"] + 0.4, s=0.8)
                if cabe({"tipo": "poltrona", "x": cx, "y": cy, "w": 0.75, "d": 0.75}):
                    add(tipo="poltrona", x=cx, y=cy, rot=0.0, w=0.75, d=0.75)
        elif t in ("patio", "externo"):
            n = max(1, int(w * d / 6))
            for i in range(n):
                add(tipo="planta", x=c["x0"] + (i + 0.5) * (c["x1"] - c["x0"]) / n, y=cy, s=1.2)
    return out


# ---------------------------------------------------------------- saída
def ordem(planta):
    prio = {"varanda": 0, "garagem": 0, "sala": 1, "estar": 1, "jantar": 2, "cozinha": 3, "servico": 4, "circ": 5,
            "banho": 6, "lavabo": 6, "escritorio": 7, "casal": 8, "dorm": 9, "patio": 10, "externo": 10}
    cs = [c for c in planta["comodos"] if c["tipo"] != "futuro"]
    return [c["id"] for c in sorted(cs, key=lambda c: (prio.get(c["tipo"], 5), c["y0"], c["x0"]))]


def espelhar(W, paredes, janelas, portas, moveis, ambientes):
    """Passa da planta (x para a direita de quem olha da rua) para o mundo 3D, que é espelhado no eixo X.

    No three.js (y para cima, z = fundos), quem olha da rua para a casa vê o x do mundo crescer para a ESQUERDA.
    Sem espelhar, a imagem 3D sai invertida em relação à planta do e-book (achado do Designer, 23/11/2026).
    Com X = largura - x, a casa vista da rua bate com a planta: porta, janelas e cômodos do mesmo lado."""
    X = lambda x: R(W - x)
    paredes = [[X(p[0]), p[1], X(p[2]), p[3], *p[4:]] for p in paredes]
    for j in janelas:
        a, b, c, d = j["seg"]
        j["seg"] = [X(c), d, X(a), b] if b == d else [X(a), b, X(c), d]
    for p in portas:  # ângulo a vira pi - a; a folha fechada continua em a0 e a aberta em a1
        p["x"], p["a0"], p["a1"] = X(p["x"]), math.pi - p["a0"], math.pi - p["a1"]
    for m in moveis:
        m["x"] = X(m["x"])
        if m.get("rot"):
            m["rot"] = R(-m["rot"])
    for a in ambientes:
        a["x0"], a["x1"] = X(a["x1"]), X(a["x0"])
    return paredes, janelas, portas, moveis, ambientes


def modulo(planta):
    paredes, janelas, portas, moveis = construir(planta)
    paredes, janelas, portas = para_desenho(planta, paredes, janelas, portas)  # parede externa para dentro, como no validador
    r = planta["_r"]
    m = r.metricas
    amb = [{"id": c["id"], "nome": c["nome"], "tipo": c["tipo"], "x0": c["x0"], "y0": c["y0"], "x1": c["x1"], "y1": c["y1"],
            "cor": CORES_AMB.get(c["tipo"], "#EEE"), "piso": PISO.get(c["tipo"], "madeira"),
            "area_livre": m["util"][c["id"]][2]}  # a área livre do validador, a mesma do e-book (F7, 24/11/2026)
           for c in planta["comodos"] if c["tipo"] != "futuro"]
    futuros = [{"id": c["id"], "nome": c["nome"], "x0": c["x0"], "y0": c["y0"], "x1": c["x1"], "y1": c["y1"]}
               for c in planta["comodos"] if c["tipo"] == "futuro"]
    paredes, janelas, portas, moveis, _ = espelhar(planta["W"], paredes, janelas, portas, moveis, amb + futuros)
    meta = {"id": planta["id"], "nome": planta["nome"], "area": m["area_fechada"], "quartos": planta["quartos_txt"],
            "banheiros": planta["banheiros"], "lote": m["lote_comercial"], "orientacao": m["orientacao"]["melhor"]}
    J = lambda v: json.dumps(v, ensure_ascii=False)
    return "\n".join([
        f"// {planta['id']} · {planta['nome']}: gerado por ferramentas/planta3d.py a partir de ebook/plantas/projetos.py. Não edite à mão.",
        f"export const LARGURA = {planta['W']};",
        f"export const PROFUNDIDADE = {planta['D']};",
        "export const PE_DIREITO = 2.8;",
        "export const ESPESSURA = 0.15;",
        f"export const META = {J(meta)};",
        f"export const ambientes = {J(amb)};",
        f"export const futuros = {J(futuros)};",
        f"export const paredes = {J(paredes)};",
        f"export const janelas = {J(janelas)};",
        f"export const portas = {J(portas)};",
        f"export const MOVEIS = {J(moveis)};",
        f"export const ORDEM = {J(ordem(planta))};",
        f"export const ENTRADA_X = {R(planta['W'] - planta.get('_entrada_x', planta['W'] / 2))};",
        "",
    ])


def main(ids):
    SAIDA.mkdir(parents=True, exist_ok=True)
    plantas = [p for p in PL.carregar() if not ids or p["id"] in ids]
    for p in plantas:
        (SAIDA / f"{p['id']}.js").write_text(modulo(p), encoding="utf-8")
    print(f"{len(plantas)} módulos em {SAIDA.relative_to(RAIZ)}")


if __name__ == "__main__":
    main(sys.argv[1:])

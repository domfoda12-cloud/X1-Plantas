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

    portas, vaos_por_comodo = [], {}

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

    paredes = []
    for (o, fixo), ivs in sorted(linhas.items()):
        for (a, b) in ivs:
            if b - a < 0.02:
                continue
            paredes.append([R(a), fixo, R(b), fixo] if o == "h" else [fixo, R(a), fixo, R(b)])

    moveis = mobiliar(planta, vaos_por_comodo, jan_por_comodo, paredes)
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
FACE = 0.075  # metade da parede do motor 3D (ESPESSURA 0,15 m, desenhada sobre o eixo): o móvel para aí, na face de dentro
CADEIRA_ZONA = (0.6, 0.75)  # largura x fundo livres na frente da escrivaninha para a cadeira e quem senta (Anexo G: 0,75 m da borda da mesa)


def recuado(c, paredes):
    """O cômodo até a face de dentro das paredes: cada lado com parede no motor 3D encolhe FACE.

    Sem isso o móvel encostado ia até o eixo da parede, e a cabeceira da cama saía pela face de fora (Arquiteto, 23/11/2026)."""
    r = dict(c)
    for lado, o, fixo, a, b in arestas(c):
        tem = any((p[1] == p[3]) == (o == "h") and abs((p[1] if o == "h" else p[0]) - fixo) < 1e-6
                  and min(max(p[0], p[2]) if o == "h" else max(p[1], p[3]), b) - max(min(p[0], p[2]) if o == "h" else min(p[1], p[3]), a) > 0.01
                  for p in paredes)
        if tem:
            k = {"frente": "y0", "fundos": "y1", "esq": "x0", "dir": "x1"}[lado]
            r[k] = c[k] + (FACE if lado in ("frente", "esq") else -FACE)
    return r


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


def moveis_na_parede(planta, tol=0.02):
    """Móveis que entram numa parede do motor 3D (15 cm sobre o eixo) mais que tol: [(amb, tipo, 'externa'|'interna', cm)].

    tol de 2 cm: o arranjo à mão (PL.movel) encosta a 6 cm do eixo da parede interna, que no 3D tem 7,5 cm de cada lado."""
    paredes, _, _, moveis = construir(planta)
    out = []
    for p in paredes:
        h = p[1] == p[3]
        a, b = (min(p[0], p[2]), max(p[0], p[2])) if h else (min(p[1], p[3]), max(p[1], p[3]))
        fixo = p[1] if h else p[0]
        caixa = (a - FACE, fixo - FACE, b + FACE, fixo + FACE) if h else (fixo - FACE, a - FACE, fixo + FACE, b + FACE)
        meio = (a + b) / 2
        lados = [(meio, fixo - 0.1), (meio, fixo + 0.1)] if h else [(fixo - 0.1, meio), (fixo + 0.1, meio)]
        externa = any((v := PL._dentro(planta, x, y)) is None or not fechado(v) for x, y in lados)
        for m in moveis:
            r = pegada(m)
            dx, dy = min(r[2], caixa[2]) - max(r[0], caixa[0]), min(r[3], caixa[3]) - max(r[1], caixa[1])
            if dx > tol and dy > tol:
                out.append((m["amb"], m["tipo"], "externa" if externa else "interna", round(100 * min(dx, dy))))
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


def janelas_sobre_portas(planta):
    """Pares (porta, janela) em que a janela caiu em cima do vão da porta (parede curta demais para os dois)."""
    _, janelas, portas, _ = construir(planta)
    out = []
    for d in portas:
        hx, hy = d["x"], d["y"]
        ex, ey = hx + d["r"] * math.cos(d["a0"]), hy + d["r"] * math.sin(d["a0"])
        for j in janelas:
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


def mobiliar(planta, vaos_por_comodo, jan_por_comodo, paredes=()):
    """Móveis de cada cômodo pelas regras de projeto. Nenhum móvel ocupa o chão de outro nem entra na parede (checar.py)."""
    out = []
    por_id = {c["id"]: c for c in planta["comodos"]}
    for c0 in planta["comodos"]:
        t, cid = c0["tipo"], c0["id"]
        c = recuado(c0, paredes)  # o arranjo automático usa o chão livre, da face de dentro das paredes
        vaos = vaos_por_comodo.get(cid, [])
        jans = jan_por_comodo.get(cid, [])
        w, d = c0["x1"] - c0["x0"], c0["y1"] - c0["y0"]  # as regras de tamanho (limiares) seguem a medida de eixo, como antes
        cx, cy = (c["x0"] + c["x1"]) / 2, (c["y0"] + c["y1"]) / 2
        aqui = []  # móveis já postos neste cômodo

        def cabe(m, folga=0.0):
            r = pegada(m)
            dentro = r[0] >= c["x0"] - 1e-6 and r[1] >= c["y0"] - 1e-6 and r[2] <= c["x1"] + 1e-6 and r[3] <= c["y1"] + 1e-6
            return dentro and not any(o["tipo"] not in NAO_COLIDE and sobrepoe(r, pegada(o), folga) for o in aqui)

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

        def encostar(tipo, larg, prof, lados=None, folga=0.0, frente=0.5, no_canto=False, **extra):
            for lado in (lados or _lados_por_preferencia(c, vaos, jans)):
                if _prof(c0, lado) < prof + frente:
                    continue
                pos = _livre_no_lado(c, lado, vaos, larg, perto_passagem=(tipo == "sofa"), ocupados=ocupados(lado, prof + folga),
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
                        if dentro and livre and not any(sobrepoe(z, zp) for zp in zonas_porta):
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
                        if any(sobrepoe(r, z) for z in portas_zona):
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
            bw, bd = (1.6, 2.0) if casal else (0.95, 1.95)
            lados = [l for l in _lados_por_preferencia(c, vaos, jans) if _prof(c0, l) >= bd + 0.6]
            lado, pos = encostar("camaCasal" if casal else "camaSolteiro", bw, bd, lados,
                                 manta="#B9C7D6" if casal else "#E3B9A4")
            if lado:
                for s in (-1, 1):
                    p = pos + s * (bw / 2 + 0.28)  # criado de 0,45 m ao lado da cama, sem entrar nela
                    a, b = (c["x0"], c["x1"]) if lado in ("frente", "fundos") else (c["y0"], c["y1"])
                    livre = all(not (l == lado and va - 0.1 < p < vb + 0.1) for (l, va, vb) in vaos)
                    x, y = _no_lado(c, lado, p, 0.4)
                    if a + 0.25 < p < b - 0.25 and livre and cabe({"tipo": "criado", "x": x, "y": y, "rot": ROT[lado]}):
                        add(tipo="criado", x=x, y=y, rot=ROT[lado])
                    if not casal:
                        break
                restantes = [l for l in _lados_por_preferencia(c, vaos, jans) if l != lado]
                for arm in ((1.8, 1.5, 1.2) if casal else (1.4, 1.2, 1.0)):  # o maior guarda-roupa que couber
                    if encostar("armario", arm, 0.6, restantes)[0]:
                        break
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
                        p_op = _livre_no_lado(c, OPOSTO[lado], vaos, 1.6, ocupados=ocupados(OPOSTO[lado], 0.4), prof=0.4)
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
                if not encostar("geladeira", 0.72, 0.7, restantes)[0] and comp_max - 0.8 >= 1.2:
                    # sem outra parede livre, a geladeira fica na ponta da bancada, na mesma parede
                    out.remove(aqui.pop())
                    a_ = (c["x0"] if lado in ("frente", "fundos") else c["y0"])
                    ini = pos - comp_max / 2
                    x, y = _no_lado(c, lado, ini + (comp_max - 0.8) / 2, 0.62)
                    add(tipo="bancada", x=x, y=y, rot=ROT[lado], w=comp_max - 0.8, d=0.62)
                    if not encostar("geladeira", 0.72, 0.7, [lado])[0]:
                        out.remove(aqui.pop())
                        x, y = _no_lado(c, lado, pos, 0.62)
                        add(tipo="bancada", x=x, y=y, rot=ROT[lado], w=comp_max, d=0.62)
            if w * d >= 8.5 and min(w, d) >= 2.6:
                mesa_de_jantar()
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
            for box_lado in opcoes:
                for bc in (False, True):
                    antes = len(aqui)
                    if encostar("box", 0.8, 0.85, [box_lado], frente=0.3, no_canto=bc)[0] and vaso_e_pia():
                        feito = True
                        break
                    tirar(antes)
                if feito:
                    break
            if not feito:  # sem box: o vaso e a pia que couberem
                encostar("vaso", 0.4, 0.65, lados, frente=0.3)[0] and encostar("pia", 0.6, 0.42, list(reversed(lados)), frente=0.3)
        elif t == "servico":
            encostar("tanque", 0.6, 0.5, None, frente=0.4, no_canto=True)  # tanque no canto, máquina ao lado
            encostar("maquina", 0.6, 0.6, None, frente=0.4) or encostar("maquina", 0.6, 0.6, None, frente=0.3)
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
    paredes = [[X(a), b, X(c), d] for (a, b, c, d) in paredes]
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
    r = planta["_r"]
    m = r.metricas
    amb = [{"id": c["id"], "nome": c["nome"], "tipo": c["tipo"], "x0": c["x0"], "y0": c["y0"], "x1": c["x1"], "y1": c["y1"],
            "cor": CORES_AMB.get(c["tipo"], "#EEE"), "piso": PISO.get(c["tipo"], "madeira")}
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

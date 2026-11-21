"""Converte as plantas validadas (ebook/plantas/projetos.py) em módulos para o motor 3D.

Para cada planta gera video/src/plantas/<ID>.js com o mesmo formato de video/src/planta.js
(LARGURA, PROFUNDIDADE, ambientes, paredes com vãos de porta, janelas, portas) e mais
MOVEIS (posicionados por regra de arquiteto), ORDEM (sequência em que os cômodos ganham vida)
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

    moveis = mobiliar(planta, vaos_por_comodo, jan_por_comodo)
    return paredes, janelas, portas, moveis


# ---------------------------------------------------------------- móveis
OPOSTO = {"frente": "fundos", "fundos": "frente", "esq": "dir", "dir": "esq"}
ROT = {"frente": 0.0, "fundos": math.pi, "esq": math.pi / 2, "dir": -math.pi / 2}


def _livre_no_lado(c, lado, vaos, w, margem=0.05, perto_passagem=False):
    """Posição central (ao longo do lado) onde cabe uma peça de largura w sem bloquear porta."""
    _, o, fixo, a, b = next(x for x in arestas(c) if x[0] == lado)
    livres = [(a + margem, b - margem)]
    perto_canto = 0.95
    for (l, va, vb) in vaos:
        if l == lado:
            livres = subtrair(livres, va - 0.1, vb + 0.1)
        elif l != OPOSTO[lado]:
            # porta num lado perpendicular, perto do canto com este lado: a peça não pode ficar na frente dela
            canto = c["y0"] if lado == "frente" else c["y1"] if lado == "fundos" else c["x0"] if lado == "esq" else c["x1"]
            if min(abs(va - canto), abs(vb - canto)) < perto_canto:
                ponta = c["x0"] if l == "esq" else c["x1"] if l == "dir" else c["y0"] if l == "frente" else c["y1"]
                # só o sofá pode chegar a 0,5 m de uma passagem aberta larga (ela não tem folha de porta)
                folga = 0.5 if perto_passagem and vb - va > 1.2 else 0.95
                livres = subtrair(livres, ponta - folga, ponta + folga)
    cabe = [(p, q) for (p, q) in livres if q - p >= w]
    if not cabe:
        return None
    p, q = max(cabe, key=lambda t: t[1] - t[0])
    return (p + q) / 2


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


def _lados_por_preferencia(c, vaos, janelas, quer_comprido=True):
    lados = ["frente", "fundos", "esq", "dir"]
    def nota(l):
        n = 0
        n -= 3 * sum(1 for (x, _, _) in vaos if x == l)
        n -= 1 * sum(1 for (x, _, _) in janelas if x == l)
        n += _comp(c, l) * (0.5 if quer_comprido else -0.5)
        return n
    return sorted(lados, key=nota, reverse=True)


def mobiliar(planta, vaos_por_comodo, jan_por_comodo):
    out = []
    for c in planta["comodos"]:
        t, cid = c["tipo"], c["id"]
        vaos = vaos_por_comodo.get(cid, [])
        jans = jan_por_comodo.get(cid, [])
        w, d = c["x1"] - c["x0"], c["y1"] - c["y0"]
        cx, cy = (c["x0"] + c["x1"]) / 2, (c["y0"] + c["y1"]) / 2
        add = lambda **m: out.append({"amb": cid, **{k: (R(v) if isinstance(v, float) else v) for k, v in m.items()}})

        def encostar(tipo, larg, prof, lados=None, folga=0.0, frente=0.5, **extra):
            for lado in (lados or _lados_por_preferencia(c, vaos, jans)):
                if _prof(c, lado) < prof + frente:
                    continue
                pos = _livre_no_lado(c, lado, vaos, larg, perto_passagem=(tipo == "sofa"))
                if pos is None:
                    continue
                x, y = _no_lado(c, lado, pos, prof, folga)
                add(tipo=tipo, x=x, y=y, rot=ROT[lado], w=larg, d=prof, **extra)
                return lado, pos
            return None, None

        if t in ("casal", "dorm"):
            casal = t == "casal"
            bw, bd = (1.6, 2.0) if casal else (0.95, 1.95)
            lados = [l for l in _lados_por_preferencia(c, vaos, jans) if _prof(c, l) >= bd + 0.6]
            lado, pos = encostar("camaCasal" if casal else "camaSolteiro", bw, bd, lados,
                                 manta="#B9C7D6" if casal else "#E3B9A4")
            if lado:
                for s in (-1, 1):
                    p = pos + s * (bw / 2 + 0.3)
                    a, b = (c["x0"], c["x1"]) if lado in ("frente", "fundos") else (c["y0"], c["y1"])
                    livre = all(not (l == lado and va - 0.1 < p < vb + 0.1) for (l, va, vb) in vaos)
                    if a + 0.25 < p < b - 0.25 and livre:
                        x, y = _no_lado(c, lado, p, 0.4)
                        add(tipo="criado", x=x, y=y)
                    if not casal:
                        break
                arm = 1.8 if casal else 1.4
                restantes = [l for l in _lados_por_preferencia(c, vaos, jans) if l != lado]
                encostar("armario", arm, 0.6, restantes)
                if not casal:
                    encostar("escrivaninha", 1.0, 0.5, [l for l in restantes])
        elif t in ("sala", "estar"):
            lados = [l for l in _lados_por_preferencia(c, vaos, jans) if _prof(c, l) >= 2.6]
            lado = pos = None
            # sofá de 3, de 2 e meio e de 2 lugares: o maior que couber sem tapar porta, medido na parede em que encosta
            for larg in (2.1, 1.8, 1.5):
                for l in (lados or _lados_por_preferencia(c, vaos, jans)):
                    lado, pos = encostar("sofa", min(larg, _comp(c, l) - 0.6), 0.88, [l], cor="#8A9A86")
                    if lado:
                        break
                if lado:
                    break
            if lado:
                op = OPOSTO[lado]
                x, y = _no_lado(c, op, pos, 0.4)
                p_op = _livre_no_lado(c, op, vaos, 1.6)
                if p_op is not None:
                    x, y = _no_lado(c, op, p_op, 0.4)
                    add(tipo="rack", x=x, y=y, rot=ROT[op], w=1.6, d=0.4)
                sx, sy = _no_lado(c, lado, pos, 0.88)
                mx, my = (sx + x) / 2, (sy + y) / 2
                vertical = lado in ("esq", "dir")
                add(tipo="tapete", x=mx, y=my, w=2.0 if vertical else 2.2, d=2.2 if vertical else 2.0, cor="#D9CBB4", borda="#B49D7C")
                add(tipo="mesaCentro", x=mx, y=my, w=1.0 if not vertical else 0.6, d=0.6 if not vertical else 1.0)
            if t == "estar" and w * d > 14:
                encostar("camaCasal", 1.4, 1.9, None, manta="#C9B59A")
            add(tipo="planta", x=c["x0"] + 0.4, y=c["y0"] + 0.4, s=0.9)
        elif t == "jantar":
            add(tipo="mesaJantar", x=cx, y=cy, w=0.85 if w < d else 1.3, d=1.3 if w < d else 0.85)
        elif t == "cozinha":
            comp_max = 0
            lado, pos = None, None
            for l in _lados_por_preferencia(c, vaos, [], True):
                if _prof(c, l) < 1.5:
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
                encostar("geladeira", 0.72, 0.7, restantes)
            if w * d >= 8.5 and min(w, d) >= 2.6:
                add(tipo="mesaJantar", x=cx, y=cy, w=0.85, d=1.2)
        elif t in ("banho", "lavabo"):
            lados = _lados_por_preferencia(c, vaos, jans)
            if min(w, d) >= 1.2 and t == "banho":
                lado, pos = encostar("box", 0.8, 0.85, [l for l in lados if _comp(c, l) >= 1.6], frente=0.3)
            encostar("vaso", 0.4, 0.65, lados, frente=0.3)
            encostar("pia", 0.6, 0.42, list(reversed(lados)), frente=0.3)
        elif t == "servico":
            encostar("tanque", 0.6, 0.5, None, frente=0.4)
            encostar("maquina", 0.6, 0.6, None, frente=0.4)
        elif t == "escritorio":
            encostar("escrivaninha", 1.2, 0.6, None)
            encostar("armario", 1.2, 0.45, None)
        elif t == "garagem":
            add(tipo="carro", x=cx, y=cy, rot=0.0, w=1.75, d=min(4.2, d - 0.6))
        elif t == "varanda":
            if c["nome"].lower().startswith("área gourmet"):
                add(tipo="mesaJantar", x=cx, y=cy, w=1.3 if w > d else 0.85, d=0.85 if w > d else 1.3)
                encostar("bancada", min(2.0, max(w, d) - 1.0), 0.6, None)
            elif min(w, d) >= 1.5:
                add(tipo="planta", x=c["x0"] + 0.4, y=c["y0"] + 0.4, s=0.8)
                add(tipo="poltrona", x=cx, y=cy, rot=0.0, w=0.75, d=0.75)
        elif t in ("patio", "externo"):
            n = max(1, int(w * d / 6))
            for i in range(n):
                add(tipo="planta", x=c["x0"] + (i + 0.5) * w / n, y=cy, s=1.2)
    return out


# ---------------------------------------------------------------- saída
def ordem(planta):
    prio = {"varanda": 0, "garagem": 0, "sala": 1, "estar": 1, "jantar": 2, "cozinha": 3, "servico": 4, "circ": 5,
            "banho": 6, "lavabo": 6, "escritorio": 7, "casal": 8, "dorm": 9, "patio": 10, "externo": 10}
    cs = [c for c in planta["comodos"] if c["tipo"] != "futuro"]
    return [c["id"] for c in sorted(cs, key=lambda c: (prio.get(c["tipo"], 5), c["y0"], c["x0"]))]


def modulo(planta):
    paredes, janelas, portas, moveis = construir(planta)
    r = planta["_r"]
    m = r.metricas
    amb = [{"id": c["id"], "nome": c["nome"], "tipo": c["tipo"], "x0": c["x0"], "y0": c["y0"], "x1": c["x1"], "y1": c["y1"],
            "cor": CORES_AMB.get(c["tipo"], "#EEE"), "piso": PISO.get(c["tipo"], "madeira")}
           for c in planta["comodos"] if c["tipo"] != "futuro"]
    futuros = [{"id": c["id"], "nome": c["nome"], "x0": c["x0"], "y0": c["y0"], "x1": c["x1"], "y1": c["y1"]}
               for c in planta["comodos"] if c["tipo"] == "futuro"]
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

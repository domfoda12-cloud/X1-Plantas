"""Gera o e-book "Que casa cabe no seu lote?" (PDF A4) a partir das 24 plantas validadas.

Uso:
    python3 ebook/gerador/livro.py                 PDF em ebook/saida/ebook.pdf
    python3 ebook/gerador/livro.py --previa DIR    também salva um PNG de cada página em DIR

Tudo sai dos dados: plantas e números de ebook/plantas/projetos.py (via ferramentas/plantas.py),
textos de cada casa de ebook/fichas/textos.py, textos gerais de ebook/gerador/paginas.py
(7 erros, glossário, terreno, próximos passos) e ebook/config.json (título, preço, bônus, contato).
Direção visual: ebook/PLANO-EBOOK.md e a prévia em ebook/visual/plano-visual.html.
"""
import html
import json
import os
import subprocess
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
EBOOK = AQUI.parent
RAIZ = EBOOK.parent
SAIDA = EBOOK / "saida"
sys.path.insert(0, str(RAIZ / "ferramentas"))
sys.path.insert(0, str(AQUI))
sys.path.insert(0, str(EBOOK / "fichas"))
import plantas as PL  # noqa: E402
import planta3d as P3  # noqa: E402
import math  # noqa: E402
import paginas as TX  # noqa: E402
import textos as FICHAS  # noqa: E402

E = html.escape
AVISO = "Planta de referência. O projeto para a prefeitura é assinado por arquiteto ou engenheiro habilitado."
CATEGORIAS = {"C": "Compactas", "E": "Terreno estreito", "F": "Família", "S": "Especiais"}
CORES = {"sala": "#E9D8BD", "estar": "#E9D8BD", "jantar": "#E9D8BD", "cozinha": "#D3E1CC", "servico": "#D9E5D1",
         "banho": "#CFE2E8", "lavabo": "#CFE2E8", "casal": "#EEDCC2", "dorm": "#F1E4CF", "circ": "#F4EFE6",
         "escritorio": "#E4DEF1", "varanda": "#E7E3DA", "garagem": "#DEDCD8", "patio": "#CFE3BB", "externo": "#CFE3BB"}
ABERTOS = {"varanda", "garagem", "patio", "externo"}
ORI = {"norte": "norte", "sul": "sul", "leste": "leste", "oeste": "oeste"}


def m(v):
    return f"{v:.2f}".replace(".", ",")


def m1(v):
    return f"{v:.1f}".replace(".", ",")


# ------------------------------------------------------------------ desenhos (SVG)
def svg_planta(p, nomes=True, cotas=True, pad=0.5, moveis=False):
    """Planta com a frente da casa para baixo: o leitor entra por baixo, como chega da rua."""
    fut = [c for c in p["comodos"] if c["tipo"] == "futuro"]
    Dm = max([p["D"]] + [c["y1"] for c in fut])
    Wm = max([p["W"]] + [c["x1"] for c in fut])
    pb = 1.1 if cotas else pad
    pl = 1.1 if cotas else pad
    Y = lambda y: Dm - y
    s = [f'<svg viewBox="{-pl} {-pad} {Wm + pl + pad} {Dm + pad + pb}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Planta da {E(p["nome"])}">']
    rotulos = []
    for c in p["comodos"]:
        x0, y0, x1, y1, t = c["x0"], c["y0"], c["x1"], c["y1"], c["tipo"]
        w, h = x1 - x0, y1 - y0
        if t == "futuro":
            s.append(f'<rect x="{x0}" y="{Y(y1)}" width="{w}" height="{h}" fill="#FFF6DE" stroke="#E0A92E" stroke-width=".06" stroke-dasharray=".25 .18"/>')
            s.append(f'<text x="{x0 + w / 2}" y="{Y(y0 + h / 2)}" text-anchor="middle" font-size=".28" font-weight="700" fill="#9A6B00">AMPLIAÇÃO</text>')
            s.append(f'<text x="{x0 + w / 2}" y="{Y(y0 + h / 2) + .36}" text-anchor="middle" font-size=".22" fill="#9A6B00">{E(c["nome"].split(" (")[0])}</text>')
            continue
        aberto = t in ABERTOS
        s.append(f'<rect x="{x0}" y="{Y(y1)}" width="{w}" height="{h}" fill="{CORES.get(t, "#EEE")}" '
                 f'stroke="{"#B9B3A8" if aberto else "#2A3340"}" stroke-width="{.03 if aberto else .12}"/>')
        if nomes and min(w, h) >= 1.15 and t not in ("circ", "externo"):
            nome = "PÁTIO" if t == "patio" else c["nome"].upper()
            fs = max(min(.34, (w - .2) / (len(nome) * .74)), .17)
            halo = 'stroke="#FBF8F2" stroke-width=".09" paint-order="stroke" stroke-linejoin="round"'
            rotulos.append(f'<text x="{x0 + w / 2}" y="{Y(y0 + h / 2) - .04}" text-anchor="middle" font-size="{fs:.3f}" font-weight="700" fill="#1E2733" {halo}>{E(nome)}</text>')
            if t not in ABERTOS:
                rotulos.append(f'<text x="{x0 + w / 2}" y="{Y(y0 + h / 2) + .3}" text-anchor="middle" font-size=".22" class="mono" fill="#56616E" {halo}>{m1(w * h)} m²</text>')
    if moveis:
        _, _, portas3d, mov = P3.construir(p)
        for mv in mov:
            rot = math.degrees(mv.get("rot", 0) or 0)
            s.append(f'<g transform="translate({mv["x"]:.3f} {Y(mv["y"]):.3f}) scale(1 -1) rotate({-rot:.2f})">{_movel(mv)}</g>')
        for d in portas3d:
            hx, hy, r = d["x"], d["y"], d["r"]
            ax, ay = hx + r * math.cos(d["a0"]), hy + r * math.sin(d["a0"])
            bx, by = hx + r * math.cos(d["a1"]), hy + r * math.sin(d["a1"])
            s.append(f'<line x1="{hx:.3f}" y1="{Y(hy):.3f}" x2="{ax:.3f}" y2="{Y(ay):.3f}" stroke="#FBF8F2" stroke-width=".16"/>')
            s.append(f'<path d="M{bx:.3f} {Y(by):.3f} A{r} {r} 0 0 1 {ax:.3f} {Y(ay):.3f}" fill="none" stroke="#C2683F" stroke-width=".025" stroke-dasharray=".06 .04"/>')
            s.append(f'<line x1="{hx:.3f}" y1="{Y(hy):.3f}" x2="{bx:.3f}" y2="{Y(by):.3f}" stroke="#C2683F" stroke-width=".04"/>')
    por_id = {c["id"]: c for c in p["comodos"]}
    for cid, lista in p["janelas"].items():
        c = por_id[cid]
        for lado, larg in lista:
            if lado in ("frente", "fundos"):
                yy = c["y0"] if lado == "frente" else c["y1"]
                x, y, w, h = (c["x0"] + c["x1"]) / 2 - larg / 2, Y(yy) - .07, larg, .14
            else:
                xx = c["x0"] if lado == "esq" else c["x1"]
                x, y, w, h = xx - .07, Y((c["y0"] + c["y1"]) / 2 + larg / 2), .14, larg
            s.append(f'<rect x="{x:.3f}" y="{y:.3f}" width="{w:.3f}" height="{h:.3f}" fill="#8ED2FF" stroke="#0B4FA8" stroke-width=".03"/>')
    for porta in p["portas"]:
        if porta[0] == "ext":
            c = por_id[porta[1]]
            if porta[2] == "frente":
                cx = porta[3] if len(porta) > 3 else (c["x0"] + c["x1"]) / 2
                s.append(f'<rect x="{cx - .45:.3f}" y="{Y(c["y0"]) - .1:.3f}" width=".9" height=".2" fill="#FFC857" stroke="#17202B" stroke-width=".03"/>')
    s.extend(rotulos)
    if cotas:
        s.append(f'<g stroke="#0B4FA8" stroke-width=".03" fill="#0B4FA8" font-size=".3" class="mono">'
                 f'<line x1="0" y1="{Dm + .5}" x2="{p["W"]}" y2="{Dm + .5}"/>'
                 f'<line x1="0" y1="{Dm + .38}" x2="0" y2="{Dm + .62}"/><line x1="{p["W"]}" y1="{Dm + .38}" x2="{p["W"]}" y2="{Dm + .62}"/>'
                 f'<text x="{p["W"] / 2}" y="{Dm + .92}" text-anchor="middle" stroke="none">{m(p["W"])} m</text>'
                 f'<line x1="-.5" y1="{Dm - p["D"]}" x2="-.5" y2="{Dm}"/>'
                 f'<text x="-.62" y="{Dm - p["D"] / 2}" text-anchor="middle" stroke="none" transform="rotate(-90 -.62 {Dm - p["D"] / 2})">{m(p["D"])} m</text></g>')
    s.append("</svg>")
    return "".join(s)



def _movel(mv):
    """Símbolo de móvel visto de cima, em coordenadas locais (encosto/cabeceira no lado -y)."""
    t, w, d = mv["tipo"], mv.get("w", .45), mv.get("d", .4)
    L = '#5B6675'
    R = lambda x, y, ww, hh, fill="#FFFFFF", sw=.025, rx=.04: f'<rect x="{x:.3f}" y="{y:.3f}" width="{ww:.3f}" height="{hh:.3f}" rx="{rx}" fill="{fill}" stroke="{L}" stroke-width="{sw}"/>'
    C = lambda x, y, r, fill="#FFFFFF": f'<circle cx="{x:.3f}" cy="{y:.3f}" r="{r:.3f}" fill="{fill}" stroke="{L}" stroke-width=".025"/>'
    if t in ("camaCasal", "camaSolteiro"):
        n = 2 if t == "camaCasal" else 1
        out = R(-w / 2, -d / 2, w, d)
        out += R(-w / 2, -d / 2 + d * .38, w, d * .62, mv.get("manta", "#B9C7D6"), rx=.03)
        lw = (w - .2) / n
        out += "".join(R(-w / 2 + .1 + i * lw + .03, -d / 2 + .08, lw - .06, .3, "#FFFFFF", rx=.05) for i in range(n))
        return out
    if t == "sofa":
        return R(-w / 2, -d / 2, w, d, "#C9D3C6") + R(-w / 2, -d / 2, w, .2, "#AEBDA9") + R(-w / 2, -d / 2, .18, d, "#AEBDA9") + R(w / 2 - .18, -d / 2, .18, d, "#AEBDA9")
    if t == "tapete":
        return f'<rect x="{-w / 2}" y="{-d / 2}" width="{w}" height="{d}" fill="#E8DCC8" stroke="#C9B59A" stroke-width=".03" stroke-dasharray=".12 .08"/>'
    if t == "mesaCentro":
        return R(-w / 2, -d / 2, w, d, "#D8C3A3")
    if t == "mesaJantar":
        cad = "".join(C(sx * (w / 2 + .2), sz, .16) for sx in (-1, 1) for sz in (-.3, .3))
        return cad + R(-w / 2, -d / 2, w, d, "#D8C3A3")
    if t == "bancada":
        return R(-w / 2, -d / 2, w, d, "#EFEDE8") + f'<rect x="{-w / 2 + .3:.3f}" y="{-d / 2 + .1:.3f}" width=".5" height=".38" rx=".06" fill="#DDE6EC" stroke="{L}" stroke-width=".02"/>' + "".join(C(w / 2 - .45 + dx, dy, .08) for dx in (-.15, .15) for dy in (-.12, .12))
    if t == "geladeira":
        return R(-w / 2, -d / 2, w, d, "#EEF1F3") + f'<line x1="{-w / 2}" y1="{-d / 2}" x2="{w / 2}" y2="{d / 2}" stroke="{L}" stroke-width=".02"/>'
    if t in ("tanque", "pia"):
        return R(-w / 2, -d / 2, w, d, "#F4F4F2") + f'<ellipse cx="0" cy=".03" rx="{w * .32:.3f}" ry="{d * .3:.3f}" fill="#DDE6EC" stroke="{L}" stroke-width=".02"/>'
    if t == "maquina":
        return R(-w / 2, -d / 2, w, d, "#F4F4F2") + C(0, 0, min(w, d) * .32, "#DDE6EC")
    if t == "vaso":
        return R(-.18, -.32, .36, .14, "#FFFFFF") + f'<ellipse cx="0" cy=".05" rx=".17" ry=".24" fill="#FFFFFF" stroke="{L}" stroke-width=".025"/>'
    if t == "box":
        return R(-w / 2, -d / 2, w, d, "#E6F0F4") + f'<line x1="{-w / 2}" y1="{d / 2}" x2="{w / 2}" y2="{-d / 2}" stroke="{L}" stroke-width=".02"/>' + C(0, 0, .05)
    if t == "armario":
        n = max(2, round(w / .5))
        return R(-w / 2, -d / 2, w, d, "#F2EEE7") + "".join(f'<line x1="{-w / 2 + w * i / n:.3f}" y1="{-d / 2}" x2="{-w / 2 + w * i / n:.3f}" y2="{d / 2}" stroke="{L}" stroke-width=".015"/>' for i in range(1, n))
    if t == "escrivaninha":
        return R(-w / 2, -d / 2, w, d, "#D8C3A3") + C(0, d / 2 + .25, .2, "#C9D3DC")
    if t == "criado":
        return R(-.22, -.2, .44, .4, "#D8C3A3")
    if t == "planta":
        r = .25 * mv.get("s", 1)
        return f'<circle r="{r:.3f}" fill="#9BBF7A" stroke="#6E8F55" stroke-width=".025"/><circle r="{r * .45:.3f}" fill="#7FA862"/>'
    if t == "carro":
        return f'<rect x="{-w / 2}" y="{-d / 2}" width="{w}" height="{d}" rx=".35" fill="#E2B1A8" stroke="{L}" stroke-width=".03"/><rect x="{-w / 2 + .15}" y="{-d * .2:.3f}" width="{w - .3}" height="{d * .35:.3f}" rx=".15" fill="#B9C7D6" stroke="{L}" stroke-width=".02"/>'
    if t == "poltrona":
        return R(-w / 2, -d / 2, w, d, "#E3C9A6") + R(-w / 2, -d / 2, w, .16, "#CFAE85")
    return ""


def svg_fachada(p, legenda=True):
    """Vista frontal simplificada: o que se vê da rua, com janelas, porta, platibanda e uma pessoa para escala."""
    cs = [c for c in p["comodos"] if c["tipo"] not in ("futuro",)]
    fechados = [c for c in cs if c["tipo"] not in ABERTOS]
    PD, PLAT = 2.8, .6
    W = p["W"]
    H = PD + PLAT
    s = [f'<svg viewBox="-1.6 -.6 {W + 3.2} {H + 1.2}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Vista frontal simplificada">']
    Yv = lambda z: H - z
    # céu suave e chão
    s.append(f'<rect x="-1.6" y="-.6" width="{W + 3.2}" height="{H + .6}" fill="#EEF4FB"/>')
    s.append(f'<rect x="-1.6" y="{H}" width="{W + 3.2}" height=".6" fill="#D9D3C4"/>')
    # para cada faixa de x, o cômodo fechado mais à frente
    xs = sorted({round(v, 3) for c in cs for v in (c["x0"], c["x1"])})
    for a, b in zip(xs, xs[1:]):
        m = (a + b) / 2
        frente = [c for c in fechados if c["x0"] - 1e-6 <= m <= c["x1"] + 1e-6]
        cob = [c for c in cs if c["tipo"] in ("varanda", "garagem") and c["x0"] - 1e-6 <= m <= c["x1"] + 1e-6 and c["y0"] < .01]
        if frente:
            y0 = min(c["y0"] for c in frente)
            tom = "#FBFAF7" if y0 < .01 else "#ECE8E1"
            s.append(f'<rect x="{a:.3f}" y="{Yv(PD + PLAT):.3f}" width="{b - a:.3f}" height="{PD + PLAT:.3f}" fill="{tom}"/>')
        if cob:
            s.append(f'<rect x="{a:.3f}" y="{Yv(PD + .25):.3f}" width="{b - a:.3f}" height=".25" fill="#DCD6CB"/>')
    # colunas das varandas e garagens
    for c in cs:
        if c["tipo"] in ("varanda", "garagem") and c["y0"] < .01:
            for x in (c["x0"] + .08, c["x1"] - .08):
                s.append(f'<rect x="{x - .08:.3f}" y="{Yv(PD):.3f}" width=".16" height="{PD:.3f}" fill="#CFC8BB"/>')
    # contorno
    s.append(f'<line x1="-1.6" y1="{H}" x2="{W + 1.6}" y2="{H}" stroke="#17202B" stroke-width=".05"/>')
    s.append(f'<rect x="0" y="0" width="{W}" height="{PLAT}" fill="#E3DED5"/>')
    # janelas e porta da frente
    # Mesmas posições de porta e janela do motor 3D (ferramentas/planta3d.py): a janela nunca fica sobre a porta
    por_id = {c["id"]: c for c in cs}
    _, jan3d, portas3d, _ = P3.construir(p)
    frontal = lambda c: all(not (o["tipo"] not in ABERTOS and o["y1"] <= c["y0"] + 1e-6 and o["x0"] < c["x1"] and o["x1"] > c["x0"]) for o in cs)
    for j in jan3d:
        c = por_id.get(j["id"])
        x0s, y0s, x1s, y1s = j["seg"]
        if not c or c["tipo"] in ABERTOS or abs(y0s - y1s) > 1e-6 or abs(y0s - c["y0"]) > 1e-6 or not frontal(c):
            continue
        a, b = min(x0s, x1s), max(x0s, x1s)
        pe = j["peitoril"]
        s.append(f'<rect x="{a:.3f}" y="{Yv(2.2):.3f}" width="{b - a:.3f}" height="{2.2 - pe:.3f}" fill="#9CCBE8" stroke="#2A3340" stroke-width=".04"/>')
        s.append(f'<line x1="{(a + b) / 2:.3f}" y1="{Yv(2.2):.3f}" x2="{(a + b) / 2:.3f}" y2="{Yv(pe):.3f}" stroke="#2A3340" stroke-width=".03"/>')
    for d in portas3d:
        # porta de entrada: da rua (ext-*) ou de uma varanda/garagem para um cômodo fechado que se vê da rua
        partes = str(d["id"]).split("-", 1)
        if abs(math.sin(d["a0"])) > 1e-6 or len(partes) != 2:
            continue
        a_id, b_id = partes
        alvo = por_id.get(b_id)
        if not alvo or alvo["tipo"] in ABERTOS or abs(d["y"] - alvo["y0"]) > 1e-6 or not frontal(alvo):
            continue
        if a_id != "ext" and (a_id not in por_id or por_id[a_id]["tipo"] not in ABERTOS):
            continue
        a = d["x"] if abs(d["a0"]) < 1e-6 else d["x"] - d["r"]
        s.append(f'<rect x="{a:.3f}" y="{Yv(2.1):.3f}" width="{d["r"]:.3f}" height="2.1" fill="#B98A5E" stroke="#2A3340" stroke-width=".04"/>')
        s.append(f'<circle cx="{a + d["r"] - .15:.3f}" cy="{Yv(1.05):.3f}" r=".04" fill="#2A3340"/>')
    # enfeites: arbustos e pessoa de 1,70 m para escala
    for x in (-.9, W + .9):
        s.append(f'<circle cx="{x}" cy="{H - .35}" r=".45" fill="#8DB46C"/><circle cx="{x + .3}" cy="{H - .25}" r=".32" fill="#7AA25A"/>')
    px = W + 1.15
    s.append(f'<g fill="#5B6675"><circle cx="{px}" cy="{Yv(1.58):.3f}" r=".12"/><rect x="{px - .14}" y="{Yv(1.45):.3f}" width=".28" height=".65" rx=".1"/>'
             f'<rect x="{px - .12}" y="{Yv(.8):.3f}" width=".1" height=".8"/><rect x="{px + .02}" y="{Yv(.8):.3f}" width=".1" height=".8"/></g>')
    if legenda:
        s.append(f'<text x="{W / 2}" y="{H + .45}" text-anchor="middle" font-size=".26" class="mono" fill="#4F5B69">vista da rua · pessoa de 1,70 m para escala</text>')
    s.append("</svg>")
    return "".join(s)


def svg_lote(p):
    r = p["_r"].metricas
    LW, LD = r["lote"]
    rec = r["recuos"]
    pad, rua = .4, 1.6
    Y = lambda y: LD - y
    fut = [c for c in p["comodos"] if c["tipo"] == "futuro"]
    s = [f'<svg viewBox="{-pad - 1.2} {-pad - .3} {LW + pad * 2 + 2.4} {LD + pad + rua + 1.1}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="A casa no lote mínimo">']
    s.append(f'<rect x="0" y="0" width="{LW}" height="{LD}" fill="#F3E6C4" stroke="#17202B" stroke-width=".07" stroke-dasharray=".3 .15"/>')
    hx, hy = rec["esq"], rec["frente"]
    for c in fut:
        s.append(f'<rect x="{hx + c["x0"]}" y="{Y(hy + c["y1"])}" width="{c["x1"] - c["x0"]}" height="{c["y1"] - c["y0"]}" fill="none" stroke="#E0A92E" stroke-width=".07" stroke-dasharray=".25 .15"/>')
    s.append(f'<rect x="{hx}" y="{Y(hy + p["D"])}" width="{p["W"]}" height="{p["D"]}" fill="#0B4FA8"/>')
    s.append(f'<text x="{hx + p["W"] / 2}" y="{Y(hy + p["D"] / 2) + .2}" text-anchor="middle" font-size=".6" font-weight="800" fill="#fff" class="tit">{p["id"]}</text>')
    s.append(f'<rect x="-1.2" y="{LD + .15}" width="{LW + 2.4}" height="{rua}" fill="#C9CED6"/>')
    s.append(f'<text x="{LW / 2}" y="{LD + .15 + rua / 2 + .18}" text-anchor="middle" font-size=".5" font-weight="700" fill="#4F5B69" letter-spacing=".1">RUA</text>')
    s.append(f'<text x="{LW / 2}" y="-.12" text-anchor="middle" font-size=".42" class="mono" fill="#17202B">{m(LW)} m</text>')
    s.append(f'<text x="-.45" y="{LD / 2}" text-anchor="middle" font-size=".42" class="mono" fill="#17202B" transform="rotate(-90 -.45 {LD / 2})">{m(LD)} m</text>')
    s.append(f'<text x="{LW / 2}" y="{Y(rec["frente"] / 2) + .15}" text-anchor="middle" font-size=".36" class="mono" fill="#6B5A2E">recuo {m1(rec["frente"])} m</text>')
    ang = {"sul": 0, "norte": 180, "leste": 90, "oeste": -90}[r["orientacao"]["melhor"]]
    s.append(f'<g transform="translate({LW + .65} .75) rotate({ang})"><circle r=".55" fill="#fff" stroke="#17202B" stroke-width=".04"/>'
             f'<path d="M0 -.48 L.16 .1 L0 0 L-.16 .1 Z" fill="#C0392B"/>'
             f'<text y="-.6" text-anchor="middle" font-size=".32" font-weight="800" fill="#17202B">N</text></g>')
    s.append("</svg>")
    return "".join(s)


def icone(tipo):
    base = '<svg viewBox="0 0 20 20" class="ico" aria-hidden="true"><circle cx="10" cy="10" r="9.5" fill="#E7EFFA"/>'
    if tipo == "sol":
        raios = "".join(f'<line x1="{10 + 5 * c:.2f}" y1="{10 + 5 * s:.2f}" x2="{10 + 6.6 * c:.2f}" y2="{10 + 6.6 * s:.2f}" stroke="#E0A92E" stroke-width="1.3" stroke-linecap="round"/>'
                        for c, s in [(1, 0), (.707, .707), (0, 1), (-.707, .707), (-1, 0), (-.707, -.707), (0, -1), (.707, -.707)])
        return base + '<circle cx="10" cy="10" r="3.2" fill="#E0A92E"/>' + raios + "</svg>"
    if tipo == "ar":
        return base + "".join(f'<path d="M4 {y} h9 a2 2 0 1 0 -2 -2" fill="none" stroke="#0B4FA8" stroke-width="1.3" stroke-linecap="round"/>' for y in (7, 10.5, 14)) + "</svg>"
    if tipo == "agua":
        return base + '<path d="M10 4 C13 8.5 14.5 10.5 14.5 12.5 A4.5 4.5 0 0 1 5.5 12.5 C5.5 10.5 7 8.5 10 4 Z" fill="#4AA3DF"/></svg>'
    return base + '<path d="M5 15 L10 5 L15 15 Z" fill="none" stroke="#0B4FA8" stroke-width="1.4" stroke-linejoin="round"/></svg>'


def svg_fita(contagem, alto=False):
    W, lo, hi = 1000, 4.2, 14.8
    X = lambda v: (v - lo) / (hi - lo) * W
    s = [f'<svg viewBox="0 0 {W} 150" class="fita" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="none">',
         f'<rect width="{W}" height="150" fill="#FFC857"/>']
    for c in range(int(lo * 10) + 1, int(hi * 10)):
        h = 34 if c % 10 == 0 else 22 if c % 5 == 0 else 12
        s.append(f'<line x1="{X(c / 10):.1f}" y1="0" x2="{X(c / 10):.1f}" y2="{h}" stroke="#1D1A12" stroke-width="{2 if c % 10 == 0 else 1}"/>')
    s.append("</svg>")
    marcas = "".join(
        f'<div class="marca" style="left:{(f - lo) / (hi - lo) * 100:.2f}%"><b>{f} m</b><small>{contagem.get(f, 0) or "—"}{" casas" if contagem.get(f, 0) > 1 else " casa" if contagem.get(f, 0) == 1 else ""}</small></div>'
        for f in range(5, 15))
    return f'<div class="fita-box">{"".join(s)}<div class="marcas">{marcas}</div></div>'


def galeria(plantas, ids, legenda=""):
    """Faixa decorativa de plantas em miniatura (sem nomes), para fechar páginas de texto."""
    por_id = {p["id"]: p for p in plantas}
    itens = "".join(f'<figure>{svg_planta(por_id[i], nomes=False, cotas=False, pad=.2)}<figcaption>{i}</figcaption></figure>' for i in ids)
    return f'<div class="galeria">{itens}</div>' + (f'<p class="galeria-leg">{E(legenda)}</p>' if legenda else "")


# ------------------------------------------------------------------ páginas
class Livro:
    def __init__(self, plantas, config):
        self.plantas = plantas
        self.config = config
        self.paginas = []
        self.inicio = {}

    def pagina(self, conteudo, classe="", orelha=None, rodape=True, aviso=False):
        n = len(self.paginas) + 1
        par = n % 2 == 0
        tab = ""
        if orelha is not None:
            top = 30 + (orelha - 5) * 24
            tab = f'<div class="orelha {"esq" if par else "dir"}" style="top:{top}mm">{orelha} m</div>'
        rod = ""
        if rodape:
            rod = (f'<div class="rodape {"par" if par else "impar"}"><span class="num">{n}</span>'
                   f'<span>{AVISO if aviso else E(self.config.get("titulo_curto", "Que casa cabe no seu lote?"))}</span></div>')
        self.paginas.append(f'<section class="pagina {classe}">{tab}<div class="miolo">{conteudo}</div>{rod}</section>')
        return n


def lote_frente(p):
    return p["_r"].metricas["lote_comercial"][0]


def montar(plantas, config, numeros):
    L = Livro(plantas, config)
    contagem = {}
    for p in plantas:
        contagem[lote_frente(p)] = contagem.get(lote_frente(p), 0) + 1
    titulo = config.get("titulo", "Que casa cabe no seu lote?")
    if titulo.startswith("["):
        titulo = "Que casa cabe no seu lote?"

    # 1. capa
    L.pagina(f"""
      <div class="capa-topo"><span class="eti">{len(plantas)} PLANTAS DE CASAS TÉRREAS · {E(config.get('ano', '2026'))}</span>
        <h1 class="capa-titulo">{E(titulo)}</h1>
        <p class="capa-sub">Casas organizadas pela frente do terreno. Mede o seu lote, acha a marca na fita, abre a página.</p></div>
      <div class="capa-planta">{svg_planta(next(p for p in plantas if p['id'] == config.get('planta_da_capa', 'C01')), nomes=True, cotas=False, moveis=True)}</div>
      {svg_fita(contagem)}""", "capa", rodape=False)

    # 2. aviso e como usar
    L.pagina(f"""
      <span class="sobre">Antes de começar</span><h2>Como usar este e-book</h2>
      <ol class="passos3">
        <li><b>Meça a frente do seu lote.</b><span>Com a trena, do muro de um vizinho ao do outro. Essa medida é a porta de entrada do e-book.</span></li>
        <li><b>Ache as casas que cabem.</b><span>Na página {numeros['lote']}, cada largura de lote leva às casas que cabem nela. A aba amarela na borda das páginas faz o mesmo quando você folheia.</span></li>
        <li><b>Leve a escolhida ao seu engenheiro.</b><span>Cada casa explica por que foi desenhada assim e traz as perguntas certas para a primeira conversa.</span></li>
      </ol>
      <div class="caixa amarela"><h3>Planta de referência</h3>{TX.AVISO_COMPLETO}</div>""")

    # 3. ache pelo lote
    linhas = []
    for f in sorted(contagem):
        casas = [p for p in plantas if lote_frente(p) == f]
        itens = "".join(f'<li><b>{p["id"]}</b> {E(p["nome"])} <span>{p["_r"].metricas["area_fechada"]:.0f} m² · {E(p["quartos_txt"].replace(" (+1 depois)", ""))}</span><i>p. {numeros[p["id"]]}</i></li>' for p in casas)
        linhas.append(f'<div class="faixa"><div class="faixa-m">{f} m</div><ul>{itens}</ul></div>')
    L.pagina(f"""
      <span class="sobre">Comece aqui</span><h2>Ache pelo seu lote</h2>
      <p class="abertura">A casa precisa caber com os recuos. A medida ao lado é a <b>menor frente</b> em que a casa cabe com os recuos de referência (3 m na frente, 1,5 m nos fundos e numa lateral; nas casas de corredor, nas duas; na de esquina, 3 m na rua lateral). Um lote mais largo também serve, se tiver o comprimento indicado e se os recuos da sua cidade não forem maiores.</p>
      <div class="faixas">{''.join(linhas)}</div>""", "lote")

    # 4. ache pelo jeito da família
    grupos = [
        ("Mora sozinho ou vai alugar", ["C02", "E03"]),
        ("Quer sair do aluguel e crescer depois", ["C03", "C01", "C05"]),
        ("Casal com 1 ou 2 filhos", ["C01", "C04", "C06", "E02", "E04", "E05"]),
        ("Família de 4 ou mais", ["F01", "F02", "F03", "F04", "E07", "S09"]),
        ("Trabalha em casa", ["S04"]),
        ("Gosta de receber", ["S07", "E06", "F05"]),
        ("Casa para a vida toda, sem degrau", ["S03"]),
        ("Casa de praia ou de fim de semana", ["S05", "C07"]),
    ]
    por_id = {p["id"]: p for p in plantas}
    blocos = "".join(f'<div class="grupo"><h3>{E(t)}</h3><p>' + " · ".join(f'<b>{i}</b> {E(por_id[i]["nome"])} <i>p. {numeros[i]}</i>' for i in ids) + "</p></div>" for t, ids in grupos)
    L.pagina(f"""<span class="sobre">Comece aqui</span><h2>Ache pelo jeito da sua família</h2>
      <p class="abertura">Se ainda não tem o lote, escolha pelo jeito de morar. Depois confira na página {numeros['lote']} se cabe.</p>
      <div class="grupos">{blocos}</div>
      {galeria(plantas, ["C02", "C03", "C06", "F01", "S03", "S07"], "Seis jeitos de morar, seis casas diferentes.")}""")

    # 5–6. como ler + glossário
    c01 = por_id["C01"]
    legenda = "".join(f"<li><b>{E(t)}.</b> {E(d)}</li>" for t, d in TX.LEGENDA_LEITURA)
    L.pagina(f"""<span class="sobre">Antes de escolher</span><h2>Como ler uma planta</h2>
      <p class="abertura">Todas as casas deste e-book são desenhadas do mesmo jeito: a <b>rua fica embaixo</b>, cada cômodo tem nome e área, as janelas são azuis e a porta de entrada é amarela.</p>
      <div class="leitura"><div class="leitura-fig">{svg_planta(c01, moveis=True)}</div><ul class="legenda">{legenda}</ul></div>
      <div class="caixa azul"><b>Dica:</b> a área do cômodo é a área por dentro das paredes. A "área fechada" da ficha soma a casa coberta, sem varanda e garagem.</div>""")
    termos = "".join(f"<div><dt>{E(t)}</dt><dd>{E(d)}</dd></div>" for t, d in TX.GLOSSARIO)
    L.pagina(f"""<span class="sobre">Antes de escolher</span><h2>As palavras da obra</h2>
      <p class="abertura">As palavras que aparecem nas plantas, na prefeitura e na conversa com o engenheiro.</p>
      <dl class="glossario">{termos}</dl>""")

    # 7–8. os 7 erros
    def erro(i, t, porque, certo):
        return f'<div class="erro"><div class="erro-n">{i}</div><div><h3>{"O mais caro: " if i == 7 else ""}{E(t)}</h3><p>{E(porque)}</p><p class="certo"><b>O jeito certo:</b> {certo}</p></div></div>'
    bl = [erro(i, *e) for i, e in enumerate(TX.ERROS, start=1)]
    L.pagina(f'<span class="sobre">Antes da laje</span><h2>Os 7 erros que saem caro</h2><p class="abertura">Cada casa deste e-book mostra quais desses erros ela evita. Use como lista de conferência antes de fechar a sua planta.</p>{"".join(bl[:4])}')
    L.pagina(f'<span class="sobre">Antes da laje</span>{"".join(bl[4:])}<div class="caixa amarela"><b>Cada item que você confere agora é uma parede que não vai ser quebrada depois.</b></div>')

    # 9. índice
    linhas = "".join(
        f'<tr><td class="mono">{p["id"]}</td><td>{E(p["nome"])}</td><td class="n">{p["_r"].metricas["area_fechada"]:.0f} m²</td>'
        f'<td>{E(p["quartos_txt"].replace(" (+1 depois)", "+1"))}</td><td class="n">{p["banheiros"]}</td>'
        f'<td class="n">{lote_frente(p)} x {p["_r"].metricas["lote_comercial"][1]}</td><td class="n">{numeros[p["id"]]}</td></tr>'
        for p in plantas)
    L.pagina(f"""<span class="sobre">Índice rápido</span><h2>As {len(plantas)} casas</h2>
      <table class="indice"><thead><tr><th>ID</th><th>Casa</th><th>Área</th><th>Quartos</th><th>Banh.</th><th>Lote mín.</th><th>Pág.</th></tr></thead><tbody>{linhas}</tbody></table>""")

    # as casas
    for p in plantas:
        dupla(L, p, por_id, numeros)

    # terreno
    L.pagina(f"""<span class="sobre">Depois de escolher</span><h2>Terreno e recuos</h2>
      <p class="abertura">A planta só serve se couber nas regras do seu lote. Confira <b>antes</b> de escolher, não depois de pagar o projeto.</p>
      <div class="duas">
        <div><h3>O que a prefeitura define</h3><ul class="lista">
          <li><b>Recuos:</b> distância mínima da casa até a rua, os vizinhos e os fundos.</li>
          <li><b>Taxa de ocupação:</b> quanto do lote a casa pode cobrir.</li>
          <li><b>Coeficiente de aproveitamento:</b> quanto se pode construir no total.</li>
          <li><b>Permeabilidade:</b> quanto do lote fica sem piso.</li></ul>
          <h3>Onde descobrir</h3><ul class="lista">
          <li>No Plano Diretor, na lei de zoneamento e no código de obras da sua cidade.</li>
          <li>Melhor: peça na prefeitura a consulta prévia do seu lote (leve a matrícula ou o IPTU).</li>
          <li>Em condomínio, leia também o regulamento.</li>
          <li>O Código Civil (art. 1.301) proíbe janela a menos de 1,5 m da divisa com o vizinho.</li></ul></div>
        <div class="caixa azul"><h3>A conta que você faz em casa</h3><p>(frente − recuos laterais) × (fundo − recuo da frente − recuo dos fundos) = espaço para a casa.</p>
          <p>Lote 10 x 20 com recuo de 3 m na frente, 1,5 m numa lateral e 1,5 m nos fundos: sobram 8,5 x 15,5 m. Cabem as casas de até 8,50 m de largura e 15,50 m de comprimento, se a taxa de ocupação da sua cidade deixar. A lateral sem recuo só vale se a prefeitura permitir encostar na divisa, e essa parede fica sem janela.</p>
          <p class="pequeno">Exemplo com recuos de referência. Os do seu lote são os da sua prefeitura.</p></div></div>
      <div class="lotes-ex">{''.join(f'<figure>{svg_lote(por_id[i])}<figcaption>{i} no lote de {lote_frente(por_id[i])} m</figcaption></figure>' for i in ["E03", "C01", "F02"])}</div>""", "texto")
    campos = ["Endereço do lote", "Frente (m)", "Fundo (m)", "Recuo da frente (m)", "Recuos laterais (m)",
              "Recuo dos fundos (m)", "Taxa de ocupação (%)", "Permeabilidade (%)", "Lado do nascente (leste)",
              "Regras do condomínio", "Casas que cabem (IDs)"]
    L.pagina(f'<span class="sobre">Depois de escolher</span><h2>Ficha do meu terreno</h2><p class="abertura">Preencha com os dados da prefeitura e leve junto na primeira conversa com o engenheiro.</p><div class="preencher">{"".join(f"<div>{c}</div>" for c in campos)}</div>')

    # próximos passos
    passos = [
        ("Escolha 2 ou 3 casas", "Pela frente do lote e pelo jeito da família. Anote os IDs."),
        ("Confira as regras do seu lote", "Faça a consulta prévia na prefeitura e preencha a ficha do terreno."),
        ("Contrate um profissional habilitado", "Arquiteto (CAU) ou engenheiro civil (CREA). Ele adapta a planta ao terreno, ao sol e às regras da cidade e emite a RRT ou a ART."),
        ("Aprove o projeto na prefeitura", "Com o projeto legal aprovado, sai o alvará de construção."),
        ("Projetos complementares e orçamento", "Estrutural, elétrico e hidráulico. Com eles o orçamento deixa de ser chute."),
        ("Construa com acompanhamento", "A obra precisa de responsável técnico, com ART ou RRT. Se for financiar, pergunte ao banco quais documentos ele pede."),
        ("Regularize a casa pronta", "Habite-se na prefeitura e averbação na matrícula, no cartório."),
    ]
    L.pagina(f'<span class="sobre">Depois de escolher</span><h2>Do e-book até a chave na mão</h2><ol class="passos">{"".join(f"<li><b>{t}</b><span>{d}</span></li>" for t, d in passos)}</ol>{galeria(plantas, ["C04", "E05", "F03", "S05"])}', "texto")

    # bônus e contato
    bonus = [b for b in config.get("bonus", []) if not b.startswith("[")]
    contato = config.get("contato", "")
    L.pagina(f"""<span class="sobre">Fim (e começo da obra)</span><h2>O que vem junto</h2>
      {'<ul class="lista">' + ''.join(f'<li>{E(b)}</li>' for b in bonus) + '</ul>' if bonus else '<p class="pendente">[bônus: decisão do dono]</p>'}
      <h3>Novas casas</h3><p>Este e-book cresce em levas.{' ' + E(config['promessa_atualizacao']) if config.get('promessa_atualizacao') else ''}</p>
      <h3>Dúvidas</h3><p>{E(contato) if contato and not contato.startswith('[') else '<span class="pendente">[contato do parceiro]</span>'}</p>
      {svg_fita(contagem)}""", "fim")
    return L


def dupla(L, p, por_id, numeros):
    r = p["_r"].metricas
    t = FICHAS.TEXTOS.get(p["id"], {})
    f = lote_frente(p)
    quartos = p["quartos_txt"].replace(" (+1 depois)", "")
    pens = PL.pensou(p)
    g = t.get("gancho", "")
    if g and (f"{f} m de frente" not in g or (f"{r['area_fechada']:.0f} m²" not in g and "m²" in g)):
        print(f"AVISO: gancho de {p['id']} não bate com o validador ({f} m, {r['area_fechada']:.0f} m²): {g}")
    erros = t.get("erros", [1, 2, 4])
    erros_html = "".join(f'<li><span class="erro-mini">{n}</span>{E(TX.ERROS[n - 1][0])}</li>' for n in erros)
    cat = CATEGORIAS[p["id"][0]]
    L.pagina(f"""
      <div class="cab"><span class="mono id">{p['id']} · {cat.upper()} · LOTE A PARTIR DE {f} x {r['lote_comercial'][1]} M</span><h2 class="nome">{E(p['nome'])}</h2>
        <p class="gancho">{E(t.get('gancho', f'{f} m de frente. {quartos}. {r["area_fechada"]:.0f} m².'))}</p></div>
      <div class="planta-grande">{svg_planta(p, moveis=True)}</div>
      <div class="duas"><div><h4>Para quem é</h4><p>{E(t.get('para_quem', ''))}</p></div>
        <div><h4>Erros que esta casa evita</h4><ul class="erros-mini">{erros_html}</ul></div></div>""",
             "casa esq", orelha=f, aviso=True)
    nao = t.get("nao_serve")
    nao_html = ""
    if nao:
        alvo = nao[1]
        nao_html = f'<div><h4>Para quem não serve</h4><p>{E(nao[0])} Veja a <b>{alvo} {E(por_id[alvo]["nome"])}</b>, p. {numeros[alvo]}.</p></div>'
    perg = t.get("perguntas", [])
    linha = lambda a, b, c="": f'<div class="r-l"><span>{a}</span><b>{b}</b><span>{c}</span></div>'
    L.pagina(f"""
      <div class="cab"><span class="mono id">{p['id']} · A CASA NO SEU LOTE</span><h2 class="nome">Cabe? Veja.</h2></div>
      <div class="lado"><div class="lote-fig">{svg_lote(p)}</div>
        <div class="rotulo"><div class="r-tit">INFORMAÇÃO DA CASA</div>
          <div class="r-por">Porção de 1 lote de {f} x {r['lote_comercial'][1]} m</div>
          <div class="r-cab"><span></span><span>nesta casa</span><span>referência</span></div>
          {linha('Área fechada', f"{r['area_fechada']:.0f} m²")}
          {linha('Medidas da casa', f"{m(p['W'])} x {m(p['D'])} m")}
          {linha('Varanda e garagem', f"{r['area_coberta_aberta']:.0f} m²" if r['area_coberta_aberta'] else '—')}
          {linha('Quartos', E(quartos))}
          {linha('Banheiros', p['banheiros'])}
          {linha('Corredor', f"{r['circulacao'] * 100:.0f}%" if r['circulacao'] else 'externo', 'até 14%')}
          {linha('Janela nos quartos', '✓', '1/6 do piso')}
          {linha('Melhor frente', ORI[r['orientacao']['melhor']])}
          {linha('Pode espelhar', 'sim', 'troca o lado')}
          <div class="r-nota">Conferido pelo validador do X1-Plantas com recuos de referência. Confira os da sua cidade.</div></div></div>
      {('<div class="atencao"><h4>Atenção: leve ao engenheiro</h4><ul>' + ''.join(f'<li>{E(a)}</li>' for a in p['_r'].avisos + p['_r'].info) + '</ul></div>') if (p['_r'].avisos or p['_r'].info) else ''}
      <div class="fachada"><h4>Vista da rua (simplificada)</h4>{svg_fachada(p)}</div>
      <div><h4>Por que esta planta é assim</h4><div class="pensou">
        {''.join(f'<div>{icone(ic)}<p>{E(x)}</p></div>' for ic, x in zip(['sol', 'ar', 'agua', 'seta'], pens))}</div></div>
      <div class="duas">{nao_html}<div><h4>Leve ao seu engenheiro</h4><ul class="perg">{''.join(f'<li>{E(q)}</li>' for q in perg)}</ul></div></div>""",
             "casa dir", orelha=f, aviso=True)


# ------------------------------------------------------------------ saída
CSS = (AQUI / "livro.css").read_text(encoding="utf-8")


def montar_gratis(plantas, config, pid):
    """Planta grátis do funil: a página dupla de uma casa e uma página que mostra o que mais existe (ímã)."""
    L = Livro(plantas, config)
    por_id = {p["id"]: p for p in plantas}
    numeros = {p["id"]: "e-book" for p in plantas}
    numeros["lote"] = 3
    L.paginas = []
    dupla(L, por_id[pid], por_id, numeros)
    contagem = {}
    for p in plantas:
        contagem[lote_frente(p)] = contagem.get(lote_frente(p), 0) + 1
    p = por_id[pid]
    f = lote_frente(p)
    fundo = p["_r"].metricas["lote_comercial"][1]
    mesmas = [q for q in plantas if lote_frente(q) <= f and q["_r"].metricas["lote_comercial"][1] <= fundo and q["id"] != pid]
    titulo_ima = "No seu lote cabem mais casas"
    frase_ima = (f"Num lote de {f} x {fundo} m, com os recuos de referência, cabem outras {len(mesmas)} casas do e-book, "
                 "cada uma com a casa no lote, a \"Informação da casa\" e o porquê de cada escolha.")
    legenda_ima = f"Algumas das casas que também cabem num lote de {f} x {fundo} m."
    if not mesmas:
        # casa do menor lote: mostra o que cabe com um pouco mais de terreno
        mesmas = sorted([q for q in plantas if q["id"] != pid], key=lambda q: (lote_frente(q), q["_r"].metricas["area_fechada"]))[:6]
        titulo_ima = "E se o lote for um pouco maior?"
        frase_ima = (f"A {p['nome']} é a casa do e-book para o lote de {f} m. Com um pouco mais de frente, as opções crescem: "
                     f"o e-book tem {len(plantas)} casas, cada uma com o lote mínimo calculado.")
        legenda_ima = "As casas dos próximos tamanhos de lote."
    L.pagina(f"""<span class="sobre">Essa foi 1 de {len(plantas)}</span><h2>{titulo_ima}</h2>
      <p class="abertura">A {E(p['nome'])} cabe a partir de {f} m de frente. {E(frase_ima)}</p>
      {galeria(plantas, [q['id'] for q in mesmas[:6]], legenda_ima)}
      <div class="caixa amarela"><h3>Me fala a frente do seu lote</h3><p>Responde aqui no WhatsApp com a medida que eu te digo quais casas cabem nele com os recuos de referência. Os da sua cidade, você confirma na prefeitura.</p></div>
      {svg_fita(contagem)}""", "fim")
    return L


def gerar(previa=None):
    config = json.loads((EBOOK / "config.json").read_text(encoding="utf-8"))
    plantas = PL.carregar()
    for p in plantas:
        if p["_r"].erros:
            sys.exit(f"{p['id']} tem erro no validador: corrija antes de gerar o e-book")
    ordem = "CEFS"
    plantas.sort(key=lambda p: (ordem.index(p["id"][0]), p["id"]))
    # 1ª passada descobre as páginas; a 2ª escreve os números certos
    numeros = {"lote": 3, **{p["id"]: 0 for p in plantas}}
    for _ in range(2):
        L = montar(plantas, config, numeros)
        novos = {"lote": 3}
        n = 10
        for p in plantas:
            novos[p["id"]] = n
            n += 2
        numeros = novos
    SAIDA.mkdir(exist_ok=True)
    doc = (f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>{E(config.get("titulo", "E-book"))}</title>'
           f'<style>{CSS}</style></head><body>{"".join(L.paginas)}</body></html>')
    arq = SAIDA / "ebook.html"
    arq.write_text(doc, encoding="utf-8")
    env = dict(os.environ)
    try:
        env["NODE_PATH"] = subprocess.run(["npm", "root", "-g"], capture_output=True, text=True).stdout.strip()
    except FileNotFoundError:
        pass
    cmd = ["node", str(AQUI / "pdf.cjs"), str(arq), str(SAIDA / "ebook.pdf")] + ([str(previa)] if previa else [])
    r = subprocess.run(cmd, env=env, capture_output=True, text=True)
    print(r.stdout.strip(), r.stderr.strip())
    print(f"{len(L.paginas)} páginas, {len(plantas)} casas")
    gratis = config.get("plantas_gratis") or [config.get("planta_gratis", "C01")]
    for pid in gratis:
        G = montar_gratis(plantas, config, pid)
        arq = SAIDA / f"planta-gratis-{pid}.html"
        arq.write_text(doc.split("<body>")[0] + "<body>" + "".join(G.paginas) + "</body></html>", encoding="utf-8")
        r = subprocess.run(["node", str(AQUI / "pdf.cjs"), str(arq), str(SAIDA / f"planta-gratis-{pid}.pdf")], env=env, capture_output=True, text=True)
        print(r.stdout.strip(), r.stderr.strip())


if __name__ == "__main__":
    prev = None
    if "--previa" in sys.argv:
        prev = Path(sys.argv[sys.argv.index("--previa") + 1]).resolve()
    gerar(prev)

"""Antes e depois de uma planta, para o dono ver o conserto com os olhos (pedido dele, 23/11/2026).

Desenha as duas plantas lado a lado no mesmo desenho do e-book (livro.svg_planta, estilo "revista"), marca com um
círculo vermelho tracejado e um número cada ponto que mudou (portas, janelas e paredes comparadas sozinhas), põe a
legenda numerada embaixo e a faixa "O que NÃO muda" (área, lote, quartos e banheiros, do validador). PNG de 2160 px.

Uso:
    python3 ferramentas/antes-depois.py C01 ebook/plantas/rascunhos/C01J.py --variante c \\
        --legenda "A porta saiu daqui" --legenda "e veio para cá" --saida ebook/plantas/rascunhos/demo.png
    Cada planta é um id oficial (ebook/plantas/projetos.py) ou um rascunho .py (ebook/plantas/rascunhos/).
    --legenda: uma frase por ponto, na ordem dos números (repita a opção ou separe com "|").
    --ponto X,Y[,raio]: ponto marcado à mão, em metros (X da esquerda, Y da frente); soma aos achados sozinhos.
        Casa redesenhada inteira: "X,Y[,raio];X2,Y2[,raio2]" marca um lugar no antes e outro no depois ("-" = não tem).
    --nota: uma frase embaixo da faixa dos números (ex.: "Ela não cabe mais num lote de 5 x 20 m").
    --sem-auto: só os pontos à mão.  --titulo: título de cima (padrão: o nome da casa).
    --dividir: duas imagens, <saida>-1.png (as duas plantas e a faixa "o que muda") e <saida>-2.png (os pontos de
        perto), cada uma com até 2160 x 4000 px, para o WhatsApp não encolher.
"""
import argparse
import contextlib
import html
import io
import os
import re
import runpy
import subprocess
import sys
import tempfile
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(RAIZ / "ferramentas"), str(RAIZ / "ebook" / "plantas"), str(RAIZ / "ebook" / "gerador")]
import plantas as PL  # noqa: E402
import planta3d as P3  # noqa: E402
import livro  # noqa: E402

E = html.escape
VERM = "#D62828"
LIMITE = 2000  # altura máxima de cada parte com --dividir, em px de CSS (a imagem sai com o dobro: 4000 px)


def carregar(ref, variante):
    """Id oficial ou rascunho .py. O rascunho roda com a variante em sys.argv[1], sem imprimir e sem regravar a prévia."""
    if not ref.endswith(".py"):
        todas = {p["id"]: p for p in PL.carregar()}
        if ref not in todas:
            sys.exit(f"planta {ref} não existe em projetos.py")
        return todas[ref]
    arq = (RAIZ / ref) if not Path(ref).is_absolute() else Path(ref)
    argv, previa = sys.argv, PL.previa
    sys.argv, PL.previa = [str(arq)] + ([variante] if variante else []), (lambda *a, **k: None)
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            ns = runpy.run_path(str(arq), run_name="rascunho")
    finally:
        sys.argv, PL.previa = argv, previa
    p = ns.get("p")
    if not isinstance(p, dict) or "comodos" not in p:
        sys.exit(f"{ref}: o rascunho precisa deixar a planta na variável p")
    if not p.get("janelas"):
        PL.auto_janelas(p)
    p["_r"] = PL.validar(p)
    return p


# ------------------------------------------------------------------ o que mudou
def _amostras(a, b, c, d, passo=.05):
    n = max(1, round(max(abs(c - a), abs(d - b)) / passo))
    return {(round(a + (c - a) * k / n, 2), round(b + (d - b) * k / n, 2)) for k in range(n + 1)}


def pecas(p):
    """Portas, janelas e paredes da planta, cada uma com a sua caixa (em metros, frente em y=0)."""
    paredes, janelas, portas, _ = P3.construir(p)
    out = []
    for d in portas:
        (hx, hy), (ax, ay), (bx, by) = PL.porta_dobradica(p, d)
        out.append(("porta", (round(hx, 2), round(hy, 2), round(ax, 2), round(ay, 2)), (min(hx, ax), min(hy, ay), max(hx, ax), max(hy, ay))))
    for j in janelas:
        x0, y0, x1, y1 = j["seg"]
        out.append(("janela", tuple(round(v, 2) for v in j["seg"]), (min(x0, x1), min(y0, y1), max(x0, x1), max(y0, y1))))
    pts = set()
    for a, b, c, d in paredes:
        pts |= _amostras(a, b, c, d)
    return out, pts


def mudancas(pa, pb):
    """Caixas do que existe numa planta e não na outra, juntadas quando ficam a menos de 20 cm uma da outra."""
    A, wa = pecas(pa)
    B, wb = pecas(pb)
    ka, kb = {(t, k) for t, k, _ in A}, {(t, k) for t, k, _ in B}
    itens = [bb for t, k, bb in A if (t, k) not in kb] + [bb for t, k, bb in B if (t, k) not in ka]
    itens += [(x, y, x, y) for x, y in (wa ^ wb)]
    perto = lambda g, h: g[0] - .2 <= h[2] and h[0] - .2 <= g[2] and g[1] - .2 <= h[3] and h[1] - .2 <= g[3]
    grupos = list(itens)
    mudou = True
    while mudou:
        mudou = False
        for i, g in enumerate(grupos):
            h = next((h for h in grupos[i + 1:] if perto(g, h)), None)
            if h:
                grupos.remove(g); grupos.remove(h)
                grupos.append((min(g[0], h[0]), min(g[1], h[1]), max(g[2], h[2]), max(g[3], h[3])))
                mudou = True
                break
    return [((g[0] + g[2]) / 2, (g[1] + g[3]) / 2, max((g[2] - g[0]) / 2 + .15, .55), max((g[3] - g[1]) / 2 + .15, .55)) for g in grupos]


def conflitos(p):
    """Centro de cada porta com janela em cima (planta3d.janelas_sobre_portas)."""
    _, _, portas, _ = P3.construir(p)
    por_id = {d["id"]: d for d in portas}
    out = []
    for pid, _ in P3.janelas_sobre_portas(p):
        (hx, hy), (ax, ay), _ = PL.porta_dobradica(p, por_id[pid])
        out.append(((hx + ax) / 2, (hy + ay) / 2))
    return out


# ------------------------------------------------------------------ desenho
def dentro(ponto, problemas):
    if ponto is None:
        return False
    x, y, rx, ry = ponto
    return any(abs(px - x) <= rx and abs(py - y) <= ry for px, py in problemas)


ETIQ = re.compile(r'<g transform="translate\(([-\d.]+) ([-\d.]+)\) scale\(([\d.]+)\) translate\([^)]*\)">(.*?)</g>')
RECT = re.compile(r'<rect x="([-\d.]+)" y="([-\d.]+)" width="([\d.]+)" height="([\d.]+)"')
TUDO = (-1e9, -1e9, 1e9, 1e9)  # caixa que nunca cabe no recorte: sai sempre do "de perto"


def textos(svg):
    """Onde há letra no SVG do e-book: (início, fim, caixa). Etiquetas dos cômodos (a pílula branca, já na escala
    dela), a seta ENTRADA, "RUA", "divisa", as cotas e a régua de escala (as duas últimas com caixa TUDO)."""
    out = []
    for m in ETIQ.finditer(svg):
        cx, cy, k = (float(v) for v in m.groups()[:3])
        r = RECT.findall(m.group(4))
        if len(r) < 2:
            continue
        x, y, w, h = (float(v) for v in r[1])  # a 1a é a sombra; a 2a, a pílula
        out.append((m.start(), m.end(), (cx + (x - cx) * k, cy + (y - cy) * k, cx + (x + w - cx) * k, cy + (y + h - cy) * k)))
    for m in re.finditer(r'<g><path d="M([-\d.]+) ([-\d.]+) l-\.2 \.22.*?ENTRADA</text></g>', svg):
        cx, cy = float(m.group(1)), float(m.group(2)) + .32
        out.append((m.start(), m.end(), (cx - .55, cy - .34, cx + .55, cy + .45)))
    for m in re.finditer(r'<text x="([-\d.]+)" y="([-\d.]+)"[^>]*>RUA</text>', svg):
        x, y = float(m.group(1)), float(m.group(2))
        out.append((m.start(), m.end(), (x - .35, y - .2, x + .35, y + .03)))
    for m in re.finditer(r'<text [^>]*>divisa</text>|<g stroke="[^"]+" stroke-width="\.022".*?</g>|<g font-size="\.15" class="mono".*?</g>', svg):
        out.append((m.start(), m.end(), TUDO))
    return out


def _cruza(a, b):
    return max(0., min(a[2], b[2]) - max(a[0], b[0])) * max(0., min(a[3], b[3]) - max(a[1], b[1]))


def marcar(p, svg, pontos, problemas, enfeites=True):
    """Põe círculos, números e a etiqueta "janela em cima da porta" no próprio SVG do e-book (mesmas coordenadas).
    O círculo entra por baixo das etiquetas dos cômodos (o nome continua legível); o número vai para o lado do
    círculo que não cobre etiqueta nem outro número. enfeites=False: só o círculo (para o "de perto")."""
    Dm = max([p["D"]] + [c["y1"] for c in p["comodos"] if c["tipo"] == "futuro"])
    vb = [float(v) for v in svg.split('viewBox="', 1)[1].split('"', 1)[0].split()]
    Y = lambda y: Dm - y
    ocupado = [bb for _, _, bb in textos(svg) if bb is not TUDO]
    cotas = [(-.2, -1.3, p["W"] + .2, -.86), (-1.25, 0, -.55, Dm)]  # as duas cotas da casa (em cima e à esquerda)
    baixo, cima = [], []
    for n, pt in enumerate(pontos, 1):
        if pt is None:  # ponto que só existe do outro lado
            continue
        x, y, rx, ry = pt
        if x - rx > p["W"] + .5 or y - ry > Dm + .5:
            continue
        cx, cy = x, Y(y)
        baixo.append(f'<ellipse cx="{cx:.3f}" cy="{cy:.3f}" rx="{rx:.3f}" ry="{ry:.3f}" fill="{VERM}" fill-opacity=".07" stroke="{VERM}" stroke-width=".085" stroke-dasharray=".26 .14"/>')
        if not enfeites:
            continue
        lugares = []
        for k, (dx, dy) in enumerate(((-.72, -.72), (.72, -.72), (-.72, .72), (.72, .72), (0, -1), (-1, 0), (1, 0), (0, 1))):
            bx = min(max(cx + rx * dx, vb[0] + .4), vb[0] + vb[2] - .4)
            by = min(max(cy + ry * dy, vb[1] + .4), vb[1] + vb[3] - .4)
            caixa = (bx - .4, by - .4, bx + .4, by + .4)
            lugares.append((round(sum(_cruza(caixa, o) for o in ocupado + cotas), 3), k, bx, by, caixa))
        _, _, bx, by, caixa = min(lugares)
        ocupado.append(caixa)
        cima.append(f'<circle cx="{bx:.3f}" cy="{by:.3f}" r=".36" fill="{VERM}" stroke="#fff" stroke-width=".07"/>'
                    f'<text x="{bx:.3f}" y="{by + .17:.3f}" text-anchor="middle" font-family="Inter" font-weight="800" font-size=".5" fill="#fff">{n}</text>')
        if dentro((x, y, rx, ry), problemas):
            txt = "janela em cima da porta"
            lw = len(txt) * .205 + .4
            tx = min(max(cx, vb[0] + lw / 2 + .05), vb[0] + vb[2] - lw / 2 - .05)
            # a etiqueta vai para o primeiro lugar livre perto do círculo (embaixo e em cima, afastando de 30 em 30 cm)
            emb, ema = [cy + ry + .5 + k * .3 for k in range(7)], [cy - ry - .3 - k * .3 for k in range(7)]
            opc = [t for par in zip(*((emb, ema) if cy < Dm / 2 else (ema, emb))) for t in par]
            fora = lambda t: t - .38 < vb[1] + .05 or t + .16 > vb[1] + vb[3] - .05
            ty = min(opc, key=lambda t: (fora(t), sum(_cruza((tx - lw / 2, t - .38, tx + lw / 2, t + .16), o) for o in ocupado + cotas)))
            ocupado.append((tx - lw / 2, ty - .38, tx + lw / 2, ty + .16))
            cima.append(f'<rect x="{tx - lw / 2:.3f}" y="{ty - .38:.3f}" width="{lw:.3f}" height=".54" rx=".27" fill="{VERM}"/>'
                        f'<text x="{tx:.3f}" y="{ty:.3f}" text-anchor="middle" font-family="Inter" font-weight="800" font-size=".34" fill="#fff">{txt}</text>')
    m = ETIQ.search(svg)
    i = m.start() if m else svg.rindex("</svg>")
    svg = svg[:i] + "".join(baixo) + svg[i:]
    return svg.replace("</svg>", "".join(cima) + "</svg>")


def numeros(p):
    m = p["_r"].metricas
    f = lambda v: f"{v:g}".replace(".", ",")
    return {"Área": f"{PL.n0(m['area_fechada'])} m²", "Lote": f"{f(m['lote_comercial'][0])} x {f(m['lote_comercial'][1])} m",
            "Quartos": p["quartos_txt"], "Banheiros": f"{p['banheiros']} banheiro{'s' if p['banheiros'] > 1 else ''}"}


CSS = """@import url('https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,800&family=Inter:wght@500;700;800&family=JetBrains+Mono:wght@500;700&display=swap');
*{margin:0;box-sizing:border-box} .mono{font-family:'JetBrains Mono',monospace}
body{width:1080px;font-family:Inter,sans-serif;color:#17202B;background:#FBF8F2;
 background-image:linear-gradient(#0B4FA812 1px,transparent 1px),linear-gradient(90deg,#0B4FA812 1px,transparent 1px);background-size:36px 36px;padding:44px 36px 40px}
h1{font-family:'Bricolage Grotesque',Inter,sans-serif;font-weight:800;font-size:58px;line-height:1.02;color:#0B4FA8;letter-spacing:-.02em}
.duas{display:grid;grid-template-columns:1fr 1fr;gap:20px;margin-top:26px}
.lado{background:#fff;border-radius:22px;padding:16px 10px 8px;box-shadow:0 2px 0 #0B4FA81f}
.tag{display:inline-block;font-family:'Bricolage Grotesque',Inter,sans-serif;font-weight:800;font-size:54px;line-height:1;padding:10px 26px 12px;border-radius:999px;margin-left:8px}
.antes .tag{background:#17202B;color:#fff} .depois .tag{background:#0B4FA8;color:#fff}
.lado svg{display:block;width:100%;height:auto;margin-top:6px}
ol{list-style:none;margin-top:26px;display:grid;gap:14px}
li{display:flex;gap:18px;align-items:flex-start;background:#fff;border-radius:20px;padding:18px 22px;font-size:40px;line-height:1.22;font-weight:700}
li b{flex:none;width:58px;height:58px;border-radius:50%;background:#D62828;color:#fff;font-size:36px;font-weight:800;display:flex;align-items:center;justify-content:center}
li>div{flex:1;min-width:0} .perto{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-top:14px}
.perto figure{background:#F4EFE6;border-radius:14px;overflow:hidden;margin:0}
.perto svg{display:block;width:100%;height:auto} .perto figcaption{font-size:24px;font-weight:800;text-transform:uppercase;letter-spacing:.06em;padding:6px 14px 8px;color:#56616E}
.igual{margin-top:22px;background:#FFC857;border-radius:22px;padding:20px 26px}
.igual h2{font-family:'Bricolage Grotesque',Inter,sans-serif;font-weight:800;font-size:44px;line-height:1}
.igual div{display:flex;flex-wrap:wrap;gap:10px 14px;margin-top:14px}
.igual span{background:#fff;border-radius:999px;padding:8px 20px;font-size:36px;font-weight:800}
.igual h2.seg{margin-top:22px} .muda{margin-top:16px;font-size:36px;line-height:1.22;font-weight:700}
.perto .nada{display:flex;flex-direction:column} .nada div{flex:1;display:flex;align-items:center;justify-content:center;min-height:120px;font-size:30px;font-weight:800;color:#56616E}
.rod{margin-top:18px;font-size:22px;opacity:.6}"""


def de_perto(p, svg, ponto, aspecto=1.5):
    """O mesmo desenho, só a janela em volta do ponto (troca o viewBox): para ler no celular sem dar zoom.
    O recorte anda um pouco (sem perder o círculo) para mostrar inteiro o nome do cômodo que ele cortaria;
    o nome que ainda ficar cortado sai, e saem as cotas e a régua (pedaço de cota confunde)."""
    Dm = max([p["D"]] + [c["y1"] for c in p["comodos"] if c["tipo"] == "futuro"])
    x, y, rx, ry = ponto
    w = max(2 * rx + 1.2, (2 * ry + 1.2) * aspecto)  # recorte largo, com folga em volta do círculo
    h = w / aspecto
    c = [x - w / 2, Dm - y - ry - .3]  # o círculo encosta em cima; embaixo fica o cômodo, para entender onde é
    circ = (x - rx - .12, Dm - y - ry - .12, x + rx + .12, Dm - y + ry + .12)
    caixa = lambda c: (c[0], c[1], c[0] + w, c[1] + h)
    cabe = lambda bb, c, m=.06: bb[0] >= c[0] + m and bb[1] >= c[1] + m and bb[2] <= c[0] + w - m and bb[3] <= c[1] + h - m
    tx = textos(svg)
    etiq = sorted((bb for _, _, bb in tx if bb is not TUDO), key=lambda bb: -_cruza(bb, caixa(c)))
    for bb in etiq:
        if cabe(bb, c) or not _cruza(bb, caixa(c)):
            continue
        dx = min(0, bb[0] - .1 - c[0]) or max(0, bb[2] + .1 - c[0] - w)
        dy = min(0, bb[1] - .1 - c[1]) or max(0, bb[3] + .1 - c[1] - h)
        novo = [c[0] + dx, c[1] + dy]
        if cabe(circ, novo, 0) and sum(cabe(e, novo) for e in etiq) > sum(cabe(e, c) for e in etiq):
            c = novo
    for i, j, bb in sorted(tx, reverse=True):  # de trás para a frente, para os índices valerem
        if not cabe(bb, c):
            svg = svg[:i] + svg[j:]
    a, b = svg.split('viewBox="', 1)
    return a + f'viewBox="{c[0]:.3f} {c[1]:.3f} {w:.3f} {h:.3f}"' + b.split('"', 1)[1]


def pagina(pa, pb, pontos, legendas, titulo, obs=None, parte=0, aspecto=1.5):
    """pontos: lista de pares (ponto no antes, ponto no depois); um lado pode ser None (não tem).
    parte=0: tudo numa imagem; 1: as duas plantas e a faixa do que muda; 2: os pontos de perto."""
    lados = {}
    for k, q in enumerate((pa, pb)):
        svg, prob = livro.svg_planta(q, humanizada=True, estilo="revista"), conflitos(q)
        lados[k] = (q, marcar(q, svg, [pp[k] for pp in pontos], prob), svg, prob)
    nota = lambda pt, prob: f' · <em style="color:{VERM};font-style:normal">janela em cima da porta</em>' if dentro(pt, prob) else ""

    def fig(k, i, nome):
        q, _, crua, prob = lados[k]
        pt = pontos[i][k]
        if pt is None:
            return f'<figure class="nada"><div>não tinha</div><figcaption>{nome}</figcaption></figure>' if k == 0 else \
                   f'<figure class="nada"><div>não tem mais</div><figcaption>{nome}</figcaption></figure>'
        return f'<figure>{de_perto(q, marcar(q, crua, [pt], prob, enfeites=False), pt, aspecto)}<figcaption>{nome}{nota(pt, prob)}</figcaption></figure>'
    svga, svgb = lados[0][1], lados[1][1]
    na, nb = numeros(pa), numeros(pb)
    iguais = "".join(f"<span>{E(v)}</span>" for k, v in na.items() if nb[k] == v)
    muda = "".join(f"<span>{k}: {E(na[k])} → {E(nb[k])}</span>" for k in na if nb[k] != na[k])
    perto = lambda i: f'<div class="perto">{fig(0, i, "antes")}{fig(1, i, "depois")}</div>' if i < len(pontos) else ""
    itens = "" if parte == 1 else "".join(
        f"<li><b>{i + 1}</b><div><span>{E(legendas[i]) if i < len(legendas) else ''}</span>{perto(i)}</div></li>"
        for i in range(max(len(legendas), len(pontos))))
    plantas = "" if parte == 2 else (f'<div class="duas"><div class="lado antes"><span class="tag">ANTES</span>{svga}</div>'
                                     f'<div class="lado depois"><span class="tag">DEPOIS</span>{svgb}</div></div>')
    faixa = "" if parte == 2 else ('<div class="igual">'
                                   + (f'<h2>O que muda</h2><div>{muda}</div>' if muda else "")
                                   + (f'<h2{" class=seg" if muda else ""}>O que NÃO muda</h2><div>{iguais}</div>' if iguais else "")
                                   + (f'<p class="muda">{E(obs)}</p>' if obs else "") + "</div>")
    rodape = {0: "", 1: " · parte 1 de 2: cada número, de perto, na parte 2", 2: " · parte 2 de 2"}[parte]
    return (f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><style>{CSS}</style></head><body>'
            f'<h1>{E(titulo if parte < 2 else pa["nome"].split(" (")[0] + ": cada mudança de perto")}</h1>'
            + plantas + (f"<ol>{itens}</ol>" if itens else "") + faixa +
            f'<p class="rod mono">{E(pa["id"])} x {E(pb["id"])} · desenho do e-book, números do validador{rodape}</p></body></html>')


def png(html_txt, saida, limite=0):
    """limite: altura máxima em px de CSS (a imagem sai com o dobro). Se passar, as duas plantas encolhem juntas,
    na mesma escala, até caber. Devolve a altura final em px de CSS."""
    with tempfile.TemporaryDirectory() as d:
        h = Path(d) / "antes-depois.html"
        h.write_text(html_txt, encoding="utf-8")
        js = """const { chromium } = require('playwright');
const [arq, saida, lim] = process.argv.slice(-3);
(async () => { const b = await chromium.launch(); const pg = await b.newPage({ viewport: { width: 1080, height: 1000 }, deviceScaleFactor: 2 });
await pg.goto('file://' + arq); await pg.evaluate(() => document.fonts.ready);
const alt = await pg.evaluate((lim) => {
  const H = () => document.documentElement.scrollHeight;
  const svgs = [...document.querySelectorAll('.lado svg')];
  if (lim > 0 && H() > lim && svgs.length) {
    const hmax = Math.max(...svgs.map(s => s.getBoundingClientRect().height));
    const f = Math.max(.3, (hmax - (H() - lim)) / hmax);
    svgs.forEach(s => { const w = s.getBoundingClientRect().width; s.style.width = (w * f) + 'px'; s.style.margin = '6px auto 0'; });
  }
  return H();
}, Number(lim));
await pg.screenshot({ path: saida, fullPage: true }); await b.close(); console.log(alt); })();"""
        env = dict(os.environ, NODE_PATH=subprocess.run(["npm", "root", "-g"], capture_output=True, text=True).stdout.strip())
        r = subprocess.run(["node", "-e", js, str(h), str(saida), str(limite)], env=env, check=True, capture_output=True, text=True)
        return int(float(r.stdout.strip().splitlines()[-1]))


def main():
    ap = argparse.ArgumentParser(description="Antes e depois de uma planta, em imagem")
    ap.add_argument("antes")
    ap.add_argument("depois")
    ap.add_argument("--variante", help="variante dos rascunhos (sys.argv[1] do .py)")
    ap.add_argument("--legenda", action="append", default=[], help='uma frase por ponto (repita ou separe com "|")')
    ap.add_argument("--ponto", action="append", default=[], help="X,Y[,raio] em metros, marcado à mão")
    ap.add_argument("--sem-auto", action="store_true", help="só os pontos à mão")
    ap.add_argument("--titulo")
    ap.add_argument("--nota", help="uma frase embaixo da faixa dos números")
    ap.add_argument("--saida", required=True)
    ap.add_argument("--dividir", action="store_true", help="duas imagens (saida-1 e saida-2) de até 2160 x 4000 px")
    a = ap.parse_args()
    pa, pb = carregar(a.antes, a.variante), carregar(a.depois, a.variante)
    pontos = [] if a.sem_auto else [(m, m) for m in mudancas(pa, pb)]

    def ler(t):
        if t.strip() == "-":
            return None
        v = [float(x) for x in t.split(",")]
        r = v[2] if len(v) > 2 else .7
        return (v[0], v[1], r, r)
    for t in a.ponto:
        lado = t.split(";")
        pontos.append((ler(lado[0]), ler(lado[-1])))
    chave = lambda pp: next(q for q in (pp[1], pp[0]) if q)  # ordena pelo depois (o que o leitor vai construir)
    pontos.sort(key=lambda pp: (-round(chave(pp)[1]), chave(pp)[0]))  # leitura: de cima (fundos) para baixo, da esquerda para a direita
    legendas = [t.strip() for x in a.legenda for t in x.split("|") if t.strip()]
    legendas = [t.split(".", 1)[1].strip() if t.split(".", 1)[0].isdigit() else t for t in legendas]
    for n, pp in enumerate(pontos, 1):
        x, y = chave(pp)[:2]
        print(f"ponto {n}: x {x:.2f} m, y {y:.2f} m (da frente)")
    if len(legendas) != len(pontos):
        print(f"AVISO: {len(pontos)} ponto(s) marcados e {len(legendas)} frase(s) de legenda")
    saida = Path(a.saida).resolve()
    saida.parent.mkdir(parents=True, exist_ok=True)
    titulo = a.titulo or f"{pa['nome'].split(' (')[0]}: o que muda"
    if not a.dividir:
        png(pagina(pa, pb, pontos, legendas, titulo, a.nota), saida)
        print(f"imagem: {saida}")
        return
    # duas imagens de até 2160 x 4000 px (o WhatsApp encolhe imagem mais comprida): na parte 1 as plantas encolhem
    # juntas; na parte 2 o recorte "de perto" fica mais largo e mais baixo até caber
    s1, s2 = (saida.with_name(f"{saida.stem}-{n}{saida.suffix}") for n in (1, 2))
    alt = png(pagina(pa, pb, pontos, legendas, titulo, a.nota, parte=1), s1, limite=LIMITE)
    print(f"imagem: {s1}" + ("" if alt <= LIMITE else f"  AVISO: {2 * alt} px de altura"))
    for asp in (1.5, 1.75, 2.0, 2.3, 2.6, 3.0):
        alt = png(pagina(pa, pb, pontos, legendas, titulo, a.nota, parte=2, aspecto=asp), s2)
        if alt <= LIMITE:
            break
    print(f"imagem: {s2}" + ("" if alt <= LIMITE else f"  AVISO: {2 * alt} px de altura, passa de {2 * LIMITE}"))


if __name__ == "__main__":
    main()

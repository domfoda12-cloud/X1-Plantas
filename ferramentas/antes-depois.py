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
    --sem-auto: só os pontos à mão.  --titulo: título de cima (padrão: o nome da casa).
"""
import argparse
import contextlib
import html
import io
import os
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
def marcar(p, svg, pontos, problemas):
    """Põe círculos, números e a etiqueta "janela em cima da porta" no próprio SVG do e-book (mesmas coordenadas)."""
    Dm = max([p["D"]] + [c["y1"] for c in p["comodos"] if c["tipo"] == "futuro"])
    vb = [float(v) for v in svg.split('viewBox="', 1)[1].split('"', 1)[0].split()]
    Y = lambda y: Dm - y
    s = []
    for n, (x, y, rx, ry) in enumerate(pontos, 1):
        if x - rx > p["W"] + .5 or y - ry > Dm + .5:
            continue
        cx, cy = x, Y(y)
        s.append(f'<ellipse cx="{cx:.3f}" cy="{cy:.3f}" rx="{rx:.3f}" ry="{ry:.3f}" fill="{VERM}" fill-opacity=".07" stroke="{VERM}" stroke-width=".085" stroke-dasharray=".26 .14"/>')
        bx = min(max(cx - rx * .72, vb[0] + .4), vb[0] + vb[2] - .4)
        by = min(max(cy - ry * .72, vb[1] + .4), vb[1] + vb[3] - .4)
        s.append(f'<circle cx="{bx:.3f}" cy="{by:.3f}" r=".36" fill="{VERM}" stroke="#fff" stroke-width=".07"/>'
                 f'<text x="{bx:.3f}" y="{by + .17:.3f}" text-anchor="middle" font-family="Inter" font-weight="800" font-size=".5" fill="#fff">{n}</text>')
        if any(abs(px - x) <= rx and abs(py - y) <= ry for px, py in problemas):
            ty = cy + ry + .5 if cy < Dm / 2 else cy - ry - .3
            txt = "janela em cima da porta"
            lw = len(txt) * .205 + .4
            tx = min(max(cx, vb[0] + lw / 2 + .05), vb[0] + vb[2] - lw / 2 - .05)
            s.append(f'<rect x="{tx - lw / 2:.3f}" y="{ty - .38:.3f}" width="{lw:.3f}" height=".54" rx=".27" fill="{VERM}"/>'
                     f'<text x="{tx:.3f}" y="{ty:.3f}" text-anchor="middle" font-family="Inter" font-weight="800" font-size=".34" fill="#fff">{txt}</text>')
    return svg.replace("</svg>", "".join(s) + "</svg>")


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
.perto svg{display:block;width:100%;height:250px} .perto figcaption{font-size:26px;font-weight:800;text-transform:uppercase;letter-spacing:.06em;padding:6px 14px 8px;color:#56616E}
.igual{margin-top:22px;background:#FFC857;border-radius:22px;padding:20px 26px}
.igual h2{font-family:'Bricolage Grotesque',Inter,sans-serif;font-weight:800;font-size:44px;line-height:1}
.igual div{display:flex;flex-wrap:wrap;gap:10px 14px;margin-top:14px}
.igual span{background:#fff;border-radius:999px;padding:8px 20px;font-size:36px;font-weight:800}
.muda{margin-top:12px;font-size:32px;font-weight:700}
.rod{margin-top:18px;font-size:22px;opacity:.6}"""


def de_perto(p, svg, ponto):
    """O mesmo desenho, só a janela em volta do ponto (troca o viewBox): para ler no celular sem dar zoom."""
    Dm = max([p["D"]] + [c["y1"] for c in p["comodos"] if c["tipo"] == "futuro"])
    x, y, rx, ry = ponto
    vb = f"{x - rx - .7:.3f} {Dm - y - ry - .75:.3f} {2 * rx + 1.4:.3f} {2 * ry + 1.85:.3f}"
    a, b = svg.split('viewBox="', 1)
    return a + f'viewBox="{vb}" preserveAspectRatio="xMidYMid slice"' + b.split('"', 1)[1]


def pagina(pa, pb, svga, svgb, legendas, titulo, pontos=()):
    na, nb = numeros(pa), numeros(pb)
    iguais = "".join(f"<span>{E(v)}</span>" for k, v in na.items() if nb[k] == v)
    muda = " · ".join(f"{k}: {E(na[k])} → {E(nb[k])}" for k in na if nb[k] != na[k])
    perto = lambda i: (f'<div class="perto"><figure>{de_perto(pa, svga, pontos[i])}<figcaption>antes</figcaption></figure>'
                       f'<figure>{de_perto(pb, svgb, pontos[i])}<figcaption>depois</figcaption></figure></div>') if i < len(pontos) else ""
    itens = "".join(f"<li><b>{i + 1}</b><div><span>{E(legendas[i]) if i < len(legendas) else ''}</span>{perto(i)}</div></li>"
                    for i in range(max(len(legendas), len(pontos))))
    return (f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><style>{CSS}</style></head><body>'
            f'<h1>{E(titulo)}</h1>'
            f'<div class="duas"><div class="lado antes"><span class="tag">ANTES</span>{svga}</div>'
            f'<div class="lado depois"><span class="tag">DEPOIS</span>{svgb}</div></div>'
            + (f"<ol>{itens}</ol>" if itens else "")
            + f'<div class="igual"><h2>O que NÃO muda</h2><div>{iguais or "<span>tudo muda nos números</span>"}</div>'
            + (f'<p class="muda">Muda: {muda}</p>' if muda else "") + "</div>"
            f'<p class="rod mono">{E(pa["id"])} x {E(pb["id"])} · desenho do e-book, números do validador</p></body></html>')


def png(html_txt, saida):
    with tempfile.TemporaryDirectory() as d:
        h = Path(d) / "antes-depois.html"
        h.write_text(html_txt, encoding="utf-8")
        js = """const { chromium } = require('playwright');
(async () => { const b = await chromium.launch(); const pg = await b.newPage({ viewport: { width: 1080, height: 1000 }, deviceScaleFactor: 2 });
await pg.goto('file://' + process.argv[process.argv.length - 2]); await pg.evaluate(() => document.fonts.ready);
await pg.screenshot({ path: process.argv[process.argv.length - 1], fullPage: true }); await b.close(); })();"""
        env = dict(os.environ, NODE_PATH=subprocess.run(["npm", "root", "-g"], capture_output=True, text=True).stdout.strip())
        subprocess.run(["node", "-e", js, str(h), str(saida)], env=env, check=True)


def main():
    ap = argparse.ArgumentParser(description="Antes e depois de uma planta, em imagem")
    ap.add_argument("antes")
    ap.add_argument("depois")
    ap.add_argument("--variante", help="variante dos rascunhos (sys.argv[1] do .py)")
    ap.add_argument("--legenda", action="append", default=[], help='uma frase por ponto (repita ou separe com "|")')
    ap.add_argument("--ponto", action="append", default=[], help="X,Y[,raio] em metros, marcado à mão")
    ap.add_argument("--sem-auto", action="store_true", help="só os pontos à mão")
    ap.add_argument("--titulo")
    ap.add_argument("--saida", required=True)
    a = ap.parse_args()
    pa, pb = carregar(a.antes, a.variante), carregar(a.depois, a.variante)
    pontos = [] if a.sem_auto else mudancas(pa, pb)
    for t in a.ponto:
        v = [float(x) for x in t.split(",")]
        r = v[2] if len(v) > 2 else .7
        pontos.append((v[0], v[1], r, r))
    pontos.sort(key=lambda q: (-round(q[1]), q[0]))  # leitura: de cima (fundos) para baixo, da esquerda para a direita
    legendas = [t.strip() for x in a.legenda for t in x.split("|") if t.strip()]
    legendas = [t.split(".", 1)[1].strip() if t.split(".", 1)[0].isdigit() else t for t in legendas]
    for n, (x, y, rx, ry) in enumerate(pontos, 1):
        print(f"ponto {n}: x {x:.2f} m, y {y:.2f} m (da frente)")
    if len(legendas) != len(pontos):
        print(f"AVISO: {len(pontos)} ponto(s) marcados e {len(legendas)} frase(s) de legenda")
    svga = marcar(pa, livro.svg_planta(pa, humanizada=True, estilo="revista"), pontos, conflitos(pa))
    svgb = marcar(pb, livro.svg_planta(pb, humanizada=True, estilo="revista"), pontos, conflitos(pb))
    saida = Path(a.saida).resolve()
    saida.parent.mkdir(parents=True, exist_ok=True)
    png(pagina(pa, pb, svga, svgb, legendas, a.titulo or f"{pa['nome'].split(' (')[0]}: o que muda", pontos), saida)
    print(f"imagem: {saida}")


if __name__ == "__main__":
    main()

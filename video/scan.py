"""Sequência de "escaneamento" da planta (pedido do dono, 22/11/2026; ver video/VIDEO.md).

Uso: python3 video/scan.py E07   ->  video/broll/clipes/scan-e07.mp4 (0,9 s, 1080x1920, 30 qps)
Três tempos de 0,3 s sobre a mesma planta 2D, só com corte seco:
  1. cotas entram uma de cada vez (a frente do lote primeiro);
  2. malha 3D de arame por cima da planta;
  3. etiquetas (área, quartos, suíte, banheiros), cada uma mais rápida que a anterior.
O quarto tempo (a casa pronta em 3D) é a cena seguinte do roteiro. Todos os números saem dos dados validados da planta.
"""
import json
import subprocess
import sys
import tempfile
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
FPS, QUADROS = 30, 27
E = 54          # pixels por metro (recalculado para cada lote)
ALT = 2.7       # altura da parede na malha de arame, em metros


def br(v):
    return f"{v:.2f}".replace(".", ",")


def etiquetas(p):
    m = p["validacao"]["metricas"]
    q = p["quartos_txt"]
    tags = [f"{round(m['area_fechada'])} m²", q.split(" (")[0]]
    if "(" in q:
        tags.append(q.split("(")[1].rstrip(")"))
    tags.append(f"{p['banheiros']} banheiro" + ("s" if p["banheiros"] > 1 else ""))
    return tags


def html(p):
    m = p["validacao"]["metricas"]
    lw, ld = m["lote"]
    global E
    E = min(90, 780 / lw, 1230 / ld)          # o lote ocupa a tela: casa larga ou comprida, tanto faz
    rec = m["recuos"]
    x0 = 150                                  # canto do lote na tela; a rua fica embaixo
    y0 = 130 + ld * E                         # em cima, para a cota da frente ficar longe do aviso legal
    X = lambda x: x0 + (rec["esq"] + x) * E   # metros da casa -> tela
    Y = lambda y: y0 - (rec["frente"] + y) * E
    s = []
    # tempo 0: a planta 2D (lote tracejado, paredes, nomes)
    s.append(f'<rect x="{x0}" y="{y0 - ld * E}" width="{lw * E}" height="{ld * E}" class="lote"/>')
    for c in p["comodos"]:
        cls = "aberto" if c["tipo"] == "varanda" else "par"
        s.append(f'<rect x="{X(c["x0"])}" y="{Y(c["y1"])}" width="{(c["x1"] - c["x0"]) * E}" height="{(c["y1"] - c["y0"]) * E}" class="{cls}"/>')
        if c["tipo"] != "varanda" and (c["x1"] - c["x0"]) >= 1.7:
            s.append(f'<text x="{X((c["x0"] + c["x1"]) / 2)}" y="{Y((c["y0"] + c["y1"]) / 2) + 8}" class="nome">{c["nome"].upper()}</text>')
    s.append(f'<text x="{x0 + lw * E / 2}" y="{y0 + 165}" class="rua">RUA</text>')

    def cota(n, xa, ya, xb, yb, txt, lado):
        """Linha de cota com dois tiques e o número; aparece a partir do quadro n."""
        horiz = ya == yb
        tiq = "".join(f'<line x1="{x - (0 if horiz else 14)}" y1="{y - (14 if horiz else 0)}" x2="{x + (0 if horiz else 14)}" y2="{y + (14 if horiz else 0)}"/>'
                      for x, y in ((xa, ya), (xb, yb)))
        if horiz:
            t = f'<text x="{(xa + xb) / 2}" y="{ya + lado}" text-anchor="middle">{txt}</text>'
        else:
            t = f'<text transform="translate({xa + lado},{(ya + yb) / 2}) rotate(-90)" text-anchor="middle">{txt}</text>'
        return f'<g class="cota" data-de="{n}" data-ate="8"><line x1="{xa}" y1="{ya}" x2="{xb}" y2="{yb}"/>{tiq}{t}</g>'

    # tempo 1 (quadros 0 a 8): cotas, uma de cada vez; a frente do lote é a primeira
    s.append(cota(1, x0, y0 + 60, x0 + lw * E, y0 + 60, f"{br(lw)} m de frente", 52))
    s.append(cota(3, X(0), Y(0) + 40, X(p["W"]), Y(0) + 40, f"{br(p['W'])} m", -16))
    s.append(cota(5, X(0) - 50, Y(0), X(0) - 50, Y(p["D"]), f"{br(p['D'])} m", -16))
    s.append(cota(7, x0 + lw * E + 44, y0, x0 + lw * E + 44, y0 - ld * E, f"{br(ld)} m", 46))

    # tempo 2 (quadros 9 a 17): malha de arame; primeiro o chão em grade, depois as paredes sobem
    dx, dy = ALT * E * 0.42, -ALT * E * 0.62
    grade = "".join(f'<line x1="{X(x / 2)}" y1="{Y(0)}" x2="{X(x / 2)}" y2="{Y(p["D"])}"/>' for x in range(int(p["W"] * 2) + 1))
    grade += "".join(f'<line x1="{X(0)}" y1="{Y(y / 2)}" x2="{X(p["W"])}" y2="{Y(y / 2)}"/>' for y in range(int(p["D"] * 2) + 1))
    s.append(f'<g class="malha" data-de="9" data-ate="17">{grade}</g>')
    caixas = ""
    for c in p["comodos"]:
        if c["tipo"] == "varanda":
            continue
        a, b, cc, d = X(c["x0"]), Y(c["y1"]), X(c["x1"]), Y(c["y0"])
        caixas += f'<rect x="{a + dx}" y="{b + dy}" width="{cc - a}" height="{d - b}"/>'
        caixas += "".join(f'<line x1="{x}" y1="{y}" x2="{x + dx}" y2="{y + dy}"/>' for x, y in ((a, b), (cc, b), (a, d), (cc, d)))
    s.append(f'<g class="arame" data-de="12" data-ate="17">{caixas}</g>')
    nos = "".join(f'<circle cx="{x}" cy="{y}" r="7"/>' for c in p["comodos"] if c["tipo"] != "varanda"
                  for x, y in ((X(c["x0"]) + dx, Y(c["y1"]) + dy), (X(c["x1"]) + dx, Y(c["y1"]) + dy)))
    s.append(f'<g class="nos" data-de="15" data-ate="17">{nos}</g>')

    # tempo 3 (quadros 18 a 26): etiquetas empilhando, cada uma mais rápida (intervalos de 3, 2 e 1 quadro)
    entradas = [18, 21, 23, 24]
    tags = "".join(f'<div class="tag" data-de="{entradas[min(i, 3)]}" data-ate="26">{t}</div>' for i, t in enumerate(etiquetas(p)))
    return f"""<!doctype html><html><head><meta charset="utf-8">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,800&family=JetBrains+Mono:wght@700&display=swap">
<style>
*{{margin:0;box-sizing:border-box}}
html,body{{width:1080px;height:1920px;overflow:hidden;background:#0B4AA8;
 background-image:linear-gradient(rgba(255,255,255,.10) 2px,transparent 2px),linear-gradient(90deg,rgba(255,255,255,.10) 2px,transparent 2px);background-size:{E}px {E}px}}
svg{{position:absolute;inset:0}}
.lote{{fill:none;stroke:rgba(255,255,255,.55);stroke-width:3;stroke-dasharray:14 10}}
.par{{fill:rgba(255,255,255,.04);stroke:#fff;stroke-width:6}} .aberto{{fill:none;stroke:rgba(255,255,255,.6);stroke-width:3;stroke-dasharray:6 8}}
.nome,.rua{{font:700 22px "JetBrains Mono",monospace;fill:rgba(255,255,255,.9);text-anchor:middle;letter-spacing:.06em}} .rua{{font-size:30px;fill:rgba(255,255,255,.5)}}
.cota line{{stroke:#FFC857;stroke-width:4}} .cota text{{font:700 36px "JetBrains Mono",monospace;fill:#FFC857}}
.malha line{{stroke:#5CF2E0;stroke-width:1.5;opacity:.75}}
.arame rect,.arame line{{fill:none;stroke:#5CF2E0;stroke-width:3.5}} .nos circle{{fill:#5CF2E0}}
.tags{{position:absolute;right:60px;top:330px;display:grid;gap:26px;justify-items:end}}
.tag{{font:800 92px "Bricolage Grotesque",sans-serif;color:#061A3A;background:#FFC857;padding:10px 30px 16px;border-radius:14px;line-height:1;box-shadow:0 10px 0 rgba(6,26,58,.55)}}
[data-de]{{visibility:hidden}}
</style></head><body><svg width="1080" height="1920">{"".join(s)}</svg><div class="tags">{tags}</div>
<script>window.quadro=n=>document.querySelectorAll('[data-de]').forEach(e=>e.style.visibility=(n>=+e.dataset.de&&n<=+e.dataset.ate)?'visible':'hidden')</script>
</body></html>"""


def main(pid):
    p = json.loads((RAIZ / f"ebook/plantas/dados/{pid}.json").read_text(encoding="utf-8"))
    saida = RAIZ / f"video/broll/clipes/scan-{pid.lower()}.mp4"
    with tempfile.TemporaryDirectory() as tmp:
        arq = Path(tmp) / "scan.html"
        arq.write_text(html(p), encoding="utf-8")
        js = ("const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();"
              "const p=await b.newPage({viewport:{width:1080,height:1920}});"
              f"await p.goto('file://{arq}');await p.evaluate(()=>document.fonts.ready);"
              f"for(let n=0;n<{QUADROS};n++){{await p.evaluate(n=>window.quadro(n),n);"
              f"await p.screenshot({{path:'{tmp}/q'+String(n).padStart(2,'0')+'.png'}});}}await b.close();}})()")
        for cmd in (["node", "-e", js],
                    ["ffmpeg", "-y", "-loglevel", "error", "-framerate", str(FPS), "-i", f"{tmp}/q%02d.png",
                     "-c:v", "libx264", "-crf", "14", "-preset", "slow", "-pix_fmt", "yuv420p", str(saida)]):
            r = subprocess.run(cmd, capture_output=True, text=True)
            if r.returncode != 0:
                sys.exit(r.stderr[-1500:])
    print(f"{saida.relative_to(RAIZ)}: {QUADROS / FPS:.1f} s, etiquetas: {', '.join(etiquetas(p))}")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "E07")

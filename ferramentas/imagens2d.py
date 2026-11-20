"""Imagens 2D das plantas para posts e anúncios (sem 3D): planta mobiliada, blueprint, vista da rua e casa no lote.

Uso: python3 ferramentas/imagens2d.py C01 E01 F03
     python3 ferramentas/imagens2d.py --previas [IDs]   (prévias mobiliadas em alta de ebook/plantas/previas/)
Saída: animacoes-3d/plantas-2d/<pasta>/{01-blueprint,02-planta-humanizada,03-fachada,04-lote}.png (1600 x 2000, 4:5)
"""
import os
import re
import subprocess
import sys
import unicodedata
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ / "ferramentas"))
sys.path.insert(0, str(RAIZ / "ebook" / "gerador"))
sys.path.insert(0, str(RAIZ / "ebook" / "fichas"))
import plantas as PL  # noqa: E402
import livro  # noqa: E402

SAIDA = RAIZ / "animacoes-3d" / "plantas-2d"
CSS = """@import url('https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,800&family=Inter:wght@500;700&family=JetBrains+Mono:wght@500;700&display=swap');
*{margin:0;box-sizing:border-box} body{width:1600px;height:2000px;font-family:Inter,sans-serif}
.q{width:1600px;height:2000px;display:grid;grid-template-rows:auto 1fr auto;padding:90px 90px 70px;gap:40px}
.azul{background:#0B4FA8;background-image:linear-gradient(rgba(255,255,255,.08) 2px,transparent 2px),linear-gradient(90deg,rgba(255,255,255,.08) 2px,transparent 2px);background-size:50px 50px;color:#fff}
.branco{background:#fff;color:#17202B}
h1{font-family:'Bricolage Grotesque',Inter,sans-serif;font-weight:800;font-size:92px;line-height:1;letter-spacing:-.02em}
.branco h1{color:#0B4FA8} .sub{font-size:40px;font-weight:700;margin-top:14px;opacity:.85}
.fig{display:grid;place-items:center;min-height:0} .fig svg{width:100%;height:100%}
.azul .fig{background:#fff;border-radius:24px;padding:40px}
.rod{font-size:24px;opacity:.75} .mono{font-family:'JetBrains Mono',monospace}"""


def pasta(nome):
    s = unicodedata.normalize("NFKD", nome).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")


def quadro(p, svg, classe, titulo):
    m = p["_r"].metricas
    sub = f"{m['area_fechada']:.0f} m² · {p['quartos_txt'].replace(' (+1 depois)', '')} · lote a partir de {m['lote_comercial'][0]} x {m['lote_comercial'][1]} m"
    return (f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>'
            f'<div class="q {classe}"><div><h1>{titulo}</h1><div class="sub">{sub}</div></div>'
            f'<div class="fig">{svg}</div><div class="rod">{livro.AVISO}</div></div></body></html>')


def main(ids, previas=False):
    todas = {p["id"]: p for p in PL.carregar()}
    trabalhos = []
    if previas:
        dprev = RAIZ / "ebook" / "plantas" / "previas"
        dprev.mkdir(parents=True, exist_ok=True)
        for pid in (ids or list(todas)):
            p = todas[pid]
            h = dprev / f"{pid}.html"
            h.write_text(quadro(p, livro.svg_planta(p, moveis=True), "branco", f"{pid} · {p['nome']}"), encoding="utf-8")
            trabalhos.append((str(h), str(dprev / f"{pid}.png")))
        ids = []
    for pid in ids:
        p = todas[pid]
        d = SAIDA / pasta(p["nome"])
        d.mkdir(parents=True, exist_ok=True)
        pecas = {
            "01-blueprint": (livro.svg_planta(p, moveis=False), "azul", p["nome"]),
            "02-planta-humanizada": (livro.svg_planta(p, moveis=True), "branco", p["nome"]),
            "03-fachada": (livro.svg_fachada(p), "branco", "Vista da rua"),
            "04-lote": (livro.svg_lote(p), "branco", "A casa no lote"),
        }
        for nome, (svg, classe, tit) in pecas.items():
            h = d / f"{nome}.html"
            h.write_text(quadro(p, svg, classe, tit), encoding="utf-8")
            trabalhos.append((str(h), str(d / f"{nome}.png")))
    js = """const { chromium } = require('playwright');
(async () => { const b = await chromium.launch(); const pg = await b.newPage({ viewport: { width: 1600, height: 2000 }, deviceScaleFactor: 2 });
for (const [h, o] of JSON.parse(process.argv[process.argv.length - 1])) { await pg.goto('file://' + h); await pg.evaluate(() => document.fonts.ready); await pg.screenshot({ path: o }); }
await b.close(); })();"""
    env = dict(os.environ, NODE_PATH=subprocess.run(["npm", "root", "-g"], capture_output=True, text=True).stdout.strip())
    import json
    subprocess.run(["node", "-e", js, json.dumps(trabalhos)], env=env, check=True)
    for h, _ in trabalhos:
        os.remove(h)
    print(f"{len(trabalhos)} imagens em {SAIDA.relative_to(RAIZ)}")


if __name__ == "__main__":
    args = sys.argv[1:]
    if args and args[0] == "--previas":
        main(args[1:], previas=True)
    else:
        main(args or ["C01", "E01", "F03"])

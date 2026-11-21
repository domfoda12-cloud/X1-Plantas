"""Gera a imagem "A casa em 3D" do e-book (ebook/visual/3d/<ID>.jpg) a partir do motor 3D.

Uso: python3 ferramentas/imagens3d.py E04 F05     (sem IDs: as 24 casas, cerca de 1 minuto cada)
Renderiza com video/render-planta.cjs, recorta em volta da casa e salva em JPEG.
"""
import re
import subprocess
import sys
import tempfile
from collections import deque
from pathlib import Path

import numpy as np
from PIL import Image

RAIZ = Path(__file__).resolve().parent.parent
VIDEO, DESTINO = RAIZ / "video", RAIZ / "ebook" / "visual" / "3d"


def recortar(origem, destino, margem=18):
    """Recorta em volta da casa: a mancha não verde ligada ao centro da imagem."""
    grande = Image.open(origem).convert("RGB")
    a = np.asarray(grande.resize((500, 625))).astype(int)
    casa = ~((a[..., 1] - np.maximum(a[..., 0], a[..., 2])) > 6)
    H, W = casa.shape
    inicio = min(zip(*np.nonzero(casa)), key=lambda p: (p[0] - H // 2) ** 2 + (p[1] - W // 2) ** 2)
    visto = np.zeros_like(casa)
    visto[inicio] = True
    fila, ys, xs = deque([inicio]), [], []
    while fila:
        y, x = fila.popleft()
        ys.append(y)
        xs.append(x)
        for ny, nx in ((y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)):
            if 0 <= ny < H and 0 <= nx < W and casa[ny, nx] and not visto[ny, nx]:
                visto[ny, nx] = True
                fila.append((ny, nx))
    k = grande.width / 500
    caixa = (max(0, (min(xs) - margem) * k), max(0, (min(ys) - margem) * k),
             min(grande.width, (max(xs) + margem) * k), min(grande.height, (max(ys) + margem) * k))
    c = grande.crop(tuple(int(v) for v in caixa))
    w = min(1400, c.width)
    c.resize((w, round(c.height * w / c.width)), Image.LANCZOS).save(destino, quality=90, optimize=True, progressive=True)


def main(ids):
    ids = ids or sorted(p.stem for p in (VIDEO / "src" / "plantas").glob("*.js"))
    DESTINO.mkdir(parents=True, exist_ok=True)
    if not (VIDEO / "node_modules" / "three").exists():  # cópia nova do projeto: as dependências do 3D não vão no git
        subprocess.run(["npm", "install", "--silent"], cwd=VIDEO, check=True)
    for pid in ids:
        txt = (VIDEO / "src" / "plantas" / f"{pid}.js").read_text(encoding="utf-8")
        W, D = (float(re.search(rf"{n} = ([\d.]+)", txt).group(1)) for n in ("LARGURA", "PROFUNDIDADE"))
        escala = round(max(1, max(W * 1.25, D) / 8.5) * 1.3, 3)  # câmera afastada o bastante para a casa inteira aparecer
        with tempfile.TemporaryDirectory() as tmp:
            subprocess.run(["node", "render-planta.cjs", "--planta", pid, "--so-imagens", "--escala", str(escala), "--saida", tmp],
                           cwd=VIDEO, check=True, capture_output=True)
            recortar(Path(tmp) / "03-perspectiva.png", DESTINO / f"{pid}.jpg")
        print("ok", pid)


if __name__ == "__main__":
    main(sys.argv[1:])

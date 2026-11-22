"""Recorta cada imagem final 4:5 em 9:16 (reel e story, 1080 x 1920 ou maior) e 1:1 (WhatsApp e feed), sem gerar de novo.

Uso: python3 ferramentas/recortes.py ebook/visual/openart/final
Saída: <pasta>/9x16/ e <pasta>/1x1/, mesmo nome de arquivo. O corte 9:16 sai da altura toda (centralizado).
"""
import sys
from pathlib import Path

from PIL import Image


def main(pasta):
    p = Path(pasta)
    for sub in ("9x16", "1x1"):
        (p / sub).mkdir(exist_ok=True)
    n = 0
    for f in sorted([*p.glob("*.jpg"), *p.glob("*.png")]):
        im = Image.open(f).convert("RGB")
        w, h = im.size
        cw = round(h * 9 / 16)
        im.crop(((w - cw) // 2, 0, (w - cw) // 2 + cw, h)).save(p / "9x16" / f.name, quality=92, subsampling=0, optimize=True)
        im.crop((0, (h - w) // 2, w, (h - w) // 2 + w)).save(p / "1x1" / f.name, quality=92, subsampling=0, optimize=True)
        n += 1
    print(f"{n} imagens recortadas em 9:16 e 1:1")


if __name__ == "__main__":
    main(sys.argv[1])

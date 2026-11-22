"""Mockups do e-book no celular e B-roll do e-book folheado, em alta resolução.

Uso: python3 ebook/gerador/livro.py --previa DIR   (gera as páginas em 2382 x 3372)
     python3 ferramentas/mockups.py DIR
Saída: ebook/visual/mockups/*.png (2160 x 2700 e 2700 x 2160) e video/broll/clipes/ebook-folheando.mp4 (2160 x 3840, 30 fps)
"""
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter

RAIZ = Path(__file__).resolve().parent.parent
MOCK = RAIZ / "ebook" / "visual" / "mockups"
BROLL = RAIZ / "video" / "broll" / "clipes"


def pagina(dir_previa, n):
    return Image.open(Path(dir_previa) / f"pagina-{n:02d}.png").convert("RGB")


def celular(im, w):
    h = int(w * im.height / im.width)
    im = im.resize((w, h), Image.LANCZOS)
    b = int(w * 0.055)
    tel = Image.new("RGBA", (w + 2 * b, h + 2 * b + int(b * 1.6)), (0, 0, 0, 0))
    d = ImageDraw.Draw(tel)
    d.rounded_rectangle([0, 0, tel.width - 1, tel.height - 1], radius=int(w * 0.11), fill="#14181F")
    tel.paste(im, (b, b + int(b * 0.8)))
    d.rounded_rectangle([tel.width // 2 - w // 10, int(b * 0.35), tel.width // 2 + w // 10, int(b * 0.75)], radius=b // 4, fill="#2A303A")
    return tel


def fundo(W, H):
    f = Image.new("RGB", (W, H), "#08397A")
    d = ImageDraw.Draw(f)
    passo = W // 27
    for x in range(0, W, passo):
        d.line([(x, 0), (x, H)], fill="#164A8E", width=2)
    for y in range(0, H, passo):
        d.line([(0, y), (W, y)], fill="#164A8E", width=2)
    return f


def colar(f, t, xy):
    s = Image.new("RGBA", t.size, (0, 0, 0, 0))
    s.paste((0, 0, 0, 130), (0, 0, t.width, t.height), t.split()[3])
    s = s.filter(ImageFilter.GaussianBlur(t.width // 25))
    f.paste(s, (xy[0] + t.width // 30, xy[1] + t.width // 20), s)
    f.paste(t, xy, t)


def mockups(dp):
    MOCK.mkdir(parents=True, exist_ok=True)
    f = fundo(2160, 2700)
    t = celular(pagina(dp, 1), 1120)
    colar(f, t, ((2160 - t.width) // 2, (2700 - t.height) // 2))
    f.save(MOCK / "capa-celular.png", optimize=True)
    f = fundo(2700, 2160)
    a, b = celular(pagina(dp, 10), 1080), celular(pagina(dp, 11), 1080)
    colar(f, a, (80, (2160 - a.height) // 2))
    colar(f, b, (2700 - 80 - b.width, (2160 - b.height) // 2))
    f.save(MOCK / "casa-c01-celulares.png", optimize=True)
    f = fundo(2160, 3840)
    a, b = celular(pagina(dp, 3), 1040), celular(pagina(dp, 1), 1040)
    colar(f, a, (180, 1100))
    colar(f, b, (2160 - 180 - b.width, 520))
    f.save(MOCK / "story-capa-lote.png", optimize=True)


def broll(dp, pags=(1, 3, 10, 11, 24, 25, 40, 48, 58)):
    BROLL.mkdir(parents=True, exist_ok=True)
    W, H, tw = 2160, 3840, 1520
    ims = [pagina(dp, p) for p in pags]
    th = int(tw * ims[0].height / ims[0].width)
    ims = [i.resize((tw, th), Image.LANCZOS) for i in ims]
    gap = 80
    fita = Image.new("RGB", (tw, (th + gap) * len(ims)), "#2A303A")
    for k, i in enumerate(ims):
        fita.paste(i, (0, k * (th + gap)))
    tel = celular(Image.new("RGB", (tw, th), "white"), tw)
    b = int(tw * 0.055)
    base = fundo(W, H)
    px, py = (W - tel.width) // 2, (H - tel.height) // 2
    colar(base, tel, (px, py))
    fps, dur, trans = 30, 1.6, 0.45
    n = len(ims)
    tmp = Path(tempfile.mkdtemp())
    try:
        total = int(fps * dur * n)
        ease = lambda t: t * t * (3 - 2 * t)
        hold = 1 - trans / dur
        for q in range(total):
            t = q / fps
            k = int(t // dur)
            r = (t - k * dur) / dur
            pos = k + (ease((r - hold) / (1 - hold)) if r > hold and k < n - 1 else 0)
            y = int(pos * (th + gap))
            fr = base.copy()
            fr.paste(fita.crop((0, y, tw, y + th)), (px + b, py + b + int(b * 0.8)))
            fr.save(tmp / f"q{q:04d}.png", compress_level=1)
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-framerate", str(fps), "-i", str(tmp / "q%04d.png"),
                        "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "20", "-preset", "medium", "-movflags", "+faststart",
                        str(BROLL / "ebook-folheando.mp4")], check=True)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    dp = sys.argv[1]
    mockups(dp)
    broll(dp)
    print("mockups e B-roll em alta prontos")

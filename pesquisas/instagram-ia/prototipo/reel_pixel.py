"""Teste de viabilidade: reel vertical em pixel art só com código (Pillow + ffmpeg).

Desenha 90 quadros numa grade 135x240, escala 8x (1080x1920) com NEAREST
e manda os quadros crus para o ffmpeg pelo stdin (sem PNG intermediário).
Uso: python3 reel_pixel.py [saida.mp4]
"""
import subprocess
import sys
import time
from pathlib import Path

from PIL import Image, ImageDraw

W, H, ESCALA, FPS, QUADROS = 135, 240, 8, 30, 90
AQUI = Path(__file__).resolve().parent
SAIDA = Path(sys.argv[1]) if len(sys.argv) > 1 else AQUI / "reel-teste.mp4"

# Paleta curta, estilo 16 cores
NOITE = (24, 20, 48)
NOITE2 = (36, 30, 70)
PAREDE = (58, 52, 96)
CHAO = (92, 64, 52)
CHAO2 = (74, 50, 42)
FIO = (20, 18, 26)
SOQUETE = (110, 110, 120)
VIDRO_OFF = (150, 150, 165)
VIDRO_OFF2 = (120, 120, 135)
LUZ = (255, 222, 89)
LUZ2 = (255, 247, 180)
BRILHO = (255, 190, 60)
TEXTO = (240, 240, 245)

# Fonte pixel 3x5 desenhada à mão
DIGITOS = {
    "0": ["111", "101", "101", "101", "111"],
    "1": ["010", "110", "010", "010", "111"],
    "2": ["111", "001", "111", "100", "111"],
    "3": ["111", "001", "111", "001", "111"],
    "4": ["101", "101", "111", "001", "001"],
    "5": ["111", "100", "111", "001", "111"],
    "6": ["111", "100", "111", "101", "111"],
    "7": ["111", "001", "010", "010", "010"],
    "8": ["111", "101", "111", "101", "111"],
    "9": ["111", "101", "111", "001", "111"],
    "%": ["101", "001", "010", "100", "101"],
}

# Lâmpada: '.' vazio, 'v' vidro, 'h' reflexo, 's' soquete
LAMPADA = [
    "....vvvvv....",
    "..vvvvvvvvv..",
    ".vvhhvvvvvvv.",
    ".vhhvvvvvvvv.",
    "vvhvvvvvvvvvv",
    "vvvvvvvvvvvvv",
    "vvvvvvvvvvvvv",
    "vvvvvvvvvvvvv",
    ".vvvvvvvvvvv.",
    ".vvvvvvvvvvv.",
    "..vvvvvvvvv..",
    "...vvvvvvv...",
    "....vvvvv....",
    "....sssss....",
    "....sssss....",
    "....sssss....",
    ".....sss.....",
]


def fundo(d):
    # Céu em faixas com pontilhado (dither) na transição
    for y in range(150):
        for x in range(W):
            if y < 70:
                c = NOITE
            elif y < 80:
                c = NOITE2 if (x + y) % 2 else NOITE
            else:
                c = NOITE2 if y < 120 else (PAREDE if (x + y) % 2 or y >= 130 else NOITE2)
            d.point((x, y), c)
    d.rectangle((0, 150, W, 150), fill=(30, 26, 40))
    for y in range(151, H):
        for x in range(W):
            d.point((x, y), CHAO2 if (x // 9 + y // 6) % 2 else CHAO)


def estrelas(d, f):
    for i, (x, y) in enumerate([(12, 14), (40, 30), (101, 9), (122, 41), (70, 22), (20, 55), (115, 66)]):
        if (f // 6 + i) % 3:
            d.point((x, y), TEXTO)


def lampada(d, acesa, f):
    x0, y0 = (W - 13) // 2, 52
    d.line((W // 2, 0, W // 2, y0 + 16), fill=FIO)  # fio pendurado
    if acesa:
        # Halo em anéis pontilhados que pulsam
        r = 22 + (f % 8 > 3)
        cx, cy = W // 2, y0 + 6
        for y in range(cy - r - 6, cy + r + 7):
            for x in range(cx - r - 6, cx + r + 7):
                dist2 = (x - cx) ** 2 + (y - cy) ** 2
                if dist2 < r * r and (x + y) % 2 == 0:
                    d.point((x, y), BRILHO)
        # Raios
        for dx, dy in [(-1, 0), (1, 0), (-1, -1), (1, -1), (-1, 1), (1, 1), (0, 1)]:
            for k in range(r + 1, r + 6):
                d.point((cx + dx * k, cy + dy * k), LUZ)
    for j, linha in enumerate(LAMPADA):
        for i, ch in enumerate(linha):
            if ch == ".":
                continue
            if ch == "s":
                c = SOQUETE
            elif ch == "h":
                c = LUZ2 if acesa else (200, 200, 210)
            else:
                c = LUZ if acesa else (VIDRO_OFF if (i + j) % 3 else VIDRO_OFF2)
            d.point((x0 + i, y0 + 16 - j), c)  # desenhada de ponta-cabeça: rosca em cima


def texto_pixel(d, s, cx, y, tam, cor, sombra=(10, 8, 20)):
    larg = len(s) * 4 * tam - tam
    x = cx - larg // 2
    for ch in s:
        for j, linha in enumerate(DIGITOS[ch]):
            for i, b in enumerate(linha):
                if b == "1":
                    px, py = x + i * tam, y + j * tam
                    d.rectangle((px + 1, py + 1, px + tam, py + tam), fill=sombra)
                    d.rectangle((px, py, px + tam - 1, py + tam - 1), fill=cor)
        x += 4 * tam


def main():
    t0 = time.time()
    base = Image.new("RGB", (W, H))
    fundo(ImageDraw.Draw(base))  # fundo fixo, desenhado uma vez
    cmd = [
        "ffmpeg", "-y", "-loglevel", "error",
        "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W*ESCALA}x{H*ESCALA}", "-r", str(FPS), "-i", "-",
        "-c:v", "libx264", "-preset", "slow", "-crf", "18", "-pix_fmt", "yuv420p",
        "-tune", "animation", "-movflags", "+faststart", str(SAIDA),
    ]
    ff = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    for f in range(QUADROS):
        img = base.copy()
        d = ImageDraw.Draw(img)
        estrelas(d, f)
        acesa = f >= 30 or (24 <= f < 30 and f % 2 == 0)  # pisca antes de acender
        lampada(d, acesa, f)
        n = round(100 * f / (QUADROS - 1))
        texto_pixel(d, f"{n}%", W // 2, 170, 7, LUZ if acesa else TEXTO)
        ff.stdin.write(img.resize((W * ESCALA, H * ESCALA), Image.NEAREST).tobytes())
        if f == 60:
            img.resize((W * ESCALA, H * ESCALA), Image.NEAREST).save(AQUI / "quadro-60.png")
    ff.stdin.close()
    ff.wait()
    dt = time.time() - t0
    print(f"ok: {SAIDA} | {QUADROS} quadros em {dt:.1f}s | {SAIDA.stat().st_size/1024:.0f} KB | ffmpeg rc={ff.returncode}")


if __name__ == "__main__":
    main()

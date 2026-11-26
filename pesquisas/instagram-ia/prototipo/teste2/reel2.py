#!/usr/bin/env python3
"""Reel piloto 2: "Pizza de 35 cm ou duas de 25 cm?" em forma de DUELO.

Uso: python3 reel2.py [saida.mp4]

Tudo sai do calculo: as areas, o placar, as notas e a "PEGADINHA" vem dos
numeros abaixo, nada escrito a mao. Estilo: lousa escura com traco de giz.
Som: numpy (ondas simples), cada fatia que enche e uma nota cuja altura segue
o placar daquele lado; o resultado trava num acorde.
Dependencias: Pillow, numpy, ffmpeg (com AAC).
"""
import math, os, subprocess, sys, tempfile, time, wave

import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

# ---------------------------------------------------------------- a conta
D_A, N_A = 35, 1          # lado A: uma pizza de 35 cm
D_B, N_B = 25, 2          # lado B: duas de 25 cm
FATIAS = 8                # fatias por pizza (so para animar e tocar)

r_A, r_B = D_A / 2, D_B / 2
area_A = N_A * math.pi * r_A ** 2
area_B = N_B * math.pi * r_B ** 2
assert round(area_A) == 962 and round(area_B) == 982, (area_A, area_B)
vence = "A" if area_A > area_B else "B"
intuicao = "A" if D_A > D_B else "B"          # o olho escolhe a pizza maior
pegadinha = vence != intuicao
dif = abs(area_B - area_A)
pct = dif / min(area_A, area_B) * 100


def br(x, casas=1):
    s = f"{x:.{casas}f}".replace(".", ",")
    return s[:-2] if s.endswith(",0") else s


# ---------------------------------------------------------------- tempo
FPS, DUR = 30, 12.0
NF = int(FPS * DUR)
W, H = 1080, 1920
SR = 48000

T_RAIO_A = (1.25, 1.65)
T_RAIO_B = (1.75, 2.15)
T_FORMULA = (2.2, 2.65)
T_A0, DUR_FATIA_A = 2.75, 0.21
# fatias de B: comecam rapidas e freiam perto da virada (tensao)
durB = [0.16] * 12 + [0.24, 0.26, 0.34]
pausa_antes_ultima = 0.32
T_B0 = 4.65
fatiasA = [(T_A0 + i * DUR_FATIA_A, DUR_FATIA_A) for i in range(FATIAS * N_A)]
fatiasB, t = [], T_B0
for d in durB:
    fatiasB.append((t, d)); t += d
t += pausa_antes_ultima
fatiasB.append((t, 0.42)); t += 0.42
assert len(fatiasB) == FATIAS * N_B
T_TRAVA = t + 0.02
T_DIF = T_TRAVA + 0.6
T_FECHO = 10.0

# ---------------------------------------------------------------- visual
FONT = "/usr/share/fonts/opentype/inter/Inter-{}.otf"
def fnt(peso, tam): return ImageFont.truetype(FONT.format(peso), tam)

LOUSA = (22, 31, 28)
GIZ = (236, 234, 222)
COR_A = (247, 183, 64)      # amarelo
COR_B = (255, 112, 92)      # coral
VERM = (255, 70, 70)
rng = np.random.default_rng(7)

K = 13.0                     # px por cm, mesma escala nos dois lados (honesto)
RA, RB = r_A * K, r_B * K
CA = (280, 770)
CB = [(800, 590), (800, 950)]


def ease(x):  # ease-out cubico
    x = min(max(x, 0.0), 1.0)
    return 1 - (1 - x) ** 3


def prog(t, a, b):
    return min(max((t - a) / (b - a), 0.0), 1.0)


def fundo():
    base = np.empty((H, W, 3), np.float32)
    base[:] = LOUSA
    # manchas de giz apagado
    m = Image.fromarray((rng.random((H // 16, W // 16)) * 255).astype(np.uint8))
    m = np.asarray(m.resize((W, H), Image.BICUBIC).filter(ImageFilter.GaussianBlur(40)), np.float32) / 255
    base += (m[..., None] - 0.5) * 18
    base += rng.normal(0, 3.0, (H, W, 1))
    # vinheta
    yy, xx = np.mgrid[0:H, 0:W]
    v = ((xx - W / 2) / (W * 0.75)) ** 2 + ((yy - H / 2) / (H * 0.7)) ** 2
    base *= (1 - 0.35 * np.clip(v, 0, 1))[..., None]
    return Image.fromarray(np.clip(base, 0, 255).astype(np.uint8)).convert("RGBA")


GRAO = np.clip(rng.normal(0.85, 0.22, (H, W)), 0, 1)


def giz(mask_img, cor, ox=0, oy=0, forca=1.0):
    """Transforma uma mascara L em traco de giz (cor com grao)."""
    m = np.asarray(mask_img, np.float32) / 255
    h, w = m.shape
    g = GRAO[oy:oy + h, ox:ox + w]
    if g.shape != m.shape:
        g = np.resize(g, m.shape)
    a = np.clip(m * g * 255 * forca, 0, 255).astype(np.uint8)
    out = Image.new("RGBA", (w, h), cor + (0,))
    out.putalpha(Image.fromarray(a))
    return out


def texto(s, peso, tam, cor, contorno=0):
    f = fnt(peso, tam)
    l, t_, r, b = f.getbbox(s, stroke_width=contorno)
    img = Image.new("RGBA", (r - l + 8, b - t_ + 8), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    d.text((4 - l, 4 - t_), s, font=f, fill=cor + (255,),
           stroke_width=contorno, stroke_fill=LOUSA + (255,))
    return img


def colar_centro(base, img, cx, cy, escala=1.0, alfa=1.0, ang=0.0):
    if escala != 1.0:
        img = img.resize((max(1, int(img.width * escala)), max(1, int(img.height * escala))), Image.LANCZOS)
    if ang:
        img = img.rotate(ang, Image.BICUBIC, expand=True)
    if alfa < 1.0:
        a = img.getchannel("A").point(lambda v: int(v * alfa))
        img = img.copy(); img.putalpha(a)
    base.alpha_composite(img, (int(cx - img.width / 2), int(cy - img.height / 2)))


def circulo_giz(r, larg=7, ss=2):
    """Contorno de pizza tremido a mao, com borda de massa tracejada."""
    tam = int(2 * r + 40)
    m = Image.new("L", (tam * ss, tam * ss), 0)
    d = ImageDraw.Draw(m)
    c = tam * ss / 2
    pts = []
    fase = rng.random() * 6.28
    for i in range(361):
        a = math.radians(i)
        rr = (r + 2.5 * math.sin(3 * a + fase) + 1.5 * math.sin(7 * a)) * ss
        pts.append((c + rr * math.cos(a), c + rr * math.sin(a)))
    d.line(pts, fill=255, width=larg * ss, joint="curve")
    # borda da massa, tracejada
    for i in range(0, 360, 9):
        a0, a1 = math.radians(i), math.radians(i + 5)
        rr = (r - 16) * ss
        d.line([(c + rr * math.cos(a0), c + rr * math.sin(a0)),
                (c + rr * math.cos(a1), c + rr * math.sin(a1))], fill=170, width=3 * ss)
    m = m.resize((tam, tam), Image.LANCZOS)
    return m


def fatia_mask(r, ini_deg, frac_raio, tam):
    m = Image.new("L", (tam, tam), 0)
    d = ImageDraw.Draw(m)
    c = tam / 2
    rr = (r - 5) * frac_raio
    d.pieslice([c - rr, c - rr, c + rr, c + rr], ini_deg, ini_deg + 360 / FATIAS, fill=255)
    return m


def tinta(r, cor, tam):
    """Camada de 'tinta' com textura, recortada depois pela mascara das fatias."""
    arr = np.empty((tam, tam, 4), np.float32)
    arr[..., :3] = cor
    n = rng.normal(0, 1, (tam // 6 + 1, tam // 6 + 1))
    n = np.asarray(Image.fromarray(((n + 3) * 40).clip(0, 255).astype(np.uint8)).resize((tam, tam), Image.BICUBIC), np.float32) / 255
    arr[..., :3] *= (0.82 + 0.3 * n)[..., None]
    # pontinhos de "pepperoni" mais escuros
    yy, xx = np.mgrid[0:tam, 0:tam]
    for _ in range(int(r / 9)):
        a, rr = rng.random() * 6.28, (r - 30) * math.sqrt(rng.random())
        px, py = tam / 2 + rr * math.cos(a), tam / 2 + rr * math.sin(a)
        rad = r * 0.09
        dd = ((xx - px) ** 2 + (yy - py) ** 2) < rad ** 2
        arr[dd, :3] *= 0.72
    arr[..., 3] = 235
    return Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8), "RGBA")


def linha_giz(base, p0, p1, frac, cor=GIZ, larg=6):
    if frac <= 0: return
    x0, y0 = p0; x1, y1 = p1
    xe, ye = x0 + (x1 - x0) * frac, y0 + (y1 - y0) * frac
    l, t_ = int(min(x0, xe)) - 10, int(min(y0, ye)) - 10
    w, h = int(abs(xe - x0)) + 21, int(abs(ye - y0)) + 21
    m = Image.new("L", (w, h), 0)
    ImageDraw.Draw(m).line([(x0 - l, y0 - t_), (xe - l, ye - t_)], fill=255, width=larg)
    base.alpha_composite(giz(m, cor, max(l, 0), max(t_, 0)), (l, t_))


def placar(valor_exato, cor, cx, y, destaque=0.0):
    s = f"{round(valor_exato):d}"
    img = texto(s, "Black", 132, cor)
    colar_centro(FR, img, cx - 30, y, escala=1 + 0.12 * destaque)
    un = texto("cm²", "Bold", 40, cor)
    FR.alpha_composite(un, (int(cx - 30 + img.width / 2 * (1 + 0.12 * destaque) + 4), int(y + 8)))


# pecas fixas
print("preparando pecas...", flush=True)
BG = fundo()
TAM_A, TAM_B = int(2 * RA + 40), int(2 * RB + 40)
CONT_A = giz(circulo_giz(RA), GIZ)
CONT_B = [giz(circulo_giz(RB), GIZ) for _ in range(N_B)]
TINTA_A = tinta(RA, COR_A, TAM_A)
TINTA_B = [tinta(RB, COR_B, TAM_B) for _ in range(N_B)]
def _fantasma(tint, r, tam):
    m = Image.new("L", (tam, tam), 0); c = tam / 2
    ImageDraw.Draw(m).ellipse([c - r + 5, c - r + 5, c + r - 5, c + r - 5], fill=80)
    f = tint.copy(); f.putalpha(m); return f
FANTASMA = {id(TINTA_A): _fantasma(TINTA_A, RA, TAM_A)}
for _t in TINTA_B: FANTASMA[id(_t)] = _fantasma(_t, RB, TAM_B)
ROT_A = texto(f"A: {N_A} de {D_A} cm", "Bold", 54, COR_A)
ROT_B = texto(f"B: {N_B} de {D_B} cm", "Bold", 54, COR_B)
VS = texto("VS", "Black", 70, GIZ)
GANCHO = texto("QUAL TEM MAIS?", "Black", 104, GIZ, contorno=0)
GANCHO = GANCHO.resize((960, int(GANCHO.height * 960 / GANCHO.width)), Image.LANCZOS)
FORMULA = texto("área = π · r²", "Bold", 72, GIZ)
PEGA = texto("PEGADINHA!", "Black", 128, VERM)
VENCE_TXT = texto(f"{'B' if vence == 'B' else 'A'} tem mais pizza", "Bold", 64, GIZ)
DIF_TXT = texto(f"+{round(dif)} cm² (uns {round(pct)}% a mais)", "SemiBold", 52, GIZ)
FECHO = texto("e aí, acertou?", "Black", 96, GIZ)
FECHO2 = texto("comenta A ou B", "SemiBold", 52, (190, 190, 180))
ROT_R_A = texto(f"r = {br(r_A)}", "Bold", 44, GIZ, contorno=4)
ROT_R_B = texto(f"r = {br(r_B)}", "Bold", 40, GIZ, contorno=4)


def enchimento(t, lista):
    """Para cada fatia: fracao do raio ja cheia (0..1)."""
    return [ease(prog(t, a, a + d * 0.9)) for a, d in lista]


def valor(t, lista, area_total):
    por = area_total / len(lista)
    return sum(por * ease(prog(t, a, a + d * 0.9)) for a, d in lista)


def desenhar_pizza(c, r, tam, contorno, tint, fracs, ang0=-90, escala=1.0):
    colar_centro(FR, FANTASMA[id(tint)], c[0], c[1], escala)
    if any(f > 0 for f in fracs):
        m = Image.new("L", (tam, tam), 0)
        for i, f in enumerate(fracs):
            if f > 0:
                m.paste(255, mask=fatia_mask(r, ang0 + i * 360 / FATIAS, f, tam))
        layer = tint.copy()
        layer.putalpha(Image.fromarray((np.asarray(m, np.float32) * np.asarray(tint.getchannel("A"), np.float32) / 255).astype(np.uint8)))
        # linhas de corte das fatias ja cheias
        d = ImageDraw.Draw(layer)
        for i, f in enumerate(fracs):
            if f >= 1:
                a = math.radians(ang0 + i * 360 / FATIAS)
                d.line([(tam / 2, tam / 2), (tam / 2 + (r - 5) * math.cos(a), tam / 2 + (r - 5) * math.sin(a))], fill=LOUSA + (200,), width=4)
        colar_centro(FR, layer, c[0], c[1], escala)
    colar_centro(FR, contorno, c[0], c[1], escala)


# ---------------------------------------------------------------- render
def quadro(i):
    global FR
    t = i / FPS
    FR = BG.copy()
    trava = prog(t, T_TRAVA, T_TRAVA + 0.25)
    # entrada de impacto: tudo bate e assenta em 0,25 s
    imp = ease(prog(t, 0, 0.25))
    esc = 1.10 - 0.10 * imp

    fA = enchimento(t, fatiasA)
    fB = enchimento(t, fatiasB)
    # fatias de B alternam entre as duas pizzas
    fB_p = [fB[k::N_B] for k in range(N_B)]

    desenhar_pizza(CA, RA, TAM_A, CONT_A, TINTA_A, fA, escala=esc)
    for k in range(N_B):
        desenhar_pizza(CB[k], RB, TAM_B, CONT_B[k], TINTA_B[k], fB_p[k], escala=esc)

    # raio desenhado
    pa = ease(prog(t, *T_RAIO_A))
    linha_giz(FR, CA, (CA[0] + RA - 6, CA[1]), pa)
    if t >= T_RAIO_A[1] - 0.1 and t < T_TRAVA:
        colar_centro(FR, ROT_R_A, CA[0] + RA / 2, CA[1] - 40, alfa=prog(t, T_RAIO_A[1] - 0.1, T_RAIO_A[1] + 0.1) * (1 - prog(t, T_A0, T_A0 + 0.3)))
    pb = ease(prog(t, *T_RAIO_B))
    for c in CB:
        linha_giz(FR, c, (c[0] + RB - 6, c[1]), pb)
        if t >= T_RAIO_B[1] - 0.1:
            colar_centro(FR, ROT_R_B, c[0] + RB / 2, c[1] - 36, alfa=prog(t, T_RAIO_B[1] - 0.1, T_RAIO_B[1] + 0.1) * (1 - prog(t, T_B0, T_B0 + 0.3)))

    # VS no meio
    if t < T_TRAVA:
        colar_centro(FR, VS, 575, 770, escala=1.6 - 0.6 * imp, alfa=1 - prog(t, T_TRAVA - 0.3, T_TRAVA))

    # topo: gancho no primeiro segundo, depois vira placar
    sai = prog(t, 1.0, 1.25)
    if sai < 1:
        colar_centro(FR, GANCHO, W / 2, 200, escala=(1.06 - 0.06 * imp) * (1 - 0.3 * sai), alfa=1 - sai)
    if t >= 1.0:
        alf = prog(t, 1.05, 1.3)
        vA, vB = valor(t, fatiasA, area_A), valor(t, fatiasB, area_B)
        if alf > 0:
            FR_al = alf
            placar(vA, COR_A, CA[0], 200, destaque=0.0)
            placar(vB, COR_B, CB[0][0], 200, destaque=trava * (vence == "B"))
    # rotulos sob o placar
    colar_centro(FR, ROT_A, CA[0], 330)
    colar_centro(FR, ROT_B, CB[0][0], 330)

    # formula
    pf = prog(t, *T_FORMULA)
    if pf > 0 and t < T_TRAVA:
        w = int(FORMULA.width * ease(pf))
        if w > 0:
            FR.alpha_composite(FORMULA.crop((0, 0, w, FORMULA.height)), (int(W / 2 - FORMULA.width / 2), 1200))

    # trava: risco no perdedor, PEGADINHA, diferenca
    if t >= T_TRAVA:
        perd_c, perd_r = (CA, RA) if vence == "B" else (CB[0], RB)
        x = ease(prog(t, T_TRAVA, T_TRAVA + 0.2))
        linha_giz(FR, (perd_c[0] - perd_r * 0.8, perd_c[1] - perd_r * 0.8), (perd_c[0] + perd_r * 0.8, perd_c[1] + perd_r * 0.8), x, VERM, 12)
        if pegadinha:
            colar_centro(FR, PEGA, W / 2, 1215, escala=1.0 + 0.6 * (1 - ease(trava)), alfa=trava, ang=6)
        else:
            colar_centro(FR, VENCE_TXT, W / 2, 1215, alfa=trava)
        pd = prog(t, T_DIF, T_DIF + 0.3)
        if pd > 0:
            colar_centro(FR, DIF_TXT, W / 2, 1345, alfa=pd)
    pfe = prog(t, T_FECHO, T_FECHO + 0.25)
    if pfe > 0:
        colar_centro(FR, FECHO, W / 2, 1445, escala=1.2 - 0.2 * ease(pfe), alfa=pfe)
        p2 = prog(t, T_FECHO + 0.6, T_FECHO + 0.9)
        if p2 > 0:
            colar_centro(FR, FECHO2, W / 2, 1535, alfa=p2)

    out = FR.convert("RGB")
    # tremida de impacto (inicio e trava)
    sh = 0
    if 0 < t < 0.2: sh = 14 * (1 - t / 0.2)
    if T_TRAVA <= t < T_TRAVA + 0.2: sh = 12 * (1 - (t - T_TRAVA) / 0.2)
    if sh:
        dx, dy = int(sh * math.sin(i * 2.1)), int(sh * math.cos(i * 1.7))
        out = Image.fromarray(np.roll(np.asarray(out), (dy, dx), (0, 1)))
    # flash curto no impacto e na trava
    fl = (0.25 if i in (1, 2) else 0.0) + max(0.0, 1 - abs(t - T_TRAVA) / 0.08) * 0.35 * (t >= T_TRAVA)
    if fl > 0:
        out = Image.blend(out, Image.new("RGB", out.size, (255, 250, 235)), fl)
    return out


# ---------------------------------------------------------------- som
N = int(SR * DUR)
L = np.zeros(N); R = np.zeros(N)


def hz(midi): return 440.0 * 2 ** ((midi - 69) / 12)


def por(sig, t0, pan=0.0, gan=1.0):
    i0 = int(t0 * SR)
    sig = sig[: max(0, N - i0)]
    gl, gr = math.cos((pan + 1) * math.pi / 4), math.sin((pan + 1) * math.pi / 4)
    L[i0:i0 + len(sig)] += sig * gan * gl * 1.414
    R[i0:i0 + len(sig)] += sig * gan * gr * 1.414


def nota(midi, dur=0.5, tau=0.25, harm=(1, .35, .12, .05), ataque=0.004):
    n = int(SR * dur); tt = np.arange(n) / SR
    f = hz(midi)
    s = sum(a * np.sin(2 * np.pi * f * (k + 1) * tt) * np.exp(-tt * (k + 1) * 0.6 / tau) for k, a in enumerate(harm))
    env = np.minimum(tt / ataque, 1) * np.exp(-tt / tau)
    return s * env


def glide(m0, m1, dur=0.22):
    n = int(SR * dur); tt = np.arange(n) / SR
    f = hz(m0) * (hz(m1) / hz(m0)) ** (tt / dur)
    ph = 2 * np.pi * np.cumsum(f) / SR
    env = np.sin(np.pi * tt / dur) ** 2
    return (np.sin(ph) + 0.2 * np.sin(2 * ph)) * env


def impacto(dur=0.45):
    n = int(SR * dur); tt = np.arange(n) / SR
    f = 45 + 95 * np.exp(-tt / 0.05)
    s = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-tt / 0.16)
    ruido = rng.normal(0, 1, n) * np.exp(-tt / 0.035)
    ruido = np.convolve(ruido, np.ones(6) / 6, "same")
    return s + 0.5 * ruido


def giz_som(dur):
    n = int(SR * dur); tt = np.arange(n) / SR
    ru = rng.normal(0, 1, n)
    ru = ru - np.convolve(ru, np.ones(30) / 30, "same")        # tira o grave
    gr = np.abs(np.sin(2 * np.pi * 9 * tt + rng.random())) ** 3   # o vai-e-vem do giz
    return ru * gr * np.sin(np.pi * tt / dur) * 0.6


def acorde(midis, dur=3.2, tau=1.3):
    n = int(SR * dur); tt = np.arange(n) / SR
    s = np.zeros(n)
    for m in midis:
        f = hz(m)
        for k in range(1, 8):
            s += np.sin(2 * np.pi * f * k * tt + k) / k ** 1.4 * np.exp(-tt * (0.4 + 0.25 * k) / tau)
    env = np.minimum(tt / 0.006, 1) * np.exp(-tt / tau)
    return s * env / len(midis)


# altura de cada valor: placar -> nota (0 cm2 = grave, area maior = agudo).
# Mesma regua para os dois lados, arredondada ao semitom.
AMAX = max(area_A, area_B)
def nota_area(v): return round(45 + 27 * v / AMAX)
def nota_cm(v): return round(52 + 12 * math.log2(v / r_B))


# 1) assinatura de 1 s: impacto + "3 1 4 1 5" (digitos do pi como graus de Do maior)
ESCALA = [0, 2, 4, 5, 7, 9, 11, 12, 14, 16]
por(impacto(), 0.0, gan=1.0)
for j, dig in enumerate([3, 1, 4, 1, 5]):
    por(nota(72 + ESCALA[dig - 1], 0.35, 0.12), 0.28 + j * 0.13, pan=-0.3 + 0.15 * j, gan=0.45)
# 2) raios: cada raio vira nota (altura pelo comprimento)
por(giz_som(T_RAIO_A[1] - T_RAIO_A[0]), T_RAIO_A[0], -0.5, 0.25)
por(nota(nota_cm(r_A), 0.6, 0.3), T_RAIO_A[1], -0.6, 0.55)
por(giz_som(T_RAIO_B[1] - T_RAIO_B[0]), T_RAIO_B[0], 0.5, 0.25)
por(nota(nota_cm(r_B), 0.6, 0.3), T_RAIO_B[1], 0.6, 0.55)
# 3) formula: o "=" sobe
por(giz_som(T_FORMULA[1] - T_FORMULA[0]), T_FORMULA[0], 0, 0.2)
f_eq = T_FORMULA[0] + (T_FORMULA[1] - T_FORMULA[0]) * 0.42
por(glide(55, 67, 0.24), f_eq, 0, 0.35)
# 4) cada fatia: nota na altura do placar daquele lado depois da fatia
for side, lista, area, pan in (("A", fatiasA, area_A, -0.6), ("B", fatiasB, area_B, 0.6)):
    por_f = area / len(lista)
    for j, (a, d) in enumerate(lista):
        por(nota(nota_area(por_f * (j + 1)), 0.5, 0.18), a, pan, 0.5)
# tensao: zumbido grave crescente enquanto B corre atras
n = int(SR * (T_TRAVA - T_B0)); tt = np.arange(n) / SR
drone = np.sin(2 * np.pi * 55 * tt) * (0.5 + 0.5 * np.sin(2 * np.pi * (2 + 4 * tt / tt[-1]) * tt)) * (tt / tt[-1]) ** 2
por(drone, T_B0, 0, 0.22)
# 5) trava: impacto + acorde maior na nota do vencedor
raiz = nota_area(max(area_A, area_B))
por(impacto(0.5), T_TRAVA, 0, 0.9)
por(acorde([raiz - 24, raiz - 12, raiz - 8, raiz - 5, raiz]), T_TRAVA, 0.25 if vence == "B" else -0.25, 1.1)
# 6) fecho "e ai, acertou?": duas notas subindo, sem resolver
por(nota(67, 0.4, 0.15), T_FECHO, 0, 0.45)
por(nota(69, 0.7, 0.3), T_FECHO + 0.18, 0, 0.5)
por(glide(69, 71, 0.3), T_FECHO + 0.5, 0, 0.15)

# sala: reverberacao curta por convolucao com ruido decaindo
ir_n = int(SR * 0.8); irt = np.arange(ir_n) / SR
ir = rng.normal(0, 1, ir_n) * np.exp(-irt / 0.18); ir[0] = 0
def rev(x):
    m = 1 << int(np.ceil(np.log2(len(x) + ir_n)))
    y = np.fft.irfft(np.fft.rfft(x, m) * np.fft.rfft(ir, m), m)[: len(x)]
    return x + 0.012 * y
L, R = rev(L), rev(R)
pico = max(np.abs(L).max(), np.abs(R).max())
L, R = L / pico * 0.89, R / pico * 0.89
fade = int(SR * 0.4)
L[-fade:] *= np.linspace(1, 0, fade); R[-fade:] *= np.linspace(1, 0, fade)


def main():
    aqui = os.path.dirname(os.path.abspath(__file__))
    saida = sys.argv[1] if len(sys.argv) > 1 else os.path.join(aqui, "reel2.mp4")
    print(f"A: {N_A}x{D_A} cm = {area_A:.2f} cm2 | B: {N_B}x{D_B} cm = {area_B:.2f} cm2 | vence {vence} | pegadinha={pegadinha} | dif {dif:.2f} cm2 ({pct:.1f}%)")
    t0 = time.time()
    tmp = tempfile.mkdtemp()
    wav = os.path.join(tmp, "som.wav")
    with wave.open(wav, "wb") as wf:
        wf.setnchannels(2); wf.setsampwidth(2); wf.setframerate(SR)
        wf.writeframes((np.stack([L, R], 1) * 32767).astype("<i2").tobytes())
    cmd = ["ffmpeg", "-y", "-loglevel", "error",
           "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
           "-i", wav,
           "-c:v", "libx264", "-preset", "slow", "-crf", "16", "-pix_fmt", "yuv420p",
           "-c:a", "aac", "-b:a", "192k", "-shortest", "-movflags", "+faststart", saida]
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    amostras = {int(x) for x in os.environ.get("QUADROS", "").split(",") if x}
    for i in range(NF):
        q = quadro(i)
        if i in amostras:
            q.save(os.path.join(os.environ.get("QDIR", tmp), f"q{i:03d}.png"))
        p.stdin.write(q.tobytes())
    p.stdin.close(); p.wait()
    print(f"render: {time.time() - t0:.1f} s -> {saida} ({os.path.getsize(saida) / 1024:.0f} KB)")


if __name__ == "__main__":
    main()

"""Trilha original do X1-Plantas: "BIG BIG", 128 BPM, estilo Brazilian Bass.

Feita do zero com síntese (nenhum sample de terceiros), então é nossa e pode ir em anúncio pago.
Uso:  python3 video/musica/gerar_trilha.py      -> video/musica/big-big-128bpm.wav e .m4a

Estrutura (16 compassos, 30 s, 1 compasso = 1,875 s):
  1-4   intro: kick, chimbal, acordes filtrados abrindo, agogô
  5-6   subida: caixa acelerando, ruído subindo, kick some no último tempo
  7-14  drop: baixo "Brazilian bass" saltando, palmas, acordes, agogô, chimbal em 16
  15-16 saída: acordes e kick, termina seco no tempo 1 do compasso 17 (emenda em loop)
"""
from pathlib import Path

import numpy as np
from scipy.signal import butter, fftconvolve, sosfilt

SR = 44100
BPM = 128
BEAT = 60 / BPM
BAR = 4 * BEAT
COMPASSOS = 16
DUR = COMPASSOS * BAR
N = int(DUR * SR) + SR  # 1 s de folga para a cauda
rng = np.random.default_rng(128)
OUT = Path(__file__).resolve().parent


def t_(d):
    return np.arange(int(d * SR)) / SR


def hz(nota):  # nota MIDI -> Hz
    return 440 * 2 ** ((nota - 69) / 12)


def filtro(x, f, tipo="low", ordem=2):
    sos = butter(ordem, f, btype=tipo, fs=SR, output="sos")
    return sosfilt(sos, x)


def por(buf, x, ini, ganho=1.0):
    i = int(ini * SR)
    j = min(len(buf), i + len(x))
    if j > i:
        buf[i:j] += ganho * x[: j - i]


def saw(f, t, detune=0.0):
    fase = (f * (1 + detune)) * t
    return 2 * (fase - np.floor(fase + 0.5))


# ---------------------------------------------------------------- instrumentos
def kick():
    t = t_(0.45)
    f = 48 + 110 * np.exp(-t * 28)
    corpo = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 7)
    clique = filtro(rng.standard_normal(len(t)), 3000, "high") * np.exp(-t * 400) * 0.3
    return np.tanh(1.6 * (corpo + clique))


def palma():
    t = t_(0.3)
    ruido = filtro(rng.standard_normal(len(t)), [900, 5000], "band")
    env = np.zeros_like(t)
    for d in (0, 0.011, 0.022):  # três estalos, como palma real
        env += (t >= d) * np.exp(-np.clip(t - d, 0, None) * (60 if d < 0.02 else 18))
    return ruido * env * 0.55


def chimbal(aberto=False):
    t = t_(0.25 if aberto else 0.06)
    x = filtro(rng.standard_normal(len(t)), 7000, "high")
    return x * np.exp(-t * (14 if aberto else 90)) * 0.22


def caixa():
    t = t_(0.18)
    tom = np.sin(2 * np.pi * 190 * t) * np.exp(-t * 30)
    ruido = filtro(rng.standard_normal(len(t)), 1500, "high") * np.exp(-t * 22)
    return (0.5 * tom + 0.6 * ruido) * 0.5


def agogo(alto=True):
    t = t_(0.16)
    f = 920 if alto else 690
    x = np.sign(np.sin(2 * np.pi * f * t)) * 0.4 + np.sin(2 * np.pi * f * 1.48 * t) * 0.6
    return filtro(x, [500, 4000], "band") * np.exp(-t * 26) * 0.16


def baixo(nota, dur, salto=False):
    """Baixo do Brazilian bass: dente de serra com filtro que abre e fecha, e um pulo de oitava."""
    t = t_(dur)
    f = hz(nota) * np.ones_like(t)
    if salto:  # sobe uma oitava na segunda metade, com deslize
        f *= 2 ** np.clip((t - dur * 0.45) / 0.03, 0, 1)
    fase = np.cumsum(f) / SR
    x = 2 * (fase - np.floor(fase + 0.5)) + 0.6 * np.sin(2 * np.pi * fase * 0.5)
    corte = 300 + 2600 * np.exp(-t * 14)
    y = np.zeros_like(x)
    # filtro passa-baixa variando no tempo, em blocos de 128 amostras
    for i in range(0, len(x), 128):
        y[i : i + 128] = filtro(x[max(0, i - 512) : i + 128], float(corte[i]), "low", 2)[-len(x[i : i + 128]):]
    env = np.minimum(1, t / 0.004) * np.exp(-t * 3.2)
    return np.tanh(2.2 * y * env) * 0.42


def acorde(notas, dur, brilho=1.0):
    t = t_(dur)
    x = sum(saw(hz(n), t, d) for n in notas for d in (-0.007, 0, 0.006))
    x = filtro(x / (3 * len(notas)), 900 + 4500 * brilho, "low")
    env = np.minimum(1, t / 0.006) * np.exp(-t * 5.5)
    return x * env * 0.5


# ---------------------------------------------------------------- arranjo
# Fá menor: Fm - Db - Ab - Eb (i - VI - III - VII), um acorde por compasso
ACORDES = [[65, 68, 72], [61, 65, 68], [68, 72, 75], [63, 67, 70]]
RAIZ = [41, 37, 44, 39]

bateria = np.zeros(N)
grave = np.zeros(N)
harmonia = np.zeros(N)
efeitos = np.zeros(N)

K, P, CX = kick(), palma(), caixa()
for c in range(COMPASSOS):
    ini = c * BAR
    drop = 6 <= c <= 13
    subida = c in (4, 5)
    for b in range(4):
        tb = ini + b * BEAT
        if not (c == 5 and b == 3):  # respiro antes do drop
            por(bateria, K, tb, 1.0)
        if drop and b in (1, 3):
            por(bateria, P, tb, 1.0)
        por(bateria, chimbal(aberto=drop), tb + BEAT / 2, 1.0 if drop else 0.7)
        if drop:
            for s in (0.25, 0.75):
                por(bateria, chimbal(), tb + s * BEAT, 0.5)
    # agogô no ritmo do samba (síncope), na intro e no drop
    if not subida:
        for s, alto in ((0, True), (0.75, False), (1.5, True), (2.5, False), (3.0, True), (3.5, False)):
            por(efeitos, agogo(alto), ini + s * BEAT, 1.0 if drop else 0.6)
    # caixa acelerando na subida: 4, 8 e depois 16 por compasso
    if subida:
        passos = 8 if c == 4 else 16
        for k in range(passos):
            por(bateria, CX, ini + k * BAR / passos, 0.35 + 0.6 * (k / passos) * (c - 3) / 2)
    # acordes: na intro e na saída filtrados; no drop, abertos e no contratempo
    ac = ACORDES[c % 4]
    if drop:
        for s in (0.5, 1.5, 2.5, 3.0, 3.5):
            por(harmonia, acorde(ac, BEAT * 0.45, 1.0), ini + s * BEAT, 0.9)
    else:
        brilho = min(1.0, c / 5) if c < 6 else 0.4
        por(harmonia, acorde(ac, BAR * 0.95, brilho), ini, 0.8)
    # baixo do drop: no contratempo, com pulo de oitava
    if drop:
        r = RAIZ[c % 4]
        for k, s in enumerate((0.5, 1.5, 2.5, 3.5)):
            por(grave, baixo(r, BEAT * 0.48, salto=(k % 2 == 1)), ini + s * BEAT, 1.0)

# ruído subindo nos compassos 5 e 6, e o impacto do drop
t = t_(2 * BAR)
sobe = rng.standard_normal(len(t))
for i in range(0, len(t), 2048):
    f = 400 + 9000 * (i / len(t)) ** 2
    sobe[i : i + 2048] = filtro(sobe[i : i + 2048], [f, min(f * 1.6, 20000)], "band")
sobe *= (t / t[-1]) ** 2 * 0.25
por(efeitos, sobe, 4 * BAR)
ti = t_(1.6)
impacto = np.sin(2 * np.pi * np.cumsum(70 * np.exp(-ti * 3) + 30) / SR) * np.exp(-ti * 2.5) * 0.6
impacto += filtro(rng.standard_normal(len(ti)), 4000, "high") * np.exp(-ti * 3) * 0.15
por(efeitos, impacto, 6 * BAR)

# ---------------------------------------------------------------- mixagem
# "sidechain": tudo menos o kick abaixa a cada batida, o famoso respiro da house
pos = (np.arange(N) / SR) % BEAT
duck = 1 - 0.75 * np.exp(-pos * 14)
grave *= duck
harmonia *= 0.55 + 0.45 * duck

# reverb simples nos acordes e efeitos
ir_t = t_(1.4)
ir = rng.standard_normal(len(ir_t)) * np.exp(-ir_t * 4)
ir = filtro(ir, 6000, "low") / 30
harm_rev = harmonia + fftconvolve(harmonia, ir)[:N]
efe_rev = efeitos + 0.5 * fftconvolve(efeitos, ir)[:N]

# eco de 3/16 de tempo nos acordes, um pouco para cada lado (estéreo)
eco = int(0.75 * BEAT * SR)
esq = bateria + grave + harm_rev + efe_rev
dir_ = bateria + grave + harm_rev + efe_rev
esq[eco:] += 0.22 * harm_rev[:-eco]
dir_[eco // 2 :] += 0.22 * harm_rev[: -(eco // 2)]

mix = np.stack([esq, dir_], axis=1)
mix = mix[: int(DUR * SR)]  # corta seco no fim do compasso 16 para emendar em loop
mix = np.tanh(1.3 * mix / np.max(np.abs(mix)))  # limitador suave
mix *= 0.89 / np.max(np.abs(mix))  # pico em -1 dB

wav = OUT / "big-big-128bpm.wav"
pcm = (mix * 32767).astype("<i2")
import wave

with wave.open(str(wav), "wb") as w:
    w.setnchannels(2)
    w.setsampwidth(2)
    w.setframerate(SR)
    w.writeframes(pcm.tobytes())
print(f"{wav} · {DUR:.1f} s · {BPM} BPM")

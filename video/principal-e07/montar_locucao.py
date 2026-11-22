"""Monta o anúncio do e-book com a locução do dono (E07, 26,25 s = 14 compassos a 128 BPM).

Uso: python3 video/principal-e07/montar_locucao.py
Entradas: voz/gravacao-dono.m4a e voz/palavras.json (transcrição com o tempo de cada palavra),
          os clipes em openart/ (ou kit-minoai/clipes/), blueprint-limpo.mp4 e ../musica/big-big-128bpm.wav.
Saídas:   ../saida/principal-e07/x1-plantas-e07-locucao.mp4 (1080 x 1920) e -whatsapp.mp4 (720 x 1280),
          e ../saida/principal-e07/conferencia-locucao.png (um quadro por frase, para conferir imagem contra fala).

Áudio pelas regras da MinoAI Frontier (rulebook v1.22, seção audio), aplicadas à mão porque as ferramentas dela
só rodam no computador do dono: corte só em silêncio, nada de compressor nem redução de ruído, voz perto de
-12 LUFS, limitador 0,80, pico até -1 dBTP, música medida sozinha (-29,5 LUFS antes do drop, -28 depois).
"""
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parent.parent
SAIDA = RAIZ / "video/saida/principal-e07"
FPS, B = 30, 60 / 128          # B = um tempo (0,469 s)
DUR = 56 * B                   # 14 compassos = 26,25 s

# --- corte da voz: sai "Eu nem respondi, só mandei construir. Olha aqui o resultado." (a casa não foi construída)
CORTE = (6.00, 9.85)           # os dois pontos caem em silêncio medido (5,87–6,47 e 9,58–9,88); 10,20 comia o "se" de "setenta"
FIM_VOZ = 28.15
novo = lambda t: t if t <= CORTE[0] else t - (CORTE[1] - CORTE[0])

O = "openart/"
# (nome, fonte, início na fonte, velocidade, fim no vídeo em tempos, sem selo? = desenho ou página nossa, não imagem gerada)
CENAS = [
    ("fachada-rosa", O + "v7-fachada-rosa.mp4", 0.0, 1.0, 5, False),      # "Meu tio viu a planta no grupo… mandou isso"
    ("almoco", O + "v8-almoco.mp4", 0.0, 1.0, 13, False),                 # a frase do tio; a imagem desmente
    ("blueprint", "blueprint-limpo.mp4", 0.9, 2.0, 20, True),             # "72 m², 3 quartos" (os quartos acendem na fala)
    ("vira-casa", O + "v1-transicao.mp4", 1.0, 2.133, 24, False),         # "sendo 1 suíte e 2 banheiros"
    ("vista-de-cima", O + "v2-voo.mp4", 0.1, 1.0, 26, False),             # drop: "Tudo dentro dos 8 metros"
    ("almoco-2", O + "v8-almoco.mp4", 3.55, 1.0, 29, False),              # "que ele jurou que não ia caber"
    ("cozinha", O + "v6-onigiri.mp4", 0.5, 1.0, 33, False),               # "A gente não é arquiteto nem engenheiro"
    ("blueprint-2", "blueprint-limpo.mp4", 0.94, 1.5, 37, True),          # "só ficamos obcecado" (a caneta desenhando)
    ("sala", O + "v3-sala.mp4", 1.6, 1.0, 41, False),                     # "até provar que dava certo"
    ("fachada", O + "v5-fachada.mp4", 0.3, 1.0, 44, False),               # "Eu volto para o Brasil" (bandeirinhas)
    ("ebook", "../broll/ebook-folheando.mp4", 0.0, 2.0, 48, True),        # "com um e-book cheio de plantas assim"
    ("fachada-rosa-2", O + "v7-fachada-rosa.mp4", 1.2, 1.0, 56, False),   # "Comenta PLANTA…" e o fim em dois tempos
]
BALAO = (5 * B, 13 * B)
FIM = {"balao": 52 * B, "resposta": 53 * B, "cta": 54 * B}

# palavras como foram ditas (a transcrição automática erra algumas); a chave é o índice em palavras.json
CORRIGE = {0: "Meu tio viu", 22: "Natal.", 81: "e-book", 82: "", 88: "", 89: "PLANTA"}
AMARELO = {"3", "quartos", "8", "metros", "Natal.", "72", "suíte", "banheiros.", "caber.", "arquiteto", "engenheiro,",
           "obcecado", "certo.", "Brasil", "e-book", "PLANTA", "metros quadrados,"}


def sh(*a, **k):
    return subprocess.run([str(x) for x in a], check=True, capture_output=True, text=True, **k)


def lufs(arq, ini=None, fim=None):
    f = "ebur128=peak=true"
    if ini is not None:
        f = f"atrim={ini}:{fim},asetpts=N/SR/TB," + f
    r = subprocess.run(["ffmpeg", "-hide_banner", "-i", str(arq), "-af", f, "-f", "null", "-"], capture_output=True, text=True).stderr
    resumo = r[r.rfind("Summary:"):]
    return float(re.search(r"I:\s+(-?[\d.]+) LUFS", resumo).group(1)), float(re.search(r"Peak:\s+(-?[\d.]+) dBFS", resumo).group(1))


def audio(tmp):
    voz = AQUI / "voz/gravacao-dono.m4a"
    cortada = tmp / "voz.wav"
    a, b = CORTE
    sh("ffmpeg", "-y", "-loglevel", "error", "-i", voz, "-filter_complex",
       f"[0:a]asplit[p][q];[p]atrim=0:{a},asetpts=N/SR/TB,afade=t=out:st={a - .012:.3f}:d=0.012[x];"
       f"[q]atrim={b}:{FIM_VOZ},asetpts=N/SR/TB,afade=t=in:d=0.012[y];[x][y]concat=n=2:v=0:a=1,aresample=48000[o]",
       "-map", "[o]", "-ac", "2", cortada)
    nivel, _ = lufs(cortada)
    ganho_voz = -11.4 - nivel
    musica = RAIZ / "video/musica/big-big-128bpm.wav"
    drop, fala_fim = 24 * B, novo(FIM_VOZ) + .15
    l1, _ = lufs(musica, 0, drop)
    l2, _ = lufs(musica, drop, fala_fim)
    g = [10 ** ((alvo - l) / 20) for alvo, l in ((-29.5, l1), (-28.0, l2), (-21.0, l2))]
    vol = (f"if(lt(t,{drop - .03}),{g[0]},if(lt(t,{drop}),{g[0]}+({g[1]}-{g[0]})*(t-{drop - .03})/.03,"
           f"if(lt(t,{fala_fim}),{g[1]},if(lt(t,{fala_fim + .3}),{g[1]}+({g[2]}-{g[1]})*(t-{fala_fim})/.3,{g[2]}))))")
    mix = tmp / "mix.wav"
    sh("ffmpeg", "-y", "-loglevel", "error", "-i", cortada, "-i", musica, "-filter_complex",
       f"[0:a]volume={ganho_voz}dB,apad=whole_dur={DUR}[v];"
       f"[1:a]atrim=0:{DUR},aresample=48000,volume='{vol}':eval=frame,afade=t=out:st={DUR - .25}:d=0.25[m];"
       f"[v][m]amix=inputs=2:normalize=0,alimiter=limit=0.8:level=0,atrim=0:{DUR}[o]",
       "-map", "[o]", mix)
    final, pico = lufs(mix)
    print(f"voz: {nivel:.1f} LUFS, ganho {ganho_voz:+.1f} dB · música sozinha: {l1 + 20 * __import__('math').log10(g[0]):.1f} / "
          f"{l2 + 20 * __import__('math').log10(g[1]):.1f} LUFS · mistura: {final:.1f} LUFS, pico {pico:.1f} dBFS")
    return mix


def legendas():
    """Blocos de até 3 palavras, com os tempos remapeados pelo corte. Sem legenda onde o balão ou o título já mostram a fala."""
    palavras = json.loads((AQUI / "voz/palavras.json").read_text(encoding="utf-8"))
    itens = []
    for i, (ini, fim, txt) in enumerate(palavras):
        if CORTE[0] <= ini < CORTE[1]:
            continue
        txt = CORRIGE.get(i, txt)
        if txt:
            itens.append([novo(ini), novo(fim), txt])
    mudos = [BALAO, (novo(9.86), novo(14.9))]           # balão; números grandes no alto
    blocos, atual = [], []
    for k, it in enumerate(itens):
        atual.append(it)
        prox = itens[k + 1] if k + 1 < len(itens) else None
        fecha = (len(atual) == 3 or prox is None or re.search(r"[.,?!]$", it[2]) or prox[0] - it[1] > .3
                 or len(" ".join(x[2] for x in atual)) > 16)
        if fecha:
            blocos.append(atual)
            atual = []
    saida = []
    for k, bl in enumerate(blocos):
        ini = bl[0][0]
        fim = min(blocos[k + 1][0][0] if k + 1 < len(blocos) else bl[-1][1] + .3, bl[-1][1] + .45)
        if any(a <= ini < b for a, b in mudos):
            continue
        html = " ".join(f"<b>{x[2]}</b>" if x[2] in AMARELO else x[2] for x in bl)
        saida.append({"ini": round(ini, 3), "fim": round(fim, 3), "html": html})
    return saida


def dados():
    t = lambda orig: round(novo(orig), 3)
    return {
        "legendas": legendas(),
        "titulos": [
            {"ini": 0, "fim": 5 * B, "html": "Meu tio disse que <b>não cabia</b>"},
            {"ini": t(9.95), "fim": t(11.95), "html": "<b>72 m²</b>", "tam": 190},
            {"ini": t(11.95), "fim": t(12.9), "html": "<b>3 quartos</b>", "tam": 170},
            {"ini": t(12.9), "fim": 24 * B, "html": "1 suíte<br><b>2 banheiros</b>", "tam": 130},
            {"ini": 24 * B, "fim": 29 * B, "html": "<b>Cabe</b> em lote<br>8 x 25 m."},
        ],
        "sem_selo": [[(CENAS[i - 1][4] if i else 0) * B, c[4] * B] for i, c in enumerate(CENAS) if c[5]],
        "balao": list(BALAO), "fim": FIM,
    }


def video_base(tmp):
    partes, quadro = [], 0
    for nome, fonte, ini, vel, fim_tempos, _ in CENAS:
        ate = round(fim_tempos * B * FPS)
        n, quadro = ate - quadro, ate
        arq = tmp / f"{nome}.mp4"
        sh("ffmpeg", "-y", "-loglevel", "error", "-ss", ini, "-i", AQUI / fonte, "-an", "-vf",
           f"setpts=(PTS-STARTPTS)/{vel},fps={FPS},scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1",
           "-frames:v", n, "-c:v", "libx264", "-crf", "12", "-preset", "veryfast", "-pix_fmt", "yuv420p", arq)
        partes.append(arq)
    lista = tmp / "lista.txt"
    lista.write_text("".join(f"file '{p}'\n" for p in partes))
    base = tmp / "base.mp4"
    sh("ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", lista, "-c", "copy", base)
    return base


NODE = r"""
const { chromium } = require('playwright'); const fs = require('fs');
const [html, dados, n, fps] = process.argv.slice(2);
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1080, height: 1920 } });
  await p.addInitScript('window.DADOS = ' + fs.readFileSync(dados, 'utf8'));
  await p.goto('file://' + html); await p.evaluate(() => window.pronto); await p.waitForTimeout(300);
  for (let i = 0; i < +n; i++) {
    await p.evaluate((t) => window.renderAt(t), i / +fps);
    const png = await p.screenshot({ omitBackground: true });
    if (!process.stdout.write(png)) await new Promise((r) => process.stdout.once('drain', r));
  }
  await b.close();
})();
"""


def main():
    SAIDA.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as t:
        tmp = Path(t)
        mix = audio(tmp)
        base = video_base(tmp)
        d = dados()
        (tmp / "dados.json").write_text(json.dumps(d, ensure_ascii=False))
        (tmp / "camadas.cjs").write_text(NODE)
        n = round(DUR * FPS)
        final = SAIDA / "x1-plantas-e07-locucao.mp4"
        camadas = subprocess.Popen(["node", tmp / "camadas.cjs", AQUI / "locucao-camadas.html", tmp / "dados.json", str(n), str(FPS)],
                                   stdout=subprocess.PIPE, cwd=AQUI)
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(base), "-f", "image2pipe", "-framerate", str(FPS), "-c:v", "png", "-i", "-",
                        "-i", str(mix), "-filter_complex", "[0:v][1:v]overlay=0:0:format=auto,format=yuv420p[v]", "-map", "[v]", "-map", "2:a",
                        "-frames:v", str(n), "-c:v", "libx264", "-crf", "25", "-preset", "slow", "-c:a", "aac", "-b:a", "160k",
                        "-movflags", "+faststart", str(final)], stdin=camadas.stdout, check=True)
        camadas.wait()
        zap = SAIDA / "x1-plantas-e07-locucao-whatsapp.mp4"
        sh("ffmpeg", "-y", "-loglevel", "error", "-i", final, "-vf", "scale=720:1280", "-c:v", "libx264", "-crf", "29", "-preset", "slow",
           "-c:a", "aac", "-b:a", "96k", "-movflags", "+faststart", zap)
        # conferência: um quadro no meio de cada frase, com a frase escrita embaixo
        frases = [(0.0, 2.07, "Meu tio viu a planta no grupo da família e mandou isso"), (2.34, 5.87, "3 quartos em 8 metros de frente, cabe nem a família no Natal"),
                  (9.95, 11.9, "72 metros quadrados"), (11.98, 12.9, "3 quartos"), (12.94, 14.84, "sendo 1 suíte e 2 banheiros"),
                  (14.98, 16.2, "Tudo dentro dos 8 metros"), (16.2, 17.04, "que ele jurou que não ia caber"),
                  (17.62, 19.5, "A gente não é arquiteto nem engenheiro"), (19.6, 20.9, "só ficamos obcecado"), (21.5, 22.97, "até provar que dava certo"),
                  (23.38, 24.6, "Eu volto para o Brasil em algumas semanas"), (24.7, 26.5, "com um e-book cheio de plantas assim"),
                  (26.68, 28.04, "Comenta PLANTA que eu te mando"), (FIM["resposta"] + .2, None, "(silêncio) balão e resposta"), (DUR - .2, None, "(silêncio) Comenta PLANTA")]
        quadros = []
        for i, (a, b, txt) in enumerate(frases):
            q = tmp / f"q{i:02d}.png"
            meio = a if b is None else (novo(a) + novo(b)) / 2      # b None = tempo já no vídeo final
            a = a if b is None else novo(a)
            sh("ffmpeg", "-y", "-loglevel", "error", "-ss", f"{meio:.3f}", "-i", final, "-frames:v", "1", "-update", "1", "-vf",
               f"scale=270:480,pad=270:560:0:0:color=white,drawtext=text='{a:.1f}s {txt[:34]}':x=6:y=490:fontsize=13:fontcolor=black,"
               f"drawtext=text='{txt[34:68]}':x=6:y=512:fontsize=13:fontcolor=black", q)
            quadros.append(q)
        entradas = [x for q in quadros for x in ("-i", q)]
        sh("ffmpeg", "-y", "-loglevel", "error", *entradas, "-filter_complex", f"xstack=inputs={len(quadros)}:grid=5x3", "-update", "1",
           SAIDA / "conferencia-locucao.png")
        for f in (final, zap):
            print(f"{f.relative_to(RAIZ)}: {f.stat().st_size / 1e6:.1f} MB")


if __name__ == "__main__":
    main()

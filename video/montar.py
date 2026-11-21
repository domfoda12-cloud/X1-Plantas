"""Monta um vídeo vertical a partir de um roteiro em JSON: clipes ou imagens, texto na tela e compressão.

Uso: python3 video/montar.py video/roteiros/principal.json
O roteiro diz a saída, o tamanho e as cenas. Cada cena tem: "fonte" (vídeo ou imagem), "dur" (segundos),
e textos opcionais: "olho", "titulo", "sub", "selo" (ex.: "Imagem ilustrativa"), "zoom" (para imagem parada)
"caber" (mostra a página inteira do e-book sobre o azul, sem cortar) e "continua" (o texto da cena anterior segue, sem piscar).
O rodapé legal ("rodape") aparece em todas as cenas. Sem música: a trilha licenciada entra na edição final.
"""
import json
import subprocess
import sys
import tempfile
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
FPS = 30

HTML = """<!doctype html><html><head><meta charset="utf-8">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,700;12..96,800&family=Inter:wght@500;600;700&family=JetBrains+Mono:wght@700&display=swap">
<style>
*{box-sizing:border-box;margin:0}
html,body{width:1080px;height:1920px;background:transparent;overflow:hidden;font-family:Inter,sans-serif;color:#fff}
.topo{position:absolute;left:0;right:0;top:0;height:760px;background:linear-gradient(rgba(6,26,58,.82),rgba(6,26,58,.55) 55%,rgba(6,26,58,0))}
.base{position:absolute;left:0;right:0;bottom:0;height:560px;background:linear-gradient(rgba(6,26,58,0),rgba(6,26,58,.78) 60%)}
.bloco{position:absolute;left:70px;right:70px;top:230px;display:grid;gap:22px}
.olho{font-family:"JetBrains Mono",monospace;font-size:34px;letter-spacing:.08em;color:#FFC857;text-transform:uppercase}
.titulo{font-family:"Bricolage Grotesque",sans-serif;font-weight:800;font-size:104px;line-height:.98;letter-spacing:-.02em;text-wrap:balance;text-shadow:0 4px 24px rgba(0,0,0,.45)}
.titulo b{color:#FFC857}
.sub{font-size:46px;font-weight:600;line-height:1.2;text-wrap:balance;text-shadow:0 2px 14px rgba(0,0,0,.5)}
.selo{position:absolute;left:70px;bottom:470px;font-size:28px;font-weight:600;background:rgba(0,0,0,.55);padding:8px 18px;border-radius:8px}
.rodape{position:absolute;left:70px;right:70px;bottom:360px;font-size:27px;font-weight:500;line-height:1.3;color:rgba(255,255,255,.92)}
/* página inteira do e-book: nada por cima dela, o aviso fica embaixo */
.caber .topo,.caber .base{display:none!important}.caber .bloco{top:130px}.caber .titulo{font-size:92px}.caber .rodape{bottom:90px}
</style></head><body class="%(classe)s">
<div class="topo" style="display:%(tem_topo)s"></div><div class="base"></div>
<div class="bloco">%(olho)s%(titulo)s%(sub)s</div>%(selo)s<div class="rodape">%(rodape)s</div>
</body></html>"""


def rodar(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        sys.exit(f"Falhou: {' '.join(map(str, cmd[:6]))}…\n{r.stderr[-1500:]}")


def texto_png(cena, rodape, destino, tmp):
    """Desenha o texto da cena numa imagem transparente (as mesmas fontes do e-book)."""
    tag = lambda classe, chave: f'<div class="{classe}">{cena[chave]}</div>' if cena.get(chave) else ""
    html = HTML
    for chave, valor in dict(olho=tag("olho", "olho"), titulo=tag("titulo", "titulo"), sub=tag("sub", "sub"),
                             selo=tag("selo", "selo"), rodape=rodape, classe="caber" if cena.get("caber") else "",
                             tem_topo="block" if any(cena.get(k) for k in ("olho", "titulo", "sub")) else "none").items():
        html = html.replace("%(" + chave + ")s", valor)
    arq = Path(tmp) / "texto.html"
    arq.write_text(html, encoding="utf-8")
    js = ("const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();"
          "const p=await b.newPage({viewport:{width:1080,height:1920}});"
          f"await p.goto('file://{arq}');await p.evaluate(()=>document.fonts.ready);"
          f"await p.screenshot({{path:'{destino}',omitBackground:true}});await b.close();}})()")
    rodar(["node", "-e", js])


def cena_mp4(cena, rodape, destino, tmp):
    fonte = RAIZ / cena["fonte"] if not Path(cena["fonte"]).is_absolute() else Path(cena["fonte"])
    dur = cena["dur"]
    png = Path(tmp) / f"{destino.stem}.png"
    texto_png(cena, rodape, png, tmp)
    enquadra = "scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920"
    if cena.get("caber"):
        # página inteira do e-book sobre o azul de projeto, com espaço em cima para o título
        base = "[0:v]scale=-2:1180,pad=1080:1920:(ow-iw)/2:520:color=0x08397A,fps=%d[v]" % FPS
        entrada = ["-loop", "1", "-t", str(dur), "-i", str(fonte)]
    elif fonte.suffix.lower() in (".png", ".jpg", ".jpeg"):
        z0, z1 = cena.get("zoom", [1.0, 1.08])
        n = int(dur * FPS)
        # imagem parada: aproximação lenta, calculada numa tela grande para não tremer
        base = (f"[0:v]scale=2160:3840:force_original_aspect_ratio=increase,crop=2160:3840:{cena.get('corte', '(iw-ow)/2:(ih-oh)/2')},"
                f"zoompan=z='{z0}+({z1}-{z0})*on/{n}':x='iw/2-(iw/zoom/2)':y='{cena.get('foco_y', 'ih/2-(ih/zoom/2)')}':d={n}:s=1080x1920:fps={FPS}[v]")
        entrada = ["-loop", "1", "-t", str(dur), "-i", str(fonte)]
    else:
        ini = cena.get("inicio", 0)
        vel = cena.get("vel", 1.0)
        base = f"[0:v]setpts={1 / vel}*PTS,fps={FPS},{enquadra}[v]"
        entrada = ["-ss", str(ini), "-i", str(fonte)]
    # "continua": o mesmo texto da cena anterior segue na tela, sem piscar no corte
    entra = "" if cena.get("continua") else ",fade=t=in:st=0:d=0.25:alpha=1"
    filtro = f"{base};[1:v]format=rgba{entra}[t];[v][t]overlay=0:0,format=yuv420p[o]"
    rodar(["ffmpeg", "-y", "-loglevel", "error", *entrada, "-loop", "1", "-t", str(dur), "-i", str(png),
           "-filter_complex", filtro, "-map", "[o]", "-t", str(dur), "-r", str(FPS),
           "-c:v", "libx264", "-crf", "16", "-preset", "medium", str(destino)])


def main(arq):
    roteiro = json.loads(Path(arq).read_text(encoding="utf-8"))
    saida = RAIZ / roteiro["saida"]
    saida.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as tmp:
        partes = []
        for i, cena in enumerate(roteiro["cenas"]):
            p = Path(tmp) / f"cena{i:02d}.mp4"
            cena_mp4(cena, roteiro.get("rodape", ""), p, tmp)
            partes.append(p)
            print(f"cena {i + 1}/{len(roteiro['cenas'])}")
        lista = Path(tmp) / "lista.txt"
        lista.write_text("".join(f"file '{p}'\n" for p in partes))
        w, h = roteiro.get("tamanho", [1080, 1920])
        total = sum(c["dur"] for c in roteiro["cenas"])
        # faixa de áudio muda: o WhatsApp e o Instagram aceitam melhor um arquivo com áudio
        rodar(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", str(lista),
               "-f", "lavfi", "-t", str(total), "-i", "anullsrc=r=44100:cl=stereo",
               "-vf", f"scale={w}:{h}", "-c:v", "libx264", "-crf", str(roteiro.get("crf", 23)), "-preset", "slow",
               "-pix_fmt", "yuv420p", "-movflags", "+faststart", "-c:a", "aac", "-b:a", "48k", "-shortest", str(saida)])
    print(f"{saida.relative_to(RAIZ)}: {saida.stat().st_size / 1e6:.1f} MB, {total:.0f} s, {w}x{h}")


if __name__ == "__main__":
    main(sys.argv[1])

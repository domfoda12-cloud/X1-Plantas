"""Monta um vídeo vertical a partir de um roteiro em JSON: clipes ou imagens, texto na tela e compressão.

Uso: python3 video/montar.py video/roteiros/principal.json
O roteiro diz a saída, o tamanho e as cenas. Cada cena tem: "fonte" (vídeo ou imagem), "dur" (segundos),
e textos opcionais: "olho", "titulo", "sub", "selo" (ex.: "Imagem ilustrativa"), "zoom" (para imagem parada)
"caber" (mostra a página inteira do e-book sobre o azul, sem cortar) e "continua" (o texto da cena anterior segue, sem piscar).
O rodapé legal ("rodape") aparece em todas as cenas. Sem música: a trilha licenciada entra na edição final.

Recursos de edição (estilo CONDOR, todos opcionais; sem eles a cena sai como antes):
  "vel": [2.5, 1]     velocidade que muda ao longo da cena (speed ramp): entra rápido e assenta.
  "zoom": [1.0, 1.1]  aproximação também em clipe de vídeo; "impacto": true dá um soco de zoom nos primeiros 0,3 s.
  "gira": 0.6         a imagem entra de cabeça para baixo e gira até a posição certa em 0,6 s; "invertida": true deixa de ponta-cabeça.
  "janela": "8×15"    letra gigante e estreita como janela: a tela fica azul e a imagem só aparece dentro das letras.
  "abre": 0.6         nos últimos 0,6 s a janela se abre (zoom para dentro da letra) e a imagem toma a tela; "abre_em": [x, y] é o ponto do zoom.
  "tam": 170          tamanho do título em px (palavra única no tempo da batida).
  "trocar": true      só um aviso para quem edita: a fonte desta cena vai ser trocada. O montador ignora.
No roteiro: "grao": 6 põe um granulado leve no vídeo todo (0 ou ausente = sem).
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
/* letra como janela: o subtítulo desce para baixo das letras */
.janela .sub{position:absolute;left:0;right:0;top:1000px}
</style></head><body class="%(classe)s">
<div class="topo" style="display:%(tem_topo)s"></div><div class="base"></div>
<div class="bloco">%(olho)s%(titulo)s%(sub)s</div>%(selo)s<div class="rodape">%(rodape)s</div>
</body></html>"""


# a tela azul com as letras vazadas; o contorno amarelo garante a leitura com qualquer imagem por trás
JANELA = """<!doctype html><html><head><meta charset="utf-8">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,800&display=swap">
<style>*{margin:0}html,body{width:1080px;height:1920px;background:transparent;overflow:hidden}
text{font-family:"Bricolage Grotesque",sans-serif;font-weight:800;font-size:%(px)spx}</style></head><body>
<svg width="1080" height="1920"><defs><mask id="m"><rect width="1080" height="1920" fill="#fff"/>
<text x="70" y="1175" textLength="940" lengthAdjust="spacingAndGlyphs" fill="#000">%(texto)s</text></mask></defs>
<rect width="1080" height="1920" fill="#061A3A" mask="url(#m)"/>
<text x="70" y="1175" textLength="940" lengthAdjust="spacingAndGlyphs" fill="none" stroke="#FFC857" stroke-width="5">%(texto)s</text></svg>
</body></html>"""


def rodar(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        sys.exit(f"Falhou: {' '.join(map(str, cmd[:6]))}…\n{r.stderr[-1500:]}")


def html_png(html, destino, tmp, escala=1):
    """Fotografa um HTML de 1080x1920 com fundo transparente."""
    arq = Path(tmp) / "texto.html"
    arq.write_text(html, encoding="utf-8")
    js = ("const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();"
          f"const p=await b.newPage({{viewport:{{width:1080,height:1920}},deviceScaleFactor:{escala}}});"
          f"await p.goto('file://{arq}');await p.evaluate(()=>document.fonts.ready);"
          f"await p.screenshot({{path:'{destino}',omitBackground:true}});await b.close();}})()")
    rodar(["node", "-e", js])


def texto_png(cena, rodape, destino, tmp):
    """Desenha o texto da cena numa imagem transparente (as mesmas fontes do e-book)."""
    tag = lambda classe, chave: f'<div class="{classe}">{cena[chave]}</div>' if cena.get(chave) else ""
    titulo = tag("titulo", "titulo")
    if cena.get("tam"):
        titulo = titulo.replace('class="titulo"', f'class="titulo" style="font-size:{cena["tam"]}px"')
    html = HTML
    for chave, valor in dict(olho=tag("olho", "olho"), titulo=titulo, sub=tag("sub", "sub"),
                             selo=tag("selo", "selo"), rodape=rodape,
                             classe="caber" if cena.get("caber") else "janela" if cena.get("janela") else "",
                             tem_topo="block" if any(cena.get(k) for k in ("olho", "titulo", "sub")) else "none").items():
        html = html.replace("%(" + chave + ")s", valor)
    html_png(html, destino, tmp)


def zoom_expr(cena, n, padrao):
    """Zoom da cena quadro a quadro: de z0 a z1, mais o soco de "impacto" nos primeiros 9 quadros."""
    z0, z1 = cena.get("zoom", padrao)
    soco = "*(1+0.12*pow(max(0,1-on/9),2))" if cena.get("impacto") else ""
    return f"({z0}+({z1}-{z0})*on/{n}){soco}"


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
        n = int(dur * FPS)
        # imagem parada: aproximação lenta, calculada numa tela grande para não tremer
        base = (f"[0:v]scale=2160:3840:force_original_aspect_ratio=increase,crop=2160:3840:{cena.get('corte', '(iw-ow)/2:(ih-oh)/2')},"
                f"zoompan=z='{zoom_expr(cena, n, [1.0, 1.08])}':x='iw/2-(iw/zoom/2)':y='{cena.get('foco_y', 'ih/2-(ih/zoom/2)')}':d={n}:s=1080x1920:fps={FPS}[v]")
        entrada = ["-loop", "1", "-t", str(dur), "-i", str(fonte)]
    else:
        ini = cena.get("inicio", 0)
        vel = cena.get("vel", 1.0)
        if isinstance(vel, list) and vel[0] != vel[1]:
            # velocidade que muda em linha reta de v0 a v1 ao longo da cena; o trecho usado da fonte é (v0+v1)/2 x dur
            v0, a = vel[0], (vel[1] - vel[0]) / dur
            tempo = f"setpts='(sqrt(max(0,{v0 * v0}+{2 * a}*(PTS-STARTPTS)*TB))-{v0})/{a}/TB'"
        else:
            tempo = f"setpts={1 / (vel[0] if isinstance(vel, list) else vel)}*(PTS-STARTPTS)"
        base = f"[0:v]{tempo},fps={FPS},{enquadra}"
        if cena.get("zoom") or cena.get("impacto"):
            base += (f",scale=2160:3840,zoompan=z='{zoom_expr(cena, int(dur * FPS), [1.0, 1.0])}':x='iw/2-(iw/zoom/2)'"
                     f":y='ih/2-(ih/zoom/2)':d=1:s=1080x1920:fps={FPS}")
        base += "[v]"
        entrada = ["-ss", str(ini), "-i", str(fonte)]
    if cena.get("invertida"):
        base = base[:-3] + ",hflip,vflip[v]"
    if cena.get("gira"):
        # entra de cabeça para baixo e gira até a posição certa, freando no fim
        base = base[:-3] + f",rotate=a='PI*pow(max(0,1-t/{cena['gira']}),2)':c={cena.get('fundo', '0x1552B0')}[v]"
    extra = []
    if cena.get("janela"):
        mascara = Path(tmp) / f"{destino.stem}-janela.png"
        html_png(JANELA.replace("%(texto)s", cena["janela"]).replace("%(px)s", str(cena.get("janela_px", 800))), mascara, tmp, 2)
        extra = ["-loop", "1", "-t", str(dur), "-i", str(mascara)]
        jan = "[2:v]format=rgba,scale=1080:1920"
        if cena.get("abre"):
            # abre a janela: zoom para dentro da letra (o zoompan vai até 10x) e a máscara some no fim
            ab, (cx, cy) = cena["abre"], cena.get("abre_em", [540, 880])
            n0, na = int((dur - ab) * FPS), max(1, int(ab * FPS))
            jan = (f"[2:v]format=rgba,zoompan=z='pow(10,pow(clip((on-{n0})/{na},0,1),2))':x='{2 * cx}*(1-1/zoom)'"
                   f":y='{2 * cy}*(1-1/zoom)':d=1:s=1080x1920:fps={FPS},fade=t=out:st={dur - ab / 2}:d={ab / 2}:alpha=1")
        base += f";{jan}[j];[v][j]overlay=0:0[v]"
    # "continua": o mesmo texto da cena anterior segue na tela, sem piscar no corte
    entra = "" if cena.get("continua") else ",fade=t=in:st=0:d=0.25:alpha=1"
    filtro = f"{base};[1:v]format=rgba{entra}[t];[v][t]overlay=0:0,format=yuv420p[o]"
    rodar(["ffmpeg", "-y", "-loglevel", "error", *entrada, "-loop", "1", "-t", str(dur), "-i", str(png), *extra,
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
               "-vf", f"scale={w}:{h}" + (f",noise=alls={roteiro['grao']}:allf=t" if roteiro.get("grao") else ""), "-c:v", "libx264", "-crf", str(roteiro.get("crf", 23)), "-preset", "slow",
               "-pix_fmt", "yuv420p", "-movflags", "+faststart", "-c:a", "aac", "-b:a", "48k", "-shortest", str(saida)])
    print(f"{saida.relative_to(RAIZ)}: {saida.stat().st_size / 1e6:.1f} MB, {total:.0f} s, {w}x{h}")


if __name__ == "__main__":
    main(sys.argv[1])

# Gera as 6 páginas-amostra do D50 (3 direções x capa + página da C01) em HTML.
# Os SVG vêm da prévia do nosso gerador (c01-planta.svg, capa-planta.svg); os textos são os da prévia.
import pathlib
S = pathlib.Path(__file__).parent
PLANTA = (S / "c01-planta.svg").read_text()
PLANTA_ESC = (S / "capa-planta.svg").read_text()
FOTO3D = "/home/user/X1-Plantas/ebook/.cache/fotos/3d-C01-900.jpg"

# luz da porta (só na direção 3): um brilho sobre a entrada, sem mexer em porta ou janela
BRILHO = ('<defs><radialGradient id="luz"><stop offset="0" stop-color="#FFC857" stop-opacity=".95"/>'
          '<stop offset=".45" stop-color="#FFC857" stop-opacity=".22"/><stop offset="1" stop-color="#FFC857" stop-opacity="0"/>'
          '</radialGradient></defs><circle cx="1.05" cy="8.75" r="2.4" fill="url(#luz)"/></svg>')
PLANTA_ESC_LUZ = PLANTA_ESC[: PLANTA_ESC.rfind("</svg>")] + BRILHO

PORTA = ('<svg class="porta-acesa" viewBox="0 0 20 30" aria-hidden="true"><path d="M3 21 L17 21 L20 30 L0 30 Z" fill="#FFC857" opacity=".35"/>'
         '<rect x="4" y="1" width="12" height="20" rx="1" fill="#FFC857"/><rect x="5.6" y="2.6" width="8.8" height="16.8" rx=".6" fill="none" stroke="#0A1630" stroke-width=".9" opacity=".35"/>'
         '<circle cx="13" cy="12" r="1.1" fill="#0A1630"/></svg>')
AVISO = "Planta de referência. O projeto para a prefeitura é assinado por arquiteto ou engenheiro habilitado."
SELO = "Planta de referência humanizada · medidas em metros · móveis para dar escala"
GANCHO = "8 m de frente. 2 quartos, varanda e banheiro largo. 51 m²."
PARA_QUEM = "Casal com 1 ou 2 filhos que quer dois quartos, varanda na entrada e banheiro largo, sem corredor comprido."
ERROS = [("1", "Ignorar o sol"), ("2", "Corredor comprido"), ("4", "Banheiro sem janela")]
SUB = "Casas organizadas pela frente do terreno. Meça a frente do seu lote, ache a medida na régua abaixo e abra a página."
CASAS = [("5 m", "Casa Fita", "56 m² · 2 quartos", "4", 12.12), ("8 m", "Casa Compacta", "51 m² · 2 quartos", "8", 57.58),
         ("10 m", "Casa Família Compacta", "71 m² · 3 quartos", "12", 87.88)]

FONTES = ("@import url('https://fonts.googleapis.com/css2?family=Big+Shoulders+Display:wght@700;800;900"
          "&family=Londrina+Solid:wght@400;900&family=Bricolage+Grotesque:opsz,wght@12..96,600;12..96,800"
          "&family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500;700&display=swap');")
BASE = """
@page { size: A4; margin: 0; }
* { box-sizing: border-box; margin: 0; padding: 0; }
body { background: #666; font-family: Inter, Arial, sans-serif; -webkit-print-color-adjust: exact; }
.pg { width: 210mm; height: 297mm; position: relative; overflow: hidden; margin: 0 auto 10mm; }
.mono { font-family: 'JetBrains Mono', monospace; }
.planta svg { width: 100%; height: 100%; display: block; }
"""


def regua(n_m=11, alto=1, cor="#17202B"):
    """Traços de trena de 0 a n_m metros (cada 10 cm), em coordenadas 0..1000 x 0..100."""
    out = []
    for i in range(n_m * 10 + 1):
        x = i * 1000 / (n_m * 10)
        h = 34 if i % 10 == 0 else (22 if i % 5 == 0 else 12)
        w = 2.2 if i % 10 == 0 else 1
        out.append(f'<line x1="{x:.1f}" y1="0" x2="{x:.1f}" y2="{h*alto}" stroke="{cor}" stroke-width="{w}"/>')
    return "".join(out)


def svg_trena(n_m=11, cor="#FFC857", tinta="#141414", marcas=()):
    riscos = "".join(f'<rect x="{m / n_m * 1000 - 3:.1f}" y="0" width="6" height="100" fill="#C8102E"/>' for m in marcas)
    return (f'<svg viewBox="0 0 1000 100" preserveAspectRatio="none" class="trena-svg"><rect width="1000" height="100" fill="{cor}"/>'
            f'{riscos}{regua(n_m, cor=tinta)}</svg>')


def rodape(cor, num="8", cls=""):
    return f'<div class="rod {cls}"><b class="mono">{num}</b><span>{AVISO}</span></div>'


# ---------------------------------------------------------------- Direção 1: A Trena
D1 = """
:root { --obra:#141414; --fita:#FFC857; --marca:#D0281C; --azul:#0B4FA8; --papel:#FFFFFF; --cinza:#4A4F57; }
.d1 { background: var(--papel); color: var(--obra); }
.d1 .tit { font-family: 'Big Shoulders Display', sans-serif; font-weight: 900; text-transform: uppercase; letter-spacing: -.005em; }
.d1.capa { background: var(--obra); color: #fff;
  background-image: linear-gradient(rgba(255,255,255,.06) .3mm, transparent .3mm), linear-gradient(90deg, rgba(255,255,255,.06) .3mm, transparent .3mm);
  background-size: 10mm 10mm; }
.d1.capa .eti { position:absolute; left:16mm; top:15mm; font-size:9pt; letter-spacing:.12em; color: var(--fita); }
.d1.capa h1 { position:absolute; left:15mm; right:15mm; top:22mm; font-size:84pt; line-height:.84; }
.d1.capa .sub { position:absolute; left:16mm; top:106mm; width:92mm; font-size:11.5pt; line-height:1.4; color:#D9DCE1; }
.d1.capa .planta { position:absolute; right:12mm; top:94mm; width:96mm; height:128mm; background:#fff; border-radius:1.5mm; padding:3mm; box-shadow:0 2mm 6mm rgba(0,0,0,.5); }
.d1.capa .pergunta { position:absolute; left:16mm; top:165mm; width:85mm; font-size:38pt; line-height:.9; color: var(--fita); }
.d1.capa .pergunta small { display:block; font-family: Inter; font-weight:600; text-transform:none; font-size:11pt; color:#fff; margin-top:4mm; letter-spacing:0; line-height:1.35; }
.d1 .trena { position:absolute; left:0; right:0; }
.d1 .trena-svg { position:absolute; inset:0; width:100%; height:100%; }
.d1.capa .trena { bottom:0; height:62mm; }
.d1 .marca { position:absolute; top:13mm; transform:translateX(-.7mm); text-align:left; color: var(--obra); max-width:31mm; }
.d1 .trena .rotulo { position:absolute; left:15mm; top:17mm; width:60mm; font-family:'JetBrains Mono'; font-weight:700; font-size:9pt; line-height:1.4; color: var(--obra); }
.d1 .trena .rotulo b { display:block; font-family:'Big Shoulders Display'; font-weight:900; font-size:22pt; line-height:.95; text-transform:uppercase; margin-bottom:2mm; }
.d1 .marca::before { content:''; position:absolute; left:0; top:-13mm; width:1.4mm; height:12mm; background: var(--marca); }
.d1 .marca b { display:block; font-family:'Big Shoulders Display'; font-weight:900; font-size:42pt; line-height:.9; white-space:nowrap; }
.d1 .marca i { display:block; font-style:normal; font-weight:700; font-size:9pt; margin-top:1mm; }
.d1 .marca span { display:inline-block; font-family:'JetBrains Mono'; font-weight:700; font-size:9pt; background: var(--obra); color: var(--fita); border-radius:1mm; padding:.6mm 2mm; margin-top:1.2mm; }
.d1.capa .ref { position:absolute; right:12mm; top:224.5mm; font-size:7.5pt; color:#AEB4BC; }
/* página de casa */
.d1.casa .trena { top:0; height:21mm; }
.d1.casa .trena .ponto { position:absolute; top:3mm; transform:translateX(-50%); font-family:'JetBrains Mono'; font-weight:700; font-size:9pt;
  background: var(--marca); color:#fff; padding:.8mm 2.2mm; border-radius:1mm; }
.d1.casa .trena .ponto::after { content:''; position:absolute; left:50%; bottom:-2.4mm; margin-left:-1.4mm; border:1.4mm solid transparent; border-top-color: var(--marca); border-bottom:0; }
.d1.casa .cab { position:absolute; left:15mm; right:15mm; top:27mm; display:grid; grid-template-columns: auto 1fr; gap:6mm; align-items:end; }
.d1.casa .num { font-family:'Big Shoulders Display'; font-weight:900; font-size:118pt; line-height:.78; color: var(--obra); }
.d1.casa .num sup { font-size:.42em; vertical-align: top; position:relative; top:.08em; }
.d1.casa .id { font-family:'JetBrains Mono'; font-size:8.5pt; letter-spacing:.1em; color: var(--cinza); }
.d1.casa h2 { font-size:40pt; line-height:.88; color: var(--azul); margin:1mm 0 2mm; }
.d1.casa .gancho { font-size:11pt; font-weight:600; line-height:1.3; }
.d1.casa .planta { position:absolute; left:15mm; right:15mm; top:68mm; height:166mm; border:.5mm solid var(--obra); border-radius:1.5mm; padding:3mm; background:#fff; }
.d1.casa .selo { position:absolute; left:15mm; top:235.5mm; font-family:'JetBrains Mono'; font-size:7pt; color: var(--cinza); }
.d1.casa .baixo { position:absolute; left:15mm; right:15mm; top:241.5mm; display:grid; grid-template-columns: 1fr 1fr; gap:6mm; font-size:9.5pt; line-height:1.35; }
.d1.casa h4 { font-size:7.5pt; letter-spacing:.12em; text-transform:uppercase; color: var(--azul); margin-bottom:1mm; }
.d1.casa ul { list-style:none; display:grid; gap:.8mm; }
.d1.casa li b { display:inline-grid; place-items:center; width:5mm; height:5mm; border-radius:50%; background: var(--fita); border:.3mm solid var(--obra); font-size:7.5pt; margin-right:2mm; }
.d1.casa .puxa { position:absolute; right:0; top:268mm; height:13mm; width:122mm; background: var(--obra); color:#fff; display:flex; align-items:center; gap:3mm; padding:0 6mm; border-radius:2mm 0 0 2mm; }
.d1.casa .puxa .tit { font-size:17pt; color: var(--fita); }
.d1.casa .puxa span { font-size:10pt; font-weight:600; }
.d1.casa .puxa .seta { margin-left:auto; font-family:'JetBrains Mono'; font-weight:700; background: var(--fita); color: var(--obra); padding:1mm 2.2mm; border-radius:1mm; font-size:9pt; }
.d1 .rod { position:absolute; left:15mm; right:15mm; bottom:6.5mm; display:flex; gap:4mm; font-size:7pt; color: var(--cinza); border-top:.3mm solid #D5D9DE; padding-top:1.5mm; }
.d1 .rod b { color: var(--marca); }
.d1 .orelha { position:absolute; left:0; top:102mm; width:7mm; height:22mm; background: var(--fita); border:.3mm solid var(--obra); border-left:0; writing-mode:vertical-rl; transform:rotate(180deg);
  display:grid; place-items:center; font-family:'JetBrains Mono'; font-weight:700; font-size:7.5pt; border-radius:1.5mm 0 0 1.5mm; }
"""


def d1():
    marcas = "".join(f'<div class="marca" style="left:{x}%"><b>{m}</b><i>{n}</i><span>pág. {p}</span></div>' for m, n, _, p, x in [(c[0], c[1], c[2], c[3], float(c[0].split()[0]) / 13 * 100) for c in CASAS])
    capa = f"""<section class="pg d1 capa">
  <div class="eti mono">3 PLANTAS DE CASAS TÉRREAS · 2026</div>
  <h1 class="tit">Antes do<br>primeiro<br>tijolo</h1>
  <p class="sub">{SUB}</p>
  <div class="planta">{PLANTA}</div>
  <div class="ref">Planta de referência · medidas em metros</div>
  <div class="pergunta tit">Qual casa cabe no seu lote?<small>Puxe a trena: a frente do lote diz a página.</small></div>
  <div class="trena">{svg_trena(13)}<div class="rotulo"><b>A frente do seu lote</b>meça de uma divisa à outra</div>{marcas}</div>
</section>"""
    casa = f"""<section class="pg d1 casa">
  <div class="trena">{svg_trena(11)}<div class="ponto" style="left:72.7%">frente 8 m</div></div>
  <div class="orelha">frente 8 m</div>
  <div class="cab"><div class="num">51<sup>m²</sup></div>
    <div><div class="id">C01 · COMPACTAS</div><h2 class="tit">Casa Compacta</h2><p class="gancho">{GANCHO}</p></div></div>
  <div class="planta">{PLANTA}</div>
  <div class="selo">{SELO}</div>
  <div class="baixo"><div><h4>Para quem é</h4><p>{PARA_QUEM}</p></div>
    <div><h4>Dos 7 erros da pág. 18, esta casa evita</h4><ul>{''.join(f'<li><b>{n}</b>{t}</li>' for n, t in ERROS)}</ul></div></div>
  <div class="puxa"><span class="tit">Próxima medida:</span><span>cabe num lote de 8 x 15 m?</span><span class="seta">pág. 9 →</span></div>
  {rodape('', '8')}
</section>"""
    return D1, capa, casa


# ---------------------------------------------------------------- Direção 2: A Placa (Lote Carente)
D2 = """
:root { --placa:#FFFFFF; --tinta:#161616; --verm:#C8102E; --fita:#FFC857; --azul:#0B4FA8; --mato:#3E8E41; --cinza:#4A4F57; }
.d2 { background:#fff; color: var(--tinta); }
.d2 .pl { font-family:'Londrina Solid', sans-serif; font-weight:900; text-transform:uppercase; letter-spacing:.005em; }
.d2.capa { background: var(--fita); }
.d2.capa .eti { position:absolute; left:16mm; top:15mm; font-size:9pt; letter-spacing:.12em; }
.d2.capa h1 { position:absolute; left:15mm; right:15mm; top:21mm; font-size:76pt; line-height:.86; color: var(--tinta); }
.d2.capa .sub { position:absolute; left:16mm; top:80mm; width:110mm; font-size:11.5pt; line-height:1.4; font-weight:500; }
.d2 .placa { position:absolute; background: var(--placa); border:1.2mm solid var(--tinta); border-radius:1.5mm; box-shadow: 2mm 2.5mm 0 var(--tinta); }
.d2 .placa::before, .d2 .placa::after { content:''; position:absolute; bottom:-25mm; width:5mm; height:25mm; background:#8A5A2B; border:.8mm solid var(--tinta); z-index:-1; }
.d2 .placa::before { left:18%; } .d2 .placa::after { right:18%; }
.d2.capa .placa { left:22mm; right:22mm; top:104mm; height:86mm; padding:7mm 8mm; transform: rotate(-2.2deg); z-index:2; }
.d2.capa .placa .l1 { font-size:28pt; color: var(--tinta); }
.d2.capa .placa .l2 { font-size:80pt; line-height:.86; color: var(--verm); margin:2mm 0 3mm; }
.d2.capa .placa .ass { font-size:18pt; color: var(--tinta); }
.d2.capa .placa .ass span { font-family: Inter; font-weight:600; text-transform:none; font-size:9pt; color: var(--cinza); margin-left:2mm; }
.d2.capa .chao { position:absolute; left:0; right:0; top:206mm; height:91mm; background:#C9A56B; overflow:hidden; z-index:1; }
.d2.capa .chao::before { content:''; position:absolute; left:0; right:0; top:0; height:7mm; background: var(--mato); }
.d2.capa .lote { position:absolute; left:12mm; right:12mm; top:22mm; bottom:-2mm; border:.6mm dashed var(--tinta); border-bottom:0; }
.d2.capa .trena2 { position:absolute; left:0; right:0; bottom:0; height:17mm; z-index:4; }
.d2.capa .trena2 svg { width:100%; height:100%; display:block; }
.d2.capa .frentes div { position:absolute; bottom:26mm; width:31mm; transform:translateX(-50%); background:#fff; border:.8mm solid var(--tinta); border-radius:1.2mm; padding:2.5mm 2.5mm 2mm; box-shadow:1.2mm 1.5mm 0 var(--tinta); z-index:5; }
.d2.capa .frentes div::after { content:''; position:absolute; left:50%; margin-left:-1.5mm; bottom:-10.5mm; width:3mm; height:9.6mm; background:#8A5A2B; border:.6mm solid var(--tinta); }

.d2.capa .frentes b { display:block; white-space:nowrap; font-family:'Londrina Solid'; font-weight:900; font-size:31pt; line-height:.95; color: var(--verm); }
.d2.capa .frentes i { display:block; font-style:normal; font-weight:700; font-size:8.5pt; line-height:1.15; min-height:7.8mm; }
.d2.capa .frentes span { display:block; font-family:'JetBrains Mono'; font-weight:700; font-size:8.5pt; color: var(--cinza); }
.d2.capa .chamada { position:absolute; left:17mm; top:231mm; font-size:26pt; color: var(--tinta); z-index:3; }
.d2.capa .ref { position:absolute; left:17mm; top:243mm; font-size:7.5pt; color: var(--tinta); z-index:3; }
/* página de casa */
.d2.casa .faixa { position:absolute; left:0; right:0; top:0; height:6mm; background: var(--verm); }
.d2.casa .id { position:absolute; left:15mm; top:15mm; font-family:'JetBrains Mono'; font-size:8.5pt; letter-spacing:.1em; color: var(--cinza); }
.d2.casa h2 { position:absolute; left:15mm; top:20mm; font-size:50pt; line-height:.88; width:95mm; }
.d2.casa .gancho { position:absolute; left:15mm; top:58mm; width:92mm; font-size:11pt; font-weight:600; line-height:1.3; }
.d2.casa .placa { right:15mm; top:13mm; width:80mm; padding:4mm 5mm; transform: rotate(2deg); }
.d2.casa .placa::before, .d2.casa .placa::after { display:none; }
.d2.casa .placa p { font-size:24pt; line-height:.95; color: var(--verm); }
.d2.casa .placa .ass { font-size:12pt; margin-top:2mm; color: var(--tinta); }
.d2.casa .placa .amostra { position:absolute; right:0; bottom:-8.5mm; font-size:6.5pt; color: var(--cinza); font-family:Inter; }
.d2.casa .planta { position:absolute; left:15mm; right:15mm; top:74mm; height:162mm; border:.8mm solid var(--tinta); border-radius:1.5mm; padding:3mm; box-shadow:1.6mm 2mm 0 var(--tinta); background:#fff; }
.d2.casa .selo { position:absolute; left:15mm; top:240mm; font-family:'JetBrains Mono'; font-size:7pt; color: var(--cinza); }
.d2.casa .baixo { position:absolute; left:15mm; right:15mm; top:246mm; display:grid; grid-template-columns: 1fr 1fr; gap:6mm; font-size:9.5pt; line-height:1.35; }
.d2.casa h4 { font-family:'Londrina Solid'; font-weight:900; font-size:11pt; text-transform:uppercase; color: var(--verm); margin-bottom:1mm; }
.d2.casa ul { list-style:none; display:grid; gap:.8mm; }
.d2.casa li b { display:inline-grid; place-items:center; width:5mm; height:5mm; border-radius:1mm; background: var(--tinta); color:#fff; font-size:7.5pt; margin-right:2mm; }
.d2.casa .puxa { position:absolute; right:15mm; top:267mm; display:flex; align-items:center; gap:3mm; font-family:'Londrina Solid'; font-weight:900; font-size:15pt; text-transform:uppercase; }
.d2.casa .puxa span { background: var(--verm); color:#fff; padding:1.2mm 3mm; border-radius:1mm; }
.d2 .rod { position:absolute; left:15mm; right:15mm; bottom:6.5mm; display:flex; gap:4mm; font-size:7pt; color: var(--cinza); border-top:.3mm solid #D5D9DE; padding-top:1.5mm; }
.d2 .rod b { color: var(--verm); }
.d2 .orelha { position:absolute; left:0; top:102mm; width:7mm; height:22mm; background: var(--verm); color:#fff; writing-mode:vertical-rl; transform:rotate(180deg);
  display:grid; place-items:center; font-family:'JetBrains Mono'; font-weight:700; font-size:7.5pt; border-radius:1.5mm 0 0 1.5mm; }
"""


def d2():
    frentes = "".join(f'<div style="left:{float(m.split()[0]) / 12 * 100:.2f}%"><b>{m}</b><i>{n}</i><span>pág. {p}</span></div>' for m, n, _, p, _x in CASAS)
    capa = f"""<section class="pg d2 capa">
  <div class="eti mono">3 PLANTAS DE CASAS TÉRREAS · 2026</div>
  <h1 class="pl">Antes do primeiro tijolo</h1>
  <p class="sub">{SUB}</p>
  <div class="placa"><div class="pl l1">Lote de 8 x 15</div><div class="pl l2">Procura-se casa</div>
    <div class="pl ass">Ass.: o Lote<span>(amostra de voz; texto final é do Redator)</span></div></div>
  <div class="chao"><div class="lote"></div></div>
  <div class="pl chamada">Qual casa cabe no seu lote?</div>
  <div class="frentes">{frentes}</div>
  <div class="trena2">{svg_trena(12, marcas=(5, 8, 10))}</div>
  <div class="ref">Planta de referência · medidas em metros</div>
</section>"""
    casa = f"""<section class="pg d2 casa">
  <div class="faixa"></div><div class="orelha">frente 8 m</div>
  <div class="id">C01 · COMPACTAS</div>
  <h2 class="pl">Casa Compacta</h2>
  <p class="gancho">{GANCHO}</p>
  <div class="placa"><p class="pl">Puxadinho é ficante. Eu quero casa.</p><div class="pl ass">Ass.: o Lote 8 x 15</div>
    <div class="amostra">voz do Instagram (rascunho, sem Revisor)</div></div>
  <div class="planta">{PLANTA}</div>
  <div class="selo">{SELO}</div>
  <div class="baixo"><div><h4>Para quem é</h4><p>{PARA_QUEM}</p></div>
    <div><h4>Dos 7 erros da pág. 18, evita</h4><ul>{''.join(f'<li><b>{n}</b>{t}</li>' for n, t in ERROS)}</ul></div></div>
  <div class="puxa">Será que cabe em mim? <span>Vira: pág. 9</span></div>
  {rodape('', '8')}
</section>"""
    return D2, capa, casa


# ---------------------------------------------------------------- Direção 3: A Porta Acesa
D3 = """
:root { --noite:#0A1630; --noite2:#12234A; --linha:#6FA8FF; --porta:#FFC857; --branco:#F4F7FB; --nevoa:#A9B6CC; --azul:#0B4FA8; }
.d3 { background: var(--noite); color: var(--branco);
  background-image: linear-gradient(rgba(111,168,255,.09) .3mm, transparent .3mm), linear-gradient(90deg, rgba(111,168,255,.09) .3mm, transparent .3mm);
  background-size: 8mm 8mm; }
.d3 .tit { font-family:'Bricolage Grotesque', sans-serif; font-weight:800; letter-spacing:-.03em; }
.d3 .porta-acesa { width:4.6mm; height:6.9mm; vertical-align:-1.6mm; filter: drop-shadow(0 0 1.6mm rgba(255,200,87,.7)); }
.d3 .portinha { display:inline-block; width:3.6mm; height:6mm; background: var(--porta); border-radius:.6mm .6mm 0 0; position:relative; box-shadow:0 0 3mm 1mm rgba(255,200,87,.55); vertical-align:-.6mm; }
.d3 .portinha::after { content:''; position:absolute; right:.7mm; top:3mm; width:.7mm; height:.7mm; border-radius:50%; background: var(--noite); }
.d3.capa .eti { position:absolute; left:16mm; top:15mm; font-size:9pt; letter-spacing:.12em; color: var(--porta); display:flex; gap:2.5mm; align-items:center; }
.d3.capa h1 { position:absolute; left:15mm; right:15mm; top:24mm; font-size:62pt; line-height:.9; }
.d3.capa .sub { position:absolute; left:16mm; top:82mm; width:120mm; font-size:11.5pt; line-height:1.4; color: var(--nevoa); }
.d3.capa .planta { position:absolute; left:32mm; right:32mm; top:96mm; height:136mm; filter: drop-shadow(0 0 6mm rgba(111,168,255,.25)); }
.d3.capa .trena3 { position:absolute; left:0; right:0; bottom:27mm; height:7mm; box-shadow:0 0 6mm rgba(255,200,87,.45); }
.d3.capa .trena3 svg { width:100%; height:100%; display:block; }
.d3.capa .frentes div { position:absolute; bottom:8mm; transform:translateX(-.7mm); border-left:.6mm solid var(--porta); padding-left:2mm; }
.d3.capa .frentes b { display:block; font-family:'Bricolage Grotesque'; font-weight:800; font-size:30pt; line-height:1; color: var(--porta); }
.d3.capa .frentes i { display:block; font-style:normal; font-weight:700; font-size:9.5pt; }
.d3.capa .frentes span { font-family:'JetBrains Mono'; font-size:8.5pt; color: var(--nevoa); }
.d3.capa .ref { position:absolute; left:15mm; bottom:8mm; width:60mm; font-size:7.5pt; color: var(--nevoa); }
.d3.capa .chamada { position:absolute; left:15mm; bottom:38mm; font-size:15pt; font-weight:700; }
/* página de casa */
.d3.casa .id { position:absolute; left:15mm; top:15mm; font-family:'JetBrains Mono'; font-size:8.5pt; letter-spacing:.1em; color: var(--nevoa); display:flex; gap:2.5mm; align-items:center; }
.d3.casa h2 { position:absolute; left:15mm; top:22mm; font-size:38pt; line-height:.95; }
.d3.casa .gancho { position:absolute; left:15mm; top:40mm; width:110mm; font-size:11pt; font-weight:500; line-height:1.3; color: var(--nevoa); }
.d3.casa .num { position:absolute; right:15mm; top:13mm; text-align:right; font-family:'Bricolage Grotesque'; font-weight:800; font-size:76pt; line-height:.85; color: var(--porta); letter-spacing:-.04em; text-shadow:0 0 6mm rgba(255,200,87,.35); }
.d3.casa .num small { display:block; font-family:Inter; font-weight:600; font-size:9pt; letter-spacing:0; color: var(--nevoa); text-shadow:none; margin-top:1mm; }
.d3.casa .planta { position:absolute; left:15mm; right:15mm; top:56mm; height:180mm; background:#fff; border-radius:3mm; padding:4mm; box-shadow:0 0 0 .4mm var(--linha), 0 4mm 12mm rgba(0,0,0,.45); }
.d3.casa .selo { position:absolute; left:15mm; top:239mm; font-family:'JetBrains Mono'; font-size:7pt; color: var(--nevoa); }
.d3.casa .baixo { position:absolute; left:15mm; right:15mm; top:245mm; display:grid; grid-template-columns: 1fr 1fr; gap:6mm; font-size:9.5pt; line-height:1.35; }
.d3.casa h4 { font-size:7.5pt; letter-spacing:.12em; text-transform:uppercase; color: var(--porta); margin-bottom:1mm; }
.d3.casa ul { list-style:none; display:grid; gap:.8mm; }
.d3.casa li b { display:inline-grid; place-items:center; width:5mm; height:5mm; border-radius:50%; border:.3mm solid var(--porta); color: var(--porta); font-size:7.5pt; margin-right:2mm; }
.d3.casa .puxa { position:absolute; right:15mm; top:268mm; display:flex; align-items:center; gap:3mm; font-weight:700; font-size:10.5pt; }
.d3.casa .puxa em { font-style:normal; font-family:'JetBrains Mono'; color: var(--noite); background: var(--porta); padding:1mm 2.4mm; border-radius:1mm; }
.d3 .rod { position:absolute; left:15mm; right:15mm; bottom:6.5mm; display:flex; gap:4mm; font-size:7pt; color: var(--nevoa); border-top:.3mm solid rgba(169,182,204,.35); padding-top:1.5mm; }
.d3 .rod b { color: var(--porta); }
.d3 .orelha { position:absolute; left:0; top:102mm; width:7mm; height:22mm; background: var(--porta); color: var(--noite); writing-mode:vertical-rl; transform:rotate(180deg);
  display:grid; place-items:center; font-family:'JetBrains Mono'; font-weight:700; font-size:7.5pt; border-radius:1.5mm 0 0 1.5mm; box-shadow:0 0 4mm rgba(255,200,87,.5); }
"""


def d3():
    frentes = "".join(f'<div style="left:{float(m.split()[0]) / 13 * 100:.2f}%"><b>{m}</b><i>{n}</i><span>pág. {p}</span></div>' for m, n, d, p, _x in CASAS)
    capa = f"""<section class="pg d3 capa">
  <div class="eti mono">{PORTA}3 PLANTAS DE CASAS TÉRREAS · 2026</div>
  <h1 class="tit">Antes do primeiro tijolo</h1>
  <p class="sub">{SUB}</p>
  <div class="planta">{PLANTA_ESC_LUZ}</div>
  <div class="chamada">Qual casa cabe no seu lote? {PORTA}</div>
  <div class="trena3">{svg_trena(13)}</div>
  <div class="frentes">{frentes}</div>
  <div class="ref">Planta de referência · medidas em metros</div>
</section>"""
    casa = f"""<section class="pg d3 casa">
  <div class="orelha">frente 8 m</div>
  <div class="id">{PORTA}C01 · COMPACTAS</div>
  <h2 class="tit">Casa Compacta</h2>
  <p class="gancho">{GANCHO}</p>
  <div class="num">51 m²<small>área fechada</small></div>
  <div class="planta">{PLANTA}</div>
  <div class="selo">{SELO}</div>
  <div class="baixo"><div><h4>Para quem é</h4><p>{PARA_QUEM}</p></div>
    <div><h4>Dos 7 erros da pág. 18, esta casa evita</h4><ul>{''.join(f'<li><b>{n}</b>{t}</li>' for n, t in ERROS)}</ul></div></div>
  <div class="puxa">{PORTA}Abra a porta: cabe num lote de 8 x 15 m? <em>pág. 9 →</em></div>
  {rodape('', '8')}
</section>"""
    return D3, capa, casa


for n, f in ((1, d1), (2, d2), (3, d3)):
    css, capa, casa = f()
    html = f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><style>{FONTES}{BASE}{css}</style></head><body>{capa}{casa}</body></html>'
    (S / f"direcao-{n}.html").write_text(html, encoding="utf-8")
print("ok")

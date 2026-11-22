// Monta o vídeo principal da E07 (15 s, 128 BPM): blueprint nosso + clipes do OpenArt + trilha original.
// Uso: node video/principal-e07/montar_e07.cjs   (antes: node render_blueprint.cjs, e os clipes em openart/)
// Plano quadro a quadro e decisão do Conselho: video/PRINCIPAL-E07.md
const { chromium } = require('playwright');
const { execFileSync } = require('child_process');
const fs = require('fs'), path = require('path');

const AQUI = __dirname, RAIZ = path.resolve(AQUI, '../..');
const TMP = fs.mkdtempSync(path.join(require('os').tmpdir(), 'e07-'));
const B = 60 / 128, FPS = 30;
const SAIDA = path.join(RAIZ, 'video/saida/principal-e07/x1-plantas-e07.mp4');
const RODAPE = 'Planta de referência. O projeto para a prefeitura é assinado por arquiteto ou engenheiro habilitado.';

// cenas do drop (7,5 a 13,13 s): 12 tempos. "de" = início no clipe, "vel" = velocidade
const CLIPES = [
  { nome: 'v1-transicao', tempos: 3, de: 1.0, vel: 2.84, janela8: true,
    titulo: '<b>Cabe</b> em lote<br>8 x 25 m.', selo: true },
  { nome: 'v2-voo', tempos: 2, de: 0.15, vel: 1.0, titulo: '72 m² · 3 quartos<br>(1 suíte) · 2 banheiros', pequeno: true, selo: true },
  { nome: 'v3-sala', tempos: 2, de: 1.6, vel: 1.0, selo: true },
  { nome: 'v4-cozinha', tempos: 2, de: 1.2, vel: 1.0, selo: true },
  { nome: 'v5-fachada', tempos: 3, de: 0, vel: 2.0, titulo: 'Casa Estreita<br><b>3 Quartos</b>', selo: true },
];

const CSS = `*{box-sizing:border-box;margin:0}html,body{width:1080px;height:1920px;background:transparent;overflow:hidden;color:#F5F1E6;font-family:"Inter Display",Inter,sans-serif}
.topo{position:absolute;left:0;right:0;top:0;height:620px;background:linear-gradient(rgba(6,26,58,.72),rgba(6,26,58,0))}
.base{position:absolute;left:0;right:0;bottom:0;height:560px;background:linear-gradient(rgba(6,26,58,0),rgba(6,26,58,.78) 60%)}
.tit{position:absolute;left:70px;right:70px;top:120px;font-weight:900;font-size:96px;line-height:1;letter-spacing:-.03em;text-shadow:0 3px 22px rgba(3,20,50,.6)}
.tit.p{font-size:66px;line-height:1.08}.tit b{color:#FFC857}
.selo{position:absolute;left:70px;bottom:470px;font:600 28px Inter,sans-serif;background:rgba(0,0,0,.55);padding:8px 18px;border-radius:8px}
.rodape{position:absolute;left:70px;right:70px;bottom:360px;font:500 27px/1.3 Inter,sans-serif;color:rgba(255,255,255,.92)}`;

function sh(args) { execFileSync('ffmpeg', ['-y', '-loglevel', 'error', ...args], { stdio: 'inherit' }); }

(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1080, height: 1920 } });
  const png = async (html, destino) => {
    await p.setContent(`<!doctype html><html><head><meta charset="utf-8"><style>${CSS}</style></head><body>${html}</body></html>`);
    await p.evaluate(() => document.fonts.ready);
    await p.screenshot({ path: destino, omitBackground: true });
  };
  // máscara do "8": o último quadro do blueprint com um 8 gigante e estreito vazado (conceito 3 do CONDOR)
  // (sem os textos: o título novo entra por cima, e o texto velho não pode crescer junto com a máscara)
  const q = path.join(TMP, 'q.png');
  await p.addInitScript(`window.E07 = ${fs.readFileSync(path.join(AQUI, 'e07.json'), 'utf8')};`);
  await p.goto('file://' + path.join(AQUI, 'blueprint.html'));
  await p.evaluate(() => window.pronto);
  await p.evaluate(() => { window.renderAt(7.49, 'abertura'); document.getElementById('txt').style.display = 'none'; document.querySelector('.base').style.display = 'none'; });
  await p.screenshot({ path: q });
  const q64 = fs.readFileSync(q).toString('base64');
  await p.setContent(`<canvas id="c" width="1080" height="1920"></canvas><style>body{margin:0;background:transparent}</style>`);
  await p.evaluate(async (src) => {
    const c = document.getElementById('c'), g = c.getContext('2d'), im = new Image();
    im.src = src; await im.decode(); await document.fonts.load('900 100px "Inter Display"');
    g.drawImage(im, 0, 0);
    g.save(); g.translate(540, 1500); g.scale(0.62, 1); g.font = '900 1500px "Inter Display"'; g.textAlign = 'center';
    g.globalCompositeOperation = 'destination-out'; g.fillText('8', 0, 0);
    g.globalCompositeOperation = 'source-over'; g.lineWidth = 9; g.strokeStyle = '#FFC857'; g.strokeText('8', 0, 0); g.restore();
  }, 'data:image/png;base64,' + q64);
  const mascara = path.join(TMP, 'mascara8.png');
  await p.screenshot({ path: mascara, omitBackground: true });

  // cenas do drop
  const partes = [path.join(AQUI, 'abertura.mp4')];
  for (const [i, c] of CLIPES.entries()) {
    const dur = c.tempos * B, fonte = path.join(AQUI, 'openart', c.nome + '.mp4');
    const txt = path.join(TMP, `t${i}.png`);
    await png(`${c.titulo ? '<div class="topo"></div>' : ''}<div class="base"></div>
      ${c.titulo ? `<div class="tit ${c.pequeno ? 'p' : ''}">${c.titulo}</div>` : ''}
      ${c.selo ? '<div class="selo">Imagem ilustrativa</div>' : ''}<div class="rodape">${RODAPE}</div>`, txt);
    const saida = path.join(TMP, `c${i}.mp4`);
    let f = `[0:v]trim=start=${c.de},setpts=(PTS-STARTPTS)/${c.vel},fps=${FPS},scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1[v]`;
    const ent = ['-i', fonte, '-loop', '1', '-t', String(dur), '-i', txt];
    if (c.janela8) {
      // o 8 cresce a partir do centro da letra até sumir para fora da tela em 2 tempos
      ent.push('-loop', '1', '-t', String(dur), '-i', mascara);
      f += `;[2:v]format=rgba,scale=w='1080*pow(14,min(t/${2 * B},1)^2)':h='1920*pow(14,min(t/${2 * B},1)^2)':eval=frame[m];` +
        `[v][m]overlay=x='540-w/2':y='1500-h*1500/1920':eval=frame:enable='lt(t,${2 * B})'[v]`;
    }
    f += `;[1:v]format=rgba,fade=t=in:st=0:d=0.12:alpha=1[t];[v][t]overlay=0:0,format=yuv420p[o]`;
    sh([...ent, '-filter_complex', f, '-map', '[o]', '-t', String(dur), '-r', String(FPS), '-an', '-c:v', 'libx264', '-crf', '14', saida]);
    partes.push(saida);
    console.log('cena', c.nome);
  }
  partes.push(path.join(AQUI, 'fim.mp4'));
  await b.close();

  // junta tudo, põe a trilha (começa no compasso 3 dela, para o drop cair em 7,5 s) e comprime
  const lista = path.join(TMP, 'lista.txt');
  fs.writeFileSync(lista, partes.map((x) => `file '${x}'\n`).join(''));
  fs.mkdirSync(path.dirname(SAIDA), { recursive: true });
  const total = 15.0;
  sh(['-f', 'concat', '-safe', '0', '-i', lista, '-ss', String(8 * B), '-i', path.join(RAIZ, 'video/musica/big-big-128bpm.wav'),
    '-filter_complex', `[0:v]fps=${FPS},noise=alls=4:allf=t,format=yuv420p[v];[1:a]atrim=0:${total},afade=t=out:st=${total - 0.08}:d=0.08[a]`,
    '-map', '[v]', '-map', '[a]', '-t', String(total), '-c:v', 'libx264', '-crf', '23', '-preset', 'slow', '-pix_fmt', 'yuv420p',
    '-c:a', 'aac', '-b:a', '192k', '-movflags', '+faststart', SAIDA]);
  console.log(SAIDA, (fs.statSync(SAIDA).size / 1e6).toFixed(1) + ' MB');
})();

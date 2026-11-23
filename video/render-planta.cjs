// Gera o material da planta que o cliente recebe: imagens estáticas e animação.
//
// Uso (dentro da pasta video):
//   node render-planta.cjs                 → tudo em ../animacoes-3d/plantas/casa-compacta
//   node render-planta.cjs --so-imagens    → só as imagens
//   node render-planta.cjs --fps 24
const { chromium } = require('playwright');
const { execFileSync } = require('child_process');
const fs = require('fs');
const path = require('path');
const http = require('http');

const args = process.argv.slice(2);
const opc = (nome, padrao) => { const i = args.indexOf(nome); return i >= 0 ? args[i + 1] : padrao; };
const FPS = Number(opc('--fps', 30));
const soImagens = args.includes('--so-imagens');

const RAIZ = __dirname;
const PLANTA = opc('--planta', '');
const DISTANCIA = Number(opc('--escala', 0)) || (() => {
  // Afasta a câmera conforme o tamanho da casa (a C01 de 8,5 m é a referência).
  if (!PLANTA) return 1;
  const txt = fs.readFileSync(path.join(RAIZ, 'src', 'plantas', `${PLANTA}.js`), 'utf8');
  const W = Number(/LARGURA = ([\d.]+)/.exec(txt)[1]); const D = Number(/PROFUNDIDADE = ([\d.]+)/.exec(txt)[1]);
  return Math.max(1, Math.max(W * 1.25, D) / 8.5);
})();
const NOME = PLANTA ? JSON.parse(/META = (\{.*\});/.exec(fs.readFileSync(path.join(RAIZ, 'src', 'plantas', `${PLANTA}.js`), 'utf8'))[1]).nome : 'Casa Compacta';
const pasta = NOME.normalize('NFKD').replace(/[\u0300-\u036f]/g, '').toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');
const DESTINO = path.resolve(RAIZ, opc('--saida', `../animacoes-3d/plantas/${pasta}`));
const QUADROS = path.join(RAIZ, 'saida', 'quadros', 'planta');
const PORTA = 8767;

const tipos = { '.html': 'text/html', '.js': 'text/javascript', '.mjs': 'text/javascript', '.json': 'application/json' };
const servidor = http.createServer((req, res) => {
  const alvo = path.normalize(path.join(RAIZ, decodeURIComponent(req.url.split('?')[0])));
  if (!alvo.startsWith(RAIZ) || !fs.existsSync(alvo) || fs.statSync(alvo).isDirectory()) { res.writeHead(404); res.end(); return; }
  res.writeHead(200, { 'Content-Type': tipos[path.extname(alvo)] || 'application/octet-stream' });
  fs.createReadStream(alvo).pipe(res);
});

const clamp = (v) => Math.min(1, Math.max(0, v));
const suave = (v) => { v = clamp(v); return v * v * (3 - 2 * v); };
const saida = (v) => 1 - Math.pow(1 - clamp(v), 3);
const lerp = (a, b, v) => a + (b - a) * v;

// Imagens estáticas: 2000 x 2500 (4:5), boas para WhatsApp, Instagram e impressão em A4.
const IMAGENS = [
  { arquivo: '01-blueprint.png', estado: { desenho: 1, paredes: 0, vida: 0 }, camera: { theta: 0, inclinacao: 0.0, distancia: 23, alvo: [0, 0.3] } },
  { arquivo: '02-planta-humanizada.png', estado: { desenho: 1, paredes: 1, vida: 1 }, camera: { theta: 0, inclinacao: 0.02, distancia: 21, alvo: [0, 0] } },
  // As perspectivas olham da rua (theta perto de pi): a casa aparece como na planta do e-book, frente embaixo.
  { arquivo: '03-perspectiva.png', estado: { desenho: 1, paredes: 1, vida: 1 }, camera: { theta: Math.PI - 0.55, inclinacao: 0.62, distancia: 20, alvo: [0, -0.4] } },
  { arquivo: '04-perspectiva-lateral.png', estado: { desenho: 1, paredes: 1, vida: 1 }, camera: { theta: Math.PI + 0.75, inclinacao: 0.6, distancia: 20, alvo: [0, -0.4] } },
];

// Animação vertical de 12 s: blueprint se desenha, paredes sobem, casa ganha vida, câmera desliza.
const DURACAO = 12;
function quadroAnimacao(t) {
  const estado = { desenho: saida(t / 2.4), paredes: suave((t - 2.2) / 1.6), vida: suave((t - 3.4) / 3.6) };
  const camera = {
    theta: lerp(0, 0.75, suave((t - 2.0) / 10)),
    inclinacao: lerp(0.0, 0.58, suave((t - 2.0) / 8)),
    distancia: lerp(27, 21, suave(t / 12)),
    alvo: [0, lerp(0.6, 0.3, suave(t / 12))],
  };
  return { estado, camera };
}

async function abrir(navegador, w, h, ss) {
  const pagina = await navegador.newPage({ viewport: { width: w, height: h }, deviceScaleFactor: 1 });
  pagina.on('pageerror', (e) => console.error('[página]', e.message));
  await pagina.goto(`http://127.0.0.1:${PORTA}/src/casa.html?w=${w}&h=${h}&ss=${ss}${PLANTA ? `&planta=${PLANTA}` : ''}`);
  await pagina.waitForFunction(() => window.pronto === true, null, { timeout: 60000 });
  return pagina;
}

(async () => {
  await new Promise((ok) => servidor.listen(PORTA, '127.0.0.1', ok));
  fs.mkdirSync(DESTINO, { recursive: true });
  const navegador = await chromium.launch({ args: ['--use-angle=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist'] });

  const pImg = await abrir(navegador, 2000, 2500, 1);
  for (const img of IMAGENS) {
    await pImg.evaluate(([e, c]) => window.desenhar(e, c), [img.estado, { ...img.camera, distancia: img.camera.distancia * DISTANCIA }]);
    await pImg.screenshot({ path: path.join(DESTINO, img.arquivo) });
    console.log('imagem', img.arquivo);
  }
  await pImg.close();

  if (!soImagens) {
    const pAnim = await abrir(navegador, 1080, 1920, 1.25);
    fs.rmSync(QUADROS, { recursive: true, force: true }); fs.mkdirSync(QUADROS, { recursive: true });
    const total = Math.round(DURACAO * FPS); const inicio = Date.now();
    for (let i = 0; i < total; i++) {
      const { estado, camera } = quadroAnimacao(i / FPS);
      await pAnim.evaluate(([e, c]) => window.desenhar(e, c), [estado, { ...camera, distancia: camera.distancia * DISTANCIA }]);
      await pAnim.screenshot({ path: path.join(QUADROS, `q_${String(i).padStart(5, '0')}.png`) });
      if (i % 60 === 0) console.log(`animação: quadro ${i}/${total} (${((Date.now() - inicio) / 1000).toFixed(0)} s)`);
    }
    execFileSync('ffmpeg', ['-y', '-loglevel', 'error', '-framerate', String(FPS), '-i', path.join(QUADROS, 'q_%05d.png'),
      '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '18', '-preset', 'medium', '-movflags', '+faststart',
      path.join(DESTINO, 'animacao.mp4')], { stdio: 'inherit' });
    console.log('animação pronta');
  }

  await navegador.close();
  servidor.close();
  console.log('Arquivos em', DESTINO);
})().catch((e) => { console.error(e); servidor.close(); process.exit(1); });

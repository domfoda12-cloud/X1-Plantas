// Gera o material da planta que o cliente recebe: imagens estáticas e animação.
// Os dados de cada planta ficam em src/plantas/<ID>.js. A pasta de saída vem do nome da
// planta (mesma regra do ferramentas/atualizar-painel.py): "Casa Compacta" → casa-compacta.
//
// Uso (dentro da pasta video):
//   node render-planta.cjs --planta C01        → os 5 arquivos em ../animacoes-3d/plantas/casa-compacta
//   node render-planta.cjs --plantas C02,C03   → várias plantas, uma depois da outra
//   node render-planta.cjs --todas             → todas as plantas de src/plantas/
//   node render-planta.cjs --planta C02 --so-imagens   → só as 4 imagens
//   node render-planta.cjs --planta C02 --saida /tmp/teste   → outra pasta (só com uma planta)
//   node render-planta.cjs --fps 24
// Sem --planta, gera a C01.
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
const PASTA_PLANTAS = path.join(RAIZ, 'src', 'plantas');
const todas = fs.readdirSync(PASTA_PLANTAS).filter((f) => /^[A-Z]\d{2}\.js$/.test(f)).map((f) => f.slice(0, 3)).sort();
const pedidas = args.includes('--todas') ? todas
  : (opc('--plantas', null) || opc('--planta', 'C01')).split(',').map((p) => p.trim().toUpperCase()).filter(Boolean);
for (const p of pedidas) if (!todas.includes(p)) { console.error(`Planta ${p} não encontrada em src/plantas/ (há: ${todas.join(', ')})`); process.exit(1); }
if (opc('--saida', null) && pedidas.length > 1) { console.error('--saida só vale com uma planta'); process.exit(1); }
const pastaDe = (nome) => nome.normalize('NFKD').replace(/[\u0300-\u036f]/g, '').toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');
let PORTA = 0;

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
// Câmeras pensadas para a C01 (6,5 x 8,5 m). Em outras plantas, distância e alvo são
// multiplicados pela escala da casa (ou pelo campo camera.escala do arquivo da planta).
const IMAGENS = [
  { arquivo: '01-blueprint.png', estado: { desenho: 1, paredes: 0, vida: 0 }, camera: { theta: 0, inclinacao: 0.0, distancia: 23, alvo: [0, 0.3] } },
  { arquivo: '02-planta-humanizada.png', estado: { desenho: 1, paredes: 1, vida: 1 }, camera: { theta: 0, inclinacao: 0.02, distancia: 21, alvo: [0, 0] } },
  { arquivo: '03-perspectiva.png', estado: { desenho: 1, paredes: 1, vida: 1 }, camera: { theta: 0.55, inclinacao: 0.62, distancia: 20, alvo: [0, 0.4] } },
  { arquivo: '04-perspectiva-lateral.png', estado: { desenho: 1, paredes: 1, vida: 1 }, camera: { theta: -0.75, inclinacao: 0.6, distancia: 20, alvo: [0, 0.4] } },
];
const escalaDe = (info) => info.camera.escala || Math.max(0.8, info.largura / 6.5, info.profundidade / 8.5);
const escalar = (c, e) => ({ ...c, distancia: c.distancia * e, alvo: c.alvo.map((v) => v * e) });

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

async function abrir(navegador, id, w, h, ss) {
  const pagina = await navegador.newPage({ viewport: { width: w, height: h }, deviceScaleFactor: 1 });
  pagina.on('pageerror', (e) => console.error('[página]', e.message));
  await pagina.goto(`http://127.0.0.1:${PORTA}/src/casa.html?planta=${id}&w=${w}&h=${h}&ss=${ss}`);
  await pagina.waitForFunction(() => window.pronto === true, null, { timeout: 60000 });
  return pagina;
}

async function gerar(navegador, id) {
  const pImg = await abrir(navegador, id, 2000, 2500, 1);
  const info = await pImg.evaluate(() => window.info);
  const DESTINO = path.resolve(RAIZ, opc('--saida', path.join('..', 'animacoes-3d', 'plantas', pastaDe(info.nome))));
  const QUADROS = path.join(RAIZ, 'saida', 'quadros', `planta-${id}`);
  const e = escalaDe(info);
  console.log(`${id} · ${info.nome} (${info.largura} x ${info.profundidade} m, escala da câmera ${e.toFixed(2)}) → ${DESTINO}`);
  fs.mkdirSync(DESTINO, { recursive: true });
  for (const img of IMAGENS) {
    await pImg.evaluate(([es, c]) => window.desenhar(es, c), [img.estado, escalar(img.camera, e)]);
    await pImg.screenshot({ path: path.join(DESTINO, img.arquivo) });
    console.log('imagem', img.arquivo);
  }
  await pImg.close();

  if (!soImagens) {
    const pAnim = await abrir(navegador, id, 1080, 1920, 1.25);
    fs.rmSync(QUADROS, { recursive: true, force: true }); fs.mkdirSync(QUADROS, { recursive: true });
    const total = Math.round(DURACAO * FPS); const inicio = Date.now();
    for (let i = 0; i < total; i++) {
      const { estado, camera } = quadroAnimacao(i / FPS);
      await pAnim.evaluate(([es, c]) => window.desenhar(es, c), [estado, escalar(camera, e)]);
      await pAnim.screenshot({ path: path.join(QUADROS, `q_${String(i).padStart(5, '0')}.png`) });
      if (i % 60 === 0) console.log(`${id} animação: quadro ${i}/${total} (${((Date.now() - inicio) / 1000).toFixed(0)} s)`);
    }
    execFileSync('ffmpeg', ['-y', '-loglevel', 'error', '-framerate', String(FPS), '-i', path.join(QUADROS, 'q_%05d.png'),
      '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '18', '-preset', 'medium', '-movflags', '+faststart',
      path.join(DESTINO, 'animacao.mp4')], { stdio: 'inherit' });
    await pAnim.close();
    fs.rmSync(QUADROS, { recursive: true, force: true });
    console.log('animação pronta');
  }
  console.log('Arquivos em', DESTINO);
}

(async () => {
  await new Promise((ok) => servidor.listen(0, '127.0.0.1', ok));
  PORTA = servidor.address().port;
  const navegador = await chromium.launch({ args: ['--use-angle=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist'] });
  for (const id of pedidas) await gerar(navegador, id);
  await navegador.close();
  servidor.close();
})().catch((e) => { console.error(e); servidor.close(); process.exit(1); });

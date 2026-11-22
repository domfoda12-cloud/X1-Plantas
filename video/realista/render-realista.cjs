// Versão realista das imagens da planta: exporta a casa do motor 3D (src/casa3d.js) e
// renderiza no Blender Cycles (luz e sombra calculadas como numa foto).
// O blueprint (01) continua o do render normal; aqui saem 02, 03 e 04.
//
// Uso (dentro da pasta video):
//   node realista/render-realista.cjs --planta C01
//   node realista/render-realista.cjs --planta C01 --amostras 64 --escala 0.5   (prévia rápida)
// Saída: ../animacoes-3d/plantas/<nome>/realista/
// Precisa do Blender 4.2+ (comando "blender") ou do Python com o pacote bpy:
//   BLENDER_PY=/caminho/do/python-com-bpy node realista/render-realista.cjs --planta C01
const { chromium } = require('playwright');
const { execFileSync } = require('child_process');
const fs = require('fs');
const path = require('path');
const http = require('http');

const args = process.argv.slice(2);
const opc = (nome, padrao) => { const i = args.indexOf(nome); return i >= 0 ? args[i + 1] : padrao; };
const id = opc('--planta', 'C01').toUpperCase();
const AMOSTRAS = opc('--amostras', '160');
const ESCALA = opc('--escala', '1');
const SO = opc('--so', '');
const RAIZ = path.resolve(__dirname, '..');
const pastaDe = (nome) => nome.normalize('NFKD').replace(/[̀-ͯ]/g, '').toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');

// Mesmas câmeras de render-planta.cjs (02, 03 e 04)
const CAMERAS = [
  { nome: '02-planta-humanizada', camera: { theta: 0, inclinacao: 0.02, distancia: 21, alvo: [0, 0] } },
  { nome: '03-perspectiva', camera: { theta: 0.55, inclinacao: 0.62, distancia: 20, alvo: [0, 0.4] } },
  { nome: '04-perspectiva-lateral', camera: { theta: -0.75, inclinacao: 0.6, distancia: 20, alvo: [0, 0.4] } },
];

const tipos = { '.html': 'text/html', '.js': 'text/javascript', '.mjs': 'text/javascript' };
const servidor = http.createServer((req, res) => {
  const alvo = path.normalize(path.join(RAIZ, decodeURIComponent(req.url.split('?')[0])));
  if (!alvo.startsWith(RAIZ) || !fs.existsSync(alvo) || fs.statSync(alvo).isDirectory()) { res.writeHead(404); res.end(); return; }
  res.writeHead(200, { 'Content-Type': tipos[path.extname(alvo)] || 'application/octet-stream' });
  fs.createReadStream(alvo).pipe(res);
});

(async () => {
  await new Promise((ok) => servidor.listen(0, '127.0.0.1', ok));
  const porta = servidor.address().port;
  const navegador = await chromium.launch({ args: ['--use-angle=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist'] });
  const pagina = await navegador.newPage();
  pagina.on('pageerror', (e) => console.error('[página]', e.message));
  await pagina.goto(`http://127.0.0.1:${porta}/realista/exportar.html?planta=${id}&cameras=${encodeURIComponent(JSON.stringify(CAMERAS))}`);
  await pagina.waitForFunction(() => window.pronto === true, null, { timeout: 120000 });
  const { glb, info } = await pagina.evaluate(() => ({ glb: window.glb, info: window.info }));
  await navegador.close(); servidor.close();

  const destino = path.resolve(RAIZ, '..', 'animacoes-3d', 'plantas', pastaDe(info.nome), 'realista');
  const tmp = path.join(RAIZ, 'saida', 'realista'); fs.mkdirSync(tmp, { recursive: true }); fs.mkdirSync(destino, { recursive: true });
  const arqGlb = path.join(tmp, `${id}.glb`);
  fs.writeFileSync(arqGlb, Buffer.from(glb, 'base64'));
  console.log(`${id}: cena exportada (${(fs.statSync(arqGlb).size / 1e6).toFixed(1)} MB). Renderizando no Cycles...`);

  const script = path.join(__dirname, 'cycles.py');
  const extra = ['--', arqGlb, destino, AMOSTRAS, ESCALA, SO];
  if (process.env.BLENDER_PY) execFileSync(process.env.BLENDER_PY, [script, ...extra], { stdio: 'inherit' });
  else execFileSync('blender', ['-b', '--factory-startup', '-P', script, ...extra], { stdio: 'inherit' });
  console.log('Imagens em', destino);
})().catch((e) => { console.error(e); servidor.close(); process.exit(1); });

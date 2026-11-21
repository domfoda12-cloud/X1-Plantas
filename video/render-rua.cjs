// Clipes realistas do motor próprio: a casa no lote, vista da rua (céu, sol, sombra, materiais).
//
// Uso (dentro da pasta video):
//   node render-rua.cjs --planta C01 --clipe rua --saida broll/clipes/rua-c01.mp4
//   node render-rua.cjs --planta C01 --clipe obra --quadro 3.0 --saida /tmp/teste.png   (um quadro só, para conferir)
// Clipes: lote (lote vazio), obra (a casa sobe no lote), rua (casa pronta, câmera chegando), drone (câmera sobe e mostra o lote).
const { chromium } = require('playwright');
const { execFileSync } = require('child_process');
const fs = require('fs');
const os = require('os');
const path = require('path');
const http = require('http');

const args = process.argv.slice(2);
const opc = (nome, padrao) => { const i = args.indexOf(nome); return i >= 0 ? args[i + 1] : padrao; };
const RAIZ = __dirname, FPS = Number(opc('--fps', 30)), PLANTA = opc('--planta', 'C01'), CLIPE = opc('--clipe', 'rua');
const SAIDA = path.resolve(opc('--saida', `broll/clipes/${CLIPE}-${PLANTA.toLowerCase()}.mp4`));
const PORTA = 8768;

const suave = (v) => { v = Math.min(1, Math.max(0, v)); return v * v * (3 - 2 * v); };
const lerp = (a, b, v) => a + (b - a) * v;
const mix = (a, b, v) => a.map((x, i) => lerp(x, b[i], v));

// Cada clipe: duração e função (t em segundos, m = medidas do lote) -> { estado, camera }.
// Câmera em metros a partir do meio da frente do lote; z negativo é a rua. Altura dos olhos: 1,6 m.
const CLIPES = {
  lote: { dur: 5, quadro: (t, m) => ({ estado: { obra: 0 },
    camera: { fov: 52, pos: mix([-1.2, 1.6, -11.5], [0.3, 1.6, -9.6], suave(t / 5)), alvo: [0, 1.2, m.LD / 2] } }) },
  obra: { dur: 7, quadro: (t, m) => ({ estado: { obra: suave((t - 0.4) / 5.6) },
    camera: { fov: 50, pos: mix([-3.2, 1.7, -11.5], [2.6, 2.3, -11], suave(t / 7)), alvo: [0, 1.5, m.OZ + 1] } }) },
  rua: { dur: 5, quadro: (t, m) => ({ estado: { obra: 1 },
    camera: { fov: 48, pos: mix([2.4, 1.6, -12.5], [0.8, 1.6, -9.8], suave(t / 5)), alvo: [0, 1.7, m.OZ] } }) },
  drone: { dur: 6, quadro: (t, m) => { const v = suave(t / 6); return { estado: { obra: 1 },
    camera: { fov: 50, pos: [lerp(-2.5, 4.5, v), lerp(1.8, 11, v), lerp(-11, -13.5, v)], alvo: [0, lerp(1.6, 0.6, v), lerp(m.OZ, m.OZ + m.PROFUNDIDADE / 2, v)] } }; } },
};

const tipos = { '.html': 'text/html', '.js': 'text/javascript', '.mjs': 'text/javascript' };
const servidor = http.createServer((req, res) => {
  const alvo = path.normalize(path.join(RAIZ, decodeURIComponent(req.url.split('?')[0])));
  if (!alvo.startsWith(RAIZ) || !fs.existsSync(alvo) || fs.statSync(alvo).isDirectory()) { res.writeHead(404); res.end(); return; }
  res.writeHead(200, { 'Content-Type': tipos[path.extname(alvo)] || 'application/octet-stream' });
  fs.createReadStream(alvo).pipe(res);
});

(async () => {
  const clipe = CLIPES[CLIPE];
  if (!clipe) throw new Error(`Clipe desconhecido: ${CLIPE}. Use: ${Object.keys(CLIPES).join(', ')}`);
  await new Promise((ok) => servidor.listen(PORTA, '127.0.0.1', ok));
  const navegador = await chromium.launch({ args: ['--use-angle=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist'] });
  const pagina = await navegador.newPage({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: 1 });
  pagina.on('pageerror', (e) => console.error('[página]', e.message));
  await pagina.goto(`http://127.0.0.1:${PORTA}/src/rua.html?w=1080&h=1920&ss=${opc('--ss', 1.25)}&planta=${PLANTA}`);
  await pagina.waitForFunction(() => window.pronto === true, null, { timeout: 120000 });
  const m = await pagina.evaluate(() => window.medidas);
  const desenha = async (t, arq) => {
    const { estado, camera } = clipe.quadro(t, m);
    await pagina.evaluate(([e, c]) => window.desenhar(e, c), [estado, camera]);
    await pagina.screenshot({ path: arq });
  };
  fs.mkdirSync(path.dirname(SAIDA), { recursive: true });
  if (opc('--quadro', null) !== null) {
    await desenha(Number(opc('--quadro')), SAIDA);
  } else {
    const tmp = fs.mkdtempSync(path.join(os.tmpdir(), 'rua-'));
    const total = Math.round(clipe.dur * FPS);
    for (let i = 0; i < total; i++) await desenha(i / FPS, path.join(tmp, `q_${String(i).padStart(5, '0')}.png`));
    execFileSync('ffmpeg', ['-y', '-loglevel', 'error', '-framerate', String(FPS), '-i', path.join(tmp, 'q_%05d.png'),
      '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '19', '-preset', 'slow', '-movflags', '+faststart', SAIDA], { stdio: 'inherit' });
    fs.rmSync(tmp, { recursive: true, force: true });
  }
  await navegador.close(); servidor.close();
  console.log('pronto:', SAIDA);
})().catch((e) => { console.error(e); servidor.close(); process.exit(1); });

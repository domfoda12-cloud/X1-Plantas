// Passeio por dentro da casa, na altura dos olhos, em movimento contínuo (motor próprio; ilustração, não foto).
//
// Uso (dentro da pasta video):
//   node render-passeio.cjs --planta F03                      → broll/clipes/passeio-f03.mp4
//   node render-passeio.cjs --planta F03 --quadro 0.4 --saida /tmp/t.png   (um quadro, u de 0 a 1)
//   node render-passeio.cjs --planta F03 --mapa --saida /tmp/mapa.png      (vista de cima com o caminho em vermelho)
// O caminho de cada casa fica em CAMINHOS (metros da planta). Velocidade constante, com partida e chegada suaves.
const { chromium } = require('playwright');
const { execFileSync } = require('child_process');
const fs = require('fs');
const os = require('os');
const path = require('path');
const http = require('http');

const args = process.argv.slice(2);
const opc = (nome, padrao) => { const i = args.indexOf(nome); return i >= 0 ? args[i + 1] : padrao; };
const RAIZ = __dirname, FPS = Number(opc('--fps', 30)), PLANTA = opc('--planta', 'F03'), VEL = Number(opc('--vel', 1.1)), SUB = Number(opc('--sub', 2));
const SAIDA = path.resolve(opc('--saida', `broll/clipes/passeio-${PLANTA.toLowerCase()}.mp4`));
const PORTA = 8769;

const CAMINHOS = {
  // F03 Casa Família: chega pela varanda, entra na sala, vai até a cozinha, volta pelo corredor e termina na suíte
  F03: '4.7,-3.6;4.7,-1.2;3.8,0.1;2.5,0.95;1.0,1.15;0.68,1.8;0.8,2.5;1.6,2.9;3.2,2.85;4.2,3.1;4.65,3.9;4.2,4.8;3.6,5.4;3.55,6.05;4.5,6.18;5.4,6.2;5.82,6.7;5.88,7.0;5.9,7.25',
};

const tipos = { '.html': 'text/html', '.js': 'text/javascript', '.mjs': 'text/javascript' };
const servidor = http.createServer((req, res) => {
  const alvo = path.normalize(path.join(RAIZ, decodeURIComponent(req.url.split('?')[0])));
  if (!alvo.startsWith(RAIZ) || !fs.existsSync(alvo) || fs.statSync(alvo).isDirectory()) { res.writeHead(404); res.end(); return; }
  res.writeHead(200, { 'Content-Type': tipos[path.extname(alvo)] || 'application/octet-stream' });
  fs.createReadStream(alvo).pipe(res);
});

(async () => {
  const caminho = opc('--caminho', CAMINHOS[PLANTA]);
  if (!caminho) throw new Error(`Sem caminho para ${PLANTA}: acrescente em CAMINHOS ou passe --caminho`);
  await new Promise((ok) => servidor.listen(PORTA, '127.0.0.1', ok));
  const navegador = await chromium.launch({ args: ['--use-angle=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist'] });
  const pagina = await navegador.newPage({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: 1 });
  pagina.on('pageerror', (e) => console.error('[página]', e.message));
  await pagina.goto(`http://127.0.0.1:${PORTA}/src/passeio.html?w=1080&h=1920&ss=${opc('--ss', 1.25)}&planta=${PLANTA}&caminho=${caminho}`);
  await pagina.waitForFunction(() => window.pronto === true, null, { timeout: 120000 });
  fs.mkdirSync(path.dirname(SAIDA), { recursive: true });
  if (args.includes('--mapa')) { await pagina.evaluate(() => window.vistaDeCima()); await pagina.screenshot({ path: SAIDA }); }
  else if (args.includes('--quadro')) { await pagina.evaluate((u) => window.desenhar(u), Number(opc('--quadro', 0))); await pagina.screenshot({ path: SAIDA }); }
  else {
    const comp = await pagina.evaluate(() => window.comprimento);
    const dur = comp / VEL + 1, n = Math.round(dur * FPS) * SUB, acel = 1 / dur; // 1 s somado para partir e chegar devagar
    // posição: aceleração e freada de 1 s, velocidade constante no meio (sem tranco)
    const pos = (t) => { const a = acel, v = 1 / (1 - a); return t < a ? v * t * t / (2 * a) : t > 1 - a ? 1 - v * (1 - t) * (1 - t) / (2 * a) : v * (t - a / 2); };
    const tmp = fs.mkdtempSync(path.join(os.tmpdir(), 'passeio-'));
    for (let i = 0; i < n; i++) {
      await pagina.evaluate((u) => window.desenhar(u), pos(i / (n - 1)));
      await pagina.screenshot({ path: path.join(tmp, `q${String(i).padStart(5, '0')}.png`) });
      if (i % 120 === 0) console.log(`quadro ${i}/${n}`);
    }
    // cor quente e uniforme, e borrão leve de movimento de verdade: cada quadro é a média de SUB instantes seguidos
    execFileSync('ffmpeg', ['-y', '-loglevel', 'error', '-framerate', String(FPS * SUB), '-i', path.join(tmp, 'q%05d.png'),
      '-vf', `tmix=frames=${SUB},framestep=${SUB},setpts=N/${FPS}/TB,eq=saturation=1.08:contrast=1.04,colorbalance=rm=0.03:bm=-0.03:rh=0.02:bh=-0.02`,
      '-r', String(FPS), '-c:v', 'libx264', '-crf', '15', '-preset', 'slow', '-pix_fmt', 'yuv420p', SAIDA]);
    fs.rmSync(tmp, { recursive: true });
    console.log(`${path.relative(RAIZ, SAIDA)}: ${dur.toFixed(1)} s, caminho de ${comp.toFixed(1)} m`);
  }
  await navegador.close(); servidor.close();
})();

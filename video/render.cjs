// Renderiza o vídeo quadro a quadro com o Chromium e monta os arquivos com o ffmpeg.
//
// Uso:
//   node render.cjs                 → vídeo completo (saida/rascunho.mp4 e saida/camada-transparente.webm)
//   node render.cjs --amostras 5,20 → só capturas nos tempos pedidos (saida/amostra-5.png...)
//   node render.cjs --fps 24        → muda a taxa de quadros (padrão 30)
const { chromium } = require('playwright');
const { spawn, execFileSync } = require('child_process');
const fs = require('fs');
const path = require('path');
const http = require('http');

const args = process.argv.slice(2);
const opc = (nome, padrao) => { const i = args.indexOf(nome); return i >= 0 ? args[i + 1] : padrao; };
const FPS = Number(opc('--fps', 30));
const amostras = opc('--amostras', null);

const RAIZ = __dirname;
const SAIDA = path.join(RAIZ, 'saida');
const QUADROS = path.join(SAIDA, 'quadros');
const PORTA = 8765;

// Servidor estático mínimo para src/ e node_modules/ (módulos ES não carregam via file://).
const tipos = { '.html': 'text/html', '.js': 'text/javascript', '.mjs': 'text/javascript', '.json': 'application/json' };
const servidor = http.createServer((req, res) => {
  const alvo = path.normalize(path.join(RAIZ, decodeURIComponent(req.url.split('?')[0])));
  if (!alvo.startsWith(RAIZ) || !fs.existsSync(alvo) || fs.statSync(alvo).isDirectory()) { res.writeHead(404); res.end(); return; }
  res.writeHead(200, { 'Content-Type': tipos[path.extname(alvo)] || 'application/octet-stream' });
  fs.createReadStream(alvo).pipe(res);
});

function ffmpeg(params) {
  execFileSync('ffmpeg', ['-y', '-loglevel', 'error', ...params], { stdio: 'inherit' });
}

(async () => {
  await new Promise((ok) => servidor.listen(PORTA, '127.0.0.1', ok));
  fs.mkdirSync(QUADROS, { recursive: true });

  const navegador = await chromium.launch({ args: ['--use-angle=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist'] });
  const pagina = await navegador.newPage({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: 1 });
  pagina.on('pageerror', (e) => console.error('[página]', e.message));
  pagina.on('console', (m) => { if (m.type() === 'error') console.error('[console]', m.text()); });
  await pagina.goto(`http://127.0.0.1:${PORTA}/src/index.html`);
  await pagina.waitForFunction(() => window.pronto === true, null, { timeout: 60000 });

  if (amostras) {
    for (const t of amostras.split(',').map(Number)) {
      await pagina.evaluate((tt) => window.renderAt(tt), t);
      await pagina.screenshot({ path: path.join(SAIDA, `amostra-${t}.png`), omitBackground: true });
    }
    // Amostra também com o fundo provisório por baixo
    await pagina.evaluate(() => window.modoFundo(true));
    await pagina.screenshot({ path: path.join(SAIDA, 'fundo.png') });
    console.log('Amostras salvas em', SAIDA);
  } else {
    const duracao = await pagina.evaluate(() => window.DURACAO);
    const total = Math.round(duracao * FPS);
    for (const f of fs.readdirSync(QUADROS)) fs.unlinkSync(path.join(QUADROS, f));
    const inicio = Date.now();
    for (let i = 0; i < total; i++) {
      await pagina.evaluate((tt) => window.renderAt(tt), i / FPS);
      await pagina.screenshot({ path: path.join(QUADROS, `q_${String(i).padStart(5, '0')}.png`), omitBackground: true });
      if (i % 150 === 0) console.log(`quadro ${i}/${total} (${((Date.now() - inicio) / 1000).toFixed(0)} s)`);
    }
    await pagina.evaluate(() => window.modoFundo(true));
    await pagina.screenshot({ path: path.join(SAIDA, 'fundo.png') });

    const seq = path.join(QUADROS, 'q_%05d.png');
    // Camada com transparência, para o editor colocar por cima da gravação
    ffmpeg(['-framerate', String(FPS), '-i', seq, '-c:v', 'libvpx-vp9', '-pix_fmt', 'yuva420p', '-b:v', '0', '-crf', '30', '-row-mt', '1',
      path.join(SAIDA, 'camada-transparente.webm')]);
    // Rascunho com o fundo provisório no lugar do apresentador
    ffmpeg(['-loop', '1', '-framerate', String(FPS), '-i', path.join(SAIDA, 'fundo.png'), '-framerate', String(FPS), '-i', seq,
      '-filter_complex', '[0:v][1:v]overlay=shortest=1,format=yuv420p', '-c:v', 'libx264', '-crf', '20', '-preset', 'medium',
      '-movflags', '+faststart', path.join(SAIDA, 'rascunho.mp4')]);
    console.log(`Pronto em ${((Date.now() - inicio) / 1000).toFixed(0)} s:`, SAIDA);
  }

  await navegador.close();
  servidor.close();
})().catch((e) => { console.error(e); servidor.close(); process.exit(1); });

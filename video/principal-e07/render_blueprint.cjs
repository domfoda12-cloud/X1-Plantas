// Renderiza o blueprint animado: node video/principal-e07/render_blueprint.cjs [--amostras 0,1,3.8,7.4] 
// Saídas: abertura.mp4 (0 a 7,5 s) e fim.mp4 (1,875 s), 1080x1920, 30 qps, sem áudio.
const { chromium } = require('playwright');
const { spawn } = require('child_process');
const fs = require('fs'), path = require('path');
const AQUI = __dirname, FPS = 30;
const args = process.argv.slice(2);
const amostras = args.includes('--amostras') ? args[args.indexOf('--amostras') + 1].split(',').map(Number) : null;

(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1080, height: 1920 } });
  const dados = fs.readFileSync(path.join(AQUI, 'e07.json'), 'utf8');
  await p.addInitScript(`window.E07 = ${dados};`);
  await p.goto('file://' + path.join(AQUI, 'blueprint.html'));
  await p.evaluate(() => window.pronto);
  await p.waitForTimeout(300);
  if (amostras) {
    for (const t of amostras) {
      const modo = t < 0 ? 'fim' : 'abertura', tt = Math.abs(t);
      await p.evaluate(([t, m]) => window.renderAt(t, m), [tt, modo]);
      await p.screenshot({ path: path.join(process.env.SAIDA || AQUI, `amostra_${modo}_${tt}.png`) });
    }
    await b.close(); return;
  }
  for (const [nome, modo, dur] of [['abertura', 'abertura', 7.5], ['fim', 'fim', 1.875]]) {
    const out = path.join(AQUI, `${nome}.mp4`);
    const ff = spawn('ffmpeg', ['-y', '-loglevel', 'error', '-f', 'image2pipe', '-framerate', String(FPS), '-i', '-',
      '-c:v', 'libx264', '-crf', '14', '-preset', 'medium', '-pix_fmt', 'yuv420p', out]);
    const n = Math.round(dur * FPS);
    for (let i = 0; i < n; i++) {
      await p.evaluate(([t, m]) => window.renderAt(t, m), [i / FPS, modo]);
      ff.stdin.write(await p.screenshot({ type: 'jpeg', quality: 95 }));
    }
    ff.stdin.end(); await new Promise((r) => ff.on('close', r));
    console.log(out);
  }
  await b.close();
})();

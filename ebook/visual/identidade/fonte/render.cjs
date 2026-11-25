// Renderiza as amostras do D50: node render.cjs <pasta-html> <pasta-png> <escala>
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const [dir, outdir, scale] = process.argv.slice(2);
  const b = await chromium.launch();
  const pg = await b.newPage({ viewport: { width: 900, height: 1200 }, deviceScaleFactor: Number(scale || 2) });
  for (const n of [1, 2, 3]) {
    await pg.goto('file://' + path.resolve(dir, `direcao-${n}.html`), { waitUntil: 'networkidle' });
    await pg.evaluate(() => document.fonts.ready);
    const f = await pg.evaluate(() => ['Big Shoulders Display', 'Londrina Solid', 'Bricolage Grotesque', 'Inter', 'JetBrains Mono']
      .map(x => x + ':' + document.fonts.check(`20px "${x}"`)));
    const over = await pg.evaluate(() => [...document.querySelectorAll('.pg')].map(p => {
      const q = p.getBoundingClientRect();
      return [...p.querySelectorAll('.pg > *')].filter(e => {
        const r = e.getBoundingClientRect();
        return r.width && (r.bottom > q.bottom + 1 || r.right > q.right + 1 || r.left < q.left - 1) && !e.matches('.trena,.chao');
      }).map(e => e.className);
    }));
    console.log(n, f.join(' '), 'fora da pagina:', JSON.stringify(over));
    const secs = await pg.$$('.pg');
    await secs[0].screenshot({ path: path.join(outdir, `direcao-${n}-capa.png`) });
    await secs[1].screenshot({ path: path.join(outdir, `direcao-${n}-casa-c01.png`) });
  }
  await b.close();
})();

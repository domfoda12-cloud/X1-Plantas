// Converte um HTML do e-book em PDF A4 com o Chromium do Playwright.
// Uso: node pdf.cjs entrada.html saida.pdf [previa-dir]
// Com previa-dir, também salva um PNG de cada página (para revisão).
// Se o Playwright não estiver na pasta, rode com NODE_PATH=$(npm root -g).
const path = require('path');
const { chromium } = require('playwright');

(async () => {
  const [entrada, saida, previa] = process.argv.slice(2);
  if (!entrada || !saida) {
    console.error('Uso: node pdf.cjs entrada.html saida.pdf [previa-dir]');
    process.exit(2);
  }
  const navegador = await chromium.launch();
  const pagina = await navegador.newPage();
  await pagina.goto('file://' + path.resolve(entrada), { waitUntil: 'load' });
  await pagina.evaluate(() => document.fonts.ready);

  // Confere se algum texto passou do limite da página (sinal de página estourada).
  const estouradas = await pagina.evaluate(() =>
    [...document.querySelectorAll('.pagina')]
      .map((p, i) => ({ i: i + 1, estourou: p.scrollHeight > p.clientHeight + 1 }))
      .filter((p) => p.estourou)
      .map((p) => p.i));
  if (estouradas.length) console.warn('AVISO: conteúdo passou do limite nas páginas ' + estouradas.join(', '));

  await pagina.pdf({ path: saida, format: 'A4', printBackground: true, preferCSSPageSize: true });

  if (previa) {
    const fs = require('fs');
    fs.mkdirSync(previa, { recursive: true });
    await pagina.setViewportSize({ width: 794, height: 1123 });
    await pagina.emulateMedia({ media: 'print' });
    const paginas = await pagina.$$('.pagina');
    for (let i = 0; i < paginas.length; i++) {
      await paginas[i].screenshot({ path: path.join(previa, `pagina-${String(i + 1).padStart(2, '0')}.png`) });
    }
  }
  await navegador.close();
  console.log(`PDF gerado: ${saida}`);
})();

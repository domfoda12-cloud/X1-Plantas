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
  await pagina.emulateMedia({ media: 'print' });
  await pagina.setViewportSize({ width: 794, height: 1123 });

  // As letras vêm do Google Fonts (@import no livro.css e no placa.css): sem rede, o Chromium troca a letra sem avisar.
  // Avisa se uma família pedida não chegou (nenhuma face dela no documento) ou se alguma face deu erro ao carregar.
  const semFonte = await pagina.evaluate(() => {
    const css = [...document.querySelectorAll('style')].map((s) => s.textContent).join('\n');
    const pedidas = new Set();
    for (const url of css.match(/fonts\.googleapis\.com\/css2\?[^'")]+/g) || [])
      for (const f of url.match(/family=[^:&]+/g) || []) pedidas.add(decodeURIComponent(f.slice(7)).replace(/\+/g, ' '));
    const faces = [...document.fonts].map((f) => ({ fam: f.family.replace(/["']/g, ''), st: f.status }));
    return [...pedidas].filter((fam) => !faces.some((f) => f.fam === fam) || faces.some((f) => f.fam === fam && f.st === 'error'));
  });
  if (semFonte.length) { console.warn('AVISO: fonte não carregou (sem rede?): ' + semFonte.join(', ')); process.exitCode = 1; }

  // Confere se algum texto passou do limite da página (sinal de página estourada).
  const estouradas = await pagina.evaluate(() =>
    [...document.querySelectorAll('.pagina')]
      .map((p, i) => {
        const m = p.querySelector('.miolo');
        const fundo = m ? m.getBoundingClientRect().bottom : 0;
        const rod = p.querySelector('.rodape');
        const limite = rod ? rod.getBoundingClientRect().top : p.getBoundingClientRect().bottom;
        const passou = m ? [...m.children].filter((c) => !c.classList.contains('fita-box')).some((c) => c.getBoundingClientRect().bottom > Math.min(fundo, limite) + 1) : false;
        return { i: i + 1, estourou: p.scrollHeight > p.clientHeight + 1 || passou };
      })
      .filter((p) => p.estourou)
      .map((p) => p.i));
  if (estouradas.length) { console.warn('AVISO: conteúdo passou do limite nas páginas ' + estouradas.join(', ')); process.exitCode = 1; }

  await pagina.pdf({ path: saida, format: 'A4', printBackground: true, preferCSSPageSize: true });

  if (previa) {
    const fs = require('fs');
    fs.mkdirSync(previa, { recursive: true });
    // Prévias em alta: 3x a página A4 a 96 dpi (2382 x 3369 px)
    const alta = await navegador.newPage({ viewport: { width: 794, height: 1123 }, deviceScaleFactor: 3 });
    await alta.goto('file://' + path.resolve(entrada), { waitUntil: 'load' });
    await alta.evaluate(() => document.fonts.ready);
    await alta.emulateMedia({ media: 'print' });
    const paginas = await alta.$$('.pagina');
    for (let i = 0; i < paginas.length; i++) {
      await paginas[i].screenshot({ path: path.join(previa, `pagina-${String(i + 1).padStart(2, '0')}.png`) });
    }
  }
  await navegador.close();
  console.log(`PDF gerado: ${saida}`);
})();

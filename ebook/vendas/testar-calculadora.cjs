// Testa a calculadora do parceiro (calculadora-lote.html) pela tela, como o parceiro usa no WhatsApp.
// O gabarito vem do validador (ferramentas/plantas.py, metricas['lote'] de cada planta), nunca da lista CASAS da
// página: comparar a lista com ela mesma sempre passaria. Para cada casa, digita em #frente e #fundo com vírgula
// e lê os ids que aparecem em #lista:
//   1. lote exato da casa: ela tem de aparecer;
//   2. 1 cm a menos na frente (e, à parte, no fundo): ela não pode aparecer;
//   3. lote grande (100 x 100 m): aparecem todas as casas do validador, nem uma a mais.
// Uso: node ebook/vendas/testar-calculadora.cjs [caminho da página]  (padrão: ebook/vendas/calculadora-lote.html)
// Nenhum pedido sai para a rede (só file:// passa). Sem Playwright (no PC do dono), avisa e sai 0: não instala nada.
// Se a calculadora disser "cabe" o que o validador nega, o caso vai ao Arquiteto e ao Revisor: não se ajusta o teste.
// Ideia adaptada de everything-claude-code (e2e), MIT, Copyright (c) 2026 Affaan Mustafa (.claude/LICENCA-everything-claude-code.txt).
const fs = require('fs');
const os = require('os');
const path = require('path');
const { execFileSync } = require('child_process');

const RAIZ = path.resolve(__dirname, '..', '..');
const PAGINA = path.resolve(process.argv[2] || path.join(__dirname, 'calculadora-lote.html'));
const GRANDE = 100;

let chromium;
try {
  ({ chromium } = require('playwright'));
} catch (e) {
  console.log('Playwright não encontrado: teste da calculadora pulado (nada foi instalado).');
  process.exit(0);
}

const virgula = (v) => String(Number(v.toFixed(2))).replace('.', ',');

function gabarito() {
  const codigo = 'import json, plantas as PL\n' +
    'ps = PL.carregar()\n' +
    'print("GABARITO " + json.dumps([{"id": p["id"], "fr": p["_r"].metricas["lote"][0], "fu": p["_r"].metricas["lote"][1]} for p in ps]))';
  const saida = execFileSync('python3', ['-c', codigo], { cwd: path.join(RAIZ, 'ferramentas'), encoding: 'utf-8' });
  const linha = saida.split('\n').find((l) => l.startsWith('GABARITO '));
  return JSON.parse(linha.slice('GABARITO '.length));
}

async function abrirNavegador() {
  try {
    return await chromium.launch();
  } catch (e) {
    if (fs.existsSync('/usr/bin/google-chrome')) return chromium.launch({ executablePath: '/usr/bin/google-chrome' });
    throw e;
  }
}

(async () => {
  if (!fs.existsSync(PAGINA)) {
    console.error(`Página não encontrada: ${PAGINA}`);
    process.exit(1);
  }
  const casas = gabarito();
  const navegador = await abrirNavegador();
  const falhas = [];
  const barrados = new Set();
  try {
    const pagina = await navegador.newPage();
    await pagina.route('**/*', (rota) => {
      const url = rota.request().url();
      if (url.startsWith('file:')) return rota.continue();
      barrados.add(new URL(url).host);
      return rota.abort();
    });
    pagina.on('pageerror', (e) => falhas.push(`erro de JavaScript na página: ${e.message}`));
    await pagina.goto('file://' + PAGINA);

    const medir = async (f, d) => {
      await pagina.fill('#frente', virgula(f));
      await pagina.fill('#fundo', virgula(d));
      return pagina.$$eval('#lista li .id', (els) => els.map((e) => e.textContent.trim()));
    };

    for (const c of casas) {
      const nome = `${c.id} (lote ${virgula(c.fr)} x ${virgula(c.fu)} m)`;
      if (!(await medir(c.fr, c.fu)).includes(c.id)) falhas.push(`${nome}: não aparece no lote exato`);
      if ((await medir(c.fr - 0.01, c.fu)).includes(c.id)) falhas.push(`${nome}: aparece com 1 cm a menos na frente`);
      if ((await medir(c.fr, c.fu - 0.01)).includes(c.id)) falhas.push(`${nome}: aparece com 1 cm a menos no fundo`);
    }
    const todas = await medir(GRANDE, GRANDE);
    const esperadas = casas.map((c) => c.id);
    for (const id of esperadas) if (!todas.includes(id)) falhas.push(`${id}: não aparece no lote de ${GRANDE} x ${GRANDE} m`);
    for (const id of todas) if (!esperadas.includes(id)) falhas.push(`${id}: está na calculadora e não no validador`);

    if (falhas.length) {
      const foto = path.join(os.tmpdir(), 'testar-calculadora-falha.png');
      await pagina.screenshot({ path: foto, fullPage: true }).catch(() => {});
      console.error(`[ERRO] calculadora diverge do validador (${falhas.length}):\n  ` + falhas.join('\n  ') + `\n  captura: ${foto}`);
    } else {
      console.log(`[OK ] calculadora bate com o validador: ${casas.length} casas, ${casas.length * 3 + 1} medições pela tela`);
    }
    if (barrados.size) console.log(`  pedidos de rede barrados: ${[...barrados].join(', ')}`);
  } finally {
    await navegador.close();
  }
  process.exit(falhas.length ? 1 : 0);
})().catch((e) => {
  console.error(`[ERRO] teste da calculadora não rodou: ${e.message}`);
  process.exit(1);
});

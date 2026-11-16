// Renderiza o vídeo quadro a quadro com o Chromium e monta os arquivos com o ffmpeg.
//
// O corpo do vídeo é igual em todas as versões; só o gancho (primeiros 3 s) muda.
// Por isso o corpo é renderizado uma vez e cada gancho separado, e depois são juntados.
//
// Uso:
//   node render.cjs                       → as 5 versões em saida/v1 ... saida/v5
//   node render.cjs --versoes 1,3         → só as versões pedidas
//   node render.cjs --amostras 1,5,30     → capturas nos tempos pedidos (versão 1)
//   node render.cjs --amostras 1 --versao 4
//   node render.cjs --fps 24              → muda a taxa de quadros (padrão 30)
const { chromium } = require('playwright');
const { execFileSync } = require('child_process');
const fs = require('fs');
const path = require('path');
const http = require('http');

const args = process.argv.slice(2);
const opc = (nome, padrao) => { const i = args.indexOf(nome); return i >= 0 ? args[i + 1] : padrao; };
const FPS = Number(opc('--fps', 30));
const amostras = opc('--amostras', null);
const versaoAmostra = Number(opc('--versao', 1));

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

const ffmpeg = (params) => execFileSync('ffmpeg', ['-y', '-loglevel', 'error', ...params], { stdio: 'inherit' });
const limpar = (dir) => { fs.rmSync(dir, { recursive: true, force: true }); fs.mkdirSync(dir, { recursive: true }); };

async function abrir(pagina, v) {
  await pagina.goto(`http://127.0.0.1:${PORTA}/src/index.html?v=${v}`);
  await pagina.waitForFunction(() => window.pronto === true, null, { timeout: 60000 });
}

async function quadros(pagina, dir, de, ate, rotulo) {
  limpar(dir);
  const total = Math.round((ate - de) * FPS);
  const inicio = Date.now();
  for (let i = 0; i < total; i++) {
    await pagina.evaluate((tt) => window.renderAt(tt), de + i / FPS);
    await pagina.screenshot({ path: path.join(dir, `q_${String(i).padStart(5, '0')}.png`), omitBackground: true });
    if (i % 150 === 0) console.log(`${rotulo}: quadro ${i}/${total} (${((Date.now() - inicio) / 1000).toFixed(0)} s)`);
  }
}

(async () => {
  await new Promise((ok) => servidor.listen(PORTA, '127.0.0.1', ok));
  fs.mkdirSync(SAIDA, { recursive: true });

  const navegador = await chromium.launch({ args: ['--use-angle=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist'] });
  const pagina = await navegador.newPage({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: 1 });
  pagina.on('pageerror', (e) => console.error('[página]', e.message));
  pagina.on('console', (m) => { if (m.type() === 'error') console.error('[console]', m.text()); });

  if (amostras) {
    await abrir(pagina, versaoAmostra);
    for (const t of amostras.split(',').map(Number)) {
      await pagina.evaluate((tt) => window.renderAt(tt), t);
      await pagina.screenshot({ path: path.join(SAIDA, `amostra-v${versaoAmostra}-${t}.png`), omitBackground: true });
    }
    await pagina.evaluate(() => window.modoFundo(true));
    await pagina.screenshot({ path: path.join(SAIDA, 'fundo.png') });
    console.log('Amostras salvas em', SAIDA);
  } else {
    await abrir(pagina, 1);
    const { duracao, gancho, nVersoes } = await pagina.evaluate(() => ({ duracao: window.DURACAO, gancho: window.DURACAO_GANCHO, nVersoes: window.VERSOES }));
    const pedidas = (opc('--versoes', null) || Array.from({ length: nVersoes }, (_, i) => i + 1).join(',')).split(',').map(Number);

    await pagina.evaluate(() => window.modoFundo(true));
    await pagina.screenshot({ path: path.join(SAIDA, 'fundo.png') });
    await pagina.evaluate(() => window.modoFundo(false));

    const dirCorpo = path.join(QUADROS, 'corpo');
    await quadros(pagina, dirCorpo, gancho, duracao, 'corpo');

    for (const v of pedidas) {
      await abrir(pagina, v);
      const dirGancho = path.join(QUADROS, `gancho-v${v}`);
      await quadros(pagina, dirGancho, 0, gancho, `gancho v${v}`);

      const destino = path.join(SAIDA, `v${v}`);
      fs.mkdirSync(destino, { recursive: true });
      // Gancho fixo do alto (muda por versão): imagem transparente sobreposta ao corpo
      const topo = path.join(QUADROS, `topo-v${v}.png`);
      await pagina.evaluate(() => { window.renderAt(window.DURACAO_GANCHO + 1); window.modoTopo(true); });
      await pagina.screenshot({ path: topo, omitBackground: true });
      await pagina.evaluate(() => window.modoTopo(false));
      const entradas = ['-framerate', String(FPS), '-i', path.join(dirGancho, 'q_%05d.png'), '-framerate', String(FPS), '-i', path.join(dirCorpo, 'q_%05d.png'),
        '-loop', '1', '-framerate', String(FPS), '-i', topo];
      const junta = (g, c, t) => `[${c}:v]format=rgba[cb];[${t}:v]format=rgba[tp];[cb][tp]overlay=format=auto:shortest=1[corpo];[${g}:v]format=rgba[ga];[ga][corpo]concat=n=2:v=1[c]`;
      // Camada com transparência, para o editor colocar por cima da gravação
      ffmpeg([...entradas, '-filter_complex', junta(0, 1, 2), '-map', '[c]',
        '-c:v', 'libvpx-vp9', '-pix_fmt', 'yuva420p', '-b:v', '0', '-crf', '30', '-row-mt', '1',
        path.join(destino, 'camada-transparente.webm')]);
      // Rascunho com o fundo provisório no lugar do apresentador
      ffmpeg(['-loop', '1', '-framerate', String(FPS), '-i', path.join(SAIDA, 'fundo.png'), ...entradas,
        '-filter_complex', `${junta(1, 2, 3)};[0:v][c]overlay=shortest=1,format=yuv420p`,
        '-c:v', 'libx264', '-crf', '20', '-preset', 'medium', '-movflags', '+faststart', path.join(destino, 'rascunho.mp4')]);
      console.log(`Versão ${v} pronta em ${destino}`);
    }
  }

  await navegador.close();
  servidor.close();
})().catch((e) => { console.error(e); servidor.close(); process.exit(1); });

// Gera as imagens dos carrosséis, do post de imagem e das capas dos reels.
//
// Uso, na raiz do projeto:
//   NODE_PATH=$(npm root -g) node instagram/posts/gerar-imagens.cjs                       gera tudo
//   NODE_PATH=$(npm root -g) node instagram/posts/gerar-imagens.cjs post-08               gera só os posts cujo nome contém "post-08"
//   NODE_PATH=$(npm root -g) node instagram/posts/gerar-imagens.cjs post-02 --saida <pasta>  grava em outra pasta (rascunho)
//
// As casas são as do lançamento (ebook/config.json, casas_lancamento). Os números (área, quartos, banheiros,
// lote e mínimo) vêm dos dados do validador (ebook/plantas/dados/<ID>.json), nunca digitados aqui (passo F20, 24/11/2026).
// As imagens 2D vêm de animacoes-3d/plantas-2d/<pasta>/ (python3 ferramentas/imagens2d.py C01 E03 F01) e a casa em 3D
// parada, de ebook/visual/3d/<ID>.jpg. Quando falta um arquivo, a tela sai com um aviso amarelo "FALTA A IMAGEM".
//
// Saída: instagram/posts/imagens/<post>/NN.png (1080 x 1350; capas de reel 1080 x 1920, em imagens/capas-reels/).

const fs = require('fs');
const path = require('path');
const { chromium } = require('playwright');

const RAIZ = path.resolve(__dirname, '..', '..');
// Imagens 2D validadas (ferramentas/imagens2d.py) e a 3D parada do nosso motor.
const PLANTAS = path.join(RAIZ, 'animacoes-3d', 'plantas-2d');
const TRES_D = path.join(RAIZ, 'ebook', 'visual', '3d');
const DADOS = path.join(RAIZ, 'ebook', 'plantas', 'dados');
const iSaida = process.argv.indexOf('--saida');
const SAIDA = iSaida > 0 ? path.resolve(process.argv[iSaida + 1]) : path.join(__dirname, 'imagens');

const COR = { azul: '#0B4FA8', escuro: '#083B80', claro: '#BFD4F2', amarelo: '#FFC857', ok: '#7EE2A8', ruim: '#FF9C8A' };
const MARCA = 'Plantas de Casas';
const AVISO = 'Planta de referência, não é projeto executivo. A obra precisa de responsável técnico.';
const SELO = 'Imagem ilustrativa';

// ---------------------------------------------------------------------------
// As casas do lançamento: números do validador, textos do instagram/posts/POSTS.md
// ---------------------------------------------------------------------------
// Só o texto fica aqui (vetado pelo Revisor em 24/11, pedidos/anexos/veto-posts-2-4-7-2026-11-24.md).
// "para" é a linha "Para quem" da tabela do post 2.
const TEXTO = {
  // "para": texto das fichas, palavra por palavra (Revisor, 24/11, condição c)
  C01: { destaque: 'sem corredor comprido, um hall curto distribui e a varanda recebe', para: 'Casal com 1 ou 2 filhos' },
  E03: { destaque: 'um quarto em cada ponta, sala e copa no meio, banheiro dentro de casa', para: 'Lote de 5 m de frente' },
  F01: { destaque: 'os 3 quartos nos fundos, longe da rua, e sala com mesa de\u00a04', para: 'Família de 4 ou 5' },
};
const slug = (s) => s.normalize('NFKD').replace(/[̀-ͯ]/g, '').toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');
const dec = (x) => x.toFixed(1).replace('.', ',');
function casa(id) {
  const d = JSON.parse(fs.readFileSync(path.join(DADOS, `${id}.json`), 'utf8'));
  const m = d.validacao.metricas;
  if (!TEXTO[id]) throw new Error(`${id} está em casas_lancamento mas não tem texto em TEXTO (gerar-imagens.cjs)`);
  const [lf, lfu] = m.lote_comercial, [mf, mfu] = m.lote;
  return {
    id, nome: d.nome, pasta: slug(d.nome), ...TEXTO[id], W: d.W, D: d.D,
    m2: Math.round(m.area_fechada), // como o n0 do validador: 70,6 vira 71
    area: `${Math.round(m.area_fechada)} m²`,
    quartos: d.quartos_txt.replace(' (+1 depois)', ''),
    banhos: `${d.banheiros} banheiro${d.banheiros === 1 ? '' : 's'}`,
    lote: `${lf} x ${lfu} m`,
    minimo: `${dec(mf)} x ${dec(mfu)} m`,
  };
}
const LANCAMENTO = JSON.parse(fs.readFileSync(path.join(RAIZ, 'ebook', 'config.json'), 'utf8')).casas_lancamento;
const CASAS = Object.fromEntries(LANCAMENTO.map((id) => [id, casa(id)]));
function de(id) {
  if (!CASAS[id]) throw new Error(`${id} não está em casas_lancamento (ebook/config.json): o post não pode mostrar casa fora do e-book`);
  return CASAS[id];
}
const P = { compacta: de('C01'), fita: de('E03'), familia: de('F01') };
const ARQ = { blueprint: '01-blueprint.png', humanizada: '02-planta-humanizada.png', perspectiva: '03-fachada.png', lateral: '04-lote.png' };
const COM_MOVEIS = new Set(['humanizada', '3d']); // imagem parada com móveis leva o selo "Imagem ilustrativa"

const faltando = new Set();
function arquivo(pl, tipo) {
  const f = tipo === '3d' ? path.join(TRES_D, `${pl.id}.jpg`) : path.join(PLANTAS, pl.pasta, ARQ[tipo]);
  if (fs.existsSync(f)) return 'file://' + f;
  faltando.add(`${pl.id} ${pl.nome}: ${path.relative(RAIZ, f)}`);
  return null;
}

// ---------------------------------------------------------------------------
// Peças visuais
// ---------------------------------------------------------------------------
const y = (t) => `<span class="y">${t}</span>`;

function falta(pl, tipo, w, h) {
  return `<div class="falta" style="width:${w}px;height:${h}px"><div>
    <div class="falta-t">FALTA A IMAGEM</div>
    <div class="falta-n">${pl.id} · ${pl.nome}</div>
    <div class="falta-a">${tipo === '3d' ? `ebook/visual/3d/${pl.id}.jpg` : `animacoes-3d/plantas-2d/${pl.pasta}/<br>${ARQ[tipo]}`}</div></div></div>`;
}

// Imagem de uma planta num cartão (object-fit: cover). Planta mobiliada e 3D levam o selo "Imagem ilustrativa".
function img(pl, tipo, w, h, { pos = 'center', raio = 22, borda = true, fit = 'cover', fundo = '', selo: comSelo = COM_MOVEIS.has(tipo) } = {}) {
  const src = arquivo(pl, tipo);
  if (!src) return falta(pl, tipo, w, h);
  // Na 3D o selo fica dentro, no canto; na planta 2D ele senta na borda de cima, fora das cotas e do título.
  const selo = comSelo ? `<span class="selo${w < 420 ? ' peq' : ''}${tipo === '3d' ? '' : ' borda'}">${SELO}</span>` : '';
  return `<div class="cardw" style="width:${w}px;height:${h}px"><div class="card${borda ? '' : ' sem-borda'}" style="width:${w}px;height:${h}px;border-radius:${raio}px${fundo ? `;background:${fundo}` : ''}">
    <img src="${src}" style="width:100%;height:100%;object-fit:${fit};object-position:${pos}"></div>${selo}</div>`;
}

// Planta mobiliada recortada nas paredes e desenhada em pixels por metro: as 3 casas ficam na mesma escala.
// A caixa das paredes (pl.caixa) é medida na própria imagem antes de desenhar (medir(), no fim do arquivo).
const MARG = { e: 1.0, d: 0.25, c: 0.55, b: 1.3 }; // metros em volta das paredes: cotas à esquerda e embaixo, veneziana em cima
const tam = (pl) => ({ w: pl.W + MARG.e + MARG.d, h: pl.D + MARG.c + MARG.b });
function escala(pl, pxm, { raio = 18 } = {}) {
  const src = arquivo(pl, 'humanizada'), { w, h } = tam(pl);
  const W = Math.round(w * pxm), H = Math.round(h * pxm);
  if (!src || !pl.caixa) return falta(pl, 'humanizada', W, H);
  const c = pl.caixa, s = (c.x1 - c.x0) / pl.W, k = pxm / s;
  return `<div class="cardw" style="width:${W}px;height:${H}px"><div class="card" style="width:${W}px;height:${H}px;border-radius:${raio}px;background:#fff;position:relative">
    <img src="${src}" style="position:absolute;left:${-(c.x0 - MARG.e * s) * k - 3}px;top:${-(c.y0 - MARG.c * s) * k - 3}px;width:${c.iw * k}px;height:${c.ih * k}px;max-width:none"></div>
    <span class="selo${W < 420 ? ' peq' : ''} borda">${SELO}</span></div>`;
}
const caberEm = (lista, larg, alt, gap) => Math.min((larg - gap * (lista.length - 1)) / lista.reduce((t, pl) => t + tam(pl).w, 0), alt / Math.max(...lista.map((pl) => tam(pl).h)));
// A casa no lote (04-lote.png), recortada no desenho (pl.lote4, medido em medir()), com altura h.
function noLote(pl, h) {
  const src = arquivo(pl, 'lateral'), c = pl.lote4;
  if (!src || !c) return falta(pl, 'lateral', Math.round(h / 2), h);
  const k = (h - 24) / (c.y1 - c.y0), w = Math.round((c.x1 - c.x0) * k) + 24;
  return `<div class="card" style="width:${w}px;height:${h}px;border-radius:14px;background:#fff;position:relative">
    <img src="${src}" style="position:absolute;left:${12 - c.x0 * k - 3}px;top:${12 - c.y0 * k - 3}px;width:${c.iw * k}px;height:${c.ih * k}px;max-width:none"></div>`;
}
// Régua amarela (trena) de 5 m na escala da tela
const regua = (pxm) => `<div class="regua"><div class="regua-b" style="width:${5 * pxm}px">${[0, 1, 2, 3, 4].map(() => '<i></i>').join('')}</div><span>5 m</span></div>`;

// Blueprint da Casa Compacta com recorte (em pixels da imagem original 2000 x 2500) e marcações.
// Coordenadas em metros viram pixels: x = 340 + 203,1·m ; y = 325 + 203,1·m
const X = (m) => 340 + 203.1 * m;
const Yp = (m) => 325 + 203.1 * m;
function recorte(pl, [vx, vy, vw, vh], w, h, marcas = '') {
  const src = arquivo(pl, 'blueprint');
  if (!src) return falta(pl, 'blueprint', w, h);
  return `<div class="card" style="width:${w}px;height:${h}px"><svg viewBox="${vx} ${vy} ${vw} ${vh}" width="${w}" height="${h}" preserveAspectRatio="xMidYMid slice">
    <image href="${src}" width="2000" height="2500"/>${marcas}</svg></div>`;
}
const marca = {
  ret: (x0, y0, x1, y1) => `<rect x="${X(x0)}" y="${Yp(y0)}" width="${X(x1) - X(x0)}" height="${Yp(y1) - Yp(y0)}" rx="14" fill="rgba(255,200,87,.28)" stroke="${COR.amarelo}" stroke-width="12"/>`,
  retPx: (x, yy, w, h) => `<rect x="${x}" y="${yy}" width="${w}" height="${h}" rx="18" fill="rgba(255,200,87,.22)" stroke="${COR.amarelo}" stroke-width="10"/>`,
  // Porta: dobradiça (hx, hy) em metros, raio r, de a0 a a1 (radianos)
  porta: (hx, hy, r, a0, a1) => {
    const p0 = [X(hx + r * Math.cos(a0)), Yp(hy + r * Math.sin(a0))];
    const p1 = [X(hx + r * Math.cos(a1)), Yp(hy + r * Math.sin(a1))];
    const R = r * 203.1;
    return `<path d="M ${X(hx)} ${Yp(hy)} L ${p0[0]} ${p0[1]} A ${R} ${R} 0 0 1 ${p1[0]} ${p1[1]} Z" fill="rgba(255,200,87,.3)" stroke="${COR.amarelo}" stroke-width="12" stroke-linejoin="round"/>`;
  },
  seta: (x0, y0, x1, y1) => `<line x1="${x0}" y1="${y0}" x2="${x1}" y2="${y1}" stroke="${COR.amarelo}" stroke-width="14" stroke-linecap="round" marker-end="url(#ponta)"/>`,
};
const defs = `<defs><marker id="ponta" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="3.2" markerHeight="3.2" orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10 z" fill="${COR.amarelo}"/></marker></defs>`;

const chips = (pl) => `<div class="chips">${[pl.area, pl.quartos, pl.banhos, `cabe num lote de ${pl.lote}`, `no mínimo ${pl.minimo}`].map((c) => `<span class="chip">${c}</span>`).join('')}</div>`;

// Moldura de uma tela 1080 x 1350
function tela({ etiqueta = '', n, total, corpo, capa = false, aviso = false, alto = 1350 }) {
  return `<div class="tela" style="height:${alto}px">
    <div class="topo"><span class="etq">${etiqueta}</span>${total ? `<span class="num">${n}/${total}</span>` : ''}</div>
    <div class="corpo">${corpo}</div>
    <div class="rodape"><span class="marca"><span class="logo"></span>${MARCA}</span>${capa ? `<span class="arrasta">arrasta →</span>` : ''}</div>
    ${aviso ? `<div class="aviso">${AVISO}</div>` : ''}
  </div>`;
}

function telaCTA(total, { titulo = 'Quer essa planta?', texto } = {}) {
  return tela({
    etiqueta: 'planta grátis', n: total, total, aviso: true,
    corpo: `<div class="cta">
      <div class="t1" style="text-align:center">${titulo}</div>
      <div class="botao">Comente <b>PLANTA</b></div>
      <div class="txt" style="text-align:center;max-width:820px">${texto || `e eu te mando a <b>planta humanizada da ${P.compacta.nome}</b> de graça no WhatsApp.`}</div>
      <div class="mini">${img(P.compacta, 'humanizada', 300, 375, { raio: 16 })}${img(P.compacta, 'blueprint', 300, 375, { raio: 16, selo: true })}${img(P.compacta, 'perspectiva', 300, 375, { raio: 16, selo: true })}</div>
    </div>`,
  });
}

// ---------------------------------------------------------------------------
// Os posts
// ---------------------------------------------------------------------------
const posts = {};

// Post 2: três plantas lado a lado
posts['post-02-tres-plantas'] = () => {
  const lista = LANCAMENTO.map(de);
  const T = 6;
  // Capa: as 3 plantas na mesma escala, em pé na mesma linha, com a régua de 5 m (a Casa Fita aparece comprida como é).
  const pxm1 = caberEm(lista, 936, 640, 34);
  const capa = tela({
    etiqueta: 'compare antes de escolher', n: 1, total: T, capa: true, aviso: true,
    corpo: `<div class="t1">${lista.length} casas, ${lista.length} terrenos.<br>Qual ${y('cabe no seu')}?</div>
      <div class="centro" style="flex-direction:column;gap:26px;justify-content:flex-end"><div class="trio">${lista.map((pl) => `<div class="trio-i">${escala(pl, pxm1, { raio: 14 })}<div class="trio-l"><b>${pl.lote.replace(' m', '')}</b><br>${pl.area}</div></div>`).join('')}</div>
      <div class="escala-l">${regua(pxm1)}<span class="txt peq">as 3 na mesma escala</span></div></div>`,
  });
  // Casa comprida (fundo maior que 1,5 x a frente): planta em pé à direita, texto à esquerda.
  const telas = lista.map((pl, i) => {
    const base = { etiqueta: `planta ${i + 1} de ${lista.length} · ${pl.id}`, n: i + 2, total: T, aviso: true };
    if (pl.D > 1.5 * pl.W) {
      const pxm = caberEm([pl], 380, 1030, 0);
      return tela({ ...base, corpo: `<div class="lado"><div class="lado-t"><div class="t2">${pl.nome}</div><div class="chips col">${[pl.area, pl.quartos, pl.banhos, `cabe num lote de ${pl.lote}`, `no mínimo ${pl.minimo}`].map((c) => `<span class="chip">${c}</span>`).join('')}</div>
        <div class="txt peq">${y('Destaque:')} ${pl.destaque}.</div>
        <div class="lote-m">${noLote(pl, 440)}<div class="txt peq">a casa no lote de ${pl.lote},<br>com a rua embaixo</div></div>${regua(pxm)}</div><div class="lado-p">${escala(pl, pxm)}</div></div>` });
    }
    return tela({ ...base, corpo: `<div class="t2">${pl.nome}</div>${chips(pl)}
      <div class="centro">${escala(pl, caberEm([pl], 936, 640, 0))}</div>
      <div class="txt peq">${y('Destaque:')} ${pl.destaque}.</div>` });
  });
  const linhas = [['Área', 'area'], ['Quartos', 'quartos'], ['Banheiros', 'banhos'], ['Lote', 'lote'], ['No mínimo', 'minimo'], ['Para quem', 'para']];
  const curto = (pl) => pl.nome.replace(/^Casa /, '').replace(' ', '<br>');
  const tabela = tela({
    etiqueta: 'lado a lado', n: 5, total: T, aviso: true,
    corpo: `<div class="t2">Qual combina com ${y('o seu terreno')}?</div>
      <table class="tab"><tr><th></th>${lista.map((pl) => `<th>${curto(pl)}</th>`).join('')}</tr>
      ${linhas.map(([rot, k]) => `<tr><td class="rot">${rot}</td>${lista.map((pl) => `<td${k === 'para' ? '' : ' class="nw"'}>${String(pl[k]).replace(/ (quartos|banheiros?)$/, '')}</td>`).join('')}</tr>`).join('')}</table>
      <div class="txt peq">O lote mínimo é frente x fundo. Os recuos mudam de cidade para cidade: confira na sua prefeitura.</div>`,
  });
  return [capa, ...telas, tabela, telaCTA(T)];
};

// Post 3: como ler uma planta baixa
posts['post-03-como-ler-planta'] = () => {
  const T = 7, pl = P.compacta;
  const dica = (n, titulo, texto, visual) => tela({
    etiqueta: `dica ${n} de 5`, n: n + 1, total: T,
    corpo: `<div class="t2">${titulo}</div><div class="txt">${texto}</div><div class="centro">${visual}</div>`,
  });
  return [
    tela({
      etiqueta: 'salve para consultar', n: 1, total: T, capa: true,
      corpo: `<div class="t1">Como ler uma<br>${y('planta baixa')}<br>em 1 minuto</div><div class="centro">${img(pl, 'blueprint', 640, 800)}</div>`,
    }),
    dica(1, 'A cota é a medida', `A linha azul embaixo da casa, com um traço em cada ponta, mostra a largura em metros: aqui, ${y('6,50 m')}. A linha do lado mostra o fundo: 8,50 m.`,
      recorte(pl, [180, 20, 1640, 1050], 900, 576, defs + marca.retPx(300, 70, 1400, 130))),
    dica(2, 'Amarelo é a porta de entrada', `É por ali que você entra da rua. Na planta com móveis, o arco de cada porta mostra ${y('para que lado ela abre')}: esse espaço fica livre, nada de móvel ali.`,
      recorte(pl, [300, 230, 1000, 900], 900, 810, marca.porta(1.0, 0, 0.9, 0, Math.PI / 2))),
    dica(3, 'Azul é janela', `Cada ${y('retângulo azul')} na parede é uma janela. Confira se cada quarto tem a sua.`,
      recorte(pl, [600, 140, 1100, 760], 900, 622, marca.ret(2.2, -0.12, 3.2, 0.12) + marca.ret(4.2, -0.12, 5.6, 0.12))),
    dica(4, 'O m² é a área do cômodo', `${y('12,7 m²')} quer dizer um quarto de 3,25 x 3,90 m. Compare com o quarto onde você dorme hoje.`,
      recorte(pl, [980, 1330, 760, 820], 760, 820, marca.ret(3.2, 5.8, 6.5, 8.5))),
    dica(5, 'Planta humanizada', `É a mesma planta com ${y('piso e móveis em escala')}. Fica fácil ver como cada cômodo vai ser usado.`,
      img(pl, 'humanizada', 640, 800)),
    telaCTA(T, { titulo: 'Quer treinar numa planta de verdade?' }),
  ];
};

// Post 5: checklist antes de contratar o pedreiro
const ITENS = [
  ['Projeto com responsável técnico', 'Arquiteto ou engenheiro, com ART ou RRT.'],
  ['Alvará da prefeitura', 'Antes de começar a obra, não depois.'],
  ['Recuos do seu lote conferidos', 'Cada prefeitura tem a sua regra.'],
  ['3 orçamentos com a mesma planta', 'Só assim dá para comparar preço.'],
  ['Uma obra dele visitada', 'Converse com o dono da casa.'],
  ['Contrato escrito', 'O que está incluído, o prazo e o que acontece se atrasar.'],
  ['Pagamento por etapa pronta', 'Nunca a obra toda adiantada.'],
  ['Quem compra o material', 'E quem confere o que chegou.'],
];
posts['post-05-checklist-pedreiro'] = () => {
  const T = 5;
  const bloco = (ini, fim, rot, n) => tela({
    etiqueta: rot, n, total: T,
    corpo: `<div class="lista">${ITENS.slice(ini, fim).map(([t, d], i) => `<div class="item"><div class="caixa">✓</div><div><div class="item-t"><span class="y">${ini + i + 1}.</span> ${t}</div><div class="item-d">${d}</div></div></div>`).join('')}</div>`,
  });
  return [
    tela({
      etiqueta: 'salve para usar na obra', n: 1, total: T, capa: true,
      corpo: `<div class="t1">Antes de contratar<br>o pedreiro, confira<br>estes ${y('8 itens')}</div>
        <div class="centro"><div class="prancheta">${ITENS.slice(0, 5).map(() => '<div class="pl"><span class="caixa peq">✓</span><span class="risco"></span></div>').join('')}</div></div>`,
    }),
    bloco(0, 3, 'documentos', 2),
    bloco(3, 6, 'escolher quem faz', 3),
    bloco(6, 8, 'pagamento e material', 4),
    tela({
      etiqueta: 'lista completa', n: 5, total: T, aviso: true,
      corpo: `<div class="t2">Tire print e leve para a ${y('conversa')}</div>
        <div class="resumo">${ITENS.map(([t], i) => `<div><span class="caixa peq">✓</span> ${i + 1}. ${t}</div>`).join('')}</div>
        <div class="botao peq">Comente <b>PLANTA</b></div><div class="txt peq" style="text-align:center">e receba a planta humanizada da Casa Compacta de graça no WhatsApp.</div>`,
    }),
  ];
};

// Post 7: Casa Família Compacta, imagem única. A 3D parada (1400 x 1207) entra inteira no alto, 1080 x 930; a ficha fica embaixo.
posts['post-07-casa-familia'] = () => [
  `<div class="tela" style="height:1350px;padding:0">${img(P.familia, '3d', 1080, 930, { raio: 0, borda: false })}
    <div class="ficha7"><div class="t2" style="margin:0">${P.familia.nome}</div>${chips(P.familia)}<div class="aviso" style="position:static;margin-top:auto">${AVISO}</div>
    <div class="marca" style="margin-top:6px"><span class="logo"></span>${MARCA}</div></div></div>`,
];

// Post 8: erros comuns na planta
posts['post-08-erros-comuns'] = () => {
  const T = 5, pl = P.compacta;
  const erro = (n, titulo, ruim, bom, visual) => tela({
    etiqueta: `erro ${n} de 3`, n: n + 1, total: T,
    corpo: `<div class="t2">${titulo}</div>
      <div class="par"><div class="ruim">✕ ${ruim}</div><div class="bom">✓ ${bom}</div></div>
      <div class="centro">${visual}</div>`,
  });
  return [
    tela({
      etiqueta: 'e como evitar cada um', n: 1, total: T, capa: true,
      corpo: `<div class="t1">3 erros na planta<br>que ${y('saem caro')}<br>na obra</div><div class="centro">${img(pl, 'blueprint', 620, 775)}</div>`,
    }),
    erro(1, 'Corredor comprido', 'Corredor custa por metro, e ninguém mora nele.', `Na Casa Compacta, só ${y('10% da área')} é circulação: ela liga os quartos e o banheiro.`,
      recorte(pl, [700, 900, 1100, 900], 860, 704, marca.ret(3.2, 4.2, 4.6, 5.8))),
    erro(2, 'Banheiro de frente pra sala', 'Quem está na sala vê a porta do banheiro.', `A porta do banho ${y('abre para o hall')}, longe da sala.`,
      recorte(pl, [330, 250, 1380, 1300], 860, 810, marca.porta(4.6, 4.5, 0.8, 0, Math.PI / 2))),
    erro(3, 'Banheiro sem janela', 'Sem ventilação natural, o mofo aparece rápido.', `${y('Janela alta')} na parede de fora: ventila e mantém a privacidade.`,
      recorte(pl, [900, 1000, 950, 700], 860, 634, defs + marca.ret(6.38, 4.62, 6.62, 5.38) + marca.seta(1500, 1500, 1640, 1420))),
    telaCTA(T, { titulo: 'Quer a planta inteira, sem esses erros?' }),
  ];
};

// Reserva: Casa Compacta completa (entra se o post 2 não estiver pronto a tempo)
posts['reserva-casa-compacta'] = () => {
  const T = 6, pl = P.compacta;
  const vista = (n, rot, titulo, tipo) => tela({
    etiqueta: rot, n, total: T, aviso: true,
    corpo: `<div class="t2">${titulo}</div><div class="centro">${img(pl, tipo, 640, 800)}</div>`,
  });
  return [
    tela({
      etiqueta: 'planta da semana · C01', n: 1, total: T, capa: true,
      corpo: `<div class="t1">${pl.nome}:<br>${y(pl.area)}, ${pl.quartos}</div>${chips(pl)}<div class="centro">${img(pl, 'humanizada', 560, 700)}</div>`,
    }),
    vista(2, 'a planta com medidas', 'Blueprint com cotas', 'blueprint'),
    vista(3, 'a casa em 3D', 'Como ela fica por dentro', 'perspectiva'),
    vista(4, 'o outro lado', 'Sala, cozinha e quartos', 'lateral'),
    tela({
      etiqueta: 'por que funciona', n: 5, total: T, aviso: true,
      corpo: `<div class="t2">Por que ${y('funciona')}</div>
        <div class="lista">
          <div class="item"><div class="caixa">✓</div><div><div class="item-t">Sala e cozinha integradas</div><div class="item-d">A casa parece maior do que é.</div></div></div>
          <div class="item"><div class="caixa">✓</div><div><div class="item-t">Só 10% da área é circulação</div><div class="item-d">Sobra área para os cômodos.</div></div></div>
          <div class="item"><div class="caixa">✓</div><div><div class="item-t">Banheiro abre para o hall</div><div class="item-d">Não para a sala.</div></div></div>
        </div>`,
    }),
    telaCTA(T),
  ];
};

// Capas dos reels (1080 x 1920). O centro (1080 x 1440) é o que aparece na grade do perfil.
function capa(titulo, visual, sub = '') {
  return `<div class="tela capa-reel" style="height:1920px">${visual}
    <div class="capa-txt"><div class="t1">${titulo}</div>${sub ? `<div class="txt">${sub}</div>` : ''}</div></div>`;
}
const fundo = (pl, tipo) => img(pl, tipo, 1080, 1920, { raio: 0, borda: false });
// Cada capa é um "post" à parte: o filtro "post-04" gera só a capa do post 4. Saem em imagens/capas-reels/<nome>.png.
const CAPAS = {
  'post-01-reel-passeio-compacta': () => capa(`Você consegue ver a casa ${y('antes de construir')}?`, fundo(P.compacta, 'perspectiva'), `${P.compacta.nome} · ${P.compacta.area} · ${P.compacta.quartos}`),
  // Post 4: texto fixo do roteiro (POSTS.md) e a 3D parada da Casa Fita inteira, dentro da parte que aparece na grade (3:4).
  'post-04-reel-casa-fita': () => {
    const pl = P.fita, frente = pl.lote.split(' x ')[0];
    return `<div class="tela capa-reel capa4" style="height:1920px">
      <div class="capa4-t t1">É possível ${y(`${pl.quartos} num lote de ${frente}\u00a0metros`)} de frente?</div>
      <div class="capa4-img">${img(pl, '3d', 760, 858, { raio: 22 })}</div>
      <div class="capa4-f"><div class="txt"><b>${pl.nome}</b> · ${pl.area} · cabe num lote de <span class="nw">${pl.lote}</span>, com recuos de referência <span class="nw">(no mínimo ${pl.minimo})</span></div>
      <div class="aviso" style="position:static">${AVISO}</div></div></div>`;
  },
  'post-06-reel-bastidor': () => capa(`POV: a planta virando ${y('casa 3D')}`, `<div class="split">${img(P.compacta, 'blueprint', 1080, 960, { raio: 0, borda: false })}${img(P.compacta, 'perspectiva', 1080, 960, { raio: 0, borda: false })}</div>`),
  'post-09-reel-material-gratis': () => capa(`Comente ${y('PLANTA')} e receba isto de graça`, fundo(P.compacta, 'humanizada'), 'planta humanizada + blueprint + 3D'),
};
for (const [nome, fazer] of Object.entries(CAPAS)) posts[`capas-reels/${nome}`] = () => [fazer()];

// ---------------------------------------------------------------------------
// Estilo
// ---------------------------------------------------------------------------
const CSS = `@import url('https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,700;12..96,800&display=swap');
*{box-sizing:border-box;margin:0;padding:0}
body{width:1080px;font-family:Inter,sans-serif;color:#fff;background:${COR.azul}}
.tela{position:relative;width:1080px;overflow:hidden;padding:64px 72px 0;display:flex;flex-direction:column;
  background-color:${COR.azul};
  background-image:linear-gradient(rgba(255,255,255,.13) 2px,transparent 2px),linear-gradient(90deg,rgba(255,255,255,.13) 2px,transparent 2px),
  linear-gradient(rgba(255,255,255,.06) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.06) 1px,transparent 1px);
  background-size:180px 180px,180px 180px,36px 36px,36px 36px;background-position:-2px -2px}
.topo{display:flex;justify-content:space-between;align-items:center;height:40px}
.etq{font-size:26px;font-weight:600;letter-spacing:3px;text-transform:uppercase;color:${COR.claro}}
.num{font-size:24px;font-weight:600;color:${COR.claro};border:2px solid rgba(191,212,242,.6);border-radius:30px;padding:4px 16px}
.corpo{flex:1;display:flex;flex-direction:column;gap:30px;padding-top:34px;padding-bottom:170px;min-height:0}
.t1{font-family:'Bricolage Grotesque',Inter,sans-serif;font-size:86px;font-weight:800;line-height:1.04;letter-spacing:-1.5px}
.t2{font-family:'Bricolage Grotesque',Inter,sans-serif;font-size:64px;font-weight:800;line-height:1.06;letter-spacing:-1px}
.txt{font-size:36px;line-height:1.35;font-weight:500;color:#EAF1FB}
.txt.peq{font-size:28px;color:${COR.claro}}
.y{color:${COR.amarelo}}
.centro{flex:1;display:flex;align-items:center;justify-content:center;min-height:0}
.card{overflow:hidden;border:3px solid rgba(255,255,255,.7);box-shadow:0 18px 50px rgba(3,25,60,.45);border-radius:22px;background:${COR.escuro};flex:none}
.card.sem-borda{border:none;box-shadow:none}
.card img{display:block}
.rodape{position:absolute;left:72px;right:72px;bottom:46px;display:flex;justify-content:space-between;align-items:center}
.marca{display:flex;align-items:center;gap:14px;font-size:26px;font-weight:700;letter-spacing:.5px}
.logo{width:34px;height:34px;border:3px solid #fff;border-radius:4px;position:relative}
.logo:after{content:'';position:absolute;left:4px;right:4px;top:12px;height:3px;background:${COR.amarelo}}
.arrasta{font-size:30px;font-weight:700;color:${COR.amarelo}}
.aviso{position:absolute;left:72px;right:72px;bottom:100px;font-size:19px;color:${COR.claro};opacity:.85;line-height:1.3}
.chips{display:flex;flex-wrap:wrap;gap:12px}
.chip{font-size:28px;font-weight:600;border:2px solid rgba(255,255,255,.75);border-radius:40px;padding:8px 22px}
.chip:first-child{background:${COR.amarelo};color:${COR.escuro};border-color:${COR.amarelo};font-weight:800}
.falta{border:5px dashed ${COR.amarelo};border-radius:22px;display:flex;align-items:center;justify-content:center;text-align:center;background:rgba(8,59,128,.75);flex:none;padding:20px}
.falta-t{font-size:44px;font-weight:800;color:${COR.amarelo};letter-spacing:2px}
.falta-n{font-size:32px;font-weight:700;margin-top:12px}
.falta-a{font-size:20px;color:${COR.claro};margin-top:14px;line-height:1.4;word-break:break-all}
.trio{display:flex;gap:34px;justify-content:center;align-items:flex-end}
.trio-i{justify-content:flex-end}
.escala-l{align-self:stretch;display:flex;align-items:center;gap:22px}
.regua{display:flex;align-items:center;gap:12px;font-size:26px;font-weight:800;color:${COR.amarelo}}
.regua-b{display:flex;height:18px;border:3px solid ${COR.amarelo};border-radius:3px}
.regua-b i{flex:1;border-right:2px solid ${COR.amarelo}}.regua-b i:nth-child(odd){background:${COR.amarelo}}.regua-b i:last-child{border-right:none}
.lado{flex:1;display:flex;gap:44px;min-height:0}
.lado-t{flex:1;display:flex;flex-direction:column;gap:30px}
.lado-t .regua{margin-top:auto}
.lote-m{display:flex;align-items:flex-end;gap:26px}
.lado-t{gap:26px}
.lado-p{display:flex;align-items:flex-start;padding-top:20px}
.chips.col{flex-direction:column;align-items:flex-start}
.trio-i{display:flex;flex-direction:column;align-items:center;gap:16px}
.trio-i .falta-t{font-size:26px}.trio-i .falta-n{font-size:22px}.trio-i .falta-a{font-size:14px}
.mini .falta-t{font-size:26px}.mini .falta-n{font-size:22px}.mini .falta-a{font-size:14px}
.trio-l{font-size:30px;text-align:center;line-height:1.3;color:${COR.claro}}
.trio-l b{color:#fff;font-size:38px}
.tab{width:100%;border-collapse:collapse;font-size:34px;margin-top:10px}
.tab th{font-size:32px;font-weight:800;color:${COR.amarelo};text-align:center;padding:16px 8px;border-bottom:3px solid rgba(255,255,255,.6)}
.tab td{text-align:center;padding:24px 8px;border-bottom:2px solid rgba(255,255,255,.25);font-weight:600}
.tab td.rot{text-align:left;color:${COR.claro};font-weight:500;font-size:30px}
.tab td.nw{white-space:nowrap;font-size:31px}
.tela{font-feature-settings:'calt' 0}
.nw{white-space:nowrap}
.cta{flex:1;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:40px}
.botao{background:${COR.amarelo};color:${COR.escuro};font-size:64px;font-weight:600;border-radius:80px;padding:26px 64px;box-shadow:0 0 0 14px rgba(255,200,87,.25)}
.botao b{font-weight:900}
.botao.peq{font-size:44px;padding:18px 48px;align-self:center;margin-top:10px}
.mini{display:flex;gap:24px;margin-top:10px}
.lista{flex:1;display:flex;flex-direction:column;justify-content:center;gap:70px}
.item{display:flex;gap:30px;align-items:flex-start}
.caixa{flex:none;width:84px;height:84px;border:4px solid ${COR.amarelo};border-radius:14px;display:flex;align-items:center;justify-content:center;font-size:46px;font-weight:900;color:${COR.amarelo}}
.caixa.peq{width:38px;height:38px;font-size:24px;border-width:3px;border-radius:8px;display:inline-flex;vertical-align:middle;margin-right:10px}
.item-t{font-size:54px;font-weight:800;line-height:1.15}
.item-d{font-size:38px;color:${COR.claro};margin-top:10px;line-height:1.3}
.prancheta{width:620px;border:4px solid rgba(255,255,255,.8);border-radius:26px;padding:40px 46px;display:flex;flex-direction:column;gap:30px;background:rgba(8,59,128,.55)}
.pl{display:flex;align-items:center;gap:18px}
.risco{flex:1;height:14px;border-radius:8px;background:rgba(255,255,255,.55)}
.resumo{display:flex;flex-direction:column;gap:26px;font-size:38px;font-weight:600;margin-top:10px}
.par{display:flex;flex-direction:column;gap:16px}
.ruim{font-size:34px;line-height:1.3;color:${COR.ruim};font-weight:600}
.bom{font-size:36px;line-height:1.3;font-weight:600}
.bom .y{font-weight:800}
.faixa{position:absolute;left:0;right:0;bottom:0;padding:44px 72px 50px;background:linear-gradient(transparent,rgba(8,59,128,.92) 30%);display:flex;flex-direction:column;gap:20px}
.capa-reel{padding:0}
.capa-reel>.cardw,.capa-reel>.falta{position:absolute;inset:0}
.capa-txt{position:absolute;left:72px;right:72px;top:600px;padding:44px 48px;border-radius:30px;background:rgba(8,59,128,.88);border:3px solid rgba(255,255,255,.6);display:flex;flex-direction:column;gap:22px}
.split{position:absolute;inset:0;display:flex;flex-direction:column}
.cardw{position:relative;flex:none}
.selo{position:absolute;top:20px;right:20px;font-size:22px;font-weight:700;color:${COR.escuro};background:#fff;border:2px solid ${COR.escuro};border-radius:30px;padding:5px 16px;line-height:1.2}
.selo.borda{top:-18px;right:28px}
.selo.peq{font-size:14px;padding:3px 10px;border-width:1.5px}
.selo.peq.borda{top:-12px;right:14px}
.ficha7{position:absolute;left:0;right:0;top:930px;bottom:0;padding:34px 72px 40px;display:flex;flex-direction:column;gap:18px}
.ficha7 .chip{font-size:29px;padding:7px 20px}
.ficha7 .t2{font-size:70px}
.capa4-t{position:absolute;left:72px;right:72px;top:262px;text-wrap:balance}
.capa4-img{position:absolute;left:0;right:0;top:560px;display:flex;justify-content:center}
.capa4-f{position:absolute;left:72px;right:72px;top:1442px;display:flex;flex-direction:column;gap:14px}
.capa4-f .txt{font-size:32px}
`;

// ---------------------------------------------------------------------------
// Render
// ---------------------------------------------------------------------------
// Caixa das paredes da planta mobiliada, medida nos pixels escuros (linha ou coluna com mais de 1/50 da imagem).
// Confere a escala: largura e fundo da casa (W e D do dado) têm de dar os mesmos pixels por metro.
async function medir(page) {
  for (const pl of Object.values(CASAS)) {
    const f = path.join(PLANTAS, pl.pasta, ARQ.humanizada);
    if (!fs.existsSync(f)) continue;
    pl.caixa = await caixa(page, f, 'paredes');
    const c = pl.caixa, sx = (c.x1 - c.x0) / pl.W, sy = (c.y1 - c.y0) / pl.D;
    if (Math.abs(sx / sy - 1) > 0.03) throw new Error(`${pl.id}: a caixa das paredes não bate com ${pl.W} x ${pl.D} m (${sx.toFixed(0)} e ${sy.toFixed(0)} px/m)`);
    const fl = path.join(PLANTAS, pl.pasta, ARQ.lateral);
    if (fs.existsSync(fl)) pl.lote4 = await caixa(page, fl, 'desenho');
  }
}
// "paredes": linhas e colunas com muitos pixels escuros. "desenho": tudo o que não é branco entre o subtítulo e o rodapé.
async function caixa(page, f, modo) {
  return page.evaluate(async ([url, modo]) => {
      const im = new Image(); im.src = url; await im.decode();
      const W = im.naturalWidth, H = im.naturalHeight, cv = document.createElement('canvas');
      cv.width = W; cv.height = H; const g = cv.getContext('2d'); g.drawImage(im, 0, 0);
      const d = g.getImageData(0, 0, W, H).data, lin = new Uint32Array(H), col = new Uint32Array(W);
      const y0 = modo === 'desenho' ? Math.round(H * 0.14) : 0, y1 = modo === 'desenho' ? Math.round(H * 0.93) : H;
      const sim = modo === 'desenho' ? (i) => Math.min(d[i], d[i + 1], d[i + 2]) < 235 : (i) => d[i] < 70 && d[i + 1] < 70 && d[i + 2] < 70;
      for (let yy = y0; yy < y1; yy++) for (let x = 0; x < W; x++) { if (sim((yy * W + x) * 4)) { lin[yy]++; col[x]++; } }
      const lim = modo === 'desenho' ? 0 : W / 50, pri = (a) => a.findIndex((v) => v > lim), ult = (a) => a.length - 1 - Array.from(a).reverse().findIndex((v) => v > lim);
      return { iw: W, ih: H, x0: pri(col), x1: ult(col), y0: pri(lin), y1: ult(lin) };
    }, ['data:image/png;base64,' + fs.readFileSync(f).toString('base64'), modo]);
}

(async () => {
  const filtro = process.argv.slice(2).filter((a, i, l) => a !== '--saida' && l[i - 1] !== '--saida')[0] || '';
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1080, height: 1350 }, deviceScaleFactor: 2 });
  await medir(page);
  const tmp = path.join(SAIDA, '.tmp.html');
  fs.mkdirSync(SAIDA, { recursive: true });
  for (const [nome, fazer] of Object.entries(posts)) {
    if (filtro && !nome.includes(filtro)) continue;
    const telas = fazer();
    const ehCapa = nome.startsWith('capas-reels/');
    for (let i = 0; i < telas.length; i++) {
      const pasta = path.join(SAIDA, ehCapa ? 'capas-reels' : nome);
      const arq = ehCapa ? `${nome.slice('capas-reels/'.length)}.png` : `${String(i + 1).padStart(2, '0')}.png`;
      fs.mkdirSync(pasta, { recursive: true });
      const alto = telas[i].includes('height:1920px') ? 1920 : 1350;
      fs.writeFileSync(tmp, `<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><style>${CSS}</style></head><body>${telas[i]}</body></html>`);
      await page.setViewportSize({ width: 1080, height: alto });
      await page.goto('file://' + tmp);
      await page.evaluate(() => document.fonts.ready);
      await page.waitForFunction(() => [...document.images].every((im) => im.complete));
      await page.screenshot({ path: path.join(pasta, arq), clip: { x: 0, y: 0, width: 1080, height: alto } });
      console.log('ok', path.relative(RAIZ, path.join(pasta, arq)));
    }
  }
  fs.rmSync(tmp, { force: true });
  await browser.close();
  if (faltando.size) {
    console.log('\nFalta imagem (as telas saíram com aviso amarelo):');
    for (const f of faltando) console.log('  -', f);
  }
})();

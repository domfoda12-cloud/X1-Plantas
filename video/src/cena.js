// Desenha cada quadro do vídeo a partir do tempo t (em segundos).
// O render.cjs chama window.renderAt(t) quadro a quadro e tira uma captura de tela.
import * as THREE from '../node_modules/three/build/three.module.js';
import { criarCasa } from './casa3d.js';
import { ambientes, paredes, janelas, portas, LARGURA, PROFUNDIDADE, ESPESSURA } from './planta.js';

// ---------------------------------------------------------------------------
// Roteiro, pensado para retenção (tempo assistido), como no reel de referência:
//   Gancho (0 a 3 s), tela cheia: o blueprint se desenha e a casa começa a ganhar vida.
//   Desenvolvimento (3 a 27 s): seis erros em cartões blueprint, do geral ao específico.
//   Desfecho (27 a 34 s), tela cheia: a casa ganha vida por completo (planta humanizada).
//   Chamada (34 a 38 s): comentar PLANTA para receber a planta.
// O corpo é igual em todas as versões; só o gancho muda (5 versões para os reels de teste).
// ---------------------------------------------------------------------------
const INFO = '55 m² · 2 quartos · 1 banho';
export const GANCHOS = [
  { titulo: 'Vou te economizar os R$ 1.000<br>que um arquiteto te economizaria', fala: 'Vou te economizar os *mil* *reais* que um arquiteto te economizaria.' },
  { titulo: 'Os R$ 1.000 que um arquiteto<br>te faria economizar, de graça', fala: 'Os *mil* *reais* que um arquiteto te faria economizar, de graça.' },
  { titulo: 'Antes de pagar R$ 1.000<br>a um arquiteto, veja isso', fala: 'Antes de pagar *mil* *reais* a um arquiteto, veja isso aqui.' },
  { titulo: '7 erros que um arquiteto<br>te cobraria R$ 1.000 pra achar', fala: 'Sete erros que um arquiteto te cobraria *mil* *reais* pra achar.' },
  { titulo: 'Um arquiteto cobraria R$ 1.000<br>pra te mostrar isso', fala: 'Um arquiteto te cobraria *mil* *reais* pra te mostrar isso.' },
];
const versao = (() => { const v = Number(new URLSearchParams(location.search).get('v') || 1); return Number.isInteger(v) && v >= 1 && v <= GANCHOS.length ? v : 1; })();
export const DURACAO_GANCHO = 3;

export const cenas = [
  { ini: 0, fim: 3, tipo: 'tela-gancho', ...GANCHOS[versao - 1] },
  { ini: 3, fim: 7, tipo: 'sol', rotulo: 'POSIÇÃO DO SOL', info: 'Casa Compacta',
    etiqueta: 'erro 1', titulo: 'Ignorar o sol', fala: 'Um: ignorar o sol. Quarto virado pro *nascente* fica fresco à tarde.' },
  { ini: 7, fim: 11, tipo: 'corredor', rotulo: 'CIRCULAÇÃO', info: 'Casa Compacta',
    etiqueta: 'erro 2', titulo: 'Corredor comprido', fala: 'Dois: corredor comprido. Corredor *custa* *por* *metro,* e ninguém mora nele.' },
  { ini: 11, fim: 15, tipo: 'banho-porta', rotulo: 'PRIVACIDADE', info: 'Casa Compacta',
    etiqueta: 'erro 3', titulo: 'Banheiro de frente pra sala', fala: 'Três: banheiro de frente pra sala. A porta tem que abrir *pro* *hall.*' },
  { ini: 15, fim: 19, tipo: 'banho-janela', rotulo: 'VENTILAÇÃO', info: 'Casa Compacta',
    etiqueta: 'erro 4', titulo: 'Banheiro sem janela', fala: 'Quatro: banheiro sem janela. Sem ventilação natural, o *mofo* aparece rápido.' },
  { ini: 19, fim: 23, tipo: 'recuos', rotulo: 'TERRENO E RECUOS', info: 'Lote 10 x 20 m',
    etiqueta: 'erro 5', titulo: 'Esquecer os recuos', fala: 'Cinco: esquecer os recuos. Cada *prefeitura* tem a sua regra, confira antes.' },
  { ini: 23, fim: 27, tipo: 'ampliacao', rotulo: 'AMPLIAÇÃO', info: 'Casa Compacta',
    etiqueta: 'erro 6', titulo: 'Não prever ampliação', fala: 'Seis: não prever ampliação. Deixe pronto por onde a casa *vai* *crescer.*' },
  { ini: 27, fim: 34, tipo: 'tela-resposta',
    etiqueta: 'erro 7 · o mais caro', titulo: 'Não ver a casa em 3D', fala: 'E o *mais* *caro* de todos: construir sem ver a casa pronta. … Olha só: cada cômodo, cada móvel, *antes* *do* *primeiro* *tijolo.*' },
  { ini: 34, fim: 38, tipo: 'cta', rotulo: 'PLANTA GRÁTIS', info: 'pelo WhatsApp',
    etiqueta: 'planta grátis', titulo: 'Comente PLANTA', fala: 'Comenta *PLANTA* que eu te mando essa planta humanizada *de* *graça* no WhatsApp.' },
];
export const DURACAO = cenas[cenas.length - 1].fim;

// ---------------------------------------------------------------------------
// Utilidades
// ---------------------------------------------------------------------------
const clamp = (v, a = 0, b = 1) => Math.min(b, Math.max(a, v));
const suave = (v) => { v = clamp(v); return v * v * (3 - 2 * v); };
const saida = (v) => 1 - Math.pow(1 - clamp(v), 3);
const lerp = (a, b, v) => a + (b - a) * v;
const m2 = (a) => a.toFixed(1).replace('.', ',') + ' m²';
const areaDe = (a) => (a.x1 - a.x0) * (a.y1 - a.y0);
const amb = (id) => ambientes.find((a) => a.id === id);

const COR = { branco: '#FFFFFF', claro: '#BFD4F2', destaque: '#FFC857', ok: '#7EE2A8', ruim: '#FF9C8A', azul: '#0B4FA8', escuro: '#083B80' };

// ---------------------------------------------------------------------------
// Planta 2D em estilo blueprint (SVG), desenhada progressivamente (p de 0 a 1)
// ---------------------------------------------------------------------------
function svgPlanta({ ox, oy, s, destaque = [], hp = 1, nomes = true, p = 1 }) {
  const X = (x) => ox + x * s; const Y = (y) => oy + y * s;
  const dash = (q) => `pathLength="1" stroke-dasharray="1 1" stroke-dashoffset="${1 - q}"`;
  let out = '<g>';
  for (const a of ambientes) {
    if (!destaque.includes(a.id) || hp <= 0) continue;
    out += `<rect x="${X(a.x0)}" y="${Y(a.y0)}" width="${(a.x1 - a.x0) * s}" height="${(a.y1 - a.y0) * s}"
      fill="${COR.destaque}" fill-opacity="${0.28 * hp}" stroke="${COR.destaque}" stroke-width="4" stroke-opacity="${hp}"/>`;
  }
  const e = ESPESSURA * s;
  paredes.forEach(([x0, y0, x1, y1], i) => {
    const q = clamp(p * 1.6 - i * 0.04);
    if (q <= 0) return;
    out += `<line x1="${X(x0)}" y1="${Y(y0)}" x2="${X(x1)}" y2="${Y(y1)}" stroke="${COR.branco}" stroke-width="${e + 2}" stroke-linecap="square" ${dash(q)}/>`;
    out += `<line x1="${X(x0)}" y1="${Y(y0)}" x2="${X(x1)}" y2="${Y(y1)}" stroke="${COR.azul}" stroke-width="${Math.max(e - 4, 1)}" stroke-linecap="square" ${dash(q)}/>`;
  });
  const pj = clamp((p - 0.55) / 0.3);
  for (const j of janelas) {
    const [x0, y0, x1, y1] = j.seg; const h = y0 === y1; const k = e / 2;
    out += `<line x1="${X(x0)}" y1="${Y(y0)}" x2="${X(x1)}" y2="${Y(y1)}" stroke="${COR.azul}" stroke-width="${e + 3}" opacity="${pj}"/>`;
    for (const d of [-k, 0, k]) {
      out += h ? `<line x1="${X(x0)}" y1="${Y(y0) + d}" x2="${X(x1)}" y2="${Y(y1) + d}" stroke="${COR.branco}" stroke-width="1.6" opacity="${pj}"/>`
        : `<line x1="${X(x0) + d}" y1="${Y(y0)}" x2="${X(x1) + d}" y2="${Y(y1)}" stroke="${COR.branco}" stroke-width="1.6" opacity="${pj}"/>`;
    }
  }
  const pd = clamp((p - 0.6) / 0.3);
  for (const d of portas) {
    const r = d.r * s; const cx = X(d.x); const cy = Y(d.y);
    const ang = lerp(d.a0, d.a1, pd);
    const xa = cx + Math.cos(d.a0) * r; const ya = cy + Math.sin(d.a0) * r;
    const xb = cx + Math.cos(ang) * r; const yb = cy + Math.sin(ang) * r;
    if (pd > 0.01) out += `<path d="M ${xa} ${ya} A ${r} ${r} 0 0 1 ${xb} ${yb}" fill="none" stroke="${COR.branco}" stroke-width="1.6" stroke-dasharray="5 4" opacity="${pd * 0.9}"/>
      <line x1="${cx}" y1="${cy}" x2="${xb}" y2="${yb}" stroke="${COR.branco}" stroke-width="2" opacity="${pd}"/>`;
  }
  if (nomes) {
    const pn = clamp((p - 0.7) / 0.3);
    for (const a of ambientes) {
      const cx = X((a.x0 + a.x1) / 2); const cy = Y((a.y0 + a.y1) / 2);
      const pequeno = a.id === 'hall' || a.id === 'banho';
      out += `<text x="${cx}" y="${cy - 2}" text-anchor="middle" font-size="${pequeno ? 15 : 20}" font-weight="700" fill="${COR.branco}" opacity="${pn}" letter-spacing="0.5">${a.nome.toUpperCase()}</text>`;
      out += `<text x="${cx}" y="${cy + (pequeno ? 17 : 22)}" text-anchor="middle" font-size="${pequeno ? 13 : 16}" fill="${COR.claro}" opacity="${pn}">${m2(areaDe(a))}</text>`;
    }
  }
  return out + '</g>';
}

function seta(x1, y1, x2, y2, p, cor = COR.destaque) {
  if (p <= 0.02) return '';
  const x = lerp(x1, x2, p); const y = lerp(y1, y2, p);
  const ang = Math.atan2(y2 - y1, x2 - x1); const t = 18;
  const pa = `${x},${y} ${x - t * Math.cos(ang - 0.45)},${y - t * Math.sin(ang - 0.45)} ${x - t * Math.cos(ang + 0.45)},${y - t * Math.sin(ang + 0.45)}`;
  return `<line x1="${x1}" y1="${y1}" x2="${x}" y2="${y}" stroke="${cor}" stroke-width="6" stroke-linecap="round"/><polygon points="${pa}" fill="${cor}"/>`;
}

function texto(x, y, linhas, { tam = 30, peso = 600, cor = COR.branco, op = 1, sobe = 0 } = {}) {
  return linhas.map((l, i) => `<text x="${x}" y="${y + i * tam * 1.3 + sobe}" font-size="${tam}" font-weight="${peso}" fill="${cor}" opacity="${op}">${l}</text>`).join('');
}
// Texto que entra subindo e aparecendo, para não "pular" na tela
const entra = (tc, ini, dur = 0.5) => { const v = saida((tc - ini) / dur); return { op: v, sobe: (1 - v) * 18 }; };

const S = 58; const OX = 60; const OY = 30; // escala e origem padrão da planta nos cartões

const cartoes2D = {
  sol(tc) {
    const p = saida(tc / 0.9); const a = saida((tc - 0.8) / 0.9);
    const sx = 770; const sy = 115; const r = 44;
    let raios = '';
    for (let i = 0; i < 12; i++) {
      const ang = (i / 12) * Math.PI * 2 + tc * 0.35;
      raios += `<line x1="${sx + Math.cos(ang) * (r + 10)}" y1="${sy + Math.sin(ang) * (r + 10)}" x2="${sx + Math.cos(ang) * (r + 26)}" y2="${sy + Math.sin(ang) * (r + 26)}" stroke="${COR.destaque}" stroke-width="5" stroke-linecap="round" opacity="${a}"/>`;
    }
    const q2 = amb('quarto2');
    return svgPlanta({ ox: OX, oy: OY, s: S, p, destaque: ['quarto2'], hp: a * (0.78 + 0.22 * Math.sin(tc * 5.5)) }) +
      `<circle cx="${sx}" cy="${sy}" r="${r}" fill="${COR.destaque}" opacity="${a}"/>${raios}` +
      seta(sx - 64, sy + 42, OX + ((q2.x0 + q2.x1) / 2) * S + 40, OY + ((q2.y0 + q2.y1) / 2) * S - 30, a) +
      texto(570, 340, ['Nascente (leste)'], { tam: 32, peso: 800, ...entra(tc, 1.0) }) +
      texto(570, 390, ['Sol da manhã nos', 'quartos: ambiente', 'mais fresco à tarde.'], { tam: 26, peso: 500, cor: COR.claro, ...entra(tc, 1.2) });
  },
  corredor(tc) {
    const p = saida(tc / 0.9); const a = saida((tc - 0.8) / 0.8);
    const hall = amb('hall');
    const barra = (y, rot, larg, cor, ini) => { const v = saida((tc - ini) / 0.7); return `<text x="520" y="${y}" font-size="24" font-weight="600" fill="${COR.claro}" opacity="${v}">${rot}</text>
      <rect x="520" y="${y + 14}" width="${Math.max(larg * v, 0.1)}" height="32" rx="8" fill="${cor}"/>`; };
    return svgPlanta({ ox: OX, oy: OY, s: S, p, destaque: ['hall'], hp: a * (0.78 + 0.22 * Math.sin(tc * 5.5)) }) +
      texto(520, 110, [`Hall: ${m2(areaDe(hall))}`], { tam: 40, peso: 800, cor: COR.destaque, ...entra(tc, 0.9) }) +
      texto(520, 160, ['Circulação curta,', 'mais área para', 'os ambientes.'], { tam: 26, peso: 500, cor: COR.claro, ...entra(tc, 1.1) }) +
      barra(330, 'Corredor comprido', 320, COR.ruim, 1.4) + barra(420, 'Hall compacto', 110, COR.ok, 1.7);
  },
  'banho-porta'(tc) {
    const p = saida(tc / 0.9); const a = saida((tc - 0.8) / 0.8);
    return svgPlanta({ ox: OX, oy: OY, s: S, p, destaque: ['banho', 'hall'], hp: a * (0.78 + 0.22 * Math.sin(tc * 5.5)) }) +
      texto(510, 140, ['✓ Abre para o hall'], { tam: 32, peso: 800, cor: COR.ok, ...entra(tc, 1.0) }) +
      texto(510, 190, ['Quem está na sala', 'não vê a porta', 'do banheiro.'], { tam: 26, peso: 500, cor: COR.claro, ...entra(tc, 1.2) }) +
      texto(510, 400, ['✗ De frente', 'para a sala'], { tam: 30, peso: 800, cor: COR.ruim, ...entra(tc, 1.8) });
  },
  'banho-janela'(tc) {
    const p = saida(tc / 0.9); const a = saida((tc - 0.8) / 0.8);
    const X = (x) => OX + x * S; const Y = (y) => OY + y * S;
    let ar = '';
    for (let i = 0; i < 3; i++) {
      const fase = (tc * 0.8 + i / 3) % 1;
      const x = X(6.5) + 12 + fase * 70; const y = Y(4.8 + i * 0.22);
      ar += `<path d="M ${x} ${y} q 12 -10 24 0 t 24 0" fill="none" stroke="${COR.claro}" stroke-width="5" stroke-linecap="round" opacity="${a * (1 - fase)}"/>`;
    }
    return svgPlanta({ ox: OX, oy: OY, s: S, p, destaque: ['banho'], hp: a * (0.78 + 0.22 * Math.sin(tc * 5.5)) }) + ar +
      texto(570, 140, ['Janela alta'], { tam: 36, peso: 800, cor: COR.destaque, ...entra(tc, 1.0) }) +
      texto(570, 185, ['peitoril de 1,6 m'], { tam: 26, peso: 600, cor: COR.branco, ...entra(tc, 1.15) }) +
      texto(570, 300, ['Ventilação natural', 'evita mofo e', 'cheiro parado.'], { tam: 26, peso: 500, cor: COR.claro, ...entra(tc, 1.35) });
  },
  recuos(tc) {
    const s = 25; const ox = 70; const oy = 30;
    const p = saida(tc / 0.8); const a = saida((tc - 0.7) / 0.8);
    const X = (x) => ox + x * s; const Y = (y) => oy + y * s;
    const cx = 1.5; const cy = 4; // casa a 1,5 m da divisa e 4 m da frente (exemplo)
    let out = `<rect x="${X(0)}" y="${Y(0)}" width="${10 * s}" height="${20 * s}" fill="none" stroke="${COR.branco}" stroke-width="3" pathLength="1" stroke-dasharray="1 1" stroke-dashoffset="${1 - p}"/>`;
    out += `<g opacity="${saida((tc - 0.4) / 0.6)}"><rect x="${X(cx)}" y="${Y(cy)}" width="${LARGURA * s}" height="${PROFUNDIDADE * s}" fill="rgba(255,255,255,0.16)" stroke="${COR.branco}" stroke-width="3"/>
      <text x="${X(cx + LARGURA / 2)}" y="${Y(cy + PROFUNDIDADE / 2) + 8}" text-anchor="middle" font-size="22" font-weight="800" fill="${COR.branco}">CASA</text></g>`;
    out += `<line x1="${X(0)}" y1="${Y(cy)}" x2="${X(10)}" y2="${Y(cy)}" stroke="${COR.destaque}" stroke-width="3" stroke-dasharray="10 8" opacity="${a}"/>`;
    out += `<line x1="${X(cx)}" y1="${Y(0)}" x2="${X(cx)}" y2="${Y(20)}" stroke="${COR.destaque}" stroke-width="3" stroke-dasharray="10 8" opacity="${a}"/>`;
    out += `<text x="${X(5)}" y="${Y(cy / 2) + 8}" text-anchor="middle" font-size="19" font-weight="800" fill="${COR.destaque}" opacity="${a}">RECUO FRONTAL</text>`;
    out += `<text x="${X(5)}" y="${Y(0) - 8}" text-anchor="middle" font-size="17" fill="${COR.claro}">rua</text>`;
    return out +
      texto(400, 110, ['Lote 10 x 20 m'], { tam: 34, peso: 800, ...entra(tc, 0.3) }) +
      texto(400, 165, ['A casa precisa caber', 'dentro dos recuos,', 'não só no terreno.'], { tam: 26, peso: 500, cor: COR.claro, ...entra(tc, 0.9) }) +
      texto(400, 380, ['Os recuos mudam', 'de cidade para cidade:', 'confira na prefeitura.'], { tam: 25, peso: 800, cor: COR.destaque, ...entra(tc, 1.5) });
  },
  ampliacao(tc) {
    const s = 52; const ox = 40; const oy = 40;
    const p = saida(tc / 0.9); const a = saida((tc - 0.9) / 0.8);
    const X = (x) => ox + x * s; const Y = (y) => oy + y * s;
    const ext = `<rect x="${X(6.5)}" y="${Y(5.8)}" width="${2.8 * s}" height="${2.7 * s}" fill="${COR.destaque}" fill-opacity="${0.18 * a}"
      stroke="${COR.destaque}" stroke-width="4" stroke-dasharray="12 8" opacity="${a}"/>
      <text x="${X(7.9)}" y="${Y(7.05)}" text-anchor="middle" font-size="19" font-weight="800" fill="${COR.destaque}" opacity="${a}">QUARTO 3</text>
      <text x="${X(7.9)}" y="${Y(7.05) + 24}" text-anchor="middle" font-size="16" fill="${COR.destaque}" opacity="${a}">(futuro)</text>`;
    return svgPlanta({ ox, oy, s, p }) + ext +
      texto(570, 110, ['Pronta para', 'crescer'], { tam: 36, peso: 800, ...entra(tc, 0.5) }) +
      texto(570, 220, ['Deixe previsto', 'por onde a casa', 'vai aumentar.'], { tam: 26, peso: 500, cor: COR.claro, ...entra(tc, 1.1) });
  },
  cta(tc) {
    const p = saida(tc / 0.6); const q = saida((tc - 0.7) / 0.6);
    const img = imagemHumanizada ? `<image href="${imagemHumanizada}" x="0" y="70" width="330" height="390" preserveAspectRatio="xMidYMid slice" clip-path="url(#recorte)"/>` : '';
    return `<defs><clipPath id="recorte"><rect x="0" y="70" width="330" height="390"/></clipPath></defs>
      <g transform="translate(100 ${40 + (1 - p) * 30}) rotate(-3 165 230)" opacity="${p}">
        <rect x="-6" y="-6" width="342" height="472" rx="12" fill="rgba(0,0,0,0.25)"/>
        <rect x="0" y="0" width="330" height="460" rx="10" fill="#FBF8F2"/>
        <rect x="0" y="0" width="330" height="70" rx="10" fill="${COR.escuro}"/>
        <text x="22" y="44" font-size="25" font-weight="800" fill="#FFFFFF">CASA COMPACTA</text>
        ${img}
      </g>
      <g opacity="${q}" transform="translate(520 ${150 + (1 - q) * 20})">
        <text x="0" y="0" font-size="34" font-weight="800" fill="${COR.branco}">Comente</text>
        <g transform="translate(150 70) scale(${1 + 0.05 * Math.sin(tc * 6)}) translate(-150 -70)"><rect x="0" y="22" width="300" height="96" rx="48" fill="${COR.destaque}"/>
        <text x="150" y="88" text-anchor="middle" font-size="46" font-weight="900" fill="${COR.escuro}">PLANTA</text></g>
        <text x="0" y="178" font-size="25" font-weight="500" fill="${COR.claro}">e receba a planta</text>
        <text x="0" y="210" font-size="25" font-weight="500" fill="${COR.claro}">humanizada grátis</text>
        <text x="0" y="242" font-size="25" font-weight="500" fill="${COR.claro}">no WhatsApp</text>
      </g>`;
  },
};

// Grade do blueprint de fundo dos cartões
const GRADE = `<defs><pattern id="grade" width="29" height="29" patternUnits="userSpaceOnUse">
  <path d="M 29 0 L 0 0 0 29" fill="none" stroke="rgba(255,255,255,0.10)" stroke-width="1"/></pattern></defs>
  <rect x="0" y="0" width="900" height="560" fill="url(#grade)"/>`;

// ---------------------------------------------------------------------------
// 3D em tela cheia
// ---------------------------------------------------------------------------
const SS = Number(new URLSearchParams(location.search).get('ss') || 1.25);
const canvas = document.getElementById('tres');
const renderer = new THREE.WebGLRenderer({ canvas, antialias: true, preserveDrawingBuffer: true });
renderer.setPixelRatio(SS); renderer.setSize(1080, 1920, false);
const casa = criarCasa(renderer);
const ASPECTO = 1080 / 1920;
let imagemHumanizada = null;

const telas = {
  // Gancho: blueprint se desenha, paredes sobem e a casa começa a ganhar vida.
  'tela-gancho'(tc) {
    casa.aplicar({ desenho: saida((tc + 0.3) / 1.3), paredes: suave((tc - 0.8) / 1.1), vida: 0.85 * suave((tc - 1.4) / 1.6) });
    casa.enquadrar({ theta: lerp(0, 0.22, suave(tc / 3)), inclinacao: lerp(0.02, 0.4, suave((tc - 0.6) / 2.4)), distancia: lerp(35, 31, saida(tc / 3)), alvo: [0, 3.8], aspecto: ASPECTO });
  },
  // Resposta: a casa ganha vida por completo e a câmera desliza devagar.
  'tela-resposta'(tc) {
    casa.aplicar({ desenho: 1, paredes: suave(tc / 1.2), vida: suave((tc - 0.6) / 2.6) });
    casa.enquadrar({ theta: lerp(-0.15, 0.5, suave(tc / 7)), inclinacao: lerp(0.05, 0.5, suave((tc - 0.4) / 5.5)), distancia: lerp(35, 29, suave(tc / 7)), alvo: [0, lerp(3.8, 3.2, suave(tc / 7))], aspecto: ASPECTO });
  },
};

// ---------------------------------------------------------------------------
// Quadro
// ---------------------------------------------------------------------------
const el = (id) => document.getElementById(id);
const dom = { topo: el('gancho-topo'), progresso: [...document.querySelectorAll('#progresso .seg')], cartao: el('cartao'), rotT: el('rotulo-titulo'), rotI: el('rotulo-info'), desenho: el('desenho'), tres: el('tres'), vinheta: el('vinheta'), legT: el('leg-titulo'), legP: el('leg-palavra') };

window.renderAt = (t) => {
  const c = cenas.find((x) => t >= x.ini && t < x.fim) || cenas[cenas.length - 1];
  const tc = t - c.ini;
  const tela = c.tipo.startsWith('tela');

  dom.tres.style.display = tela ? 'block' : 'none';
  dom.vinheta.style.display = tela ? 'block' : 'none';
  if (tela) { telas[c.tipo](tc); casa.render(); }

  // Cartão: entra deslizando de leve (sem "pulo")
  const entrada = saida(tc / 0.35);
  dom.cartao.style.opacity = tela ? 0 : entrada;
  dom.cartao.style.transform = `translateY(${(1 - entrada) * 40}px)`;
  if (!tela) {
    dom.rotT.textContent = c.rotulo; dom.rotI.textContent = c.info;
    const zoom = 1 + 0.045 * suave(tc / (c.fim - c.ini));
    dom.desenho.innerHTML = `<svg viewBox="0 0 900 560" xmlns="http://www.w3.org/2000/svg" font-family="Inter, sans-serif">${GRADE}<g transform="translate(450 280) scale(${zoom}) translate(-450 -280)">${cartoes2D[c.tipo](tc)}</g></svg>`;
  }

  // Legenda no estilo das referências: etiqueta pequena + título do item, e a fala
  // em blocos de 2 a 3 palavras, em letra fina; a palavra-chave aparece em amarelo.
  const gancho = c.tipo === 'tela-gancho';
  dom.legT.innerHTML = gancho ? c.titulo : `<small>${c.etiqueta}</small>${c.titulo}`;
  dom.legT.classList.toggle('gancho', gancho);
  const { texto: bloco, desde } = blocoNoTempo(c, tc);
  dom.legP.innerHTML = bloco;
  dom.legP.style.transform = `scale(${1 + 0.08 * (1 - saida(desde / 0.12))})`;
  dom.topo.innerHTML = GANCHOS[versao - 1].titulo;
  dom.topo.style.opacity = gancho ? 0 : 1;

  // Barra de progresso: 7 itens; mostra quantos faltam
  const idx = c.tipo === 'tela-gancho' ? -1 : c.tipo === 'cta' ? 7 : cenas.indexOf(c) - 1;
  dom.progresso.forEach((seg, i) => {
    const cheio = i < idx ? 1 : i === idx ? clamp(tc / (c.fim - c.ini)) : 0;
    seg.firstChild.style.width = `${cheio * 100}%`;
  });
};

// Divide a fala em blocos de até 3 palavras (quebra na pontuação); "…" é pausa proposital.
// A duração de cada bloco é proporcional ao tamanho das palavras. *palavra* = ênfase.
function blocosDaFala(fala) {
  const blocos = []; let atual = [];
  const fecha = () => { if (atual.length) { blocos.push(atual); atual = []; } };
  for (const tok of fala.split(' ')) {
    if (tok === '…') { fecha(); blocos.push(null); continue; }
    atual.push(tok);
    const limpo = tok.replace(/\*/g, '');
    const letras = atual.reduce((n, w) => n + w.replace(/\*/g, '').length, 0);
    if (/[.,:!?]$/.test(limpo) || atual.length >= 3 || letras >= 15) fecha();
  }
  fecha();
  return blocos;
}
const peso = (w) => 0.7 + w.replace(/[^\p{L}\d]/gu, '').length / 5;
function blocoNoTempo(c, tc) {
  const blocos = blocosDaFala(c.fala);
  const pesos = blocos.map((b) => (b ? b.reduce((n, w) => n + peso(w), 0) : 2.2));
  const total = pesos.reduce((a, b) => a + b, 0);
  const util = c.fim - c.ini - 0.1;
  const html = (b) => b.map((w) => (w.includes('*') ? `<em>${w.replace(/\*/g, '')}</em>` : w)).join(' ');
  let acum = 0.03; let ultimo = '';
  for (let i = 0; i < blocos.length; i++) {
    const dur = (pesos[i] / total) * util;
    if (tc < acum + dur) return blocos[i] ? { texto: html(blocos[i]), desde: tc - acum } : { texto: ultimo, desde: 1 };
    if (blocos[i]) ultimo = html(blocos[i]);
    acum += dur;
  }
  return { texto: ultimo, desde: 1 };
}

window.modoFundo = (ativo) => document.body.classList.toggle('modo-fundo', ativo);
// Só o gancho fixo do alto (muda por versão): o render sobrepõe essa imagem ao corpo, que é igual em todas.
window.modoTopo = (ativo) => document.body.classList.toggle('modo-topo', ativo);
window.DURACAO = DURACAO;
window.DURACAO_GANCHO = DURACAO_GANCHO;
window.VERSOES = GANCHOS.length;

document.fonts.ready.then(() => {
  // Foto da planta humanizada para o cartão final (renderizada uma vez)
  casa.aplicar({ desenho: 1, paredes: 1, vida: 1 });
  casa.enquadrar({ theta: 0, inclinacao: 0.02, distancia: 21, alvo: [0, 0], aspecto: ASPECTO });
  casa.render();
  imagemHumanizada = canvas.toDataURL('image/jpeg', 0.9);
  window.renderAt(0);
  window.pronto = true;
});

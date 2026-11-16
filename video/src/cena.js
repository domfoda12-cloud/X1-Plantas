// Desenha cada quadro do vídeo a partir do tempo t (em segundos).
// O render.cjs chama window.renderAt(t) quadro a quadro e tira uma captura de tela.
import * as THREE from '../node_modules/three/build/three.module.js';
import { ambientes, paredes, janelas, LARGURA, PROFUNDIDADE, PE_DIREITO, ESPESSURA } from './planta.js';

// ---------------------------------------------------------------------------
// Roteiro, pensado para retenção (tempo assistido), como no reel de referência:
//   Gancho (0 a 3 s): faz uma pergunta e a casa já aparece subindo em 3D.
//   Desenvolvimento (3 a 27 s): seis erros, 4 s cada, do mais geral ao mais específico.
//   Desfecho (27 a 34 s): responde a pergunta do gancho, com a casa girando em 3D.
//   Chamada (34 a 38 s): comentar PLANTA para receber o material.
// O corpo é igual em todas as versões; só o gancho muda (5 versões para os reels de teste).
// ---------------------------------------------------------------------------
const INFO = '55 m² · 2 quartos · 1 banho';
export const GANCHOS = [
  { titulo: 'Qual é o erro mais caro<br>na planta de uma casa?', fala: 'fica até o final' },
  { titulo: '7 erros na planta<br>(o último é o pior)', fala: 'veja antes de construir' },
  { titulo: 'Antes de construir,<br>confira esses 7 pontos', fala: 'o último quase ninguém faz' },
  { titulo: 'O erro de planta<br>que ninguém te conta', fala: 'e mais seis no caminho' },
  { titulo: 'Construir sem esse<br>cuidado sai caro', fala: 'você vai ver no final' },
];
const versao = clampVersao(Number(new URLSearchParams(location.search).get('v') || 1));
function clampVersao(v) { return Number.isInteger(v) && v >= 1 && v <= GANCHOS.length ? v : 1; }
export const DURACAO_GANCHO = 3;

export const cenas = [
  { ini: 0, fim: 3, tipo: '3d-gancho', rotulo: 'Casa Compacta', info: INFO, ...GANCHOS[versao - 1] },
  { ini: 3, fim: 7, tipo: 'sol', rotulo: 'Posição do sol', info: 'Casa Compacta',
    titulo: '1. Ignorar o sol', fala: 'quarto com sol da manhã' },
  { ini: 7, fim: 11, tipo: 'corredor', rotulo: 'Circulação', info: 'Casa Compacta',
    titulo: '2. Corredor comprido', fala: 'corredor também custa por metro' },
  { ini: 11, fim: 15, tipo: 'banho-porta', rotulo: 'Privacidade', info: 'Casa Compacta',
    titulo: '3. Banheiro de frente pra sala', fala: 'a porta abre para o hall' },
  { ini: 15, fim: 19, tipo: 'banho-janela', rotulo: 'Ventilação', info: 'Casa Compacta',
    titulo: '4. Banheiro sem janela', fala: 'ventilação natural evita mofo' },
  { ini: 19, fim: 23, tipo: 'recuos', rotulo: 'Terreno e recuos', info: 'Lote 10 x 20 m',
    titulo: '5. Esquecer os recuos', fala: 'o terreno manda na planta' },
  { ini: 23, fim: 27, tipo: 'ampliacao', rotulo: 'Ampliação', info: 'Casa Compacta',
    titulo: '6. Não prever ampliação', fala: 'pense na casa daqui a cinco anos' },
  { ini: 27, fim: 34, tipo: '3d-orbita', rotulo: 'A resposta', info: INFO,
    titulo: '7. O mais caro:<br>não ver a casa em 3D', fala: 'veja cada cômodo antes do primeiro tijolo' },
  { ini: 34, fim: 38, tipo: 'cta', rotulo: 'Material gratuito', info: 'pelo WhatsApp',
    titulo: 'Comente PLANTA', fala: 'e receba a planta grátis' },
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

// Divide as paredes em trechos cheios e trechos de janela (peitoril e verga).
function trechosDeParede() {
  const trechos = [];
  for (const [x0, y0, x1, y1] of paredes) {
    const horizontal = y0 === y1;
    const ini = horizontal ? Math.min(x0, x1) : Math.min(y0, y1);
    const fim = horizontal ? Math.max(x0, x1) : Math.max(y0, y1);
    const fixo = horizontal ? y0 : x0;
    const nessa = janelas
      .map((j) => ({ ...j, h: j.seg[1] === j.seg[3] }))
      .filter((j) => j.h === horizontal && (horizontal ? j.seg[1] : j.seg[0]) === fixo)
      .map((j) => ({ ...j, a: horizontal ? j.seg[0] : j.seg[1], b: horizontal ? j.seg[2] : j.seg[3] }))
      .filter((j) => j.a >= ini && j.b <= fim)
      .sort((p, q) => p.a - q.a);
    let cursor = ini;
    const ponto = (s) => (horizontal ? [s, fixo] : [fixo, s]);
    const add = (a, b, z0, z1, janela) => {
      if (b - a < 0.01) return;
      const [ax, ay] = ponto(a); const [bx, by] = ponto(b);
      trechos.push({ x0: ax, y0: ay, x1: bx, y1: by, z0, z1, janela });
    };
    for (const j of nessa) {
      add(cursor, j.a, 0, PE_DIREITO, false);
      add(j.a, j.b, 0, j.peitoril, true);
      add(j.a, j.b, j.verga, PE_DIREITO, true);
      cursor = j.b;
    }
    add(cursor, fim, 0, PE_DIREITO, false);
  }
  return trechos;
}

// ---------------------------------------------------------------------------
// Planta 2D em SVG
// ---------------------------------------------------------------------------
function svgPlanta({ ox, oy, s, destaque = [], nomes = true, opacidade = 1 }) {
  const X = (x) => ox + x * s; const Y = (y) => oy + y * s;
  let out = `<g opacity="${opacidade}">`;
  for (const a of ambientes) {
    const d = destaque.includes(a.id);
    out += `<rect x="${X(a.x0)}" y="${Y(a.y0)}" width="${(a.x1 - a.x0) * s}" height="${(a.y1 - a.y0) * s}"
      fill="${a.cor}" ${d ? 'stroke="#C2683F" stroke-width="5"' : ''}/>`;
  }
  for (const [x0, y0, x1, y1] of paredes) {
    out += `<line x1="${X(x0)}" y1="${Y(y0)}" x2="${X(x1)}" y2="${Y(y1)}" stroke="#3A332B"
      stroke-width="${ESPESSURA * s}" stroke-linecap="square"/>`;
  }
  for (const j of janelas) {
    const [x0, y0, x1, y1] = j.seg; const h = y0 === y1; const e = (ESPESSURA * s) / 2;
    out += `<line x1="${X(x0)}" y1="${Y(y0)}" x2="${X(x1)}" y2="${Y(y1)}" stroke="#FFFFFF" stroke-width="${ESPESSURA * s}"/>`;
    for (const k of [-e, e]) {
      out += h
        ? `<line x1="${X(x0)}" y1="${Y(y0) + k}" x2="${X(x1)}" y2="${Y(y1) + k}" stroke="#3A332B" stroke-width="2"/>`
        : `<line x1="${X(x0) + k}" y1="${Y(y0)}" x2="${X(x1) + k}" y2="${Y(y1)}" stroke="#3A332B" stroke-width="2"/>`;
    }
  }
  if (nomes) {
    for (const a of ambientes) {
      const cx = X((a.x0 + a.x1) / 2); const cy = Y((a.y0 + a.y1) / 2);
      const pequeno = a.id === 'hall' || a.id === 'banho';
      out += `<text x="${cx}" y="${cy - 2}" text-anchor="middle" font-size="${pequeno ? 17 : 22}" font-weight="700" fill="#2B2620">${a.nome}</text>`;
      out += `<text x="${cx}" y="${cy + (pequeno ? 18 : 24)}" text-anchor="middle" font-size="${pequeno ? 15 : 18}" fill="#6B5B45">${m2(areaDe(a))}</text>`;
    }
  }
  return out + '</g>';
}

function seta(x1, y1, x2, y2, p, cor = '#C2683F') {
  const x = lerp(x1, x2, p); const y = lerp(y1, y2, p);
  const ang = Math.atan2(y2 - y1, x2 - x1); const t = 18;
  const pa = `${x},${y} ${x - t * Math.cos(ang - 0.45)},${y - t * Math.sin(ang - 0.45)} ${x - t * Math.cos(ang + 0.45)},${y - t * Math.sin(ang + 0.45)}`;
  return p <= 0.02 ? '' : `<line x1="${x1}" y1="${y1}" x2="${x}" y2="${y}" stroke="${cor}" stroke-width="6" stroke-linecap="round"/>
    <polygon points="${pa}" fill="${cor}"/>`;
}

function texto(x, y, linhas, { tam = 30, peso = 600, cor = '#2B2620', op = 1 } = {}) {
  return linhas.map((l, i) => `<text x="${x}" y="${y + i * tam * 1.3}" font-size="${tam}" font-weight="${peso}" fill="${cor}" opacity="${op}">${l}</text>`).join('');
}

// Cada tipo de cartão 2D recebe o progresso local (segundos desde o início da cena).
const cartoes2D = {
  sol(tc) {
    const s = 58; const ox = 60; const oy = 28;
    const p = saida((tc - 0.4) / 1.0);
    const sx = 760; const sy = 120; const r = 46;
    let raios = '';
    for (let i = 0; i < 12; i++) {
      const a = (i / 12) * Math.PI * 2 + tc * 0.4;
      raios += `<line x1="${sx + Math.cos(a) * (r + 10)}" y1="${sy + Math.sin(a) * (r + 10)}" x2="${sx + Math.cos(a) * (r + 28)}" y2="${sy + Math.sin(a) * (r + 28)}" stroke="#E0A33A" stroke-width="6" stroke-linecap="round"/>`;
    }
    const q2 = amb('quarto2');
    return svgPlanta({ ox, oy, s, destaque: p > 0.5 ? ['quarto2'] : [] }) +
      `<circle cx="${sx}" cy="${sy}" r="${r}" fill="#F2C14E"/>${raios}` +
      seta(sx - 70, sy + 40, ox + ((q2.x0 + q2.x1) / 2) * s + 40, oy + ((q2.y0 + q2.y1) / 2) * s - 30, p) +
      texto(570, 340, ['Nascente (leste)'], { tam: 32, peso: 700, op: p }) +
      texto(570, 390, ['Sol da manhã nos', 'quartos: ambiente', 'mais fresco à tarde.'], { tam: 27, peso: 500, cor: '#6B5B45', op: p });
  },
  corredor(tc) {
    const s = 58; const ox = 60; const oy = 28;
    const p = saida((tc - 0.4) / 1.0);
    const hall = amb('hall');
    const barra = (y, rot, larg, cor) => `<text x="520" y="${y}" font-size="25" font-weight="600" fill="#6B5B45">${rot}</text>
      <rect x="520" y="${y + 14}" width="${larg * p}" height="34" rx="8" fill="${cor}"/>`;
    return svgPlanta({ ox, oy, s, destaque: p > 0.3 ? ['hall'] : [] }) +
      texto(520, 110, [`Hall: ${m2(areaDe(hall))}`], { tam: 40, peso: 800, cor: '#C2683F', op: p }) +
      texto(520, 160, ['Circulação curta,', 'mais área para', 'os ambientes.'], { tam: 27, peso: 500, cor: '#6B5B45', op: p }) +
      barra(330, 'Corredor comprido', 320, '#D9B9A5') +
      barra(420, 'Hall compacto', 110, '#5E7350');
  },
  'banho-porta'(tc) {
    const s = 58; const ox = 60; const oy = 28;
    const p = saida((tc - 0.4) / 1.0);
    const X = (x) => ox + x * s; const Y = (y) => oy + y * s;
    // Arco da porta do banheiro (abre para o hall)
    const porta = `<path d="M ${X(4.6)} ${Y(4.5)} A ${0.8 * s} ${0.8 * s} 0 0 0 ${X(3.8)} ${Y(5.3)} L ${X(4.6)} ${Y(5.3)}" fill="none" stroke="#C2683F" stroke-width="3" stroke-dasharray="6 5" opacity="${p}"/>`;
    return svgPlanta({ ox, oy, s, destaque: p > 0.3 ? ['banho', 'hall'] : [] }) + porta +
      texto(510, 140, ['✓ Abre para o hall'], { tam: 32, peso: 700, cor: '#5E7350', op: p }) +
      texto(510, 190, ['Quem está na sala', 'não vê a porta', 'do banheiro.'], { tam: 27, peso: 500, cor: '#6B5B45', op: p }) +
      texto(510, 400, ['✗ De frente', 'para a sala'], { tam: 30, peso: 700, cor: '#C2683F', op: saida((tc - 1.4) / 0.8) });
  },
  'banho-janela'(tc) {
    const s = 58; const ox = 60; const oy = 28;
    const p = saida((tc - 0.4) / 1.0);
    const X = (x) => ox + x * s; const Y = (y) => oy + y * s;
    let ar = '';
    for (let i = 0; i < 3; i++) {
      const fase = ((tc * 0.8 + i / 3) % 1);
      const x = X(6.5) + 10 + fase * 70; const y = Y(4.8 + i * 0.22);
      ar += `<path d="M ${x} ${y} q 12 -10 24 0 t 24 0" fill="none" stroke="#7FA7B5" stroke-width="5" stroke-linecap="round" opacity="${p * (1 - fase)}"/>`;
    }
    return svgPlanta({ ox, oy, s, destaque: p > 0.3 ? ['banho'] : [] }) + ar +
      texto(560, 140, ['Janela alta'], { tam: 34, peso: 800, cor: '#C2683F', op: p }) +
      texto(560, 185, ['peitoril de 1,6 m'], { tam: 27, peso: 600, cor: '#6B5B45', op: p }) +
      texto(560, 300, ['Ventilação natural', 'evita mofo e', 'cheiro parado.'], { tam: 27, peso: 500, cor: '#6B5B45', op: p });
  },
  recuos(tc) {
    const s = 25; const ox = 70; const oy = 30; // lote 10 x 20 m
    const p = saida((tc - 0.3) / 1.0);
    const X = (x) => ox + x * s; const Y = (y) => oy + y * s;
    // Casa no lote: 1,5 m da divisa esquerda e 4 m da frente (valores de exemplo)
    const cx = 1.5; const cy = 4;
    let out = `<rect x="${X(0)}" y="${Y(0)}" width="${10 * s}" height="${20 * s}" fill="#DCE4CF" stroke="#5E7350" stroke-width="4"/>`;
    out += `<rect x="${X(cx)}" y="${Y(cy)}" width="${LARGURA * s}" height="${PROFUNDIDADE * s}" fill="#E8D7BC" stroke="#3A332B" stroke-width="4"/>`;
    out += `<text x="${X(cx + LARGURA / 2)}" y="${Y(cy + PROFUNDIDADE / 2) + 8}" text-anchor="middle" font-size="22" font-weight="700" fill="#2B2620">Casa</text>`;
    out += `<line x1="${X(0)}" y1="${Y(cy)}" x2="${X(10)}" y2="${Y(cy)}" stroke="#C2683F" stroke-width="3" stroke-dasharray="10 8" opacity="${p}"/>`;
    out += `<line x1="${X(cx)}" y1="${Y(0)}" x2="${X(cx)}" y2="${Y(20)}" stroke="#C2683F" stroke-width="3" stroke-dasharray="10 8" opacity="${p}"/>`;
    out += `<text x="${X(5)}" y="${Y(cy / 2) + 8}" text-anchor="middle" font-size="20" font-weight="700" fill="#C2683F" opacity="${p}">recuo frontal</text>`;
    out += `<text x="${X(5)}" y="${Y(0) - 8}" text-anchor="middle" font-size="18" fill="#6B5B45">rua</text>`;
    return out +
      texto(400, 110, ['Lote 10 x 20 m'], { tam: 34, peso: 800, cor: '#2B2620' }) +
      texto(400, 165, ['A casa precisa caber', 'dentro dos recuos,', 'não só no terreno.'], { tam: 27, peso: 500, cor: '#6B5B45', op: p }) +
      texto(400, 380, ['Os recuos mudam', 'de cidade para cidade:', 'confira na prefeitura.'], { tam: 25, peso: 700, cor: '#C2683F', op: saida((tc - 1.2) / 0.8) });
  },
  ampliacao(tc) {
    const s = 52; const ox = 40; const oy = 40;
    const p = saida((tc - 0.5) / 1.0);
    const X = (x) => ox + x * s; const Y = (y) => oy + y * s;
    const ext = `<rect x="${X(6.5)}" y="${Y(5.8)}" width="${2.8 * s}" height="${2.7 * s}" fill="#F3E5DB" fill-opacity="${p}"
      stroke="#C2683F" stroke-width="4" stroke-dasharray="12 8" opacity="${p}"/>
      <text x="${X(7.9)}" y="${Y(7.05)}" text-anchor="middle" font-size="20" font-weight="700" fill="#C2683F" opacity="${p}">Quarto 3</text>
      <text x="${X(7.9)}" y="${Y(7.05) + 24}" text-anchor="middle" font-size="17" fill="#C2683F" opacity="${p}">(futuro)</text>`;
    return svgPlanta({ ox, oy, s }) + ext +
      texto(560, 110, ['Pronta para', 'crescer'], { tam: 36, peso: 800, cor: '#2B2620' }) +
      texto(560, 220, ['Deixe previsto', 'por onde a casa', 'vai aumentar.'], { tam: 27, peso: 500, cor: '#6B5B45', op: p });
  },
  cta(tc) {
    const p = saida((tc - 0.2) / 0.8);
    const q = saida((tc - 0.9) / 0.6);
    // Página do material gratuito, levemente inclinada
    let out = `<g transform="translate(110 40) rotate(-4 160 230)" opacity="${p}">
      <rect x="0" y="0" width="330" height="460" rx="10" fill="#FBF8F2" stroke="#E2D6C4" stroke-width="3"/>
      <rect x="0" y="0" width="330" height="70" rx="10" fill="#5E7350"/>
      <text x="24" y="45" font-size="26" font-weight="800" fill="#FFFFFF">Casa Compacta</text>
      ${svgPlanta({ ox: 70, oy: 100, s: 28, nomes: false })}
      <text x="24" y="370" font-size="20" font-weight="700" fill="#2B2620">Planta baixa + guia</text>
      <text x="24" y="400" font-size="18" fill="#6B5B45">Como ler a planta e o que</text>
      <text x="24" y="425" font-size="18" fill="#6B5B45">checar antes de construir</text>
    </g>`;
    out += `<g opacity="${q}" transform="translate(520 170)">
      <text x="0" y="0" font-size="34" font-weight="700" fill="#2B2620">Comente</text>
      <rect x="0" y="22" width="300" height="96" rx="48" fill="#C2683F"/>
      <text x="150" y="88" text-anchor="middle" font-size="46" font-weight="800" fill="#FFFFFF">PLANTA</text>
      <text x="0" y="180" font-size="26" font-weight="500" fill="#6B5B45">e receba grátis</text>
      <text x="0" y="214" font-size="26" font-weight="500" fill="#6B5B45">no WhatsApp</text>
    </g>`;
    return out;
  },
};

// ---------------------------------------------------------------------------
// Cena 3D
// ---------------------------------------------------------------------------
const canvas = document.getElementById('tres');
const renderer = new THREE.WebGLRenderer({ canvas, antialias: true, preserveDrawingBuffer: true });
renderer.setPixelRatio(1);
renderer.setSize(900, 560, false);
renderer.shadowMap.enabled = true;
renderer.shadowMap.type = THREE.PCFSoftShadowMap;
renderer.outputColorSpace = THREE.SRGBColorSpace;

const cena3d = new THREE.Scene();
cena3d.background = new THREE.Color('#F4EFE6');
const camera = new THREE.PerspectiveCamera(38, 900 / 560, 0.1, 200);
const centro = new THREE.Vector3(LARGURA / 2, 0, PROFUNDIDADE / 2);
// No 3D o eixo x é espelhado, para a casa vista da rua bater com as plantas 2D (frente no alto).
const mx = (x) => LARGURA - x;

cena3d.add(new THREE.HemisphereLight('#FFFFFF', '#D8D2C6', 1.25));
const sol = new THREE.DirectionalLight('#FFF0DC', 2.1);
sol.position.set(-8, 14, -10);
sol.target.position.copy(centro);
sol.castShadow = true;
sol.shadow.mapSize.set(2048, 2048);
Object.assign(sol.shadow.camera, { left: -10, right: 10, top: 10, bottom: -10, near: 1, far: 40 });
sol.shadow.bias = -0.0005;
cena3d.add(sol, sol.target);

// Terreno: gramado e lote
const chao = new THREE.Mesh(new THREE.PlaneGeometry(60, 60), new THREE.MeshStandardMaterial({ color: '#A9BC8C', roughness: 1 }));
chao.rotation.x = -Math.PI / 2; chao.position.y = -0.02; chao.receiveShadow = true;
cena3d.add(chao);
const calcada = new THREE.Mesh(new THREE.PlaneGeometry(10, 4), new THREE.MeshStandardMaterial({ color: '#DDD6C8', roughness: 1 }));
calcada.rotation.x = -Math.PI / 2; calcada.position.set(LARGURA / 2 + 0.25, -0.01, -2.2); calcada.receiveShadow = true;
cena3d.add(calcada);

// Pisos e nomes dos ambientes
const rotulos = [];
for (const a of ambientes) {
  const w = a.x1 - a.x0; const d = a.y1 - a.y0;
  const piso = new THREE.Mesh(new THREE.BoxGeometry(w, 0.06, d), new THREE.MeshStandardMaterial({ color: a.cor, roughness: 0.9 }));
  piso.position.set(mx(a.x0 + w / 2), 0.03, a.y0 + d / 2); piso.receiveShadow = true;
  cena3d.add(piso);
  if (a.id === 'hall') continue;
  const c = document.createElement('canvas'); c.width = 512; c.height = 200;
  const g = c.getContext('2d');
  g.fillStyle = '#2B2620'; g.font = '700 74px Inter, sans-serif'; g.textAlign = 'center';
  g.fillText(a.nome, 256, 92);
  g.fillStyle = '#6B5B45'; g.font = '500 54px Inter, sans-serif';
  g.fillText(m2(areaDe(a)), 256, 160);
  const tex = new THREE.CanvasTexture(c); tex.colorSpace = THREE.SRGBColorSpace; tex.anisotropy = 8;
  const larg = Math.min(w * 0.9, 2.5);
  const r = new THREE.Mesh(new THREE.PlaneGeometry(larg, larg * 200 / 512), new THREE.MeshBasicMaterial({ map: tex, transparent: true, depthWrite: false }));
  r.rotation.set(-Math.PI / 2, 0, Math.PI); r.position.set(mx(a.x0 + w / 2), 0.07, a.y0 + d / 2 + 0.15);
  cena3d.add(r); rotulos.push(r);
}

// Paredes: cada trecho é um grupo com altura 1, escalado conforme a "subida" da parede.
const matParede = new THREE.MeshStandardMaterial({ color: '#FFFFFF', roughness: 0.9 });
const matJanela = new THREE.MeshStandardMaterial({ color: '#F3EEE6', roughness: 0.9 });
const matAresta = new THREE.LineBasicMaterial({ color: '#6E6354' });
const grupos = trechosDeParede().map((tr, i) => {
  const comp = Math.hypot(tr.x1 - tr.x0, tr.y1 - tr.y0) + (tr.janela ? 0 : ESPESSURA);
  const horizontal = tr.y0 === tr.y1;
  const geo = new THREE.BoxGeometry(horizontal ? comp : ESPESSURA, 1, horizontal ? ESPESSURA : comp);
  const g = new THREE.Group();
  const m = new THREE.Mesh(geo, tr.janela ? matJanela : matParede); m.castShadow = true; m.receiveShadow = true;
  g.add(m, new THREE.LineSegments(new THREE.EdgesGeometry(geo), matAresta));
  g.position.set(mx((tr.x0 + tr.x1) / 2), 0, (tr.y0 + tr.y1) / 2);
  cena3d.add(g);
  return { g, tr, atraso: (i % 8) * 0.12 };
});

// Vidros das janelas
for (const j of janelas) {
  const [x0, y0, x1, y1] = j.seg; const horizontal = y0 === y1;
  const comp = Math.hypot(x1 - x0, y1 - y0); const alt = j.verga - j.peitoril;
  const vidro = new THREE.Mesh(new THREE.BoxGeometry(horizontal ? comp : 0.03, alt, horizontal ? 0.03 : comp),
    new THREE.MeshStandardMaterial({ color: '#9CC3D0', roughness: 0.2, metalness: 0.1, transparent: true, opacity: 0.55 }));
  vidro.position.set(mx((x0 + x1) / 2), j.peitoril + alt / 2, (y0 + y1) / 2);
  vidro.userData.janela = j; cena3d.add(vidro);
  grupos.push({ vidro, atraso: 0.9 });
}

// Móveis simples, para dar escala
const movel = (w, h, d, x, y, cor, z0 = 0) => {
  const m = new THREE.Mesh(new THREE.BoxGeometry(w, h, d), new THREE.MeshStandardMaterial({ color: cor, roughness: 0.8 }));
  m.position.set(mx(x), z0 + h / 2 + 0.06, y); m.castShadow = true; m.receiveShadow = true;
  m.userData.base = { h, z0 }; cena3d.add(m); return m;
};
const moveis = [
  movel(2.1, 0.75, 0.85, 1.6, 3.55, '#C2683F'), // sofá
  movel(1.6, 0.5, 0.4, 1.6, 0.35, '#7A5C3E'), // rack
  movel(0.6, 0.9, 2.6, 6.1, 1.6, '#9C7A55'), // bancada
  movel(1.2, 0.75, 0.8, 4.6, 2.6, '#B08B62'), // mesa
  movel(1.45, 0.5, 1.95, 1.6, 7.35, '#EEE7DB'), // cama de casal
  movel(1.45, 1.0, 0.1, 1.6, 8.36, '#7A5C3E'), // cabeceira
  movel(0.95, 0.5, 1.95, 5.75, 7.4, '#EEE7DB'), // cama de solteiro
  movel(0.5, 0.45, 0.65, 6.1, 5.3, '#FFFFFF'), // vaso
  movel(0.6, 0.85, 0.45, 5.2, 4.45, '#FFFFFF'), // pia
];

function posicionar3D(subida, mov, theta, raio, altura) {
  const topo = PE_DIREITO * 1.0;
  for (const it of grupos) {
    const v = suave((subida - it.atraso) / 1.4);
    if (it.vidro) { it.vidro.visible = v > 0.98; continue; }
    const { g, tr } = it;
    const limite = topo * v;
    const vis = Math.max(0, Math.min(tr.z1, limite) - tr.z0);
    g.visible = vis > 0.005;
    g.scale.y = Math.max(vis, 0.0001);
    g.position.y = tr.z0 + vis / 2;
  }
  moveis.forEach((m, i) => {
    const v = saida((mov - i * 0.08) / 0.5);
    m.visible = v > 0.01; m.scale.set(1, Math.max(v, 0.001), 1);
    m.position.y = m.userData.base.z0 + 0.06 + (m.userData.base.h * v) / 2;
  });
  camera.position.set(centro.x + raio * Math.sin(theta), altura, centro.z - raio * Math.cos(theta));
  camera.lookAt(centro);
  renderer.render(cena3d, camera);
}

const cenas3D = {
  '3d-gancho'(tc) {
    // Gancho: a casa sobe rápido já no primeiro segundo, para prender o olhar.
    const k = clamp(tc / 3);
    posicionar3D(tc * 1.6 - 0.1, tc * 1.6 - 2.2, lerp(-0.6, 0.05, suave(k)), lerp(9.5, 8, saida(k)), lerp(16, 13.5, saida(k)));
  },
  '3d-crescer'(tc) {
    // Paredes sobem de 0,3 s a ~2,6 s; móveis aparecem depois; câmera gira devagar.
    const k = clamp(tc / 5.5);
    posicionar3D(tc - 0.3, tc - 2.6, lerp(-0.7, 0.15, suave(k)), lerp(10, 8, saida(k)), lerp(17, 13.5, saida(k)));
  },
  '3d-orbita'(tc) {
    const k = clamp(tc / 6);
    posicionar3D(99, 99, lerp(0.35, 1.9, suave(k)), 9.5, lerp(14, 12.5, k));
  },
};

// ---------------------------------------------------------------------------
// Quadro
// ---------------------------------------------------------------------------
const el = (id) => document.getElementById(id);
const dom = {
  abertura: el('abertura'), cartao: el('cartao'), rotT: el('rotulo-titulo'), rotI: el('rotulo-info'),
  desenho: el('desenho'), tres: el('tres'), legT: el('leg-titulo'), legP: el('leg-palavra'),
};

window.renderAt = (t) => {
  const c = cenas.find((x) => t >= x.ini && t < x.fim) || cenas[cenas.length - 1];
  const tc = t - c.ini;
  const entrada = saida(tc / 0.25);

  // Abertura
  dom.abertura.innerHTML = c.abertura || '';
  dom.abertura.style.opacity = c.tipo === 'abertura' ? entrada : 0;

  // Cartão
  const temCartao = c.tipo !== 'abertura';
  dom.cartao.style.opacity = temCartao ? entrada : 0;
  dom.cartao.style.transform = `scale(${0.94 + 0.06 * entrada})`;
  if (temCartao) {
    dom.rotT.textContent = c.rotulo; dom.rotI.textContent = c.info;
    const e3d = c.tipo.startsWith('3d');
    dom.tres.style.display = e3d ? 'block' : 'none';
    dom.desenho.style.display = e3d ? 'none' : 'block';
    if (e3d) cenas3D[c.tipo](tc);
    else dom.desenho.innerHTML = `<svg viewBox="0 0 900 560" xmlns="http://www.w3.org/2000/svg" font-family="Inter, sans-serif">${cartoes2D[c.tipo](tc)}</svg>`;
  }

  // Legenda: título do item e uma palavra por vez, como na referência
  dom.legT.innerHTML = c.titulo;
  const palavras = c.fala.split(' ');
  const passo = (c.fim - c.ini - 0.3) / palavras.length;
  dom.legP.textContent = palavras[clamp(Math.floor((tc - 0.15) / passo), 0, palavras.length - 1)];
};

window.modoFundo = (ativo) => document.body.classList.toggle('modo-fundo', ativo);
window.DURACAO = DURACAO;
window.DURACAO_GANCHO = DURACAO_GANCHO;
window.VERSOES = GANCHOS.length;
document.fonts.ready.then(() => { window.renderAt(0); window.pronto = true; });

// Casa em 3D a partir dos dados de uma planta (src/plantas/<ID>.js), em três estágios:
//   1. Blueprint: fundo azul quadriculado, paredes, portas, móveis e cotas desenhados em branco.
//   2. Ganhando vida: paredes sobem, pisos de madeira/porcelanato aparecem cômodo por cômodo,
//      móveis surgem e o jardim cresce em volta.
//   3. Planta humanizada: paredes cortadas a ~1,1 m, vista de cima, sombras suaves.
//
// Coordenadas: x do mundo = x da planta; z do mundo = y da planta (0 = frente). Com a câmera
// do lado dos fundos (+z) olhando para a frente, a imagem fica igual à planta 2D (frente no alto).
import * as THREE from '../node_modules/three/build/three.module.js';
import { RoundedBoxGeometry } from '../node_modules/three/examples/jsm/geometries/RoundedBoxGeometry.js';
// Qual planta: ?planta=C01 carrega ./plantas/C01.js (gerado por ferramentas/planta3d.py); sem parâmetro, a C01.
const ID_PLANTA = new URLSearchParams(globalThis.location ? location.search : '').get('planta');
const DADOS = await import(`./plantas/${ID_PLANTA || 'C01'}.js`);
const { ambientes, paredes, janelas, portas, LARGURA, PROFUNDIDADE, ESPESSURA } = DADOS;
const META = DADOS.META || { nome: 'Casa Compacta', area: 55, quartos: '2 quartos', banheiros: 1 };
const FUTUROS = DADOS.futuros || [];

const clamp = (v, a = 0, b = 1) => Math.min(b, Math.max(a, v));
const suave = (v) => { v = clamp(v); return v * v * (3 - 2 * v); };
const saida = (v) => 1 - Math.pow(1 - clamp(v), 3);
const volta = (v) => { v = clamp(v); const c = 1.6; return 1 + (c + 1) * Math.pow(v - 1, 3) + c * Math.pow(v - 1, 2); }; // ease-out-back
const lerp = (a, b, v) => a + (b - a) * v;
const m2 = (a) => a.toFixed(1).replace('.', ',') + ' m²';

// Números aleatórios com semente: o mesmo quadro sai igual em todo render.
function aleatorio(semente) {
  let s = semente >>> 0;
  return () => { s = (s + 0x6D2B79F5) >>> 0; let t = s; t = Math.imul(t ^ (t >>> 15), t | 1); t ^= t + Math.imul(t ^ (t >>> 7), t | 61); return ((t ^ (t >>> 14)) >>> 0) / 4294967296; };
}

export const CORES = {
  azul: '#0B4FA8', azulEscuro: '#083B80', grade: 'rgba(255,255,255,0.10)', gradeForte: 'rgba(255,255,255,0.22)',
  branco: '#FFFFFF', azulParede: '#5C93E6', destaque: '#FFC857',
};

// ---------------------------------------------------------------------------
// Paredes divididas em trechos (cheios e janelas)
// ---------------------------------------------------------------------------
function trechos() {
  const out = [];
  for (const [x0, y0, x1, y1] of paredes) {
    const h = y0 === y1;
    const ini = h ? Math.min(x0, x1) : Math.min(y0, y1);
    const fim = h ? Math.max(x0, x1) : Math.max(y0, y1);
    const fixo = h ? y0 : x0;
    const js = janelas
      .filter((j) => (j.seg[1] === j.seg[3]) === h && (h ? j.seg[1] : j.seg[0]) === fixo)
      .map((j) => ({ ...j, a: h ? j.seg[0] : j.seg[1], b: h ? j.seg[2] : j.seg[3] }))
      .filter((j) => j.a >= ini && j.b <= fim)
      .sort((p, q) => p.a - q.a);
    const pt = (s) => (h ? [s, fixo] : [fixo, s]);
    let c = ini;
    const add = (a, b, janela) => {
      if (b - a < 0.01) return;
      const [ax, ay] = pt(a); const [bx, by] = pt(b);
      out.push({ x0: ax, y0: ay, x1: bx, y1: by, h, janela });
    };
    for (const j of js) { add(c, j.a, null); add(j.a, j.b, j); c = j.b; }
    add(c, fim, null);
  }
  return out;
}
const TRECHOS = trechos();

// ---------------------------------------------------------------------------
// Móveis: posição em metros da planta, rotação em radianos (0 = frente do móvel para +z)
// ---------------------------------------------------------------------------
const MOVEIS = DADOS.MOVEIS || [
  // Sala
  { tipo: 'tapete', amb: 'sala', x: 1.45, y: 2.2, w: 2.0, d: 2.5, cor: '#D9CBB4', borda: '#B49D7C' },
  { tipo: 'sofa', amb: 'sala', x: 2.78, y: 2.2, rot: -Math.PI / 2, w: 2.1, d: 0.88, cor: '#8A9A86' },
  { tipo: 'rack', amb: 'sala', x: 0.3, y: 2.2, rot: Math.PI / 2, w: 1.7, d: 0.4 },
  { tipo: 'mesaCentro', amb: 'sala', x: 1.55, y: 2.2, w: 0.6, d: 1.0 },
  { tipo: 'planta', amb: 'sala', x: 0.45, y: 0.5, s: 1.0 },
  { tipo: 'planta', amb: 'sala', x: 3.15, y: 3.85, s: 0.8 },
  // Cozinha
  { tipo: 'bancada', amb: 'cozinha', x: 6.12, y: 1.75, rot: -Math.PI / 2, w: 3.0, d: 0.62 },
  { tipo: 'geladeira', amb: 'cozinha', x: 6.07, y: 3.72, rot: -Math.PI / 2, w: 0.72, d: 0.7 },
  { tipo: 'mesaJantar', amb: 'cozinha', x: 4.55, y: 2.35, w: 0.85, d: 1.3 },
  { tipo: 'planta', amb: 'cozinha', x: 3.85, y: 0.5, s: 0.8 },
  // Quarto 1
  { tipo: 'tapete', amb: 'quarto1', x: 1.6, y: 7.1, w: 2.3, d: 1.7, cor: '#E4D6C3', borda: '#C9B59A' },
  { tipo: 'camaCasal', amb: 'quarto1', x: 1.6, y: 7.42, rot: Math.PI, w: 1.6, d: 2.0, manta: '#B9C7D6' },
  { tipo: 'criado', amb: 'quarto1', x: 0.5, y: 8.17 },
  { tipo: 'criado', amb: 'quarto1', x: 2.7, y: 8.17 },
  { tipo: 'armario', amb: 'quarto1', x: 1.05, y: 4.58, w: 1.8, d: 0.6 },
  { tipo: 'planta', amb: 'quarto1', x: 2.85, y: 5.95, s: 0.85 },
  // Quarto 2
  { tipo: 'camaSolteiro', amb: 'quarto2', x: 5.45, y: 7.55, rot: -Math.PI / 2, w: 0.95, d: 1.95, manta: '#E3B9A4' },
  { tipo: 'criado', amb: 'quarto2', x: 6.17, y: 6.8 },
  { tipo: 'escrivaninha', amb: 'quarto2', x: 3.95, y: 8.17, rot: Math.PI, w: 1.1, d: 0.5 },
  { tipo: 'armario', amb: 'quarto2', x: 5.2, y: 6.17, w: 1.6, d: 0.55 },
  // Banho
  { tipo: 'box', amb: 'banho', x: 6.09, y: 4.64, w: 0.68, d: 0.74 },
  { tipo: 'vaso', amb: 'banho', x: 6.17, y: 5.42, rot: -Math.PI / 2 },
  { tipo: 'pia', amb: 'banho', x: 5.15, y: 5.52, rot: Math.PI, w: 0.6, d: 0.42 },
];

// Ordem em que os cômodos ganham vida
const ORDEM = DADOS.ORDEM || ['sala', 'cozinha', 'hall', 'banho', 'quarto1', 'quarto2'];

// ---------------------------------------------------------------------------
// Texturas desenhadas em canvas
// ---------------------------------------------------------------------------
const PXM = 128; // pixels por metro nas texturas de piso

function texturaPiso(a) {
  const w = a.x1 - a.x0; const d = a.y1 - a.y0;
  const c = document.createElement('canvas'); c.width = Math.round(w * PXM); c.height = Math.round(d * PXM);
  const g = c.getContext('2d'); const rnd = aleatorio(a.id.length * 7919 + Math.round(w * 100));
  const tipoPiso = a.piso || (a.id === 'cozinha' || a.id === 'banho' ? 'porcelanato' : 'madeira');
  if (tipoPiso === 'grama' || tipoPiso === 'cimento') {
    const base = tipoPiso === 'grama' ? [112, 146, 82] : [196, 190, 180];
    g.fillStyle = `rgb(${base})`; g.fillRect(0, 0, c.width, c.height);
    for (let i = 0; i < w * d * 900; i++) {
      const v = (rnd() - 0.5) * 40; g.fillStyle = `rgba(${base[0] + v},${base[1] + v},${base[2] + v},0.5)`;
      g.fillRect(rnd() * c.width, rnd() * c.height, 2, tipoPiso === 'grama' ? 5 : 2);
    }
    if (tipoPiso === 'cimento') { g.strokeStyle = 'rgba(120,115,105,0.5)'; g.lineWidth = 1.5; for (let x = 0; x <= w; x += 1.0) { g.beginPath(); g.moveTo(x * PXM, 0); g.lineTo(x * PXM, c.height); g.stroke(); } }
  } else if (tipoPiso === 'porcelanato') {
    const molhado = a.id === 'banho' || a.tipo === 'banho' || a.tipo === 'lavabo';
    const base = molhado ? [226, 228, 226] : [222, 216, 205];
    const lado = molhado ? 0.45 : 0.6;
    for (let y = 0; y < d; y += lado) for (let x = 0; x < w; x += lado) {
      const v = (rnd() - 0.5) * 10;
      g.fillStyle = `rgb(${base[0] + v},${base[1] + v},${base[2] + v})`;
      g.fillRect(x * PXM, y * PXM, lado * PXM, lado * PXM);
    }
    g.strokeStyle = 'rgba(150,140,125,0.55)'; g.lineWidth = 1.5;
    for (let x = 0; x <= w; x += lado) { g.beginPath(); g.moveTo(x * PXM, 0); g.lineTo(x * PXM, c.height); g.stroke(); }
    for (let y = 0; y <= d; y += lado) { g.beginPath(); g.moveTo(0, y * PXM); g.lineTo(c.width, y * PXM); g.stroke(); }
  } else {
    // Piso vinílico de madeira: réguas no sentido do eixo x
    const larg = 0.18;
    for (let y = 0; y < d; y += larg) {
      let x = -rnd() * 1.2;
      while (x < w) {
        const comp = 0.9 + rnd() * 0.9;
        const t = rnd();
        const r = 186 + t * 26; const gg = 150 + t * 22; const b = 108 + t * 18;
        g.fillStyle = `rgb(${r},${gg},${b})`;
        g.fillRect(x * PXM, y * PXM, comp * PXM, larg * PXM);
        g.strokeStyle = 'rgba(110,80,50,0.12)'; g.lineWidth = 1;
        for (let k = 0; k < 5; k++) { // veios
          const yy = (y + rnd() * larg) * PXM;
          g.beginPath(); g.moveTo(x * PXM, yy); g.bezierCurveTo((x + comp * 0.3) * PXM, yy + 2, (x + comp * 0.6) * PXM, yy - 2, (x + comp) * PXM, yy); g.stroke();
        }
        g.fillStyle = 'rgba(90,60,35,0.35)'; g.fillRect((x + comp) * PXM - 1, y * PXM, 1.5, larg * PXM);
        x += comp;
      }
      g.fillStyle = 'rgba(90,60,35,0.30)'; g.fillRect(0, y * PXM, c.width, 1.2);
    }
  }
  // Sombra suave junto às paredes (oclusão "assada" na textura)
  const sombra = (x0, y0, x1, y1) => { const gr = g.createLinearGradient(x0, y0, x1, y1); gr.addColorStop(0, 'rgba(40,30,20,0.32)'); gr.addColorStop(1, 'rgba(40,30,20,0)'); return gr; };
  const e = 0.28 * PXM;
  g.fillStyle = sombra(0, 0, 0, e); g.fillRect(0, 0, c.width, e);
  g.fillStyle = sombra(0, c.height, 0, c.height - e); g.fillRect(0, c.height - e, c.width, e);
  g.fillStyle = sombra(0, 0, e, 0); g.fillRect(0, 0, e, c.height);
  g.fillStyle = sombra(c.width, 0, c.width - e, 0); g.fillRect(c.width - e, 0, e, c.height);
  // Sombra de contato dos móveis
  for (const m of MOVEIS.filter((mm) => mm.amb === a.id && mm.tipo !== 'tapete')) {
    const [fw, fd] = pegada(m);
    const cx = (m.x - a.x0) * PXM; const cy = (m.y - a.y0) * PXM;
    g.save(); g.translate(cx, cy); g.rotate(-(m.rot || 0)); g.filter = 'blur(10px)';
    g.fillStyle = 'rgba(30,22,14,0.30)'; g.fillRect((-fw / 2) * PXM - 6, (-fd / 2) * PXM - 6, fw * PXM + 12, fd * PXM + 12);
    g.restore();
  }
  const tex = new THREE.CanvasTexture(c); tex.colorSpace = THREE.SRGBColorSpace; tex.anisotropy = 8;
  return tex;
}

function texturaTapete(m) {
  const c = document.createElement('canvas'); c.width = Math.round(m.w * PXM); c.height = Math.round(m.d * PXM);
  const g = c.getContext('2d'); const rnd = aleatorio(Math.round(m.x * 100 + m.y * 7));
  g.fillStyle = m.cor; g.fillRect(0, 0, c.width, c.height);
  for (let i = 0; i < 4000; i++) { g.fillStyle = `rgba(${rnd() < 0.5 ? '255,255,255' : '80,60,40'},0.05)`; g.fillRect(rnd() * c.width, rnd() * c.height, 2, 2); }
  g.strokeStyle = m.borda; g.lineWidth = 10; g.strokeRect(16, 16, c.width - 32, c.height - 32);
  g.lineWidth = 3; g.strokeRect(34, 34, c.width - 68, c.height - 68);
  const tex = new THREE.CanvasTexture(c); tex.colorSpace = THREE.SRGBColorSpace; return tex;
}

function texturaGrama() {
  const c = document.createElement('canvas'); c.width = 512; c.height = 512;
  const g = c.getContext('2d'); const rnd = aleatorio(42);
  g.fillStyle = '#6E9150'; g.fillRect(0, 0, 512, 512);
  for (let i = 0; i < 9000; i++) {
    const t = rnd(); g.fillStyle = `rgba(${60 + t * 60},${100 + t * 60},${40 + t * 30},0.45)`;
    const x = rnd() * 512; const y = rnd() * 512; g.fillRect(x, y, 2, 4 + rnd() * 5);
  }
  const tex = new THREE.CanvasTexture(c); tex.colorSpace = THREE.SRGBColorSpace;
  tex.wrapS = tex.wrapT = THREE.RepeatWrapping; tex.repeat.set(24, 24); tex.anisotropy = 8;
  return tex;
}

function texturaGrade() {
  const c = document.createElement('canvas'); c.width = 256; c.height = 256;
  const g = c.getContext('2d');
  g.fillStyle = CORES.azul; g.fillRect(0, 0, 256, 256);
  g.strokeStyle = CORES.grade; g.lineWidth = 1;
  for (let i = 0; i <= 4; i++) { g.beginPath(); g.moveTo(i * 64, 0); g.lineTo(i * 64, 256); g.stroke(); g.beginPath(); g.moveTo(0, i * 64); g.lineTo(256, i * 64); g.stroke(); }
  g.strokeStyle = CORES.gradeForte; g.lineWidth = 2; g.strokeRect(0, 0, 256, 256);
  const tex = new THREE.CanvasTexture(c); tex.colorSpace = THREE.SRGBColorSpace;
  tex.wrapS = tex.wrapT = THREE.RepeatWrapping; tex.repeat.set(40, 40); tex.anisotropy = 8; // 2 m por bloco, quadrados de 0,5 m
  return tex;
}

// Pegada (largura x profundidade) de cada móvel, para sombras e símbolos do blueprint
function pegada(m) {
  const tab = { criado: [0.45, 0.4], vaso: [0.4, 0.65], planta: [0.5 * (m.s || 1), 0.5 * (m.s || 1)] };
  return tab[m.tipo] || [m.w, m.d];
}

// ---------------------------------------------------------------------------
// Blueprint: desenho em canvas sobre um plano, com progresso de 0 a 1
// ---------------------------------------------------------------------------
const BP_TAM = Math.max(16, Math.max(LARGURA, PROFUNDIDADE) + 8);
const BP = { x0: LARGURA / 2 - BP_TAM / 2, z0: PROFUNDIDADE / 2 - BP_TAM / 2 + 0.25, tam: BP_TAM, px: Math.min(4096, Math.round(2048 * BP_TAM / 16)) };
const m1 = (v) => v.toFixed(2).replace('.', ',') + ' m';
const K = BP.px / BP.tam;
const P = (x, z) => [(x - BP.x0) * K, (z - BP.z0) * K];

export function desenharBlueprint(g, p, { cotas = true, nomes = true, moveis = true } = {}) {
  g.clearRect(0, 0, BP.px, BP.px);
  g.lineCap = 'round'; g.lineJoin = 'round';
  // Paredes: linhas duplas desenhadas em sequência
  const total = TRECHOS.reduce((s, t) => s + Math.hypot(t.x1 - t.x0, t.y1 - t.y0), 0);
  let resta = suave(p / 0.45) * total;
  const e = ESPESSURA / 2;
  for (const t of TRECHOS) {
    const comp = Math.hypot(t.x1 - t.x0, t.y1 - t.y0);
    if (resta <= 0) break;
    const f = Math.min(1, resta / comp); resta -= comp;
    const xb = lerp(t.x0, t.x1, f); const yb = lerp(t.y0, t.y1, f);
    const ox = t.h ? 0 : e; const oy = t.h ? e : 0;
    if (t.janela) {
      g.strokeStyle = 'rgba(255,255,255,0.85)'; g.lineWidth = 2;
      for (const k of [-1, 0, 1]) { const [a, b] = P(t.x0 + ox * k, t.y0 + oy * k); const [c2, d2] = P(xb + ox * k, yb + oy * k); g.beginPath(); g.moveTo(a, b); g.lineTo(c2, d2); g.stroke(); }
    } else {
      const [a1, b1] = P(t.x0 - ox, t.y0 - oy); const [c1, d1] = P(xb - ox, yb - oy);
      const [a2, b2] = P(t.x0 + ox, t.y0 + oy); const [c2, d2] = P(xb + ox, yb + oy);
      g.fillStyle = 'rgba(255,255,255,0.22)';
      g.beginPath(); g.moveTo(a1, b1); g.lineTo(c1, d1); g.lineTo(c2, d2); g.lineTo(a2, b2); g.closePath(); g.fill();
      g.strokeStyle = CORES.branco; g.lineWidth = 3;
      g.beginPath(); g.moveTo(a1, b1); g.lineTo(c1, d1); g.stroke();
      g.beginPath(); g.moveTo(a2, b2); g.lineTo(c2, d2); g.stroke();
    }
  }
  // Portas
  const pp = suave((p - 0.42) / 0.15);
  if (pp > 0) {
    g.strokeStyle = `rgba(255,255,255,${0.9 * pp})`; g.lineWidth = 2;
    for (const d of portas) {
      const [cx, cy] = P(d.x, d.y); const r = d.r * K;
      g.beginPath(); g.arc(cx, cy, r, d.a0, lerp(d.a0, d.a1, pp)); g.stroke();
      g.beginPath(); g.moveTo(cx, cy); g.lineTo(cx + Math.cos(d.a1) * r * pp, cy + Math.sin(d.a1) * r * pp); g.stroke();
    }
  }
  // Símbolos dos móveis
  const pm = suave((p - 0.55) / 0.2);
  if (moveis && pm > 0) {
    g.strokeStyle = `rgba(255,255,255,${0.75 * pm})`; g.lineWidth = 2;
    for (const m of MOVEIS) {
      const [fw, fd] = pegada(m); const [cx, cy] = P(m.x, m.y);
      g.save(); g.translate(cx, cy); g.rotate(-(m.rot || 0));
      if (m.tipo === 'planta') { g.beginPath(); g.arc(0, 0, (fw / 2) * K, 0, Math.PI * 2); g.stroke(); }
      else if (m.tipo === 'tapete') { g.setLineDash([10, 8]); g.strokeRect((-fw / 2) * K, (-fd / 2) * K, fw * K, fd * K); g.setLineDash([]); }
      else {
        g.strokeRect((-fw / 2) * K, (-fd / 2) * K, fw * K, fd * K);
        if (m.tipo.startsWith('cama')) { // travesseiros na cabeceira (lado -z local)
          const n = m.tipo === 'camaCasal' ? 2 : 1; const lw = (fw - 0.2) / n;
          for (let i = 0; i < n; i++) g.strokeRect((-fw / 2 + 0.1 + i * lw + 0.03) * K, (-fd / 2 + 0.08) * K, (lw - 0.06) * K, 0.32 * K);
        }
        if (m.tipo === 'mesaJantar') for (const sx of [-1, 1]) for (const sz of [-0.3, 0.3]) { g.beginPath(); g.arc(sx * (fw / 2 + 0.22) * K, sz * K, 0.17 * K, 0, Math.PI * 2); g.stroke(); }
        if (m.tipo === 'vaso') { g.beginPath(); g.ellipse(0, 0.08 * K, 0.16 * K, 0.22 * K, 0, 0, Math.PI * 2); g.stroke(); }
      }
      g.restore();
    }
  }
  // Nomes, áreas e cotas
  const pn = suave((p - 0.7) / 0.2);
  if (nomes && pn > 0) {
    g.fillStyle = `rgba(255,255,255,${pn})`; g.textAlign = 'center';
    for (const a of ambientes) {
      if (a.id === 'hall' || a.tipo === 'circ' || a.tipo === 'externo' || Math.min(a.x1 - a.x0, a.y1 - a.y0) < 1.15) continue;
      if (a.tipo === 'patio') { const [px2, py2] = P((a.x0 + a.x1) / 2, (a.y0 + a.y1) / 2); g.font = '600 24px Inter, sans-serif'; g.fillText('PÁTIO', px2, py2); continue; }
      const [cx, cy] = P((a.x0 + a.x1) / 2, (a.y0 + a.y1) / 2);
      const larg = (a.x1 - a.x0) * K; let fs = 34; g.font = `700 ${fs}px Inter, sans-serif`;
      while (g.measureText(a.nome.toUpperCase()).width > larg - 16 && fs > 18) { fs -= 2; g.font = `700 ${fs}px Inter, sans-serif`; }
      g.fillText(a.nome.toUpperCase(), cx, cy - 6);
      g.font = '500 28px Inter, sans-serif'; g.fillText(m2((a.x1 - a.x0) * (a.y1 - a.y0)), cx, cy + 30);
    }
  }
  const pc = suave((p - 0.8) / 0.2);
  if (cotas && pc > 0) {
    g.strokeStyle = `rgba(255,255,255,${0.9 * pc})`; g.fillStyle = `rgba(255,255,255,${pc})`; g.lineWidth = 2; g.font = '600 30px Inter, sans-serif';
    const cota = (xa, za, xb, zb, txt, vertical) => {
      const [a, b] = P(xa, za); const [c2, d2] = P(xb, zb);
      g.beginPath(); g.moveTo(a, b); g.lineTo(c2, d2); g.stroke();
      for (const [u, v] of [[a, b], [c2, d2]]) { g.beginPath(); g.moveTo(u - 10, v + 10); g.lineTo(u + 10, v - 10); g.stroke(); }
      g.save(); g.translate((a + c2) / 2, (b + d2) / 2); if (vertical) g.rotate(-Math.PI / 2);
      g.textAlign = 'center'; g.fillText(txt, 0, -14); g.restore();
    };
    cota(0, -0.8, LARGURA, -0.8, m1(LARGURA), false);
    cota(-0.8, 0, -0.8, PROFUNDIDADE, m1(PROFUNDIDADE), true);
    g.font = '700 30px Inter, sans-serif'; g.textAlign = 'left';
    const [tx, ty] = P(0, PROFUNDIDADE + 1.0);
    g.fillText(META.nome.toUpperCase(), tx, ty); g.font = '500 26px Inter, sans-serif';
    g.fillText(`${Math.round(META.area)} m² · ${META.quartos} · ${META.banheiros} banho${META.banheiros > 1 ? 's' : ''}`, tx, ty + 34);
    // Ampliação prevista (casa que cresce): tracejado amarelo
    g.strokeStyle = `rgba(255,200,87,${pc})`; g.fillStyle = `rgba(255,200,87,${pc})`; g.setLineDash([16, 12]); g.lineWidth = 4;
    for (const f of FUTUROS) {
      const [a, b] = P(f.x0, f.y0); const [c2, d2] = P(f.x1, f.y1); g.strokeRect(a, b, c2 - a, d2 - b);
      g.textAlign = 'center'; g.font = '600 26px Inter, sans-serif'; g.fillText(f.nome.toUpperCase(), (a + c2) / 2, (b + d2) / 2);
    }
    g.setLineDash([]);
  }
}

// ---------------------------------------------------------------------------
// Construção da cena
// ---------------------------------------------------------------------------
export function criarCasa(renderer) {
  renderer.shadowMap.enabled = true;
  renderer.shadowMap.type = THREE.PCFSoftShadowMap;
  renderer.outputColorSpace = THREE.SRGBColorSpace;
  renderer.toneMapping = THREE.ACESFilmicToneMapping;
  renderer.toneMappingExposure = 1.05;

  const cena = new THREE.Scene();
  cena.background = new THREE.Color(CORES.azul);
  const centro = new THREE.Vector3(LARGURA / 2, 0, PROFUNDIDADE / 2);

  const hemi = new THREE.HemisphereLight('#FFFFFF', '#B5AA98', 1.3); cena.add(hemi);
  const sol = new THREE.DirectionalLight('#FFF3E2', 2.2);
  sol.position.set(centro.x - 4, 22, centro.z - 3.5); sol.target.position.copy(centro);
  sol.castShadow = true; sol.shadow.mapSize.set(2048, 2048);
  const RS = Math.max(12, Math.max(LARGURA, PROFUNDIDADE) * 0.8 + 4);
  Object.assign(sol.shadow.camera, { left: -RS, right: RS, top: RS, bottom: -RS, near: 1, far: 60 });
  sol.shadow.bias = -0.0004; sol.shadow.radius = 9; sol.shadow.blurSamples = 16;
  cena.add(sol, sol.target);

  // Fundo do blueprint (quadriculado) e desenho
  const grade = new THREE.Mesh(new THREE.PlaneGeometry(80, 80), new THREE.MeshBasicMaterial({ map: texturaGrade(), toneMapped: false }));
  grade.rotation.x = -Math.PI / 2; grade.position.set(centro.x, -0.05, centro.z); cena.add(grade);
  const canvasBP = document.createElement('canvas'); canvasBP.width = canvasBP.height = BP.px;
  const gBP = canvasBP.getContext('2d');
  const texBP = new THREE.CanvasTexture(canvasBP); texBP.colorSpace = THREE.SRGBColorSpace; texBP.anisotropy = 8;
  const desenho = new THREE.Mesh(new THREE.PlaneGeometry(BP.tam, BP.tam), new THREE.MeshBasicMaterial({ map: texBP, transparent: true, toneMapped: false, depthWrite: false }));
  desenho.rotation.x = -Math.PI / 2; desenho.position.set(BP.x0 + BP.tam / 2, 0.005, BP.z0 + BP.tam / 2); desenho.renderOrder = 1;
  cena.add(desenho);

  // Mundo real: grama, calçada, caminho
  const grama = new THREE.Mesh(new THREE.PlaneGeometry(80, 80), new THREE.MeshStandardMaterial({ map: texturaGrama(), roughness: 1, transparent: true, opacity: 0 }));
  grama.rotation.x = -Math.PI / 2; grama.position.set(centro.x, -0.02, centro.z); grama.receiveShadow = true; cena.add(grama);
  const reais = []; // objetos externos que surgem com o jardim
  const portaEntrada = portas.find((d) => d.id === 'entrada' || (String(d.id).startsWith('ext-') && Math.abs(d.y) < 0.01));
  const ENTRADA_X = portaEntrada ? (portaEntrada.a0 === Math.PI ? portaEntrada.x - portaEntrada.r / 2 : portaEntrada.x + portaEntrada.r / 2) : LARGURA / 2;
  const rua = new THREE.Mesh(new THREE.BoxGeometry(40, 0.04, 2.2), new THREE.MeshStandardMaterial({ color: '#C9C3B6', roughness: 1 }));
  rua.position.set(centro.x, 0, -3.6); rua.receiveShadow = true; cena.add(rua); reais.push({ obj: rua, t: 0.55 });
  for (let i = 0; i < 5; i++) {
    const placa = new THREE.Mesh(new RoundedBoxGeometry(0.75, 0.05, 0.42, 2, 0.03), new THREE.MeshStandardMaterial({ color: '#D8D1C3', roughness: 0.9 }));
    placa.position.set(ENTRADA_X, 0.02, -0.45 - i * 0.55); placa.receiveShadow = true; cena.add(placa); reais.push({ obj: placa, t: 0.5 + i * 0.03 });
  }

  // Arbustos e árvores (copas de esferas), com semente fixa
  const rnd = aleatorio(7);
  const geoFolha = new THREE.IcosahedronGeometry(1, 2);
  const verdes = ['#4F7A3A', '#5E8C45', '#6C9A4E', '#3F6A30', '#7AA25A'].map((c) => new THREE.MeshStandardMaterial({ color: c, roughness: 0.95, flatShading: true }));
  const moita = (x, z, raio, n, alturaBase) => {
    const grupo = new THREE.Group();
    for (let i = 0; i < n; i++) {
      const s = raio * (0.45 + rnd() * 0.55);
      const m = new THREE.Mesh(geoFolha, verdes[Math.floor(rnd() * verdes.length)]);
      m.scale.set(s, s * 0.8, s); m.position.set((rnd() - 0.5) * raio * 1.6, alturaBase + s * 0.6, (rnd() - 0.5) * raio * 1.6);
      m.castShadow = true; m.receiveShadow = true; grupo.add(m);
    }
    grupo.position.set(x, 0, z); cena.add(grupo); return grupo;
  };
  const jardim = [];
  // cerca viva na frente e nas laterais
  for (let x = 0.2; x < LARGURA - 0.1; x += 0.55) if (Math.abs(x - ENTRADA_X) > 0.8) jardim.push({ obj: moita(x, -0.55, 0.32, 3, 0), t: 0.62 + rnd() * 0.15 });
  for (let z = 0.5; z < PROFUNDIDADE - 0.3; z += 0.6) { jardim.push({ obj: moita(-0.65, z, 0.32, 3, 0), t: 0.62 + rnd() * 0.2 }); jardim.push({ obj: moita(LARGURA + 0.65, z, 0.32, 3, 0), t: 0.62 + rnd() * 0.2 }); }
  for (let x = 0.2; x < LARGURA - 0.1; x += 0.6) jardim.push({ obj: moita(x, PROFUNDIDADE + 0.65, 0.32, 3, 0), t: 0.62 + rnd() * 0.2 });
  // árvores em volta
  for (const [x0a, z0a, r] of [[-2.6, -1.8, 1.5], [9.2, -1.2, 1.7], [-2.8, 4.5, 1.4], [9.4, 4.2, 1.5], [-2.5, 10.6, 1.8], [9.1, 10.9, 1.6], [3.4, 12.2, 1.9], [-4.6, 8.0, 1.6], [11.0, 7.6, 1.7], [0.6, 13.0, 1.4], [6.6, 13.6, 1.5]]) {
    const x = x0a > 6.5 ? x0a + LARGURA - 6.5 : x0a; const z = z0a > 8.5 ? z0a + PROFUNDIDADE - 8.5 : z0a;
    jardim.push({ obj: moita(x, z, r, 9, 0.6), t: 0.6 + rnd() * 0.25 });
  }

  // Pisos (começam transparentes: o blueprint aparece por baixo)
  const pisos = {};
  for (const a of ambientes) {
    const w = a.x1 - a.x0; const d = a.y1 - a.y0;
    const mat = new THREE.MeshStandardMaterial({ map: texturaPiso(a), roughness: 0.75, transparent: true, opacity: 0 });
    const m = new THREE.Mesh(new THREE.BoxGeometry(w, 0.04, d), mat);
    m.position.set(a.x0 + w / 2, 0.02, a.y0 + d / 2); m.receiveShadow = true; cena.add(m);
    pisos[a.id] = m;
  }

  // Paredes: grupos de altura 1, escalados conforme a altura atual
  const matParede = new THREE.MeshStandardMaterial({ color: CORES.azulParede, roughness: 0.9, transparent: true, opacity: 0.55 });
  const matTopo = new THREE.MeshStandardMaterial({ color: '#E9E5DE', roughness: 0.9 });
  const matVidro = new THREE.MeshStandardMaterial({ color: '#A9D2E0', roughness: 0.15, metalness: 0.1, transparent: true, opacity: 0.8 });
  const matAresta = new THREE.LineBasicMaterial({ color: '#FFFFFF', transparent: true, opacity: 1 });
  const paredesObj = TRECHOS.map((t) => {
    const comp = Math.hypot(t.x1 - t.x0, t.y1 - t.y0) + (t.janela ? 0 : ESPESSURA);
    const geo = new THREE.BoxGeometry(t.h ? comp : ESPESSURA, 1, t.h ? ESPESSURA : comp);
    const g = new THREE.Group();
    const corpo = new THREE.Mesh(geo, matParede); corpo.castShadow = true; corpo.receiveShadow = true;
    const linhas = new THREE.LineSegments(new THREE.EdgesGeometry(geo), matAresta);
    g.add(corpo, linhas);
    g.position.set((t.x0 + t.x1) / 2, 0, (t.y0 + t.y1) / 2); cena.add(g);
    let vidro = null;
    if (t.janela) {
      vidro = new THREE.Mesh(new THREE.BoxGeometry(t.h ? comp : 0.05, 1, t.h ? 0.05 : comp), matVidro);
      vidro.position.copy(g.position); cena.add(vidro);
    }
    return { g, t, vidro };
  });

  // Móveis
  const moveis = MOVEIS.map((m) => {
    const obj = construirMovel(m);
    obj.position.set(m.x, 0.04, m.y); obj.rotation.y = m.rot || 0;
    obj.traverse((o) => { if (o.isMesh) { o.castShadow = m.tipo !== 'tapete'; o.receiveShadow = true; } });
    cena.add(obj);
    return { m, obj };
  });

  const camera = new THREE.PerspectiveCamera(30, 1, 0.1, 300);

  // -------------------------------------------------------------------------
  // Estado: desenho (0-1), paredes (0-1), vida (0-1), corte (altura em m)
  // -------------------------------------------------------------------------
  let ultimoDesenho = -1;
  function aplicar({ desenho: pd = 1, paredes: pp = 1, vida = 1, corte = 1.1 }) {
    if (Math.abs(pd - ultimoDesenho) > 1e-4) { desenharBlueprint(gBP, pd); texBP.needsUpdate = true; ultimoDesenho = pd; }
    desenho.material.opacity = 1 - suave((vida - 0.55) / 0.3);
    desenho.visible = desenho.material.opacity > 0.01 && pd > 0;

    // Cor das paredes: azul translúcido → branco
    const vp = suave(vida / 0.45);
    matParede.color.set(CORES.azulParede).lerp(new THREE.Color('#FBFAF7'), vp);
    matParede.opacity = lerp(0.55, 1, vp); matParede.transparent = vp < 0.99; matParede.depthWrite = vp > 0.5;
    matAresta.opacity = lerp(1, 0.18, vp); matAresta.color.set('#FFFFFF').lerp(new THREE.Color('#9C9284'), vp);

    const altura = corte * saida(pp);
    paredesObj.forEach(({ g, t, vidro }, i) => {
      const atraso = (i % 9) * 0.035;
      const hAqui = corte * saida((pp - atraso) / (1 - 0.3));
      let hMax = hAqui;
      if (t.janela) hMax = Math.min(hAqui, Math.min(t.janela.peitoril, corte - 0.12));
      g.visible = hMax > 0.003; g.scale.y = Math.max(hMax, 0.001); g.position.y = hMax / 2;
      if (vidro) {
        const topo = Math.min(hAqui, corte); const hv = Math.max(0, topo - hMax);
        vidro.visible = hv > 0.003 && vp > 0.3; vidro.scale.y = Math.max(hv, 0.001); vidro.position.y = hMax + hv / 2;
      }
    });
    void altura;

    // Cômodos ganham vida em sequência
    ORDEM.forEach((id, i) => {
      const ini = 0.12 + i * 0.075; const v = suave((vida - ini) / 0.22);
      const piso = pisos[id]; if (!piso) return; piso.material.opacity = v; piso.visible = v > 0.005; piso.material.transparent = v < 0.99;
      for (const { m, obj } of moveis) {
        if (m.amb !== id) continue;
        const atraso = MOVEIS.filter((mm) => mm.amb === id).indexOf(m) * 0.03;
        const vm = clamp((vida - ini - 0.1 - atraso) / 0.2);
        const s = m.tipo === 'tapete' ? saida(vm) : volta(vm);
        obj.visible = vm > 0.001; obj.scale.set(s, m.tipo === 'tapete' ? 1 : s, s);
      }
    });

    // Jardim
    const vg = suave((vida - 0.45) / 0.35);
    grama.material.opacity = vg; grama.visible = vg > 0.005; grama.material.transparent = vg < 0.99;
    for (const { obj, t } of reais) { const v = saida((vida - t) / 0.2); obj.visible = v > 0.01; obj.scale.set(1, v, 1); }
    for (const { obj, t } of jardim) { const v = volta((vida - t) / 0.25); obj.visible = v > 0.01; obj.scale.setScalar(Math.max(v, 0.001)); }
    hemi.intensity = lerp(1.6, 1.3, vg); sol.intensity = lerp(1.2, 1.9, vg);
  }

  // Câmera em coordenadas esféricas ao redor do centro da casa.
  // theta = 0: câmera do lado dos fundos (+z), imagem igual à planta 2D (frente no alto).
  // inclinacao: 0 = vista de cima; ~0.6 = perspectiva.
  function enquadrar({ theta = 0, inclinacao = 0.02, distancia = 22, fov = 30, alvo = [0, 0], aspecto = 1 }) {
    camera.fov = fov; camera.aspect = aspecto; camera.updateProjectionMatrix();
    const alvoV = new THREE.Vector3(centro.x + alvo[0], 0, centro.z + alvo[1]);
    const horiz = Math.sin(inclinacao) * distancia; const vert = Math.cos(inclinacao) * distancia;
    camera.position.set(alvoV.x + Math.sin(theta) * horiz, vert, alvoV.z + Math.cos(theta) * horiz);
    // Em vista quase de cima, "para cima" na tela aponta para a frente da casa (-z).
    camera.up.set(-Math.sin(theta), 0, -Math.cos(theta)).lerp(new THREE.Vector3(0, 1, 0), clamp(inclinacao / 1.2)).normalize();
    camera.lookAt(alvoV);
  }

  function render() { renderer.render(cena, camera); }
  aplicar({ desenho: 0, paredes: 0, vida: 0 });
  return { cena, camera, aplicar, enquadrar, render };
}

// ---------------------------------------------------------------------------
// Móveis (geometria simples com cantos arredondados)
// ---------------------------------------------------------------------------
function caixa(w, h, d, cor, r = 0.03, rough = 0.8) {
  const raio = Math.min(r, w / 2 - 0.001, h / 2 - 0.001, d / 2 - 0.001);
  const m = new THREE.Mesh(new RoundedBoxGeometry(w, h, d, 2, Math.max(raio, 0.001)), new THREE.MeshStandardMaterial({ color: cor, roughness: rough }));
  return m;
}
function em(obj, x, y, z) { obj.position.set(x, y, z); return obj; }

function construirMovel(m) {
  const g = new THREE.Group();
  const madeira = '#9B7653'; const madeiraClara = '#C9A77E'; const branco = '#F4F1EC';
  switch (m.tipo) {
    case 'tapete': {
      const t = new THREE.Mesh(new THREE.BoxGeometry(m.w, 0.012, m.d), new THREE.MeshStandardMaterial({ map: texturaTapete(m), roughness: 1 }));
      g.add(em(t, 0, 0.006, 0)); break;
    }
    case 'sofa': {
      g.add(em(caixa(m.w, 0.42, m.d, m.cor, 0.06), 0, 0.21, 0));
      g.add(em(caixa(m.w, 0.5, 0.22, m.cor, 0.07), 0, 0.5, -m.d / 2 + 0.11));
      for (const s of [-1, 1]) g.add(em(caixa(0.2, 0.55, m.d, m.cor, 0.07), s * (m.w / 2 - 0.1), 0.3, 0));
      const n = 3; const lw = (m.w - 0.4) / n;
      for (let i = 0; i < n; i++) g.add(em(caixa(lw - 0.03, 0.12, m.d - 0.3, '#9DAD98', 0.05), -m.w / 2 + 0.2 + lw * (i + 0.5), 0.48, 0.08));
      g.add(em(caixa(0.38, 0.32, 0.12, '#E8D6B5', 0.05), -m.w / 2 + 0.45, 0.62, -m.d / 2 + 0.3));
      break;
    }
    case 'rack': {
      g.add(em(caixa(m.w, 0.45, m.d, madeira, 0.02), 0, 0.225, 0));
      g.add(em(caixa(1.2, 0.7, 0.05, '#1E1E1E', 0.01, 0.3), 0, 0.85, -0.08));
      break;
    }
    case 'mesaCentro': g.add(em(caixa(m.w, 0.38, m.d, madeiraClara, 0.04), 0, 0.19, 0)); g.add(em(caixa(0.18, 0.08, 0.25, '#7A8F6A', 0.03), 0, 0.42, 0)); break;
    case 'mesaJantar': {
      g.add(em(caixa(m.w, 0.05, m.d, madeiraClara, 0.02), 0, 0.75, 0));
      g.add(em(caixa(m.w - 0.15, 0.7, m.d - 0.3, '#7D5E40', 0.02), 0, 0.37, 0));
      for (const sx of [-1, 1]) for (const sz of [-0.3, 0.3]) {
        const c = new THREE.Group();
        c.add(em(caixa(0.4, 0.05, 0.4, '#EDE6DA', 0.03), 0, 0.45, 0));
        c.add(em(caixa(0.05, 0.4, 0.4, '#EDE6DA', 0.02), sx * 0.18, 0.65, 0));
        c.add(em(caixa(0.34, 0.43, 0.34, '#7D5E40', 0.02), 0, 0.21, 0));
        c.position.set(sx * (m.w / 2 + 0.22), 0, sz); g.add(c);
      }
      g.add(em(caixa(0.16, 0.18, 0.16, '#6E8F5A', 0.06), 0, 0.86, 0));
      break;
    }
    case 'bancada': {
      g.add(em(caixa(m.w, 0.86, m.d, '#F2EEE7', 0.01), 0, 0.43, 0));
      g.add(em(caixa(m.w + 0.02, 0.04, m.d + 0.02, '#3B3936', 0.01, 0.4), 0, 0.88, 0));
      g.add(em(caixa(0.55, 0.02, 0.4, '#9EA3A6', 0.02, 0.3), -0.5, 0.905, 0.02)); // cuba
      g.add(em(caixa(0.6, 0.015, 0.5, '#141414', 0.01, 0.2), 0.8, 0.905, 0.0)); // cooktop
      for (const [dx, dz] of [[-0.14, -0.12], [0.14, -0.12], [-0.14, 0.12], [0.14, 0.12]]) {
        const boca = new THREE.Mesh(new THREE.TorusGeometry(0.07, 0.008, 6, 20), new THREE.MeshStandardMaterial({ color: '#5A5A5A' }));
        boca.rotation.x = Math.PI / 2; g.add(em(boca, 0.8 + dx, 0.915, dz));
      }
      break;
    }
    case 'geladeira': g.add(em(caixa(m.w, 1.3, m.d, '#D9DCDF', 0.04, 0.35), 0, 0.65, 0)); break;
    case 'camaCasal': case 'camaSolteiro': {
      g.add(em(caixa(m.w + 0.06, 0.3, m.d + 0.04, madeira, 0.03), 0, 0.15, 0));
      g.add(em(caixa(m.w, 0.22, m.d, branco, 0.08), 0, 0.4, 0));
      g.add(em(caixa(m.w + 0.08, 0.06, m.d * 0.6, m.manta, 0.05), 0, 0.53, m.d * 0.2));
      g.add(em(caixa(m.w + 0.06, 0.9, 0.08, madeira, 0.03), 0, 0.45, -m.d / 2 - 0.03));
      const n = m.tipo === 'camaCasal' ? 2 : 1; const lw = (m.w - 0.2) / n;
      for (let i = 0; i < n; i++) g.add(em(caixa(lw - 0.06, 0.12, 0.36, '#FFFFFF', 0.06), -m.w / 2 + 0.1 + lw * (i + 0.5), 0.56, -m.d / 2 + 0.28));
      break;
    }
    case 'criado': g.add(em(caixa(0.45, 0.5, 0.4, madeiraClara, 0.02), 0, 0.25, 0)); g.add(em(new THREE.Mesh(new THREE.SphereGeometry(0.1, 16, 12), new THREE.MeshStandardMaterial({ color: '#F6E7C8', emissive: '#6B5530', roughness: 0.6 })), 0, 0.6, 0)); break;
    case 'armario': {
      g.add(em(caixa(m.w, 1.25, m.d, '#EFEAE2', 0.02), 0, 0.625, 0));
      const n = Math.round(m.w / 0.45);
      for (let i = 1; i < n; i++) g.add(em(caixa(0.01, 1.2, 0.01, '#BDB5A8', 0.004), -m.w / 2 + (m.w / n) * i, 0.62, m.d / 2));
      break;
    }
    case 'escrivaninha': {
      g.add(em(caixa(m.w, 0.04, m.d, madeiraClara, 0.015), 0, 0.74, 0));
      for (const s of [-1, 1]) g.add(em(caixa(0.04, 0.72, m.d - 0.04, '#EFEAE2', 0.01), s * (m.w / 2 - 0.03), 0.36, 0));
      g.add(em(caixa(0.5, 0.3, 0.03, '#2A2A2A', 0.01, 0.3), 0, 0.92, -0.12));
      const cadeira = new THREE.Group(); cadeira.add(em(caixa(0.45, 0.06, 0.45, '#3E4A57', 0.04), 0, 0.46, 0)); cadeira.add(em(caixa(0.45, 0.45, 0.06, '#3E4A57', 0.04), 0, 0.7, 0.2)); cadeira.add(em(caixa(0.06, 0.43, 0.06, '#555555', 0.02), 0, 0.22, 0));
      cadeira.position.set(0, 0, 0.5); g.add(cadeira);
      break;
    }
    case 'box': {
      g.add(em(caixa(m.w, 0.03, m.d, '#C9CED1', 0.01), 0, 0.015, 0));
      const vidro = new THREE.MeshStandardMaterial({ color: '#BFE0EA', transparent: true, opacity: 0.35, roughness: 0.1 });
      const lado = new THREE.Mesh(new THREE.BoxGeometry(m.w, 1.9, 0.015), vidro); g.add(em(lado, 0, 0.95, m.d / 2));
      const lado2 = new THREE.Mesh(new THREE.BoxGeometry(0.015, 1.9, m.d), vidro); g.add(em(lado2, -m.w / 2, 0.95, 0));
      g.add(em(new THREE.Mesh(new THREE.CylinderGeometry(0.1, 0.1, 0.02, 20), new THREE.MeshStandardMaterial({ color: '#9A9A9A', metalness: 0.6 })), 0.1, 1.95, -0.1));
      break;
    }
    case 'vaso': {
      g.add(em(caixa(0.36, 0.38, 0.5, '#FFFFFF', 0.12, 0.3), 0, 0.19, 0.05));
      g.add(em(caixa(0.38, 0.32, 0.17, '#FFFFFF', 0.04, 0.3), 0, 0.5, -0.22));
      break;
    }
    case 'pia': g.add(em(caixa(m.w, 0.8, m.d, madeiraClara, 0.02), 0, 0.4, 0)); g.add(em(caixa(m.w - 0.12, 0.05, m.d - 0.12, '#FFFFFF', 0.04, 0.3), 0, 0.83, 0)); break;
    case 'planta': {
      const s = m.s || 1;
      g.add(em(new THREE.Mesh(new THREE.CylinderGeometry(0.15 * s, 0.12 * s, 0.32 * s, 20), new THREE.MeshStandardMaterial({ color: '#C8B49A', roughness: 0.9 })), 0, 0.16 * s, 0));
      const rr = aleatorio(Math.round(m.x * 97 + m.y * 13));
      const verde = ['#4C7A3A', '#5F8F48', '#3E6A31'];
      for (let i = 0; i < 7; i++) {
        const f = new THREE.Mesh(new THREE.IcosahedronGeometry(0.16 * s, 1), new THREE.MeshStandardMaterial({ color: verde[i % 3], roughness: 0.9, flatShading: true }));
        g.add(em(f, (rr() - 0.5) * 0.3 * s, (0.45 + rr() * 0.4) * s, (rr() - 0.5) * 0.3 * s));
      }
      break;
    }
    case 'tanque': g.add(em(caixa(m.w, 0.85, m.d, '#F4F4F2', 0.03, 0.4), 0, 0.425, 0)); g.add(em(caixa(m.w - 0.1, 0.03, m.d - 0.12, '#C9CED1', 0.02), 0, 0.86, 0)); break;
    case 'maquina': g.add(em(caixa(m.w, 0.9, m.d, '#ECEEF0', 0.04, 0.35), 0, 0.45, 0)); g.add(em(new THREE.Mesh(new THREE.CylinderGeometry(0.2, 0.2, 0.02, 24), new THREE.MeshStandardMaterial({ color: '#9FB3C2', metalness: 0.3 })), 0, 0.91, 0)); break;
    case 'poltrona': {
      const cor = '#B9895E';
      g.add(em(caixa(m.w, 0.38, m.d, cor, 0.06), 0, 0.19, 0)); g.add(em(caixa(m.w, 0.45, 0.14, cor, 0.06), 0, 0.55, -m.d / 2 + 0.07));
      break;
    }
    case 'carro': {
      const corCarro = '#B33A3A';
      g.add(em(caixa(m.w, 0.6, m.d, corCarro, 0.12, 0.35), 0, 0.5, 0));
      g.add(em(caixa(m.w - 0.15, 0.45, m.d * 0.5, '#2E3A44', 0.1, 0.2), 0, 1.0, -0.1));
      for (const sx of [-1, 1]) for (const sz of [-1, 1]) {
        const roda = new THREE.Mesh(new THREE.CylinderGeometry(0.3, 0.3, 0.22, 20), new THREE.MeshStandardMaterial({ color: '#1C1C1C' }));
        roda.rotation.z = Math.PI / 2; g.add(em(roda, sx * (m.w / 2 - 0.08), 0.3, sz * (m.d / 2 - 0.7)));
      }
      break;
    }
    default: break;
  }
  return g;
}

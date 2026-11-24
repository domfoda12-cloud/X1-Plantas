// Decoração da visita 3D: quadros, portas, cortinas, luminárias, objetos de uso e o lado de fora.
// Não mexe no motor (casa-*.js) nem nas medidas: só acrescenta objetos à cena, sempre no mesmo lugar para a mesma casa
// (semente pelo id do cômodo). Regras de colocação, conferidas em código:
//   - nada em cima de janela nem no vão ou no giro de porta;
//   - objeto de chão só entra se o caminho continuar igual: tudo o que se alcançava com 80 cm e com 60 cm de passagem
//     livre antes continua alcançável depois (grade de 5 cm, função fazerGrade);
//   - nada atravessa parede, móvel da planta ou outro objeto (caixas em A.obst);
//   - quadro só em trecho de parede livre de janela, porta e móvel alto, com o centro a 1,5 m do piso.
// Se um item não cabe num cômodo, ele não entra naquele cômodo.
import * as THREE from './lib/three.module.min.js';
import { RoundedBoxGeometry } from './lib/RoundedBox.js';

const PI = Math.PI;
const clamp = (v, a, b) => Math.min(b, Math.max(a, v));
const FORA = ['varanda', 'garagem', 'patio', 'jardim', 'futuro', 'quintal'];

export const PADRAO = { parede: 'neve', piso: 'madeira', sofa: 'salvia', cama: 'planta', quadros: 'formas', hora: 'tarde', maquina: true, decor: true };
export const OPCOES = {
  parede: [['neve', 'Branco neve', '#FBFAF7'], ['gelo', 'Gelo', '#E3E7E5'], ['palha', 'Palha', '#F2E7BF'], ['areia', 'Areia', '#E4D2B4'], ['erva', 'Verde erva-doce', '#CDE2CF'], ['sereno', 'Azul sereno', '#C9DBEB']],
  piso: [['madeira', 'Madeira'], ['porcelanato', 'Porcelanato'], ['cimento', 'Cimento queimado']],
  sofa: [['salvia', 'Verde sálvia', '#8A9A86'], ['cinza', 'Cinza', '#8E9196'], ['marinho', 'Azul-marinho', '#3C4F6B'], ['terracota', 'Terracota', '#B5654A'], ['caramelo', 'Caramelo', '#B98A5A']],
  cama: [['planta', 'Como na planta', null], ['branco', 'Branco', '#F1EEE8'], ['azul', 'Azul', '#7F9FC4'], ['verde', 'Verde', '#8DAE8C'], ['rosa', 'Rosa', '#E0A6A0'], ['mostarda', 'Mostarda', '#D9A941']],
  quadros: [['formas', 'Formas'], ['paisagens', 'Paisagens'], ['projeto', 'Projeto']],
  hora: [['manha', 'Manhã'], ['tarde', 'Fim de tarde'], ['noite', 'Noite']],
  maquina: [[true, 'Com máquina de lavar'], [false, 'Só o tanque']],
  decor: [[true, 'Com decoração'], [false, 'Só os móveis da planta']],
};
const corDe = (grupo, id) => (OPCOES[grupo].find((o) => o[0] === id) || OPCOES[grupo][0])[2];

function semente(s) { let h = 2166136261; for (const ch of String(s)) { h ^= ch.charCodeAt(0); h = Math.imul(h, 16777619); } return h >>> 0; }
function aleatorio(seed) { let s = seed >>> 0; return () => { s = (s + 0x6D2B79F5) >>> 0; let t = s; t = Math.imul(t ^ (t >>> 15), t | 1); t ^= t + Math.imul(t ^ (t >>> 7), t | 61); return ((t ^ (t >>> 14)) >>> 0) / 4294967296; }; }
function tom(hex, f) { const n = parseInt(hex.slice(1), 16), c = (v) => clamp(Math.round(f <= 1 ? v * f : v + (255 - v) * (f - 1)), 0, 255); return '#' + [n >> 16, (n >> 8) & 255, n & 255].map((v) => c(v).toString(16).padStart(2, '0')).join(''); }

// ---------------------------------------------------------------------------
// Geometrias e materiais únicos: tudo o que é miúdo vira instância (poucas chamadas de desenho)
// ---------------------------------------------------------------------------
const GEO = {
  caixa: new THREE.BoxGeometry(1, 1, 1), macio: new RoundedBoxGeometry(1, 1, 1, 2, 0.2), cil: new THREE.CylinderGeometry(0.5, 0.5, 1, 12),
  esfera: new THREE.SphereGeometry(0.5, 10, 7), cone: new THREE.CylinderGeometry(0.32, 0.5, 1, 12), ponta: new THREE.ConeGeometry(0.5, 1, 6), plano: new THREE.PlaneGeometry(1, 1),
};
const MAT = { fosco: new THREE.MeshStandardMaterial({ roughness: 0.85 }), luz: new THREE.MeshBasicMaterial({ color: '#FFF1CF' }) };

class Lote {
  constructor() { this.itens = []; }
  add(i) { this.itens.push(i); }
  montar(grupo) {
    const porChave = new Map();
    for (const i of this.itens) { const k = i.t + (i.s ? '|s' : ''); if (!porChave.has(k)) porChave.set(k, []); porChave.get(k).push(i); }
    const o = new THREE.Object3D(), c = new THREE.Color();
    for (const arr of porChave.values()) {
      const t = arr[0].t, im = new THREE.InstancedMesh(GEO[t === 'luz' ? 'esfera' : t], t === 'luz' ? MAT.luz : MAT.fosco, arr.length);
      arr.forEach((i, n) => {
        o.position.set(i.x, i.y, i.z); o.rotation.set(i.rx, i.ry, i.rz, 'YXZ'); o.scale.set(i.sx, i.sy, i.sz); o.updateMatrix(); im.setMatrixAt(n, o.matrix);
        if (t !== 'luz') im.setColorAt(n, c.set(i.cor));
      });
      im.castShadow = !!arr[0].s; im.receiveShadow = t !== 'luz'; im.frustumCulled = false; grupo.add(im);
    }
  }
}

// Referencial local: x ao longo da largura, z para a frente (para dentro do cômodo), y a partir de y0. Todas as alturas são a BASE da peça.
function ref(lote, grupo, x, z, th = 0, y0 = 0) {
  const c = Math.cos(th), s = Math.sin(th);
  const W = (lx, lz) => [x + lx * c + lz * s, z - lx * s + lz * c];
  const p = (t, sx, sy, sz, cor, lx, y, lz, o = {}) => { const [wx, wz] = W(lx, lz); lote.add({ t, sx, sy, sz, cor, x: wx, y: y0 + y + (o.centro ? 0 : sy / 2), z: wz, ry: th + (o.ry || 0), rx: o.rx || 0, rz: o.rz || 0, s: o.sombra }); };
  return {
    x, z, th, y0, W,
    cx: (w, h, d, cor, lx, y, lz, o) => p('caixa', w, h, d, cor, lx, y, lz, o),
    mc: (w, h, d, cor, lx, y, lz, o) => p('macio', w, h, d, cor, lx, y, lz, o),
    ci: (dia, h, cor, lx, y, lz, o) => p('cil', dia, h, (o && o.dz) || dia, cor, lx, y, lz, o),
    es: (dx, dy, dz, cor, lx, y, lz, o) => p('esfera', dx, dy, dz, cor, lx, y, lz, o),
    co: (dia, h, cor, lx, y, lz, o) => p('cone', dia, h, (o && o.dz) || dia, cor, lx, y, lz, o),
    po: (dia, h, cor, lx, y, lz, o) => p('ponta', dia, h, (o && o.dz) || dia, cor, lx, y, lz, o),
    lu: (dx, dy, dz, lx, y, lz) => p('luz', dx, dy, dz, '#fff', lx, y, lz),
    malha: (m, lx, y, lz, o = {}) => { const [wx, wz] = W(lx, lz); m.position.set(wx, y0 + y, wz); m.rotation.set(o.rx || 0, th + (o.ry || 0), o.rz || 0, 'YXZ'); grupo.add(m); return m; },
    sub: (lx, lz, dth = 0, dy = 0) => { const [wx, wz] = W(lx, lz); return ref(lote, grupo, wx, wz, th + dth, y0 + dy); },
  };
}

// ---------------------------------------------------------------------------
// Texturas de canvas pequenas (até 256 px), guardadas para as três casas
// ---------------------------------------------------------------------------
const TEX = new Map(), MATS = new Map();
function tex(chave, w, h, desenhar) {
  let t = TEX.get(chave);
  if (!t) { const c = document.createElement('canvas'); c.width = Math.max(8, Math.round(w)); c.height = Math.max(8, Math.round(h)); desenhar(c.getContext('2d'), c.width, c.height); t = new THREE.CanvasTexture(c); t.colorSpace = THREE.SRGBColorSpace; t.anisotropy = 4; TEX.set(chave, t); }
  return t;
}
function matTex(chave, t, o = {}) { let m = MATS.get(chave); if (!m) { m = o.basico ? new THREE.MeshBasicMaterial({ map: t }) : new THREE.MeshStandardMaterial({ map: t, roughness: o.rough ?? 0.9 }); MATS.set(chave, m); } return m; }

const PAL = ['#C8553D', '#E0A23A', '#2F5D73', '#8A9A86', '#D9A08B', '#3E4A57'];
function plantaBaixa(g, w, h, D) {      // a planta desta casa, do jeito do e-book: frente embaixo
  const M = Math.min(w, h) * 0.12, k = Math.min((w - 2 * M) / D.LARGURA, (h - 2 * M) / D.PROFUNDIDADE), ox = (w - D.LARGURA * k) / 2, oz = (h - D.PROFUNDIDADE * k) / 2;
  const X = (x) => w - (ox + x * k), Z = (z) => h - (oz + z * k);
  g.strokeStyle = '#fff'; g.lineWidth = Math.max(2, k * 0.14); g.lineCap = 'square';
  for (const [x0, y0, x1, y1] of D.paredes) { g.beginPath(); g.moveTo(X(x0), Z(y0)); g.lineTo(X(x1), Z(y1)); g.stroke(); }
  g.strokeStyle = '#FFC857'; g.lineWidth = Math.max(1.5, k * 0.07);
  for (const j of D.janelas) { g.beginPath(); g.moveTo(X(j.seg[0]), Z(j.seg[1])); g.lineTo(X(j.seg[2]), Z(j.seg[3])); g.stroke(); }
  g.strokeStyle = 'rgba(255,255,255,.8)'; g.lineWidth = 1;
  for (const p of D.portas) { g.beginPath(); g.arc(X(p.x), Z(p.y), p.r * k, p.a0 + PI, p.a1 + PI, p.a1 < p.a0); g.stroke(); g.beginPath(); g.moveTo(X(p.x), Z(p.y)); g.lineTo(X(p.x + Math.cos(p.a1) * p.r), Z(p.y + Math.sin(p.a1) * p.r)); g.stroke(); }
}
function arte(g, W, H, est, v, rnd, D) {
  const m = Math.round(Math.min(W, H) * 0.09);
  g.fillStyle = '#FBF8F1'; g.fillRect(0, 0, W, H);
  g.save(); g.beginPath(); g.rect(m, m, W - 2 * m, H - 2 * m); g.clip(); g.translate(m, m);
  const w = W - 2 * m, h = H - 2 * m, r = Math.min(w, h), circ = (x, y, rr, cor) => { g.fillStyle = cor; g.beginPath(); g.arc(x, y, rr, 0, 2 * PI); g.fill(); };
  const morro = (y0, amp, cor, fase) => { g.fillStyle = cor; g.beginPath(); g.moveTo(0, h); for (let x = 0; x <= w; x += 4) g.lineTo(x, y0 + Math.sin(x / w * 5 + fase) * amp + Math.sin(x / w * 11 + fase * 2) * amp * 0.3); g.lineTo(w, h); g.fill(); };
  const grad = (c0, c1) => { const gr = g.createLinearGradient(0, 0, 0, h); gr.addColorStop(0, c0); gr.addColorStop(1, c1); g.fillStyle = gr; g.fillRect(0, 0, w, h); };
  if (est === 'projeto') {
    g.fillStyle = '#0B4FA8'; g.fillRect(0, 0, w, h); g.strokeStyle = 'rgba(255,255,255,.13)'; g.lineWidth = 1;
    for (let x = 0; x <= w; x += r / 8) { g.beginPath(); g.moveTo(x, 0); g.lineTo(x, h); g.stroke(); } for (let y = 0; y <= h; y += r / 8) { g.beginPath(); g.moveTo(0, y); g.lineTo(w, y); g.stroke(); }
    g.strokeStyle = '#fff'; g.lineWidth = 2.5; g.lineJoin = 'round';
    if (v === 0) plantaBaixa(g, w, h, D);
    else if (v === 1) {            // fachada com cota
      const bx = w * 0.18, bw = w * 0.64, by = h * 0.72, bh = h * 0.3; g.strokeRect(bx, by - bh, bw, bh);
      g.beginPath(); g.moveTo(bx - w * 0.05, by - bh); g.lineTo(w / 2, by - bh - h * 0.2); g.lineTo(bx + bw + w * 0.05, by - bh); g.closePath(); g.stroke();
      g.strokeRect(bx + bw * 0.12, by - bh * 0.72, bw * 0.2, bh * 0.72); g.strokeRect(bx + bw * 0.5, by - bh * 0.72, bw * 0.34, bh * 0.4);
      g.lineWidth = 1.5; g.strokeStyle = '#FFC857'; g.beginPath(); g.moveTo(bx, by + h * 0.09); g.lineTo(bx + bw, by + h * 0.09); g.stroke();
      for (const x of [bx, bx + bw]) { g.beginPath(); g.moveTo(x - 5, by + h * 0.09 + 5); g.lineTo(x + 5, by + h * 0.09 - 5); g.stroke(); }
      g.strokeStyle = '#fff'; g.beginPath(); g.moveTo(0, by); g.lineTo(w, by); g.stroke();
    } else if (v === 2) {          // esquadro, compasso e trena
      g.beginPath(); g.moveTo(w * 0.15, h * 0.8); g.lineTo(w * 0.15, h * 0.25); g.lineTo(w * 0.7, h * 0.8); g.closePath(); g.stroke();
      g.beginPath(); g.arc(w * 0.62, h * 0.36, r * 0.22, 0, 2 * PI); g.stroke(); g.lineWidth = 1.2; g.beginPath(); g.arc(w * 0.62, h * 0.36, r * 0.12, 0, 2 * PI); g.stroke();
      g.strokeStyle = '#FFC857'; g.lineWidth = 5; g.beginPath(); g.moveTo(w * 0.1, h * 0.9); g.lineTo(w * 0.9, h * 0.9); g.stroke(); g.strokeStyle = '#2A2108'; g.lineWidth = 1;
      for (let x = w * 0.12; x < w * 0.9; x += w * 0.04) { g.beginPath(); g.moveTo(x, h * 0.9 - 2.5); g.lineTo(x, h * 0.9 + 1); g.stroke(); }
    } else {                        // casinha em perspectiva
      const cx = w / 2, cy = h * 0.6, a = r * 0.26, pt = (i, j, kk) => [cx + (i - j) * a * 0.87, cy + (i + j) * a * 0.5 - kk * a];
      const lin = (...ps) => { g.beginPath(); ps.forEach((q, i) => (i ? g.lineTo(q[0], q[1]) : g.moveTo(q[0], q[1]))); g.stroke(); };
      lin(pt(0, 1, 0), pt(1, 1, 0), pt(1, 0, 0)); lin(pt(0, 1, 0), pt(0, 1, 1), pt(1, 1, 1), pt(1, 1, 0)); lin(pt(1, 1, 1), pt(1, 0, 1), pt(1, 0, 0)); lin(pt(0, 1, 1), pt(0, 0, 1), pt(1, 0, 1));
      lin(pt(0, 1, 1), pt(0.5, 1, 1.6), pt(1, 1, 1)); lin(pt(0.5, 1, 1.6), pt(0.5, 0, 1.6), pt(1, 0, 1)); lin(pt(0.5, 0, 1.6), pt(0, 0, 1));
    }
  } else if (est === 'paisagens') {
    if (v === 0) { grad('#F7D3A0', '#FBEFD8'); circ(w * 0.68, h * 0.3, r * 0.13, '#F2A65A'); ['#8FB3AE', '#5E8C7B', '#3F6F5E', '#2F5546'].forEach((c, i) => morro(h * (0.5 + i * 0.13), h * 0.06, c, i * 1.7 + rnd() * 3)); }
    else if (v === 1) {
      grad('#BFE3F0', '#FCE9C9'); circ(w * 0.3, h * 0.36, r * 0.11, '#F6B95B'); g.fillStyle = '#2F7FA8'; g.fillRect(0, h * 0.55, w, h); g.fillStyle = 'rgba(255,255,255,.22)';
      for (let i = 0; i < 9; i++) g.fillRect(rnd() * w * 0.8, h * (0.6 + rnd() * 0.36), w * (0.1 + rnd() * 0.2), 2);
      g.fillStyle = '#4F7A4A'; g.beginPath(); g.ellipse(w * 0.82, h * 0.55, w * 0.2, h * 0.07, 0, PI, 0); g.fill();
      const bx = w * 0.45, by = h * 0.68; g.fillStyle = '#fff'; g.beginPath(); g.moveTo(bx, by - r * 0.26); g.lineTo(bx, by - 3); g.lineTo(bx + r * 0.15, by - 3); g.fill(); g.beginPath(); g.moveTo(bx - 3, by - r * 0.2); g.lineTo(bx - 3, by - 3); g.lineTo(bx - r * 0.1, by - 3); g.fill();
      g.fillStyle = '#7A3E2A'; g.beginPath(); g.moveTo(bx - r * 0.13, by); g.lineTo(bx + r * 0.17, by); g.lineTo(bx + r * 0.12, by + r * 0.05); g.lineTo(bx - r * 0.09, by + r * 0.05); g.fill();
    } else if (v === 2) {           // ipê-amarelo
      grad('#CFE8F5', '#EAF5F2'); g.fillStyle = '#8DB36B'; g.fillRect(0, h * 0.8, w, h); g.strokeStyle = '#5B4030'; g.lineCap = 'round';
      g.lineWidth = r * 0.05; g.beginPath(); g.moveTo(w * 0.5, h * 0.84); g.quadraticCurveTo(w * 0.47, h * 0.6, w * 0.5, h * 0.46); g.stroke(); g.lineWidth = r * 0.025;
      for (const [dx, dy] of [[-0.2, -0.16], [0.2, -0.18], [-0.08, -0.24], [0.1, -0.26]]) { g.beginPath(); g.moveTo(w * 0.5, h * 0.5); g.lineTo(w * (0.5 + dx), h * (0.5 + dy)); g.stroke(); }
      for (let i = 0; i < 90; i++) { const a = rnd() * 2 * PI, d = Math.sqrt(rnd()); circ(w * 0.5 + Math.cos(a) * d * w * 0.34, h * 0.33 + Math.sin(a) * d * h * 0.22, r * (0.03 + rnd() * 0.035), ['#F2C230', '#F7D95C', '#E0A800'][i % 3]); }
      for (let i = 0; i < 14; i++) circ(w * (0.2 + rnd() * 0.6), h * (0.83 + rnd() * 0.12), r * 0.012, '#F2C230');
    } else {                        // casinhas coloridas
      grad('#F9DDB0', '#FCF0DA'); circ(w * 0.8, h * 0.22, r * 0.09, '#F6B95B'); morro(h * 0.5, h * 0.05, '#A9C4A0', rnd() * 3);
      const cores = ['#E36F5A', '#F2C14E', '#5BA4B6', '#8DBF86', '#D98FB3'], n = w > h ? 5 : 4, lw = w / n;
      for (let i = 0; i < n; i++) { const ch = h * (0.3 + rnd() * 0.14), x = i * lw, y = h * 0.86 - ch; g.fillStyle = cores[(i + Math.floor(rnd() * 5)) % 5]; g.fillRect(x + 1, y, lw - 2, ch); g.fillStyle = '#B5553A'; g.fillRect(x, y - h * 0.035, lw, h * 0.04); g.fillStyle = '#4A3526'; g.fillRect(x + lw * 0.16, h * 0.86 - ch * 0.5, lw * 0.26, ch * 0.5); g.fillStyle = '#FDF8EC'; g.fillRect(x + lw * 0.56, y + ch * 0.28, lw * 0.28, ch * 0.3); }
      g.fillStyle = '#9A8F80'; g.fillRect(0, h * 0.86, w, h);
    }
  } else {
    g.fillStyle = '#F1E7D3'; g.fillRect(0, 0, w, h); const q = Math.floor(rnd() * 6);
    if (v === 0) { circ(w * 0.5, h * 0.27, r * 0.15, PAL[(q + 1) % 6]); g.lineCap = 'butt'; for (let i = 0; i < 4; i++) { g.strokeStyle = PAL[(q + i) % 6]; g.lineWidth = r * 0.075; g.beginPath(); g.arc(w * 0.5, h * 0.97, r * (0.46 - i * 0.105), PI, 0); g.stroke(); } }
    else if (v === 1) { circ(w * 0.36, h * 0.4, r * 0.3, PAL[(q + 2) % 6]); g.fillStyle = PAL[q]; g.beginPath(); g.arc(w * 0.66, h * 0.62, r * 0.24, PI * 0.5, PI * 1.5); g.fill(); circ(w * 0.72, h * 0.24, r * 0.09, PAL[(q + 1) % 6]); g.fillStyle = PAL[5]; g.fillRect(w * 0.14, h * 0.74, w * 0.4, h * 0.07); g.strokeStyle = PAL[5]; g.lineWidth = 2; g.beginPath(); g.moveTo(w * 0.1, h * 0.9); g.lineTo(w * 0.9, h * 0.14); g.stroke(); }
    else if (v === 2) {             // folha em traço
      g.fillStyle = PAL[4]; g.beginPath(); g.ellipse(w * 0.55, h * 0.45, w * 0.28, h * 0.3, 0.4, 0, 2 * PI); g.fill(); g.strokeStyle = '#2F4F38'; g.lineWidth = 2.5; g.lineCap = 'round';
      g.beginPath(); g.moveTo(w * 0.42, h * 0.95); g.quadraticCurveTo(w * 0.5, h * 0.5, w * 0.6, h * 0.1); g.stroke(); g.fillStyle = '#4F7A55';
      for (let i = 0; i < 7; i++) { const t = 0.15 + i * 0.11, x = w * (0.43 + t * 0.17), y = h * (0.95 - t * 0.85), s = i % 2 ? 1 : -1; g.save(); g.translate(x, y); g.rotate(s * 0.9 - 0.2); g.beginPath(); g.ellipse(s * r * 0.11, 0, r * 0.12, r * 0.045, 0, 0, 2 * PI); g.fill(); g.restore(); }
    } else for (let i = 0; i < 6; i++) { g.fillStyle = PAL[(q + i) % 6]; g.beginPath(); g.moveTo(0, h); for (let x = 0; x <= w; x += 4) g.lineTo(x, h * (0.12 + i * 0.15) + Math.sin(x / w * 6 + i * 1.3 + q) * h * 0.045); g.lineTo(w, h); g.fill(); }
  }
  g.restore(); g.strokeStyle = 'rgba(0,0,0,.14)'; g.lineWidth = 1; g.strokeRect(m + 0.5, m + 0.5, W - 2 * m - 1, H - 2 * m - 1);
}

function desenharRelogio(g, W) {      // marca a hora do aparelho de quem visita
  const d = new Date(), c = W / 2; g.clearRect(0, 0, W, W); g.fillStyle = '#FDFBF5'; g.beginPath(); g.arc(c, c, c - 2, 0, 2 * PI); g.fill();
  g.strokeStyle = '#2B2B2B'; g.lineCap = 'round';
  for (let i = 0; i < 12; i++) { const a = i * PI / 6; g.lineWidth = i % 3 ? 2 : 4; g.beginPath(); g.moveTo(c + Math.sin(a) * c * 0.78, c - Math.cos(a) * c * 0.78); g.lineTo(c + Math.sin(a) * c * 0.88, c - Math.cos(a) * c * 0.88); g.stroke(); }
  const mao = (a, comp, lw, cor) => { g.strokeStyle = cor; g.lineWidth = lw; g.beginPath(); g.moveTo(c, c); g.lineTo(c + Math.sin(a) * c * comp, c - Math.cos(a) * c * comp); g.stroke(); };
  mao((d.getHours() % 12 + d.getMinutes() / 60) * PI / 6, 0.48, 6, '#2B2B2B'); mao(d.getMinutes() * PI / 30, 0.72, 4, '#2B2B2B'); g.fillStyle = '#C8553D'; g.beginPath(); g.arc(c, c, 5, 0, 2 * PI); g.fill();
  return d.getHours() * 60 + d.getMinutes();
}

// ---------------------------------------------------------------------------
// Análise da planta: paredes de verdade, lados de cada cômodo, caixas dos móveis, zonas de porta e de janela
// ---------------------------------------------------------------------------
const ALT_MOVEL = { sofa: 0.78, rack: 1.22, mesaCentro: 0.47, mesaJantar: 0.95, bancada: 0.93, geladeira: 1.3, camaCasal: 0.9, camaSolteiro: 0.9, criado: 0.7, armario: 1.25, escrivaninha: 1.07, cadeira: 0.93, box: 1.97, vaso: 0.66, pia: 0.86, planta: 1.0, tanque: 0.88, maquina: 0.92, poltrona: 0.78, carro: 1.45 };
function caixaMovel(m) {
  const tab = { criado: [0.45, 0.4], vaso: [0.4, 0.65], cadeira: [0.45, 0.5], planta: [0.5 * (m.s || 1), 0.5 * (m.s || 1)] };
  let [w, d] = tab[m.tipo] || [m.w, m.d];
  if (m.tipo === 'mesaJantar') { w = m.w + 0.84; d = Math.max(m.d, 1.0); }      // com as cadeiras
  const q = Math.abs(Math.round((m.rot || 0) / (PI / 2))) % 2, hx = (q ? d : w) / 2, hz = (q ? w : d) / 2;
  return { x0: m.x - hx, x1: m.x + hx, z0: m.y - hz, z1: m.y + hz, y0: 0.04, y1: 0.04 + (ALT_MOVEL[m.tipo] || 0.8), t: m.tipo === 'tapete' ? 'tapete' : 'movel', m };
}
const frenteDe = (m) => ({ x: Math.round(Math.sin(m.rot || 0)), z: Math.round(Math.cos(m.rot || 0)) });

function fazerGrade(D, paredes, obst, portas, chaves) {
  const C = 0.05, M = 1.5, nx = Math.ceil((D.LARGURA + 2 * M) / C), nz = Math.ceil((D.PROFUNDIDADE + 2 * M) / C), n = nx * nz, D2 = C * 1.4142;
  const base = new Uint8Array(n), forca = new Uint8Array(n);
  const marcar = (arr, x0, x1, z0, z1) => {
    const i0 = Math.max(0, Math.ceil((x0 + M) / C - 0.5)), i1 = Math.min(nx - 1, Math.floor((x1 + M) / C - 0.5)), j0 = Math.max(0, Math.ceil((z0 + M) / C - 0.5)), j1 = Math.min(nz - 1, Math.floor((z1 + M) / C - 0.5));
    for (let j = j0; j <= j1; j++) for (let i = i0; i <= i1; i++) arr[j * nx + i] = 1;
  };
  for (const w of paredes) { if (w.h) marcar(base, w.a, w.b, w.fixo - w.esp / 2, w.fixo + w.esp / 2); else marcar(base, w.fixo - w.esp / 2, w.fixo + w.esp / 2, w.a, w.b); }
  for (const o of obst) if (o.t === 'movel') marcar(base, o.x0, o.x1, o.z0, o.z1);
  for (const p of portas) { const ax = p.cx - p.d1.x * 0.6, az = p.cz - p.d1.z * 0.6, bx = p.cx + p.d1.x * 0.6, bz = p.cz + p.d1.z * 0.6; marcar(forca, Math.min(ax, bx) - 0.08, Math.max(ax, bx) + 0.08, Math.min(az, bz) - 0.08, Math.max(az, bz) + 0.08); }
  const idx = (x, z) => { const i = Math.floor((x + M) / C), j = Math.floor((z + M) / C); return i < 0 || j < 0 || i >= nx || j >= nz ? -1 : j * nx + i; };
  const alcance = (extras) => {
    const bl = extras.length ? base.slice() : base; for (const b of extras) marcar(bl, b.x0, b.x1, b.z0, b.z1);
    const d = new Float32Array(n);
    for (let j = 0; j < nz; j++) for (let i = 0; i < nx; i++) { const k = j * nx + i; if (bl[k]) { d[k] = 0; continue; } let v = 99; if (i > 0) v = Math.min(v, d[k - 1] + C); if (j > 0) { v = Math.min(v, d[k - nx] + C); if (i > 0) v = Math.min(v, d[k - nx - 1] + D2); if (i < nx - 1) v = Math.min(v, d[k - nx + 1] + D2); } d[k] = v; }
    for (let j = nz - 1; j >= 0; j--) for (let i = nx - 1; i >= 0; i--) { const k = j * nx + i; let v = d[k]; if (i < nx - 1) v = Math.min(v, d[k + 1] + C); if (j < nz - 1) { v = Math.min(v, d[k + nx] + C); if (i < nx - 1) v = Math.min(v, d[k + nx + 1] + D2); if (i > 0) v = Math.min(v, d[k + nx - 1] + D2); } d[k] = v; }
    return [0.4, 0.3].map((r) => {         // 80 cm e 60 cm de passagem
      const lim = r - 0.02, vis = new Uint8Array(n), fila = new Int32Array(n); let q0 = 0, q1 = 0; const s = idx(D.LARGURA / 2, -1.0); vis[s] = 1; fila[q1++] = s;
      while (q0 < q1) { const c = fila[q0++], i = c % nx, j = (c - i) / nx; for (const [di, dj] of [[1, 0], [-1, 0], [0, 1], [0, -1]]) { const a = i + di, b = j + dj; if (a < 0 || b < 0 || a >= nx || b >= nz) continue; const k = b * nx + a; if (!vis[k] && !bl[k] && (d[k] >= lim || forca[k])) { vis[k] = 1; fila[q1++] = k; } } }
      return chaves.map(([x, z]) => { const k = idx(x, z); return k >= 0 && vis[k] ? 1 : 0; });
    });
  };
  const antes = alcance([]);
  return { antes, ok: (extras) => alcance(extras).every((arr, t) => arr.every((v, i) => v >= antes[t][i])) };
}

function analisar(D) {
  const E = D.ESPESSURA || 0.15;
  const paredes = D.paredes.map(([x0, y0, x1, y1, esp = E]) => { const h = y0 === y1; return { h, fixo: h ? y0 : x0, a: (h ? Math.min(x0, x1) : Math.min(y0, y1)) - E / 2, b: (h ? Math.max(x0, x1) : Math.max(y0, y1)) + E / 2, esp }; });
  const paredeDe = (h, fixo, tol) => paredes.filter((w) => w.h === h && Math.abs(w.fixo - fixo) <= tol && w.b - w.a > 0.2).sort((p, q) => Math.abs(p.fixo - fixo) - Math.abs(q.fixo - fixo))[0];
  const interno = (x, z) => D.ambientes.some((a) => !FORA.includes(a.tipo) && x > a.x0 && x < a.x1 && z > a.y0 && z < a.y1);
  const ambienteEm = (x, z) => D.ambientes.find((a) => x > a.x0 && x < a.x1 && z > a.y0 && z < a.y1);
  const janelas = D.janelas.map((j) => { const h = j.seg[1] === j.seg[3], fixo = h ? j.seg[1] : j.seg[0], w = paredeDe(h, fixo, 0.16); return { h, fixo: w ? w.fixo : fixo, a: Math.min(h ? j.seg[0] : j.seg[1], h ? j.seg[2] : j.seg[3]), b: Math.max(h ? j.seg[0] : j.seg[1], h ? j.seg[2] : j.seg[3]), p: j.peitoril, v: j.verga }; });
  const portas = D.portas.map((p) => {
    const d0 = { x: Math.round(Math.cos(p.a0)), z: Math.round(Math.sin(p.a0)) }, d1 = { x: Math.round(Math.cos(p.a1)), z: Math.round(Math.sin(p.a1)) }, h = d0.x !== 0, fixo = h ? p.y : p.x;
    const s0 = h ? p.x : p.y, s1 = s0 + (h ? d0.x : d0.z) * p.r, w = paredeDe(h, fixo, 0.05), cx = p.x + d0.x * p.r / 2, cz = p.y + d0.z * p.r / 2;
    return { id: p.id, H: { x: p.x, z: p.y }, d0, d1, r: p.r, h, fixo, a: Math.min(s0, s1), b: Math.max(s0, s1), esp: w ? w.esp : E, cx, cz, ext: !interno(cx - d1.x * 0.5, cz - d1.z * 0.5) || !interno(cx + d1.x * 0.5, cz + d1.z * 0.5) };
  });
  const cx2 = (ax, az, bx, bz, y0, y1, t, extra) => ({ x0: Math.min(ax, bx), x1: Math.max(ax, bx), z0: Math.min(az, bz), z1: Math.max(az, bz), y0, y1, t, ...extra });
  const obst = (D.MOVEIS || []).map(caixaMovel);
  for (const o of obst.slice()) if (o.m.tipo.startsWith('cama')) obst.push({ x0: o.x0 - 0.6, x1: o.x1 + 0.6, z0: o.z0 - 0.6, z1: o.z1 + 0.6, y0: 0, y1: 1, t: 'margem' });   // 60 cm livres ao lado da cama
  for (const p of portas) {
    const { H, d0, d1, r } = p;
    obst.push(cx2(H.x + d0.x * 0.01, H.z + d0.z * 0.01, H.x + d0.x * 0.08 + d1.x * r, H.z + d0.z * 0.08 + d1.z * r, 0, 2.12, 'folha'));
    obst.push(cx2(H.x, H.z, H.x + (d0.x + d1.x) * r, H.z + (d0.z + d1.z) * r, 0, 2.12, 'giro'));
    obst.push(cx2(H.x - d1.x * 0.75, H.z - d1.z * 0.75, H.x + d0.x * r + d1.x * 0.08, H.z + d0.z * r + d1.z * 0.08, 0, 2.12, 'passo'));
  }
  for (const j of janelas) obst.push(j.h ? { x0: j.a, x1: j.b, z0: j.fixo - 0.5, z1: j.fixo + 0.5, y0: j.p - 0.08, y1: j.v + 0.06, t: 'janela', h: true } : { x0: j.fixo - 0.5, x1: j.fixo + 0.5, z0: j.a, z1: j.b, y0: j.p - 0.08, y1: j.v + 0.06, t: 'janela', h: false });

  const comodos = D.ambientes.map((a) => {
    const mk = (id, h, c, lo, hi, n, th, sx) => {
      const pecas = paredes.filter((w) => w.h === h && Math.abs(w.fixo - c) <= 0.1 && w.b > lo + 0.01 && w.a < hi - 0.01).map((w) => [Math.max(w.a, lo), Math.min(w.b, hi), w.fixo + n * w.esp / 2]);
      const total = pecas.reduce((s, p) => s + p[1] - p[0], 0), maior = pecas.slice().sort((p, q) => (q[1] - q[0]) - (p[1] - p[0]))[0];
      return { id, h, c, lo, hi, n, th, sx, pecas, face: maior && total > (hi - lo) * 0.3 ? maior[2] : c,
        janelas: janelas.filter((j) => j.h === h && Math.abs(j.fixo - c) <= 0.16 && j.b > lo && j.a < hi),
        portas: portas.filter((p) => p.h === h && Math.abs(p.fixo - c) <= 0.1 && p.b > lo && p.a < hi).map((p) => [p.a, p.b]) };
    };
    const lados = [mk('N', true, a.y0, a.x0, a.x1, 1, 0, 1), mk('S', true, a.y1, a.x0, a.x1, -1, PI, -1), mk('O', false, a.x0, a.y0, a.y1, 1, PI / 2, -1), mk('L', false, a.x1, a.y0, a.y1, -1, -PI / 2, 1)];
    const int = { x0: lados[2].face, x1: lados[3].face, z0: lados[0].face, z1: lados[1].face };
    for (const l of lados) {              // trechos cheios, só dentro do cômodo, emendados
      const lo = l.h ? int.x0 : int.z0, hi = l.h ? int.x1 : int.z1, s = [];
      for (const [pa, pb, f] of l.pecas.map((p) => [Math.max(p[0], lo), Math.min(p[1], hi), p[2]]).filter((p) => p[1] - p[0] > 0.02).sort((p, q) => p[0] - q[0])) { const u = s[s.length - 1]; if (u && pa <= u[1] + 0.02 && Math.abs(f - u[2]) < 0.005) u[1] = Math.max(u[1], pb); else s.push([pa, pb, f]); }
      l.solidos = s;
    }
    return { a, tipo: a.tipo, lados, int, sem: semente(D.META.id + a.id), moveis: obst.filter((o) => o.t === 'movel' && o.m.amb === a.id) };
  });

  // pontos que precisam continuar alcançáveis: os dois lados de cada porta, a frente de cada móvel, as laterais e o pé das camas
  const chaves = [];
  for (const p of portas) for (const s of [-1, 1]) chaves.push([p.cx + s * p.d1.x * 0.6, p.cz + s * p.d1.z * 0.6]);
  for (const o of obst) {
    if (o.t !== 'movel' || ['mesaJantar', 'criado', 'mesaCentro', 'cadeira', 'box', 'planta'].includes(o.m.tipo)) continue;
    const m = o.m, f = frenteDe(m), hd = (f.x ? o.x1 - o.x0 : o.z1 - o.z0) / 2, hw = (f.x ? o.z1 - o.z0 : o.x1 - o.x0) / 2;
    if (m.tipo.startsWith('cama')) { chaves.push([m.x + f.x * (hd + 0.3), m.y + f.z * (hd + 0.3)]); for (const s of [-1, 1]) chaves.push([m.x + s * f.z * (hw + 0.3), m.y - s * f.x * (hw + 0.3)]); }
    else chaves.push([m.x + f.x * (hd + 0.45), m.y + f.z * (hd + 0.45)]);
  }
  const solido = (h, fixo, s0, s1) => paredes.some((w) => w.h === h && Math.abs(w.fixo - fixo) < 0.05 && w.a <= s0 + 1e-6 && w.b >= s1 - 1e-6) && !janelas.some((j) => j.h === h && Math.abs(j.fixo - fixo) < 0.05 && j.b > s0 - 0.04 && j.a < s1 + 0.04);
  const naParede = (x, z) => paredes.some((w) => (w.h ? (x > w.a - 0.02 && x < w.b + 0.02 && Math.abs(z - w.fixo) < w.esp / 2 + 0.03) : (z > w.a - 0.02 && z < w.b + 0.02 && Math.abs(x - w.fixo) < w.esp / 2 + 0.03)));
  return { E, paredes, janelas, portas, obst, comodos, chaves, solido, naParede, interno, ambienteEm, grade: fazerGrade(D, paredes, obst, portas, chaves), chao: [], barreiras: [], portao: null };
}

// ---------------------------------------------------------------------------
// A decoração de uma casa
// ---------------------------------------------------------------------------
export function decorar(casa, D, op = PADRAO) {
  const A = analisar(D), ALT = D.PE_DIREITO || 2.8, lote = new Lote(), grupo = new THREE.Group(); grupo.name = 'decor';
  const F = (x, z, th = 0, y0 = 0) => ref(lote, grupo, x, z, th, y0);
  const resumo = {}, nota = (R, s) => { const k = typeof R === 'string' ? R : R.a.id; if (!resumo[k]) resumo[k] = []; resumo[k].push(s); };
  const giram = [], telas = [], balancam = [];
  const registrar = (box, t = 'decor') => { A.obst.push({ ...box, t }); return box; };
  const toca = (a, b) => a.x0 < b.x1 - 0.005 && a.x1 > b.x0 + 0.005 && a.z0 < b.z1 - 0.005 && a.z1 > b.z0 + 0.005 && a.y0 < b.y1 - 0.005 && a.y1 > b.y0 + 0.005;
  const colide = (box, tipos) => A.obst.some((o) => (!tipos || tipos.includes(o.t)) && toca(box, o));
  const semMaquina = (o) => !op.maquina && o.m && o.m.tipo === 'maquina';
  const mv = (R, tipo) => R.moveis.filter((o) => o.m.tipo === tipo && !semMaquina(o)).map((o) => o.m);
  const fm = (m) => F(m.x, m.y, m.rot || 0, 0.04);

  // ---- paredes: trechos livres e fixação -----------------------------------
  const caixaParede = (l, u, larg, face, prof, v0, v1) => { const p0 = Math.min(face, face + l.n * prof), p1 = Math.max(face, face + l.n * prof); return l.h ? { x0: u - larg / 2, x1: u + larg / 2, z0: p0, z1: p1, y0: v0, y1: v1 } : { x0: p0, x1: p1, z0: u - larg / 2, z1: u + larg / 2, y0: v0, y1: v1 }; };
  const refParede = (l, u, face) => (l.h ? F(u, face, l.th) : F(face, u, l.th));
  function livres(l, v0, v1, prof, ign = ['margem', 'tapete']) {
    const out = [];
    for (const [sa, sb, face] of l.solidos) {
      let ivs = [[sa, sb]];
      const corta = (a, b) => { ivs = ivs.flatMap(([x, y]) => (b <= x || a >= y ? [[x, y]] : [[x, Math.min(a, y)], [Math.max(b, x), y]].filter((i) => i[1] - i[0] > 0.02))); };
      for (const [a, b] of l.portas) corta(a - 0.1, b + 0.1);
      const p0 = Math.min(face, face + l.n * prof), p1 = Math.max(face, face + l.n * prof);
      for (const o of A.obst) {
        if (ign.includes(o.t) || o.y0 >= v1 - 1e-3 || o.y1 <= v0 + 1e-3) continue;
        const fg = o.t === 'folha' ? 0.3 : 0, q0 = (l.h ? o.z0 : o.x0) - fg, q1 = (l.h ? o.z1 : o.x1) + fg; if (q0 >= p1 - 0.005 || q1 <= p0 + 0.005) continue;
        corta((l.h ? o.x0 : o.z0) - 0.04, (l.h ? o.x1 : o.z1) + 0.04);
      }
      for (const [a, b] of ivs) out.push([a, b, face]);
    }
    return out;
  }
  function fixar(l, u, larg, v0, v1, prof = 0.04, o = {}) {
    let m = null;
    for (const [a, b, face] of livres(l, v0, v1, prof, o.ign)) { if (b - a < larg + 0.04) continue; const uu = clamp(u, a + larg / 2 + 0.02, b - larg / 2 - 0.02), dv = Math.abs(uu - u); if (dv <= (o.desvio ?? 0) + 1e-6 && (!m || dv < m.dv)) m = { uu, dv, face }; }
    if (!m) return null;
    const box = caixaParede(l, m.uu, larg, m.face, prof, v0, v1);
    if (o.grade) { if (!A.grade.ok([...A.chao, box])) return null; A.chao.push(box); }
    registrar(box);
    return { f: refParede(l, m.uu, m.face), l, u: m.uu, box };
  }
  function naParede(R, larg, v0, v1, prof = 0.04, o = {}) {       // o maior trecho livre do cômodo
    let m = null;
    for (const l of (o.lados || R.lados)) for (const [a, b, face] of livres(l, v0, v1, prof, o.ign)) { if (b - a < larg + 0.12) continue; const n = (b - a) + (o.gosto ? o.gosto(l, (a + b) / 2) : 0); if (!m || n > m.n) m = { l, a, b, n }; }
    return m ? fixar(m.l, (m.a + m.b) / 2, larg, v0, v1, prof, { ...o, desvio: 0.02 }) : null;
  }
  const ladoAtras = (R, m) => { const f = frenteDe(m), l = R.lados.find((q) => (q.h ? (f.x === 0 && f.z === q.n) : (f.z === 0 && f.x === q.n))); if (!l) return null; const b = caixaMovel(m), borda = l.h ? (l.n > 0 ? b.z0 : b.z1) : (l.n > 0 ? b.x0 : b.x1); return Math.abs(borda - l.c) < 0.3 ? l : null; };
  const uDe = (l, m) => (l.h ? m.x : m.y);

  // ---- chão: encostado numa parede, fora do caminho --------------------------
  function noChao(R, w, d, o = {}) {
    const alt = o.alt ?? 0.5, cands = [];
    for (const l of R.lados) for (const [a, b, face] of l.solidos) {
      const us = []; for (let u = a + w / 2 + 0.03; u < b - w / 2 - 0.03; u += 0.1) us.push(u); if (b - a >= w + 0.06) us.push(b - w / 2 - 0.03);
      for (const u of us) {
        const box = caixaParede(l, u, w, face + l.n * 0.01, d, 0.04, 0.04 + alt);
        if (box.x0 < R.int.x0 || box.x1 > R.int.x1 || box.z0 < R.int.z0 || box.z1 > R.int.z1) continue;
        if (A.obst.some((q) => q.t !== 'tapete' && toca(box, q))) continue;
        const cx = (box.x0 + box.x1) / 2, cz = (box.z0 + box.z1) / 2;
        const sobJanela = A.obst.some((q) => q.t === 'janela' && box.x0 < q.x1 && box.x1 > q.x0 && box.z0 < q.z1 && box.z1 > q.z0) ? 4 : 0;
        cands.push({ box, l, u, face, n: sobJanela + (o.gosto ? o.gosto(cx, cz) : (l.h ? Math.min(u - R.int.x0, R.int.x1 - u) : Math.min(u - R.int.z0, R.int.z1 - u))) });
      }
    }
    cands.sort((p, q) => p.n - q.n);
    for (const c of cands.slice(0, 14)) if (A.grade.ok([...A.chao, c.box])) { A.chao.push(c.box); registrar(c.box); const cx = (c.box.x0 + c.box.x1) / 2, cz = (c.box.z0 + c.box.z1) / 2; return { f: F(cx, cz, c.l.th, 0.04), cx, cz, l: c.l }; }
    return null;
  }
  function tapete(R, cx, cz, w, d, cor, o = {}) {
    const box = { x0: cx - w / 2, x1: cx + w / 2, z0: cz - d / 2, z1: cz + d / 2, y0: 0.04, y1: 0.06 };
    if (box.x0 < R.int.x0 + 0.05 || box.x1 > R.int.x1 - 0.05 || box.z0 < R.int.z0 + 0.05 || box.z1 > R.int.z1 - 0.05) return false;
    if (colide(box, ['movel', 'tapete', 'decor', 'giro', 'passo'])) return false;
    registrar(box, 'tapete'); const f = F(cx, cz, 0, 0.04);
    if (o.macio) f.mc(w, 0.02, d, cor, 0, 0, 0); else { f.cx(w, 0.008, d, tom(cor, 0.78), 0, 0, 0); f.cx(w - 0.1, 0.01, d - 0.1, cor, 0, 0, 0); const ao = d > w, n = Math.max(2, Math.round((ao ? d : w) / 0.28)); for (let i = 1; i < n; i++) f.cx(ao ? w - 0.1 : 0.03, 0.011, ao ? 0.03 : d - 0.1, tom(cor, 1.35), ao ? 0 : -w / 2 + w * i / n, 0, ao ? -d / 2 + d * i / n : 0); }
    return true;
  }
  const tapeteLocal = (R, m, lx, lz, w, d, cor, o) => { const f = fm(m), [cx, cz] = f.W(lx, lz), q = Math.abs(Math.round((m.rot || 0) / (PI / 2))) % 2; return tapete(R, cx, cz, q ? d : w, q ? w : d, cor, o); };

  // ---- peças prontas ---------------------------------------------------------
  function vasoPlanta(f, lx, lz, s, rnd, tipo = 'espada', corVaso = '#C56A4A') {
    f.co(0.34 * s, 0.3 * s, corVaso, lx, 0, lz, { rx: PI }); f.ci(0.3 * s, 0.02, '#4A3B2E', lx, 0.285 * s, lz);
    if (tipo === 'espada') for (let i = 0; i < 9; i++) { const a = rnd() * 2 * PI, r = (0.02 + rnd() * 0.07) * s, h = (0.42 + rnd() * 0.32) * s; f.po(0.075 * s, h, i % 3 ? '#4F7A3A' : '#8AA24B', lx + Math.cos(a) * r, 0.28 * s, lz + Math.sin(a) * r, { rx: (rnd() - 0.5) * 0.28, rz: (rnd() - 0.5) * 0.28, dz: 0.03 * s }); }
    else for (let i = 0; i < 7; i++) { const a = rnd() * 2 * PI, r = rnd() * 0.12 * s, d = (0.2 + rnd() * 0.14) * s; f.es(d, d * 0.85, d, ['#4C7A3A', '#5F8F48', '#3E6A31'][i % 3], lx + Math.cos(a) * r, (0.3 + rnd() * 0.28) * s, lz + Math.sin(a) * r); }
  }
  function quadro(pos, w, h, variante, o = {}) {
    const est = o.estilo || op.quadros, W = w >= h ? 256 : Math.round(256 * w / h), H = w >= h ? Math.round(256 * h / w) : 256;
    const chave = `q|${est}|${variante}|${W}x${H}|${est === 'projeto' && variante === 0 ? D.META.id : ''}|${o.sem || 0}`;
    const t = tex(chave, W, H, (g) => arte(g, W, H, est, variante, aleatorio(semente(chave)), D)), y = 1.5 - h / 2 + (o.dy || 0), lx = o.lx || 0;
    pos.f.cx(w, h, 0.028, o.moldura || ['#2B2B2B', '#8B6644', '#C9A77E', '#3E4A57'][(o.sem || 0) % 4], lx, y, 0.014);
    pos.f.malha(new THREE.Mesh(GEO.plano, matTex(chave, t)), lx, y + h / 2, 0.0292).scale.set(w - 0.05, h - 0.05, 1);
  }
  function quadrosLivres(R, n, tamanhos, o = {}) {
    let feitos = 0;
    for (let i = 0; i < n; i++) for (const [w, h] of tamanhos) { const pos = naParede(R, w, 1.5 - h / 2 - 0.03, 1.5 + h / 2 + 0.03, 0.04, o); if (pos) { quadro(pos, w, h, (R.sem + i + (o.v0 || 0)) % 4, { sem: R.sem + i }); feitos++; break; } }
    if (feitos) nota(R, feitos + (feitos > 1 ? ' quadros' : ' quadro')); return feitos;
  }
  function prateleira(pos, larg, y, rnd, o = {}) {
    const f = pos.f; f.cx(larg, 0.03, 0.2, '#9B7653', 0, y, 0.1); for (const s of [-1, 1]) f.cx(0.016, 0.05, 0.15, '#8E9196', s * (larg / 2 - 0.08), y - 0.05, 0.075);
    let x = -larg / 2 + 0.05; const fim = larg / 2 - 0.05, topo = y + 0.03;
    if (o.servico) { f.cx(0.16, 0.22, 0.09, '#3D8FBF', x + 0.1, topo, 0.1); f.cx(0.16, 0.05, 0.091, '#F2C14E', x + 0.1, topo + 0.09, 0.1); f.ci(0.09, 0.2, '#E7A6C0', x + 0.28, topo, 0.1); f.ci(0.04, 0.04, '#B5567E', x + 0.28, topo + 0.2, 0.1); f.ci(0.08, 0.17, '#F4F1EC', x + 0.41, topo, 0.1); f.ci(0.035, 0.035, '#3D8FBF', x + 0.41, topo + 0.17, 0.1); return; }
    const nl = 4 + Math.floor(rnd() * 3);
    for (let i = 0; i < nl && x < fim - 0.3; i++) { const e = 0.026 + rnd() * 0.02, h = 0.17 + rnd() * 0.08; f.cx(e, h, 0.14, PAL[Math.floor(rnd() * 6)], x + e / 2, topo, 0.1, i === nl - 1 ? { rz: -0.22 } : undefined); x += e + 0.004; }
    x += 0.09; if (x < fim - 0.2) { f.ci(0.09, 0.11, '#F1E7D3', x, topo, 0.1); f.es(0.11, 0.1, 0.11, '#5F8F48', x, topo + 0.09, 0.1); x += 0.16; }
    if (x < fim - 0.14) { f.cx(0.2, 0.025, 0.14, PAL[2], x + 0.08, topo, 0.1); f.cx(0.18, 0.022, 0.13, PAL[0], x + 0.08, topo + 0.025, 0.1, { ry: 0.2 }); x += 0.26; }
    if (x < fim - 0.06) { f.cx(0.13, 0.16, 0.012, '#2B2B2B', x + 0.06, topo, 0.12, { rx: -0.15 }); f.cx(0.1, 0.13, 0.004, PAL[1], x + 0.06, topo + 0.015, 0.128, { rx: -0.15 }); }   // porta-retratos sem rosto: só uma cor
  }

  // ---- portas: folha aberta, maçaneta, batente, guarnição e interruptor ---------
  function portasDecor() {
    const BR = '#F4F1EC', MET = '#C9CCD0';
    for (const p of A.portas) {
      const { H, d0, d1, r, esp } = p, cor = p.ext ? '#7B5539' : '#B98F63', esc = tom(cor, 0.86);
      const f = F(H.x + d0.x * 0.04, H.z + d0.z * 0.04, Math.atan2(-d1.z, d1.x), 0.04), len = r - esp / 2 - 0.02, c0 = esp / 2 + 0.01 + len / 2;
      f.cx(len, 2.05, 0.032, cor, c0, 0, 0, { sombra: true });
      for (const s of [-1, 1]) {
        f.cx(len - 0.2, 0.82, 0.004, esc, c0, 1.1, s * 0.017); f.cx(len - 0.2, 0.78, 0.004, esc, c0, 0.18, s * 0.017);
        f.ci(0.05, 0.012, MET, c0 + len / 2 - 0.07, 1.0, s * 0.022, { rx: PI / 2, centro: true }); f.cx(0.11, 0.018, 0.018, MET, c0 + len / 2 - 0.115, 0.991, s * 0.046);
      }
      const g = F(H.x, H.z, Math.atan2(-d0.z, d0.x), 0.04);
      g.cx(0.02, 2.07, esp + 0.012, BR, 0.01, 0, 0); g.cx(0.02, 2.07, esp + 0.012, BR, r - 0.01, 0, 0); g.cx(r, 0.02, esp + 0.012, BR, r / 2, 2.05, 0);
      const dir = p.h ? d0.x : d0.z, s0 = p.h ? H.x : H.z, tem = (la) => A.solido(p.h, p.fixo, s0 + dir * la - 0.03, s0 + dir * la + 0.03);
      for (const s of [-1, 1]) {
        if (tem(-0.035)) g.cx(0.06, 2.07, 0.012, BR, -0.03, 0, s * (esp / 2 + 0.006)); if (tem(r + 0.035)) g.cx(0.06, 2.07, 0.012, BR, r + 0.03, 0, s * (esp / 2 + 0.006));
        g.cx(r + (tem(-0.035) ? 0.06 : 0) + (tem(r + 0.035) ? 0.06 : 0), 0.06, 0.012, BR, r / 2 + ((tem(r + 0.035) ? 0.03 : 0) - (tem(-0.035) ? 0.03 : 0)), 2.07, s * (esp / 2 + 0.006));
      }
      // interruptor do lado da maçaneta, na face para onde a porta abre (senão, na outra face)
      for (const s of [1, -1]) {
        const la = r + 0.17, u = s0 + dir * la; if (!A.solido(p.h, p.fixo, u - 0.06, u + 0.06)) break;
        const n = { x: s * d1.x, z: s * d1.z }, face = p.fixo + (p.h ? n.z : n.x) * esp / 2, x = p.h ? u : face, z = p.h ? face : u;
        const box = { x0: x - (p.h ? 0.06 : 0) + Math.min(0, n.x * 0.03), x1: x + (p.h ? 0.06 : 0) + Math.max(0, n.x * 0.03), z0: z - (p.h ? 0 : 0.06) + Math.min(0, n.z * 0.03), z1: z + (p.h ? 0 : 0.06) + Math.max(0, n.z * 0.03), y0: 1.02, y1: 1.3 };
        if (colide(box, ['movel', 'folha', 'janela', 'decor']) || !A.interno(x + n.x * 0.2, z + n.z * 0.2)) continue;
        registrar(box); const q = F(x, z, Math.atan2(n.x, n.z)); q.cx(0.075, 0.115, 0.01, BR, 0, 1.1, 0.005); q.cx(0.03, 0.045, 0.006, '#DDD8CE', 0, 1.135, 0.011); break;
      }
    }
    nota('casa', `${A.portas.length} portas com folha, maçaneta, guarnição e interruptor`);
  }

  // ---- cortinas (sala e quartos): ao lado da janela, sem tampar o vidro ----------
  function cortinas(R) {
    if (!['sala', 'dorm', 'casal'].includes(R.tipo)) return;
    const cor = ['#EFE7D8', '#E6EAEA', '#EADDCB'][R.sem % 3];
    for (const l of R.lados) for (const j of l.janelas) {
      const peca = l.solidos.find((s) => s[0] <= j.a + 0.02 && s[1] >= j.b - 0.02); if (!peca) continue;
      const [pa, pb, face] = peca, topo = j.v + 0.12, feitos = [], meio = (j.a + j.b) / 2;
      for (const lado of [-1, 1]) {
        const borda = lado < 0 ? j.a : j.b; let u0 = borda + lado * 0.27, u1 = borda - lado * 0.06; if (u0 > u1) [u0, u1] = [u1, u0];
        u0 = Math.max(u0, pa + 0.03); u1 = Math.min(u1, pb - 0.03); if (u1 - u0 < 0.2) continue;
        for (const baixo of [0.14, j.p - 0.25]) { const box = caixaParede(l, (u0 + u1) / 2, u1 - u0, face, 0.1, baixo, topo); if (colide(box, ['movel', 'folha', 'decor'])) continue; registrar(box); feitos.push([u0, u1, baixo]); break; }
      }
      const f = refParede(l, meio, face), lx = (u) => (u - meio) * l.sx;
      if (feitos.length) {
        const e0 = Math.min(j.a, ...feitos.map((q) => q[0])) - 0.04, e1 = Math.max(j.b, ...feitos.map((q) => q[1])) + 0.04;
        f.ci(0.022, e1 - e0, '#6B6258', lx((e0 + e1) / 2), topo + 0.02, 0.06, { rz: PI / 2, centro: true }); for (const e of [e0, e1]) f.es(0.04, 0.04, 0.04, '#6B6258', lx(e), topo, 0.06);
        for (const [u0, u1, baixo] of feitos) { const nn = Math.max(3, Math.round((u1 - u0) / 0.075)); for (let i = 0; i < nn; i++) f.ci((u1 - u0) / nn * 1.3, topo - baixo, i % 2 ? cor : tom(cor, 0.94), lx(u0 + (u1 - u0) * (i + 0.5) / nn), baixo, 0.06); }
        nota(R, feitos.some((q) => q[2] > 0.2) ? 'cortina curta' : 'cortina');
      } else { f.cx(j.b - j.a + 0.06, 0.1, 0.06, '#E9E4DA', 0, j.v - 0.08, 0.03); nota(R, 'persiana recolhida'); }
    }
  }

  // ---- luz do teto ---------------------------------------------------------------
  function luminaria(R) {
    const a = R.a, f = F((a.x0 + a.x1) / 2, (a.y0 + a.y1) / 2);
    if (R.tipo === 'dorm' || R.tipo === 'casal') {              // ventilador de teto com luz, girando devagar
      f.ci(0.03, 0.22, '#EDEAE4', 0, ALT - 0.22, 0); f.ci(0.2, 0.1, '#EDEAE4', 0, ALT - 0.32, 0); f.lu(0.17, 0.1, 0.17, 0, ALT - 0.41, 0);
      const pas = new THREE.InstancedMesh(GEO.caixa, MATS.get('pa') || MATS.set('pa', new THREE.MeshStandardMaterial({ color: '#B98F63', roughness: 0.7 })).get('pa'), 3), o = new THREE.Object3D();
      for (let k = 0; k < 3; k++) { const an = k * 2 * PI / 3; o.position.set(Math.cos(an) * 0.36, 0, -Math.sin(an) * 0.36); o.rotation.set(0, an, 0); o.scale.set(0.52, 0.012, 0.13); o.updateMatrix(); pas.setMatrixAt(k, o.matrix); }
      pas.position.set(f.x, ALT - 0.27, f.z); pas.rotation.y = (R.sem % 6); grupo.add(pas); giram.push(pas); nota(R, 'ventilador de teto');
    } else if (R.tipo === 'sala' || R.tipo === 'cozinha') {
      f.ci(0.1, 0.025, '#EDEAE4', 0, ALT - 0.025, 0); f.cx(0.008, 0.42, 0.008, '#3A3A3A', 0, ALT - 0.445, 0); f.co(0.38, 0.2, R.tipo === 'sala' ? '#E0A23A' : '#F4F1EC', 0, ALT - 0.64, 0); f.lu(0.1, 0.1, 0.1, 0, ALT - 0.67, 0); nota(R, 'pendente');
    } else { f.ci(0.3, 0.045, '#F4F1EC', 0, ALT - 0.045, 0); f.lu(0.24, 0.03, 0.24, 0, ALT - 0.07, 0); nota(R, 'plafon'); }
  }

  // ---- móveis da planta ganham o que fica em cima -----------------------------------
  function mesaJantar(m) {
    const f = fm(m), jogo = ['#8A9A86', '#D9A08B', '#2F5D73'][semente(D.META.id) % 3];
    for (const sx of [-1, 1]) for (const sz of [-0.3, 0.3]) { f.cx(0.3, 0.006, 0.38, jogo, sx * (m.w / 2 - 0.18), 0.775, sz); f.ci(0.2, 0.012, '#FDFBF5', sx * (m.w / 2 - 0.18), 0.781, sz); }
    f.ci(0.09, 0.24, '#C8553D', 0, 0.775, m.d / 2 - 0.16); f.ci(0.065, 0.05, '#2B2B2B', 0, 1.015, m.d / 2 - 0.16); f.cx(0.02, 0.12, 0.03, '#2B2B2B', 0.055, 0.86, m.d / 2 - 0.16);       // garrafa térmica do café
    f.co(0.26, 0.07, '#B98F63', 0, 0.775, -m.d / 2 + 0.2, { rx: PI }); [['#E8862E', -0.05, 0.02], ['#E8862E', 0.05, -0.03], ['#F2C230', 0.0, 0.06], ['#C8553D', 0.01, -0.07], ['#7BA05B', -0.06, -0.05]].forEach(([c, dx, dz], i) => f.es(0.085, 0.08, 0.085, c, dx, 0.81 + (i === 2 ? 0.03 : 0), -m.d / 2 + 0.2 + dz));
  }
  function sofa(R, m) {
    const f = fm(m), ac = { salvia: ['#E0A23A', '#F1E7D3'], cinza: ['#E0A23A', '#3C4F6B'], marinho: ['#E8D6B5', '#C8553D'], terracota: ['#F1E7D3', '#8A9A86'], caramelo: ['#2F5D73', '#F1E7D3'] }[op.sofa] || ['#E0A23A', '#F1E7D3'];
    f.mc(0.36, 0.34, 0.12, ac[0], m.w / 2 - 0.42, 0.5, -m.d / 2 + 0.32, { rx: -0.25, ry: -0.15 });
    if (m.w >= 1.9) f.mc(0.3, 0.28, 0.11, ac[1], 0.05, 0.5, -m.d / 2 + 0.32, { rx: -0.25 });
    f.mc(0.24, 0.03, m.d * 0.55, ac[1], m.w / 2 - 0.1, 0.572, 0.06); f.cx(0.02, 0.26, m.d * 0.55, ac[1], m.w / 2 - 0.212, 0.33, 0.06);      // manta no braço
    nota(R, 'almofadas e manta no sofá');
    const l = ladoAtras(R, m); if (!l) return;
    if (m.w >= 1.9) { const pos = fixar(l, uDe(l, m), 1.3, 1.2, 1.8, 0.04, { desvio: 0.35 }); if (pos) { [-0.45, 0, 0.45].forEach((lx, i) => quadro(pos, 0.36, 0.48, (R.sem + i) % 4, { lx, sem: R.sem + i, moldura: '#2B2B2B' })); nota(R, 'trio de quadros sobre o sofá'); return; } }
    const pos = fixar(l, uDe(l, m), 0.8, 1.2, 1.8, 0.04, { desvio: 0.3 }); if (pos) { quadro(pos, 0.8, 0.55, R.sem % 4, { sem: R.sem }); nota(R, 'quadro sobre o sofá'); }
  }
  function rack(R, m) {
    const f = fm(m), rnd = aleatorio(R.sem + 5);
    f.cx(0.34, 0.05, 0.16, '#222222', 0, 0.45, -0.08); f.cx(0.22, 0.035, 0.15, '#2B2B2B', -0.3, 0.45, 0.07); f.cx(0.006, 0.006, 0.006, '#59D36B', -0.22, 0.465, 0.146);
    vasoPlanta(f, m.w / 2 - 0.1, 0.02, 0.42, rnd, 'moita', '#F1E7D3'); f.cx(0.2, 0.03, 0.15, PAL[2], -m.w / 2 + 0.13, 0.45, 0.02); f.cx(0.18, 0.025, 0.14, PAL[1], -m.w / 2 + 0.13, 0.48, 0.02, { ry: 0.25 });
    const tela = new THREE.Mesh(GEO.plano, matTex('tv', tex('tv', 256, 144, (g, W, H) => arte(g, W, H, 'paisagens', 1, aleatorio(7), D)), { basico: true })); tela.scale.set(1.14, 0.64, 1); tela.visible = false; f.malha(tela, 0, 0.85, -0.054); telas.push(tela);
    nota(R, 'TV (acende à noite), aparelho, vaso e livros no rack');
    const l = ladoAtras(R, m); if (!l) return; const larg = Math.min(1.2, m.w), pos = fixar(l, uDe(l, m), larg, 1.48, 1.84, 0.22, { desvio: 0.2 });
    if (pos) { prateleira(pos, larg, 1.5, rnd); nota(R, 'prateleira com livros'); }
  }
  function mesaCentro(R, m) {
    const f = fm(m); f.cx(0.2, 0.025, 0.27, PAL[0], 0.12, 0.38, -0.3, { ry: 0.2 }); f.cx(0.18, 0.02, 0.25, PAL[2], 0.12, 0.405, -0.3, { ry: -0.1 });
    f.ci(0.075, 0.09, '#F4F1EC', -0.12, 0.38, 0.3); f.cx(0.012, 0.05, 0.04, '#F4F1EC', -0.165, 0.4, 0.3); f.ci(0.06, 0.004, '#4A3526', -0.12, 0.462, 0.3); f.cx(0.045, 0.015, 0.16, '#222222', 0.15, 0.38, 0.27, { ry: 0.5 });
    nota(R, 'livros, caneca de café e controle na mesa de centro');
  }
  function bancada(R, m) {
    const f = fm(m), lc = Math.min(0.6, m.w * 0.45), ls = Math.min(0.55, m.w * 0.4), xc = Math.min(0.8, m.w / 2 - lc / 2 - 0.03), xs = -Math.min(0.5, m.w / 2 - ls / 2 - 0.03), k = lc / 0.6, T = 0.9;
    f.ci(0.17 * k, 0.1, '#3A3A3A', xc - 0.14 * k, T + 0.015, -0.12); f.ci(0.18 * k, 0.012, '#6A6A6A', xc - 0.14 * k, T + 0.115, -0.12); f.es(0.035, 0.03, 0.035, '#222222', xc - 0.14 * k, T + 0.125, -0.12); f.cx(0.24 * k, 0.015, 0.025, '#222222', xc - 0.14 * k, T + 0.085, -0.12);
    f.ci(0.19 * k, 0.035, '#222222', xc + 0.14 * k, T + 0.015, 0.12); f.cx(0.15, 0.014, 0.025, '#222222', xc + 0.14 * k, T + 0.035, 0.12 + 0.16, { ry: PI / 2 });
    f.ci(0.026, 0.2, '#C9CCD0', xs, T, -m.d / 2 + 0.07); f.cx(0.02, 0.02, 0.15, '#C9CCD0', xs, T + 0.19, -m.d / 2 + 0.14); f.cx(0.05, 0.13, 0.035, '#E8C547', xs + ls / 2 - 0.02, T, -m.d / 2 + 0.06); f.cx(0.08, 0.025, 0.05, '#7BB661', xs - ls / 2 + 0.07, T, -m.d / 2 + 0.06);
    const g0 = xs + ls / 2 + 0.03, g1 = xc - lc / 2 - 0.03, gw = Math.min(0.38, g1 - g0);
    if (gw >= 0.2) { const gx = (g0 + g1) / 2; f.cx(gw, 0.02, 0.3, '#D9DCDF', gx, T, 0.02); for (const s of [-1, 1]) f.cx(gw, 0.09, 0.008, '#B9BEC3', gx, T + 0.02, 0.02 + s * 0.146); const np = Math.max(2, Math.floor((gw - 0.12) / 0.045)); for (let i = 0; i < np; i++) f.ci(0.2, 0.012, '#FDFBF5', gx - gw / 2 + 0.05 + i * 0.045, T + 0.125, -0.02, { rz: PI / 2 - 0.12, centro: true }); f.ci(0.07, 0.09, '#9CC5D6', gx + gw / 2 - 0.06, T + 0.02, 0.1); nota(R, 'escorredor com pratos'); }
    nota(R, 'panela, frigideira, torneira e detergente na bancada');
    const l = ladoAtras(R, m); if (!l) return; const u = uDe(l, m); let fez = false;
    for (const [a, b, face] of livres(l, 1.45, 2.12, 0.34)) {       // armário aéreo só onde não há janela
      const a2 = Math.max(a, u - m.w / 2), b2 = Math.min(b, u + m.w / 2), w = b2 - a2; if (w < 0.4) continue;
      registrar(caixaParede(l, (a2 + b2) / 2, w, face, 0.33, 1.47, 2.1)); const q = refParede(l, (a2 + b2) / 2, face), n = Math.max(1, Math.round(w / 0.45));
      q.cx(w, 0.62, 0.32, '#F2EEE7', 0, 1.47, 0.16); for (let i = 0; i < n; i++) { const x = -w / 2 + w / n * (i + 0.5); q.cx(w / n - 0.012, 0.6, 0.012, '#E6E0D4', x, 1.48, 0.326); q.cx(0.012, 0.12, 0.014, '#9AA0A6', x + (i % 2 ? -1 : 1) * (w / n / 2 - 0.05), 1.52, 0.339); }
      fez = true;
    }
    nota(R, fez ? 'armário aéreo sobre a bancada' : 'sem armário aéreo (a janela fica em cima da bancada)');
    tapeteLocal(R, m, 0, m.d / 2 + 0.34, Math.min(m.w - 0.2, 1.3), 0.5, '#B9785A') && nota(R, 'passadeira');
  }
  function geladeira(R, m) {
    const f = fm(m), z = m.d / 2;
    f.cx(m.w - 0.04, 0.008, 0.006, '#AEB3B8', 0, 0.86, z + 0.002); f.cx(0.022, 0.24, 0.02, '#9AA0A6', -m.w / 2 + 0.08, 0.92, z + 0.012); f.cx(0.022, 0.3, 0.02, '#9AA0A6', -m.w / 2 + 0.08, 0.5, z + 0.012);
    [[0.1, 1.12, '#C8553D'], [0.2, 1.05, '#E0A23A'], [0.05, 0.98, '#2F5D73'], [0.22, 1.18, '#7BB661']].forEach(([x, y, c]) => f.cx(0.04, 0.04, 0.008, c, x, y, z + 0.004)); f.cx(0.13, 0.17, 0.004, '#FDFBF5', 0.12, 0.62, z + 0.002, { rz: 0.06 });      // ímãs e um recado
    f.cx(0.46, 0.26, 0.34, '#E9EAEB', 0, 1.3, 0); f.cx(0.3, 0.2, 0.01, '#1E2226', -0.06, 1.33, 0.171); f.cx(0.1, 0.2, 0.01, '#C9CCD0', 0.17, 1.33, 0.171);
    registrar({ x0: m.x - 0.36, x1: m.x + 0.36, z0: m.y - 0.36, z1: m.y + 0.36, y0: 1.3, y1: 1.62 }); nota(R, 'micro-ondas em cima da geladeira, ímãs e recado');
  }
  function cama(R, m, i) {
    const f = fm(m), base = op.cama === 'planta' ? m.manta : corDe('cama', op.cama), casal = m.tipo === 'camaCasal', acs = ['#E0A23A', '#C8553D', '#2F5D73', '#8A9A86', '#F1E7D3'], ac = acs[(R.sem + i) % 5];
    f.mc(m.w, 0.03, 0.4, tom(base, 0.74), 0, 0.555, m.d / 2 - 0.28);                                    // peseira
    if (casal) for (const s of [-1, 1]) f.mc(0.34, 0.3, 0.1, s < 0 ? ac : tom(base, 0.74), s * 0.3, 0.55, -m.d / 2 + 0.6, { rx: -0.5 }); else f.mc(0.32, 0.28, 0.1, ac, 0, 0.55, -m.d / 2 + 0.6, { rx: -0.5 });
    if (R.tipo === 'dorm' && i === 0) {       // bicho de pelúcia: só bolinhas, sem rosto
      const b = '#B5835A', x = m.w / 2 - 0.24, z = 0.05; f.es(0.17, 0.19, 0.15, b, x, 0.56, z); f.es(0.13, 0.13, 0.12, b, x, 0.73, z); for (const s of [-1, 1]) { f.es(0.05, 0.05, 0.03, b, x + s * 0.05, 0.84, z); f.es(0.06, 0.06, 0.09, b, x + s * 0.08, 0.57, z + 0.08); f.es(0.05, 0.08, 0.05, b, x + s * 0.09, 0.64, z + 0.03); }
      nota(R, 'bicho de pelúcia na cama');
    }
    const lados = [[m.w / 2 + 0.4, 0.15], [-(m.w / 2 + 0.4), 0.15]]; if ((R.sem + i) % 2) lados.reverse();
    for (const [lx, lz] of lados) if (tapeteLocal(R, m, lx, lz, 0.6, 1.1, ['#C9B59A', '#9DB0B8', '#C9A0A0'][(R.sem + i) % 3])) { nota(R, 'tapete ao lado da cama'); break; }
  }
  function criado(R, m, i) {
    const f = fm(m); f.co(0.24, 0.15, ['#F3E6C8', '#E9D3B0'][i % 2], 0, 0.66, 0); f.cx(0.13, 0.02, 0.17, PAL[(R.sem + i) % 6], 0.14, 0.5, 0.09, { ry: 0.15 }); f.cx(0.06, 0.008, 0.12, '#222222', -0.15, 0.5, 0.11, { ry: -0.2 });
  }
  function armario(R, m, i) {                 // malas em cima do guarda-roupa
    const f = fm(m); if (m.w < 1.2) return;
    f.mc(0.62, 0.22, Math.min(0.4, m.d - 0.04), PAL[(R.sem + i) % 6], -m.w / 2 + 0.4, 1.25, 0); f.cx(0.16, 0.02, 0.03, '#2B2B2B', -m.w / 2 + 0.4, 1.33, m.d / 2 - 0.02); f.cx(0.5, 0.2, Math.min(0.34, m.d - 0.06), '#B99A6B', m.w / 2 - 0.36, 1.25, 0); f.cx(0.52, 0.03, Math.min(0.36, m.d - 0.04), '#A88957', m.w / 2 - 0.36, 1.45, 0);
    registrar({ x0: m.x - Math.max(m.w, m.d) / 2, x1: m.x + Math.max(m.w, m.d) / 2, z0: m.y - Math.max(m.w, m.d) / 2, z1: m.y + Math.max(m.w, m.d) / 2, y0: 1.29, y1: 1.52 }); if (i === 0) nota(R, 'mala e caixa em cima do guarda-roupa');
  }
  function escrivaninha(R, m) {
    const f = fm(m), rnd = aleatorio(R.sem + 9), T = 0.76;
    f.cx(0.3, 0.012, 0.1, '#DADDE0', 0, T, 0.1); f.mc(0.05, 0.02, 0.08, '#2B2B2B', 0.24, T, 0.11); f.ci(0.07, 0.09, PAL[2], -m.w / 2 + 0.09, T, -0.13);
    for (let i = 0; i < 3; i++) f.cx(0.008, 0.15, 0.008, PAL[i], -m.w / 2 + 0.08 + i * 0.012, T + 0.04, -0.13, { rz: (i - 1) * 0.15 });
    for (let i = 0; i < 3; i++) f.cx(0.03, 0.2 - i * 0.02, 0.14, PAL[(i + 3) % 6], m.w / 2 - 0.05 - i * 0.034, T, -0.14);
    nota(R, 'teclado, lápis e livros na escrivaninha');
    const l = ladoAtras(R, m); if (!l) return; const larg = Math.min(0.9, m.w), pos = fixar(l, uDe(l, m), larg, 1.4, 1.76, 0.22, { desvio: 0.15 });
    if (pos) { prateleira(pos, larg, 1.42, rnd); nota(R, 'prateleira com livros'); }
  }
  function pia(R, m) {
    const f = fm(m), T = 0.86;
    f.ci(0.022, 0.13, '#C9CCD0', 0, T, -m.d / 2 + 0.09); f.cx(0.018, 0.018, 0.1, '#C9CCD0', 0, T + 0.12, -m.d / 2 + 0.13); f.ci(0.05, 0.08, '#9CC5D6', m.w / 2 - 0.11, T, -0.07);
    f.cx(0.008, 0.14, 0.008, '#C8553D', m.w / 2 - 0.115, T + 0.02, -0.07, { rz: 0.15 }); f.cx(0.008, 0.14, 0.008, '#2F5D73', m.w / 2 - 0.1, T + 0.02, -0.07, { rz: -0.12 }); f.mc(0.08, 0.025, 0.055, '#F3E6C8', -m.w / 2 + 0.12, T, -0.06);
    const l = ladoAtras(R, m); if (!l) return;
    for (const [v0, v1] of [[1.1, 1.78], [1.02, 1.5]]) { const larg = Math.min(m.w, 0.5), pos = fixar(l, uDe(l, m), larg, v0, v1, 0.03, { desvio: 0.12 }); if (pos) { espelho(pos, larg, v1 - v0, v0); nota(R, 'espelho sobre a pia, copo com escovas e sabonete'); return; } }
  }
  function espelho(pos, w, h, y) {
    const t = tex('espelho', 64, 128, (g, W, H) => { const gr = g.createLinearGradient(0, 0, W, H); gr.addColorStop(0, '#DCEAF0'); gr.addColorStop(0.45, '#B7CBD6'); gr.addColorStop(0.5, '#EEF6F8'); gr.addColorStop(0.58, '#BCD0DA'); gr.addColorStop(1, '#A9BFCC'); g.fillStyle = gr; g.fillRect(0, 0, W, H); });
    pos.f.cx(w, h, 0.022, '#3A3A3A', 0, y, 0.011); pos.f.malha(new THREE.Mesh(GEO.plano, matTex('espelho', t, { rough: 0.25 })), 0, y + h / 2, 0.0232).scale.set(w - 0.04, h - 0.04, 1);
  }
  function box(R, m) {
    const f = fm(m), tentativas = [[m.w / 2, 0, -PI / 2, m.d], [0, -m.d / 2, 0, m.w]];        // parede do lado +x e parede do fundo do box
    for (const [lx, lz, dth, comp] of tentativas) {
      const [wx, wz] = f.W(lx + Math.sign(lx) * 0.07, lz + Math.sign(lz) * 0.07); if (!A.naParede(wx, wz)) continue;
      const [cx, cz] = f.W(lx * 0.86, lz * 0.86); if (colide({ x0: cx - 0.15, x1: cx + 0.15, z0: cz - 0.15, z1: cz + 0.15, y0: 1.05, y1: 1.35 }, ['janela', 'decor'])) continue;
      const q = f.sub(lx, lz, dth, 0), off = Math.min(0.12, comp / 2 - 0.2);
      q.cx(0.28, 0.015, 0.1, '#C9CCD0', off, 1.1, 0.05); q.ci(0.055, 0.17, '#7BB661', off - 0.08, 1.115, 0.05); q.ci(0.03, 0.03, '#FDFBF5', off - 0.08, 1.285, 0.05); q.ci(0.05, 0.14, '#F4F1EC', off, 1.115, 0.05); q.ci(0.028, 0.03, '#2F5D73', off, 1.255, 0.05); q.mc(0.07, 0.025, 0.05, '#E7A6C0', off + 0.09, 1.115, 0.05);
      nota(R, 'porta-shampoo no box'); return;
    }
  }
  function vaso(R, m) {
    const l = ladoAtras(R, m); if (!l) return;
    for (const s of [1, -1]) { const pos = fixar(l, uDe(l, m) + s * 0.36, 0.16, 0.55, 0.82, 0.12, { desvio: 0.06 }); if (pos) { pos.f.cx(0.02, 0.02, 0.09, '#C9CCD0', 0, 0.7, 0.045); pos.f.ci(0.11, 0.1, '#FAFAFA', 0, 0.69, 0.08, { rz: PI / 2, centro: true }); nota(R, 'papel higiênico'); return; } }
  }
  function tanque(R, m) {
    const f = fm(m); f.ci(0.022, 0.2, '#C9CCD0', 0, 0.86, -m.d / 2 + 0.06); f.cx(0.018, 0.018, 0.12, '#C9CCD0', 0, 1.04, -m.d / 2 + 0.11); f.cx(0.09, 0.03, 0.05, '#E7D36B', 0.15, 0.89, -m.d / 2 + 0.07); f.cx(0.12, 0.012, 0.16, '#E36F5A', -0.12, 0.89, 0.02, { ry: 0.3 });
    nota(R, 'torneira, sabão e pano no tanque');
  }
  function maquina(R, m) {
    const l = ladoAtras(R, m); if (!l) return; const pos = fixar(l, uDe(l, m), 0.55, 1.45, 1.82, 0.22, { desvio: 0.25 });
    if (pos) { prateleira(pos, 0.55, 1.47, null, { servico: true }); nota(R, 'prateleira com sabão e amaciante'); }
  }

  // ---- cômodos ------------------------------------------------------------------------
  function sala(R) {
    mv(R, 'sofa').forEach((m) => sofa(R, m)); mv(R, 'rack').forEach((m) => rack(R, m)); mv(R, 'mesaCentro').forEach((m) => mesaCentro(R, m));
    const rnd = aleatorio(R.sem), pv = noChao(R, 0.4, 0.4, { alt: 0.84 }); if (pv) { vasoPlanta(pv.f, 0, 0, 1, rnd); nota(R, 'vaso de espada-de-são-jorge'); }
    const pg = noChao(R, 0.46, 0.2, { alt: 1.05 });
    if (pg) { const f = pg.f, c = '#B9763E'; f.ci(0.36, 0.09, c, 0, 0.02, -0.02, { rx: PI / 2 - 0.16, centro: false }); f.ci(0.27, 0.09, c, 0, 0.3, -0.07, { rx: PI / 2 - 0.16 }); f.ci(0.09, 0.012, '#2B2B2B', 0, 0.27, -0.005, { rx: PI / 2 - 0.16 }); f.cx(0.05, 0.5, 0.025, '#4A3526', 0, 0.48, -0.115, { rx: -0.16 }); f.cx(0.07, 0.13, 0.025, '#2B2B2B', 0, 0.95, -0.19, { rx: -0.16 }); nota(R, 'violão encostado'); }
    const pp = naParede(R, 0.5, 1.12, 1.88, 0.04); if (pp) { quadro(pp, 0.5, 0.7, 0, { estilo: 'projeto', moldura: '#8B6644', sem: 1 }); nota(R, 'a planta desta casa emoldurada'); }
    quadrosLivres(R, 1, [[0.6, 0.45], [0.4, 0.5]], { v0: 2 });
  }
  function cozinha(R) {
    mv(R, 'bancada').forEach((m) => bancada(R, m)); mv(R, 'geladeira').forEach((m) => geladeira(R, m));
    const pr = naParede(R, 0.34, 1.74, 2.08, 0.05);
    if (pr) { const t = tex('relogio', 128, 128, (g, W) => desenharRelogio(g, W)); pr.f.ci(0.32, 0.03, '#2B2B2B', 0, 1.91, 0.015, { rx: PI / 2, centro: true }); pr.f.malha(new THREE.Mesh(GEO.plano, matTex('relogio', t)), 0, 1.91, 0.0312).scale.set(0.29, 0.29, 1); nota(R, 'relógio de parede com a hora certa'); }
    const pc = naParede(R, 0.3, 1.25, 1.72, 0.03);
    if (pc) { const d = new Date(), t = tex('folhinha' + d.getMonth() + d.getDate(), 128, 180, (g, W, H) => { g.fillStyle = '#FDFBF5'; g.fillRect(0, 0, W, H); g.fillStyle = '#C8553D'; g.fillRect(0, 0, W, 46); g.fillStyle = '#fff'; g.textAlign = 'center'; g.font = '700 22px Inter, Arial, sans-serif'; g.fillText(['JANEIRO', 'FEVEREIRO', 'MARÇO', 'ABRIL', 'MAIO', 'JUNHO', 'JULHO', 'AGOSTO', 'SETEMBRO', 'OUTUBRO', 'NOVEMBRO', 'DEZEMBRO'][d.getMonth()], W / 2, 31); g.fillStyle = '#2B2B2B'; g.font = '800 92px Inter, Arial, sans-serif'; g.fillText(String(d.getDate()), W / 2, 138); g.font = '600 15px Inter, Arial, sans-serif'; g.fillText(['domingo', 'segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sábado'][d.getDay()], W / 2, 166); }); pc.f.malha(new THREE.Mesh(GEO.plano, matTex('folhinha', t)), 0, 1.49, 0.006).scale.set(0.26, 0.37, 1); pc.f.ci(0.012, 0.012, '#9AA0A6', 0, 1.685, 0.006, { rx: PI / 2, centro: true }); nota(R, 'folhinha com o dia de hoje'); }
    const pl = noChao(R, 0.26, 0.26, { alt: 0.36 }); if (pl) { pl.f.co(0.2, 0.3, '#8E9196', 0, 0, 0, { rx: PI }); pl.f.ci(0.25, 0.025, '#5E6166', 0, 0.3, 0); nota(R, 'lixeira'); }
    quadrosLivres(R, 1, [[0.4, 0.5], [0.3, 0.3]]);
  }
  function varalTeto(R) {
    let { x0, x1, z0, z1 } = R.int; x0 += 0.25; x1 -= 0.25; z0 += 0.25; z1 -= 0.25;
    for (const o of A.obst) if (o.t === 'janela' && o.x0 < x1 && o.x1 > x0 && o.z0 < z1 && o.z1 > z0) { if (o.h) { if ((o.z0 + o.z1) / 2 < (z0 + z1) / 2) z0 = Math.max(z0, o.z1 + 0.05); else z1 = Math.min(z1, o.z0 - 0.05); } else if ((o.x0 + o.x1) / 2 < (x0 + x1) / 2) x0 = Math.max(x0, o.x1 + 0.05); else x1 = Math.min(x1, o.x0 - 0.05); }
    const ao = (z1 - z0) >= (x1 - x0), comp = Math.min(1.7, ao ? z1 - z0 : x1 - x0), larg = Math.min(0.7, ao ? x1 - x0 : z1 - z0); if (comp < 0.9 || larg < 0.4) return;
    const f = F((x0 + x1) / 2, (z0 + z1) / 2, ao ? PI / 2 : 0), Y = 2.56;
    for (const s of [-1, 1]) { f.cx(0.025, 0.025, larg, '#DADDE0', s * comp / 2, Y - 0.005, 0); for (const t of [-1, 1]) f.cx(0.006, ALT - Y - 0.02, 0.006, '#9A9A9A', s * comp / 2, Y + 0.02, t * larg * 0.4); }
    for (let i = 0; i < 4; i++) f.cx(comp, 0.006, 0.006, '#F4F4F4', 0, Y, -larg / 2 + larg * (i + 0.5) / 4);
    const lz = (i) => -larg / 2 + larg * (i + 0.5) / 4;
    f.cx(0.32, 0.34, 0.012, '#5BA4B6', -comp * 0.28, Y - 0.34, lz(0)); f.cx(0.46, 0.11, 0.012, '#5BA4B6', -comp * 0.28, Y - 0.12, lz(0)); f.cx(0.38, 0.32, 0.016, '#F2C14E', comp * 0.2, Y - 0.32, lz(1)); f.cx(0.3, 0.3, 0.012, '#F4F1EC', -comp * 0.05, Y - 0.3, lz(2)); f.cx(0.3, 0.26, 0.012, '#E36F5A', comp * 0.3, Y - 0.26, lz(3));
    nota(R, 'varal de teto com roupa');
  }
  function servico(R) {
    mv(R, 'tanque').forEach((m) => tanque(R, m)); mv(R, 'maquina').forEach((m) => maquina(R, m)); varalTeto(R);
    const pc = noChao(R, 0.4, 0.4, { alt: 0.52 }); if (pc) { pc.f.co(0.34, 0.46, '#C9A77E', 0, 0, 0, { rx: PI }); pc.f.ci(0.36, 0.02, '#B18C5F', 0, 0.46, 0); pc.f.mc(0.26, 0.1, 0.24, '#E36F5A', 0.01, 0.42, 0); pc.f.mc(0.18, 0.08, 0.2, '#F4F1EC', -0.04, 0.47, 0.02, { ry: 0.5 }); nota(R, 'cesto de roupa'); }
    const pb = noChao(R, 0.36, 0.3, { alt: 1.32 });
    if (pb) { const f = pb.f; f.co(0.22, 0.24, '#3D8FBF', -0.05, 0, 0.02, { rx: PI }); f.cx(0.012, 1.25, 0.012, '#C9A77E', 0.11, 0.04, -0.07, { rx: -0.1 }); f.cx(0.26, 0.05, 0.03, '#2B2B2B', 0.11, 0, -0.005, {}); f.cx(0.012, 1.2, 0.012, '#8E9196', 0.16, 0.06, -0.09, { rx: -0.07, rz: -0.05 }); f.cx(0.05, 0.14, 0.2, '#D9A441', 0.2, 0, -0.02); nota(R, 'balde, rodo e vassoura'); }
  }
  function quarto(R) {
    const camas = [...mv(R, 'camaCasal'), ...mv(R, 'camaSolteiro')], casal = R.tipo === 'casal';
    mv(R, 'criado').forEach((m, i) => criado(R, m, i)); mv(R, 'armario').forEach((m, i) => armario(R, m, i)); mv(R, 'escrivaninha').forEach((m) => escrivaninha(R, m));
    camas.forEach((m, i) => {
      const l = ladoAtras(R, m), larg = casal ? 0.9 : 0.5, alt = casal ? 0.5 : 0.4, pos = l && fixar(l, uDe(l, m), larg, 1.5 - alt / 2 - 0.03, 1.5 + alt / 2 + 0.03, 0.04, { desvio: 0.2 });
      if (pos) { quadro(pos, larg, alt, (R.sem + i) % 4, { sem: R.sem + i }); nota(R, 'quadro sobre a cabeceira'); }
      cama(R, m, i);
    });
    nota(R, 'almofadas e peseira na cama, abajur com cúpula, livro e celular no criado');
    if (casal) { const pe = naParede(R, 0.46, 0.12, 1.75, 0.03); if (pe) { espelho(pe, 0.46, 1.42, 0.3); nota(R, 'espelho de corpo inteiro'); } }
    const pc = naParede(R, 0.6, 0.3, 1.78, 0.16, { grade: true });
    if (pc) {
      const f = pc.f; f.cx(0.6, 0.08, 0.02, '#9B7653', 0, 1.62, 0.01); for (let i = 0; i < 4; i++) f.ci(0.02, 0.07, '#3A3A3A', -0.225 + i * 0.15, 1.66, 0.05, { rx: PI / 2, centro: true });
      if (casal) { f.mc(0.3, 0.24, 0.09, '#8B6644', -0.15, 1.2, 0.07); f.cx(0.012, 0.22, 0.012, '#8B6644', -0.15, 1.44, 0.07); f.ci(0.34, 0.02, '#D9BE8A', 0.16, 1.5, 0.045, { rx: PI / 2, centro: true }); f.ci(0.17, 0.09, '#D9BE8A', 0.16, 1.5, 0.09, { rx: PI / 2, centro: true }); nota(R, 'cabideiro com bolsa e chapéu de palha'); }
      else { const c = PAL[(R.sem) % 3]; f.mc(0.3, 0.4, 0.13, c, -0.12, 1.2, 0.085); f.mc(0.2, 0.16, 0.05, tom(c, 0.8), -0.12, 1.24, 0.16); f.cx(0.03, 0.08, 0.02, '#2B2B2B', -0.12, 1.6, 0.06); f.es(0.2, 0.15, 0.13, '#C8553D', 0.2, 1.49, 0.07); f.cx(0.17, 0.012, 0.1, '#A8432F', 0.2, 1.44, 0.075, { rx: 0.9 }); nota(R, 'cabideiro com mochila e boné'); }
    }
    if (!casal) { const pt = noChao(R, 0.5, 0.36, { alt: 0.26 }); if (pt) { const f = pt.f; f.es(0.21, 0.21, 0.21, '#FDFBF5', -0.12, 0, 0); for (const [a, b] of [[0, 0.1], [0.07, 0.03], [-0.06, 0.05], [0.02, -0.02]]) f.es(0.06, 0.06, 0.03, '#2B2B2B', -0.12 + a, 0.075 + b, 0.09); [['#C8553D', 0.1, 0, 0.02], ['#F2C14E', 0.19, 0, -0.03], ['#2F5D73', 0.14, 0.08, 0]].forEach(([c, x, y, z]) => f.cx(0.08, 0.08, 0.08, c, x, y, z, { ry: x * 3 })); nota(R, 'bola e blocos de montar'); } }
    quadrosLivres(R, 1, [[0.5, 0.4], [0.4, 0.5], [0.3, 0.3]], { v0: 1 });
  }
  function banho(R) {
    mv(R, 'pia').forEach((m) => pia(R, m)); mv(R, 'box').forEach((m) => box(R, m)); mv(R, 'vaso').forEach((m) => vaso(R, m));
    const pt = naParede(R, 0.56, 0.62, 1.26, 0.09, { grade: true });
    if (pt) { const f = pt.f, c = ['#5BA4B6', '#D9A08B', '#8A9A86'][R.sem % 3]; f.ci(0.016, 0.5, '#C9CCD0', 0, 1.18, 0.06, { rz: PI / 2, centro: true }); for (const s of [-1, 1]) f.cx(0.02, 0.02, 0.06, '#C9CCD0', s * 0.25, 1.17, 0.03); f.mc(0.34, 0.5, 0.035, c, 0, 0.7, 0.06); f.cx(0.34, 0.03, 0.036, tom(c, 0.8), 0, 0.78, 0.06); nota(R, 'toalheiro com toalha'); }
    const v = mv(R, 'vaso')[0], pl = noChao(R, 0.2, 0.2, { alt: 0.28, gosto: v ? (x, z) => Math.hypot(x - v.x, z - v.y) : null }); if (pl) { pl.f.ci(0.18, 0.24, '#F4F1EC', 0, 0, 0); pl.f.ci(0.19, 0.02, '#8E9196', 0, 0.24, 0); nota(R, 'lixeira'); }
    const p = mv(R, 'pia')[0], b = mv(R, 'box')[0], cor = ['#5BA4B6', '#D9A08B', '#8A9A86'][R.sem % 3];
    if ((p && tapeteLocal(R, p, 0, p.d / 2 + 0.26, 0.55, 0.38, cor, { macio: true })) || (b && (tapeteLocal(R, b, 0, b.d / 2 + 0.26, 0.55, 0.38, cor, { macio: true }) || tapeteLocal(R, b, -b.w / 2 - 0.26, 0, 0.38, 0.55, cor, { macio: true })))) nota(R, 'tapetinho');
  }
  function circ(R) {
    quadrosLivres(R, 2, [[0.5, 0.7], [0.4, 0.5], [0.3, 0.3]]);
    const ps = noChao(R, 0.7, 0.3, { alt: 0.48 }); if (ps) { const f = ps.f; f.cx(0.7, 0.44, 0.28, '#C9A77E', 0, 0, 0); f.cx(0.66, 0.012, 0.25, '#9B7653', 0, 0.2, 0.02); for (const s of [-1, 1]) f.mc(0.1, 0.05, 0.22, s < 0 ? '#2F5D73' : '#C8553D', s * 0.15, 0.44, 0); nota(R, 'sapateira baixa'); } else nota(R, 'sem sapateira (a passagem ficaria com menos de 80 cm)');
    const pc = naParede(R, 0.5, 0.3, 1.78, 0.13, { grade: true });
    if (pc) { const f = pc.f; f.cx(0.5, 0.08, 0.02, '#9B7653', 0, 1.62, 0.01); for (let i = 0; i < 3; i++) f.ci(0.02, 0.07, '#3A3A3A', -0.16 + i * 0.16, 1.66, 0.05, { rx: PI / 2, centro: true }); f.mc(0.26, 0.3, 0.07, '#C8553D', -0.16, 1.24, 0.06); f.cx(0.012, 0.14, 0.012, '#C8553D', -0.16, 1.52, 0.06); f.ci(0.02, 0.5, '#3E4A57', 0.16, 1.14, 0.05); f.co(0.07, 0.3, '#3E4A57', 0.16, 1.06, 0.05); nota(R, 'cabideiro de parede com sacola e guarda-chuva'); }
  }
  function varanda(R) {
    const rnd = aleatorio(R.sem), pc = noChao(R, 0.62, 0.62, { alt: 0.84 });
    if (pc) { const f = pc.f, c = ['#C8553D', '#2F5D73', '#E0A23A'][R.sem % 3]; for (const sx of [-1, 1]) for (const sz of [-1, 1]) f.ci(0.03, 0.4, '#2B2B2B', sx * 0.24, 0, sz * 0.22); f.mc(0.56, 0.07, 0.52, c, 0, 0.38, 0.02); f.mc(0.56, 0.44, 0.07, c, 0, 0.4, -0.24, { rx: -0.18 }); for (let i = 0; i < 6; i++) f.cx(0.012, 0.42, 0.012, tom(c, 1.4), -0.22 + i * 0.088, 0.41, -0.2, { rx: -0.18 }); nota(R, 'cadeira de varanda'); }
    const pv = noChao(R, 0.36, 0.36, { alt: 0.8 }); if (pv) { vasoPlanta(pv.f, 0, 0, 0.9, rnd); nota(R, 'vaso de espada-de-são-jorge'); }
  }

  // ---- rodapé: em toda parede cheia dos cômodos de dentro, parando em porta e em móvel encostado -------
  function rodapes() {
    let n = 0;
    for (const R of A.comodos) { if (FORA.includes(R.tipo)) continue; for (const l of R.lados) for (const [a, b, face] of livres(l, 0.045, 0.11, 0.02, ['margem', 'tapete', 'giro', 'passo', 'folha', 'janela'])) { if (b - a < 0.08) continue; refParede(l, (a + b) / 2, face).cx(b - a, 0.07, 0.012, '#DCD4C5', 0, 0.04, 0.006); n++; } }
    nota('casa', `rodapé em ${n} trechos de parede`);
  }

  // ---- lado de fora ------------------------------------------------------------------
  const moitas = casa.cena.children.filter((o) => o.isGroup && o.children.length && o.children.every((c) => c.isMesh && c.geometry.type === 'IcosahedronGeometry'));
  const escondidas = [], limpar = (x, z, r) => { for (const g of moitas) if (g.children[0].scale.x < 0.4 && Math.hypot(g.position.x - x, g.position.z - z) < r && !escondidas.includes(g)) escondidas.push(g); };
  function exterior() {
    const L = D.LARGURA, P = D.PROFUNDIDADE, gx = D.ENTRADA_X ?? L / 2, zm = -2.25, vao = 1.1, f = F(0, 0), MURO = '#EFE9DD', GRADE = '#2F3A44', rnd = aleatorio(semente(D.META.id + 'fora'));
    for (const [a, b] of [[-1.0, gx - vao / 2 - 0.2], [gx + vao / 2 + 0.2, L + 1.0]]) { f.cx(b - a, 0.9, 0.12, MURO, (a + b) / 2, 0, zm, { sombra: true }); f.cx(b - a + 0.04, 0.04, 0.18, '#D8D0C2', (a + b) / 2, 0.9, zm); }
    A.barreiras.push([-1.0, zm, gx - vao / 2 - 0.1, zm, 0.12], [gx + vao / 2 + 0.1, zm, L + 1.0, zm, 0.12]); A.portao = gx;
    for (const s of [-1, 1]) { f.cx(0.2, 1.15, 0.2, '#E4DCCD', gx + s * (vao / 2 + 0.1), 0, zm, { sombra: true }); f.cx(0.26, 0.05, 0.26, '#D8D0C2', gx + s * (vao / 2 + 0.1), 1.15, zm); }
    const an = 1.4, g = F(gx + vao / 2, zm, Math.atan2(-Math.sin(an), -Math.cos(an)));          // portão aberto para dentro
    for (const y of [0.1, 0.98]) g.cx(vao - 0.04, 0.04, 0.03, GRADE, vao / 2, y, 0); for (let i = 0; i <= 8; i++) g.cx(i % 8 ? 0.018 : 0.04, 0.92, i % 8 ? 0.018 : 0.03, GRADE, 0.02 + (vao - 0.08) * i / 8, 0.1, 0); g.cx(0.1, 0.03, 0.05, '#C9CCD0', vao - 0.1, 0.6, 0);
    const xc = gx - vao / 2 - 0.1; f.cx(0.2, 0.14, 0.09, '#C8553D', xc, 0.84, zm - 0.145); f.cx(0.14, 0.012, 0.004, '#2B2B2B', xc, 0.93, zm - 0.192); f.cx(0.01, 0.07, 0.01, '#F2C14E', xc + 0.107, 0.9, zm - 0.14);           // caixa de correio
    const num = String(101 + semente(D.META.id) % 880), tn = tex('num' + num, 128, 128, (c, W) => { c.fillStyle = '#FDFBF5'; c.fillRect(0, 0, W, W); c.strokeStyle = '#1F4F9A'; c.lineWidth = 7; c.strokeRect(8, 8, W - 16, W - 16); c.lineWidth = 2; c.strokeRect(19, 19, W - 38, W - 38); c.fillStyle = '#1F4F9A'; c.textAlign = 'center'; c.font = '800 52px Inter, Arial, sans-serif'; c.fillText(num, W / 2, W / 2 + 19); });
    F(gx + vao / 2 + 0.1, zm - 0.101, PI).malha(new THREE.Mesh(GEO.plano, matTex('num' + num, tn)), 0, 0.9, 0.002).scale.set(0.17, 0.17, 1);                                           // número em azulejo
    const xl = gx - vao / 2 - 1.5; f.ci(0.04, 0.95, GRADE, xl, 0.02, -2.95); f.cx(0.42, 0.02, 0.3, GRADE, xl, 0.95, -2.95); for (const [dx, dz, w, d] of [[0, -0.15, 0.42, 0.015], [0, 0.15, 0.42, 0.015], [-0.21, 0, 0.015, 0.3], [0.21, 0, 0.015, 0.3]]) f.cx(w, 0.015, d, GRADE, xl + dx, 1.16, -2.95 + dz); for (const sx of [-1, 1]) for (const sz of [-1, 1]) f.cx(0.012, 0.2, 0.012, GRADE, xl + sx * 0.2, 0.97, -2.95 + sz * 0.14);   // lixeira de calçada
    f.cx(60, 0.03, 6, '#4A4C50', L / 2, -0.025, -7.76); f.cx(60, 0.05, 0.14, '#BDB6A8', L / 2, -0.02, -4.77); for (let i = -6; i <= 6; i++) f.cx(1.6, 0.004, 0.12, '#E9C84A', L / 2 + i * 4, 0.004, -7.76);                   // rua, meio-fio e faixa
    nota('fora', `muro baixo, portão aberto, caixa de correio, número ${num} em azulejo, lixeira de calçada, rua com meio-fio`);

    // capacho, chinelos e vaso na porta de entrada
    const ent = A.portas.find((p) => p.id === 'entrada') || A.portas.find((p) => p.ext && /sala/.test(p.id)) || A.portas.find((p) => p.ext);
    if (ent) {
      const { d0, d1, r, esp } = ent, ox = ent.cx - d1.x * (esp / 2 + 0.3), oz = ent.cz - d1.z * (esp / 2 + 0.3), tc = tex('capacho', 256, 150, (c, W, H) => { c.fillStyle = '#8A6A45'; c.fillRect(0, 0, W, H); const rr = aleatorio(3); for (let i = 0; i < 2600; i++) { c.fillStyle = `rgba(${rr() < 0.5 ? '60,40,20' : '190,160,110'},.25)`; c.fillRect(rr() * W, rr() * H, 2, 3); } c.strokeStyle = '#4A3526'; c.lineWidth = 6; c.strokeRect(9, 9, W - 18, H - 18); c.fillStyle = '#3A2A1C'; c.textAlign = 'center'; c.font = '800 34px Inter, Arial, sans-serif'; c.fillText('BEM-VINDO', W / 2, H / 2 + 12); });
      const th = Math.atan2(-d1.x, -d1.z), q = F(ox, oz, th, 0.047); q.cx(0.7, 0.012, 0.42, '#6E5236', 0, 0, 0); const mc = new THREE.Mesh(GEO.plano, matTex('capacho', tc, { rough: 1 })); q.malha(mc, 0, 0.0135, 0, { rx: -PI / 2 }); mc.scale.set(0.7, 0.42, 1);
      limpar(ox, oz, 0.95); limpar(ent.cx - d1.x * 1.2, ent.cz - d1.z * 1.2, 0.95);
      const cs = F(ent.cx - d1.x * (esp / 2 + 0.16) + d0.x * (r / 2 + 0.2), ent.cz - d1.z * (esp / 2 + 0.16) + d0.z * (r / 2 + 0.2), th + 0.3, 0.047);
      for (const s of [-1, 1]) { cs.mc(0.095, 0.022, 0.25, '#2F7FA8', s * 0.065, 0, s * 0.02); cs.cx(0.012, 0.012, 0.09, '#FDFBF5', s * 0.065 + 0.02, 0.026, -0.05, { ry: 0.5 }); cs.cx(0.012, 0.012, 0.09, '#FDFBF5', s * 0.065 - 0.02, 0.026, -0.05, { ry: -0.5 }); }
      let fezVaso = false;
      if (!A.ambienteEm(ox, oz)) for (const s of [1, -1]) {       // sem varanda: um vaso ao lado da porta, só em parede cheia e fora de janela
        const la = s > 0 ? r + 0.34 : -0.34, dir = ent.h ? d0.x : d0.z, u = (ent.h ? ent.H.x : ent.H.z) + dir * la; if (!A.solido(ent.h, ent.fixo, u - 0.2, u + 0.2)) continue;
        const vx = ent.H.x + d0.x * la - d1.x * (esp / 2 + 0.24), vz = ent.H.z + d0.z * la - d1.z * (esp / 2 + 0.24); vasoPlanta(F(vx, vz, 0, 0), 0, 0, 0.9, rnd); limpar(vx, vz, 0.6); fezVaso = true; break;
      }
      nota('fora', 'capacho "Bem-vindo" e chinelos na porta' + (fezVaso ? ', vaso de espada-de-são-jorge ao lado' : ''));
    }
    for (const p of A.portas) if (p.ext && p !== ent && !A.ambienteEm(p.cx - p.d1.x * 0.5, p.cz - p.d1.z * 0.5)) limpar(p.cx - p.d1.x * 0.7, p.cz - p.d1.z * 0.7, 0.8);

    // mangueira enrolada na parede dos fundos
    const fundo = A.paredes.filter((w) => w.h && Math.abs(w.fixo - (P - 0.075)) < 0.02);
    let iv = fundo.map((w) => [w.a, w.b]); const corta = (a, b) => { iv = iv.flatMap(([x, y]) => (b <= x || a >= y ? [[x, y]] : [[x, Math.min(a, y)], [Math.max(b, x), y]].filter((i) => i[1] - i[0] > 0.05))); };
    for (const j of A.janelas) if (j.h && Math.abs(j.fixo - (P - 0.075)) < 0.1) corta(j.a - 0.25, j.b + 0.25); for (const p of A.portas) if (p.h && Math.abs(p.fixo - (P - 0.075)) < 0.1) corta(p.a - 0.35, p.b + 0.35);
    const m = iv.sort((p, q) => (q[1] - q[0]) - (p[1] - p[0]))[0];
    if (m && m[1] - m[0] > 0.7) {
      const q = F((m[0] + m[1]) / 2, P, 0), anel = new THREE.Mesh(MATS.get('gt') || MATS.set('gt', new THREE.TorusGeometry(0.17, 0.028, 8, 28)).get('gt'), MATS.get('mg') || MATS.set('mg', new THREE.MeshStandardMaterial({ color: '#3F8F4E', roughness: 0.6 })).get('mg'));
      q.malha(anel, 0, 0.85, 0.05); q.malha(anel.clone(), 0.012, 0.86, 0.085).scale.setScalar(0.9); q.cx(0.08, 0.08, 0.14, '#6B6258', 0, 0.86, 0.07); q.ci(0.02, 0.1, '#C9A227', 0, 1.2, 0.05, { rx: PI / 2 }); q.cx(0.07, 0.016, 0.016, '#C9A227', 0, 1.29, 0.07); nota('fora', 'mangueira enrolada e torneira na parede dos fundos');
    }

    // varal no quintal dos fundos, onde não bate em árvore
    const copas = []; for (const gq of moitas) for (const c of gq.children) copas.push([gq.position.x + c.position.x, c.position.y, gq.position.z + c.position.z, c.scale.x]);
    const livre = (x, y, z) => copas.every(([cx, cy, cz, r]) => Math.hypot(x - cx, (y - cy) * 1.25, z - cz) > r + 0.12);
    let lugar = null;
    busca: for (let z = P + 1.3; z <= P + 3.4; z += 0.25) for (let k = 0; k < 16; k++) { const x0 = L / 2 - 1.1 + (k % 2 ? 1 : -1) * Math.ceil(k / 2) * 0.4; let ok = true; for (let t = 0; t <= 2.2 && ok; t += 0.2) for (const y of [0.3, 1.0, 1.4, 1.8]) for (const dz of [-0.3, 0, 0.3]) if (!livre(x0 + t, y, z + dz)) { ok = false; break; } if (ok) { lugar = [x0, z]; break busca; } }
    if (lugar) {
      const [x0, z] = lugar, v = F(x0 + 1.1, z, 0, 0); for (const s of [-1, 1]) { v.ci(0.05, 1.8, '#8E9196', s * 1.1, 0, 0, { sombra: true }); v.cx(0.04, 0.04, 0.6, '#8E9196', s * 1.1, 1.74, 0); }
      for (const dz of [-0.24, 0, 0.24]) v.cx(2.2, 0.006, 0.006, '#F4F4F4', 0, 1.755, dz);
      const mr = MATS.get('roupa') || MATS.set('roupa', new THREE.MeshStandardMaterial({ roughness: 0.9, side: THREE.DoubleSide })).get('roupa');
      [[-0.75, -0.24, 0.5, 0.62, '#F4F1EC'], [-0.1, -0.24, 0.42, 0.4, '#5BA4B6'], [0.6, 0, 0.7, 0.75, '#F2C14E'], [-0.5, 0.24, 0.36, 0.36, '#E36F5A'], [0.15, 0.24, 0.36, 0.34, '#8A9A86'], [0.75, 0.24, 0.3, 0.42, '#3E4A57']].forEach(([lx, lz, w, h, c], i) => {
        const piv = new THREE.Group(), pano = new THREE.Mesh(GEO.caixa, mr.clone()); pano.material.color.set(c); pano.scale.set(w, h, 0.012); pano.position.y = -h / 2; piv.add(pano); v.malha(piv, lx, 1.75, lz); balancam.push([piv, i * 1.7]);
      });
      nota('fora', 'varal com roupa no quintal dos fundos');
    } else nota('fora', 'sem varal no quintal (as árvores ocupam o fundo)');
  }

  // ---- ordem: primeiro o que é fixo, depois o que procura lugar ------------------------
  portasDecor();
  for (const R of A.comodos) cortinas(R);
  const feitos = { sala, cozinha, servico, dorm: quarto, casal: quarto, banho, lavabo: banho, circ, varanda };
  for (const R of A.comodos) {
    if (!['patio', 'jardim', 'futuro', 'quintal'].includes(R.tipo)) luminaria(R);
    mv(R, 'mesaJantar').forEach((m) => { mesaJantar(m); nota(R, 'mesa posta, garrafa térmica e fruteira'); });
    if (feitos[R.tipo]) feitos[R.tipo](R);
  }
  exterior(); rodapes();
  lote.montar(grupo); casa.cena.add(grupo);

  let minuto = -1;
  return {
    grupo, barreiras: A.barreiras, portao: A.portao, resumo, chao: A.chao, pecas: lote.itens.length,
    mostrar(v) { grupo.visible = v; for (const g of escondidas) g.visible = !v; },
    hora(h) { for (const t of telas) t.visible = h === 'noite'; },
    animar(seg, parado) {                    // ventilador girando, roupa ao vento e relógio com a hora do aparelho
      if (!parado) { for (const p of giram) p.rotation.y = seg * 2.2; for (const [p, f] of balancam) p.rotation.x = Math.sin(seg * 1.3 + f) * 0.09 + 0.04; }
      const d = new Date(), agora = d.getHours() * 60 + d.getMinutes(), t = TEX.get('relogio'); if (t && agora !== minuto) { minuto = agora; desenharRelogio(t.image.getContext('2d'), t.image.width); t.needsUpdate = true; }
    },
    tirar() { for (const g of escondidas) g.visible = true; casa.cena.remove(grupo); grupo.traverse((o) => { if (o.isInstancedMesh) o.dispose(); }); },
  };
}

// ---------------------------------------------------------------------------
// Personalização: cores, piso, hora do dia. Acha as peças do motor pela cena, sem mexer nele.
// ---------------------------------------------------------------------------
const HORAS = {
  manha: { ceu: ['#86BEEC', '#DDEEF8', '#B8CFB0'], sol: ['#FFF8EA', 2.7, [8, 13, -7]], hemi: ['#F2F8FF', '#BCAE94', 1.4], luz: ['#FFE9C8', 1.0], lamp: '#FFF8E6', expo: 1.05, criado: 0.6 },
  tarde: { ceu: ['#EBC38C', '#F8E6C6', '#D9C9A0'], sol: ['#FFD9A0', 2.4, [-9, 13, -7]], hemi: ['#FFF4E2', '#C9A77C', 1.25], luz: ['#FFE2B8', 5], lamp: '#FFF1CF', expo: 1.05, criado: 1 },
  noite: { ceu: ['#060B1E', '#1A2850', '#0E1626'], sol: ['#93A9E0', 0.55, [7, 14, 6]], hemi: ['#7388C0', '#2A2A33', 0.42], luz: ['#FFD08A', 6.5], lamp: '#FFE7A8', expo: 0.95, criado: 2.6 },
};
function partes(casa, D) {
  if (casa._partes) return casa._partes;
  const P = { pisos: [], sofas: [], camas: [], maquinas: [], criados: [], pontos: [], vergas: [] };
  casa.cena.traverse((o) => {
    if (o.isLineSegments && o.parent) { const m = o.parent.children.find((c) => c.isMesh); if (m) P.parede = m.material; }
    if (o.isDirectionalLight) P.sol = o; if (o.isHemisphereLight) P.hemi = o; if (o.isPointLight) P.pontos.push(o);
    if (o.isMesh && o.userData.verga) P.vergas.push(o.material);
    if (o.isMesh && o.geometry.type === 'BoxGeometry' && o.geometry.parameters.height === 0.04 && o.material.map) { const a = D.ambientes.find((q) => Math.abs((q.x0 + q.x1) / 2 - o.position.x) < 0.01 && Math.abs((q.y0 + q.y1) / 2 - o.position.z) < 0.01); if (a) P.pisos.push({ a, mesh: o, original: o.material.map }); }
  });
  for (const m of (D.MOVEIS || [])) {
    const obj = casa.cena.children.find((o) => o.isGroup && Math.abs(o.position.y - 0.04) < 1e-6 && o.position.x === m.x && o.position.z === m.y); if (!obj) continue;
    const comCor = (hex) => obj.children.filter((c) => c.isMesh && c.material.color && '#' + c.material.color.getHexString().toUpperCase() === hex.toUpperCase());
    if (m.tipo === 'sofa') P.sofas.push({ corpo: comCor(m.cor), assento: comCor('#9DAD98'), cor: m.cor });
    if (m.tipo.startsWith('cama')) P.camas.push({ manta: comCor(m.manta), cor: m.manta });
    if (m.tipo === 'maquina') P.maquinas.push(obj);
    if (m.tipo === 'criado') obj.traverse((c) => { if (c.isMesh && c.geometry.type === 'SphereGeometry') P.criados.push(c.material); });
  }
  // céu: uma cúpula com degradê, estrelas e lua para a noite
  const geo = new THREE.SphereGeometry(70, 24, 14); geo.setAttribute('color', new THREE.BufferAttribute(new Float32Array(geo.attributes.position.count * 3), 3));
  P.ceu = new THREE.Mesh(geo, new THREE.MeshBasicMaterial({ vertexColors: true, side: THREE.BackSide, depthWrite: false, toneMapped: false })); P.ceu.position.set(D.LARGURA / 2, 0, D.PROFUNDIDADE / 2); P.ceu.renderOrder = -2; casa.cena.add(P.ceu);
  const rnd = aleatorio(11), pos = []; for (let i = 0; i < 260; i++) { const a = rnd() * 2 * PI, e = 0.12 + rnd() * 1.3, r = 66; pos.push(D.LARGURA / 2 + Math.cos(a) * Math.cos(e) * r, Math.sin(e) * r, D.PROFUNDIDADE / 2 + Math.sin(a) * Math.cos(e) * r); }
  const ge = new THREE.BufferGeometry(); ge.setAttribute('position', new THREE.Float32BufferAttribute(pos, 3));
  P.estrelas = new THREE.Points(ge, new THREE.PointsMaterial({ color: '#FFFFFF', size: 1.8, sizeAttenuation: false, toneMapped: false, depthWrite: false })); P.estrelas.renderOrder = -1; casa.cena.add(P.estrelas);
  P.lua = new THREE.Mesh(GEO.esfera, new THREE.MeshBasicMaterial({ color: '#F4F0DC', toneMapped: false })); P.lua.scale.setScalar(4.5); P.lua.position.set(D.LARGURA / 2 + 30, 34, D.PROFUNDIDADE / 2 + 44); casa.cena.add(P.lua);
  return (casa._partes = P);
}
function texPisoAlt(D, a, tipo) {
  const K = 96, w = a.x1 - a.x0, d = a.y1 - a.y0;
  const t = tex(`piso|${D.META.id}|${a.id}|${tipo}`, w * K, d * K, (g, W, H) => {
    const rnd = aleatorio(semente(a.id + tipo));
    if (tipo === 'porcelanato') {
      const lado = 0.8; for (let y = 0; y < d; y += lado) for (let x = 0; x < w; x += lado) { const v = (rnd() - 0.5) * 7; g.fillStyle = `rgb(${229 + v},${223 + v},${212 + v})`; g.fillRect(x * K, y * K, lado * K + 1, lado * K + 1); }
      g.strokeStyle = 'rgba(150,140,125,.5)'; g.lineWidth = 1.2; for (let x = 0; x <= w; x += lado) { g.beginPath(); g.moveTo(x * K, 0); g.lineTo(x * K, H); g.stroke(); } for (let y = 0; y <= d; y += lado) { g.beginPath(); g.moveTo(0, y * K); g.lineTo(W, y * K); g.stroke(); }
    } else {
      g.fillStyle = '#B4B2AC'; g.fillRect(0, 0, W, H);
      for (let i = 0; i < w * d * 26; i++) { const x = rnd() * W, y = rnd() * H, r = 20 + rnd() * 70, gr = g.createRadialGradient(x, y, 0, x, y, r), c = rnd() < 0.5 ? '255,255,255' : '70,68,64'; gr.addColorStop(0, `rgba(${c},.07)`); gr.addColorStop(1, `rgba(${c},0)`); g.fillStyle = gr; g.fillRect(x - r, y - r, 2 * r, 2 * r); }
      g.strokeStyle = 'rgba(90,88,84,.35)'; g.lineWidth = 1; for (let x = 1.5; x < w; x += 1.5) { g.beginPath(); g.moveTo(x * K, 0); g.lineTo(x * K, H); g.stroke(); }
    }
    const e = 0.28 * K, s = (x0, y0, x1, y1) => { const gr = g.createLinearGradient(x0, y0, x1, y1); gr.addColorStop(0, 'rgba(40,30,20,.3)'); gr.addColorStop(1, 'rgba(40,30,20,0)'); return gr; };
    g.fillStyle = s(0, 0, 0, e); g.fillRect(0, 0, W, e); g.fillStyle = s(0, H, 0, H - e); g.fillRect(0, H - e, W, e); g.fillStyle = s(0, 0, e, 0); g.fillRect(0, 0, e, H); g.fillStyle = s(W, 0, W - e, 0); g.fillRect(W - e, 0, e, H);
    g.shadowColor = 'rgba(30,22,14,.45)'; g.shadowBlur = 12; g.shadowOffsetX = 4000; g.fillStyle = '#000';     // sombra de contato dos móveis
    for (const m of (D.MOVEIS || [])) { if (m.amb !== a.id || m.tipo === 'tapete') continue; const b = caixaMovel(m); g.fillRect((b.x0 - a.x0) * K - 4000 - 3, (b.z0 - a.y0) * K - 3, (b.x1 - b.x0) * K + 6, (b.z1 - b.z0) * K + 6); }
  });
  t.anisotropy = 8; return t;
}

export function aplicarOpcoes(casa, D, op, renderer) {
  const P = partes(casa, D), cor = new THREE.Color();
  const cp = corDe('parede', op.parede); if (P.parede) P.parede.color.set(cp); for (const m of P.vergas) m.color.set(cp);
  for (const p of P.pisos) { if (p.a.piso !== 'madeira') continue; const novo = op.piso === 'madeira' ? p.original : texPisoAlt(D, p.a, op.piso); if (p.mesh.material.map !== novo) { p.mesh.material.map = novo; p.mesh.material.needsUpdate = true; } }
  const cs = corDe('sofa', op.sofa); for (const s of P.sofas) { s.corpo.forEach((m) => m.material.color.set(cs)); s.assento.forEach((m) => m.material.color.set(tom(cs, 1.16))); }
  for (const c of P.camas) c.manta.forEach((m) => m.material.color.set(op.cama === 'planta' ? c.cor : corDe('cama', op.cama)));
  for (const o of P.maquinas) o.visible = op.maquina !== false;
  const h = HORAS[op.hora] || HORAS.tarde, cx = D.LARGURA / 2, cz = D.PROFUNDIDADE / 2;
  if (P.sol) { P.sol.color.set(h.sol[0]); P.sol.intensity = h.sol[1]; P.sol.position.set(cx + h.sol[2][0], h.sol[2][1], cz + h.sol[2][2]); }
  if (P.hemi) { P.hemi.color.set(h.hemi[0]); P.hemi.groundColor.set(h.hemi[1]); P.hemi.intensity = h.hemi[2]; }
  for (const l of P.pontos) { l.color.set(h.luz[0]); l.intensity = h.luz[1]; }
  for (const m of P.criados) m.emissiveIntensity = h.criado;
  MAT.luz.color.set(h.lamp); if (renderer) renderer.toneMappingExposure = h.expo;
  const zen = new THREE.Color(h.ceu[0]), hor = new THREE.Color(h.ceu[1]), chao = new THREE.Color(h.ceu[2]), pos = P.ceu.geometry.attributes.position, col = P.ceu.geometry.attributes.color;
  for (let i = 0; i < pos.count; i++) { const t = pos.getY(i) / 70; if (t >= 0) cor.copy(hor).lerp(zen, Math.pow(t, 0.55)); else cor.copy(hor).lerp(chao, Math.min(1, -t * 5)); col.setXYZ(i, cor.r, cor.g, cor.b); }
  col.needsUpdate = true; casa.cena.background = hor; P.estrelas.visible = P.lua.visible = op.hora === 'noite';
}

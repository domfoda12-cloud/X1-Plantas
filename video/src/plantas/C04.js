// C04 · Casa Duo. 6,4 x 7,5 m = 48 m². Provisório até o arquiteto validar.
// Dois quartos do mesmo tamanho nos fundos, com o banho entre eles e um hall mínimo.
import { montar } from './montar.js';
const PI = Math.PI;

export default montar({
  id: 'C04',
  nome: 'Casa Duo',
  ficha: '48 m² · 2 quartos · 1 banho',
  largura: 6.4,
  profundidade: 7.5,

  ambientes: [
    { id: 'sala', nome: 'Sala', x0: 0, y0: 0, x1: 3.6, y1: 3.7, piso: 'madeira' },
    { id: 'cozinha', nome: 'Cozinha', x0: 3.6, y0: 0, x1: 6.4, y1: 3.7, piso: 'porcelanato' },
    { id: 'hall', nome: 'Hall', x0: 2.5, y0: 3.7, x1: 3.9, y1: 5.0, piso: 'madeira', rotulo: false },
    { id: 'quarto1', nome: 'Quarto 1', x0: 0, y0: 3.7, x1: 2.5, y1: 7.5, piso: 'madeira', letra: 0.85, rotulo: [1.0, 5.0] },
    { id: 'banho', nome: 'Banho', x0: 2.5, y0: 5.0, x1: 3.9, y1: 7.5, piso: 'ceramica', letra: 0.7, rotulo: [3.0, 6.25] },
    { id: 'quarto2', nome: 'Quarto 2', x0: 3.9, y0: 3.7, x1: 6.4, y1: 7.5, piso: 'madeira', letra: 0.85, rotulo: [5.3, 5.0] },
  ],

  paredes: [
    [0, 0, 6.4, 0], [0, 7.5, 6.4, 7.5], [0, 0, 0, 7.5], [6.4, 0, 6.4, 7.5],
    [0, 3.7, 2.5, 3.7], [3.9, 3.7, 6.4, 3.7], // social | quartos
    [2.5, 3.7, 2.5, 7.5], [3.9, 3.7, 3.9, 7.5], // quartos | hall e banho
    [2.5, 5.0, 3.9, 5.0], // hall | banho
  ],
  portas: [
    { id: 'entrada', x: 0.4, y: 0, larg: 0.9, eixo: 'h', abre: 1, dob: 'ini' },
    { id: 'quarto1', x: 2.5, y: 3.8, larg: 0.8, eixo: 'v', abre: -1, dob: 'ini' },
    { id: 'quarto2', x: 3.9, y: 3.8, larg: 0.8, eixo: 'v', abre: 1, dob: 'ini' },
    { id: 'banho', x: 2.6, y: 5.0, larg: 0.7, eixo: 'h', abre: 1, dob: 'ini' },
  ],
  janelas: [
    { seg: [1.9, 0, 3.1, 0], peitoril: 1.0, verga: 2.2, id: 'sala' },
    { seg: [4.4, 0, 5.6, 0], peitoril: 1.1, verga: 2.2, id: 'cozinha' },
    { seg: [0, 5.3, 0, 6.5], peitoril: 1.0, verga: 2.2, id: 'quarto1' },
    { seg: [2.9, 7.5, 3.5, 7.5], peitoril: 1.6, verga: 2.2, id: 'banho' },
    { seg: [4.2, 7.5, 5.3, 7.5], peitoril: 1.0, verga: 2.2, id: 'quarto2' },
  ],

  moveis: [
    { tipo: 'tapete', amb: 'sala', x: 1.4, y: 2.0, w: 1.8, d: 2.2, cor: '#D9CBB4', borda: '#B49D7C' },
    { tipo: 'rack', amb: 'sala', x: 0.27, y: 2.0, rot: PI / 2, w: 1.6, d: 0.4 },
    { tipo: 'sofa', amb: 'sala', x: 2.6, y: 2.0, rot: -PI / 2, w: 2.0, d: 0.85, cor: '#A08C72' },
    { tipo: 'mesaCentro', amb: 'sala', x: 1.4, y: 2.0, w: 0.55, d: 0.95 },
    { tipo: 'planta', amb: 'sala', x: 3.3, y: 0.4, s: 0.85 },
    { tipo: 'bancada', amb: 'cozinha', x: 6.02, y: 1.45, rot: -PI / 2, w: 2.4, d: 0.62 },
    { tipo: 'geladeira', amb: 'cozinha', x: 5.98, y: 3.12, rot: -PI / 2, w: 0.72, d: 0.7 },
    { tipo: 'mesaJantar', amb: 'cozinha', x: 4.55, y: 1.6, rot: PI / 2, w: 0.75, d: 1.1 },
    { tipo: 'camaCasal', amb: 'quarto1', x: 1.0, y: 6.45, rot: PI, w: 1.4, d: 1.9, manta: '#B9C7D6' },
    { tipo: 'criado', amb: 'quarto1', x: 2.05, y: 7.2 },
    { tipo: 'armario', amb: 'quarto1', x: 0.85, y: 4.08, w: 1.5, d: 0.6 },
    { tipo: 'planta', amb: 'quarto1', x: 2.15, y: 5.3, s: 0.75 },
    { tipo: 'camaSolteiro', amb: 'quarto2', x: 5.85, y: 6.45, rot: PI, w: 0.9, d: 1.9, manta: '#E3B9A4' },
    { tipo: 'escrivaninha', amb: 'quarto2', x: 4.55, y: 7.18, rot: PI, w: 1.0, d: 0.5 },
    { tipo: 'armario', amb: 'quarto2', x: 5.55, y: 4.08, w: 1.5, d: 0.6 },
    { tipo: 'pia', amb: 'banho', x: 3.62, y: 5.42, rot: -PI / 2, w: 0.6, d: 0.42 },
    { tipo: 'vaso', amb: 'banho', x: 3.5, y: 6.2, rot: -PI / 2 },
    { tipo: 'box', amb: 'banho', x: 3.2, y: 6.98, rot: PI, w: 1.2, d: 0.9 },
  ],
  ordem: ['sala', 'cozinha', 'hall', 'banho', 'quarto1', 'quarto2'],
  entradas: [0.85],
});

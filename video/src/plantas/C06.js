// C06 · Casa Compacta Suíte. 7,2 x 8,6 m = 62 m². Provisório até o arquiteto validar.
// Suíte do casal com banho próprio, quarto 2 e banho social, sem corredor comprido.
import { montar } from './montar.js';
const PI = Math.PI;

export default montar({
  id: 'C06',
  nome: 'Casa Compacta Suíte',
  ficha: '62 m² · 2 quartos (1 suíte) · 2 banhos',
  largura: 7.2,
  profundidade: 8.6,

  ambientes: [
    { id: 'sala', nome: 'Sala', x0: 0, y0: 0, x1: 3.8, y1: 3.8, piso: 'madeira' },
    { id: 'cozinha', nome: 'Cozinha', x0: 3.8, y0: 0, x1: 7.2, y1: 3.8, piso: 'porcelanato' },
    { id: 'hall', nome: 'Hall', x0: 3.6, y0: 3.8, x1: 4.6, y1: 5.4, piso: 'madeira', rotulo: false },
    { id: 'banho', nome: 'Banho', x0: 4.6, y0: 3.8, x1: 7.2, y1: 5.4, piso: 'ceramica', letra: 0.85 },
    { id: 'entradaSuite', nome: 'Suíte', x0: 2.0, y0: 3.8, x1: 3.6, y1: 5.6, piso: 'madeira', rotulo: false },
    { id: 'banhoSuite', nome: 'Banho suíte', x0: 0, y0: 3.8, x1: 2.0, y1: 5.6, piso: 'ceramica', letra: 0.7, rotulo: [1.0, 4.95] },
    { id: 'suite', nome: 'Suíte', x0: 0, y0: 5.6, x1: 3.6, y1: 8.6, piso: 'madeira', area: 13.68, rotulo: [1.7, 6.3] },
    { id: 'quarto2', nome: 'Quarto 2', x0: 3.6, y0: 5.4, x1: 7.2, y1: 8.6, piso: 'madeira' },
  ],

  paredes: [
    [0, 0, 7.2, 0], [0, 8.6, 7.2, 8.6], [0, 0, 0, 8.6], [7.2, 0, 7.2, 8.6],
    [0, 3.8, 3.6, 3.8], [4.6, 3.8, 7.2, 3.8], // social | íntima
    [2.0, 3.8, 2.0, 5.6], [0, 5.6, 2.0, 5.6], // banho da suíte
    [3.6, 3.8, 3.6, 8.6], // suíte | hall e quarto 2
    [4.6, 3.8, 4.6, 5.4], [3.6, 5.4, 7.2, 5.4], // banho social e quarto 2
  ],
  portas: [
    { id: 'entrada', x: 0.5, y: 0, larg: 0.9, eixo: 'h', abre: 1, dob: 'ini' },
    { id: 'suite', x: 3.6, y: 3.9, larg: 0.8, eixo: 'v', abre: -1, dob: 'ini' },
    { id: 'banhoSuite', x: 2.0, y: 4.0, larg: 0.7, eixo: 'v', abre: -1, dob: 'ini' },
    { id: 'banho', x: 4.6, y: 4.3, larg: 0.7, eixo: 'v', abre: 1, dob: 'fim' },
    { id: 'quarto2', x: 3.7, y: 5.4, larg: 0.8, eixo: 'h', abre: 1, dob: 'ini' },
  ],
  janelas: [
    { seg: [2.0, 0, 3.3, 0], peitoril: 1.0, verga: 2.2, id: 'sala' },
    { seg: [4.6, 0, 6.0, 0], peitoril: 1.1, verga: 2.2, id: 'cozinha' },
    { seg: [0, 4.85, 0, 5.35], peitoril: 1.6, verga: 2.2, id: 'banhoSuite' },
    { seg: [0, 7.2, 0, 8.2], peitoril: 1.0, verga: 2.2, id: 'suite' },
    { seg: [7.2, 4.75, 7.2, 5.25], peitoril: 1.6, verga: 2.2, id: 'banho' },
    { seg: [4.5, 8.6, 5.7, 8.6], peitoril: 1.0, verga: 2.2, id: 'quarto2' },
  ],

  moveis: [
    { tipo: 'tapete', amb: 'sala', x: 1.5, y: 2.1, w: 2.0, d: 2.4, cor: '#D9CBB4', borda: '#B49D7C' },
    { tipo: 'rack', amb: 'sala', x: 0.27, y: 2.1, rot: PI / 2, w: 1.8, d: 0.4 },
    { tipo: 'sofa', amb: 'sala', x: 2.85, y: 2.1, rot: -PI / 2, w: 2.1, d: 0.88, cor: '#8A9A86' },
    { tipo: 'mesaCentro', amb: 'sala', x: 1.5, y: 2.1, w: 0.6, d: 1.0 },
    { tipo: 'planta', amb: 'sala', x: 3.45, y: 0.45, s: 0.8 },
    { tipo: 'bancada', amb: 'cozinha', x: 6.82, y: 1.5, rot: -PI / 2, w: 2.6, d: 0.62 },
    { tipo: 'geladeira', amb: 'cozinha', x: 6.78, y: 3.38, rot: -PI / 2, w: 0.72, d: 0.7 },
    { tipo: 'mesaJantar', amb: 'cozinha', x: 5.0, y: 1.8, rot: PI / 2, w: 0.8, d: 1.2 },
    { tipo: 'planta', amb: 'cozinha', x: 4.2, y: 3.4, s: 0.8 },
    { tipo: 'box', amb: 'banhoSuite', x: 0.45, y: 4.22, rot: PI / 2, w: 0.7, d: 0.74 },
    { tipo: 'vaso', amb: 'banhoSuite', x: 0.4, y: 5.1, rot: PI / 2 },
    { tipo: 'pia', amb: 'banhoSuite', x: 1.45, y: 5.32, rot: PI, w: 0.6, d: 0.42 },
    { tipo: 'tapete', amb: 'suite', x: 1.7, y: 7.3, w: 2.4, d: 1.8, cor: '#E4D6C3', borda: '#C9B59A' },
    { tipo: 'camaCasal', amb: 'suite', x: 1.7, y: 7.5, rot: PI, w: 1.6, d: 2.0, manta: '#B9C7D6' },
    { tipo: 'criado', amb: 'suite', x: 0.45, y: 8.23 },
    { tipo: 'criado', amb: 'suite', x: 2.95, y: 8.23 },
    { tipo: 'armario', amb: 'suite', x: 0.37, y: 6.4, rot: PI / 2, w: 1.4, d: 0.6 },
    { tipo: 'planta', amb: 'entradaSuite', x: 2.4, y: 5.3, s: 0.8 },
    { tipo: 'box', amb: 'banho', x: 6.75, y: 4.25, w: 0.7, d: 0.74 },
    { tipo: 'vaso', amb: 'banho', x: 6.78, y: 5.0, rot: -PI / 2 },
    { tipo: 'pia', amb: 'banho', x: 5.65, y: 4.09, w: 0.6, d: 0.42 },
    { tipo: 'camaSolteiro', amb: 'quarto2', x: 6.55, y: 7.55, rot: PI, w: 0.95, d: 1.95, manta: '#E3B9A4' },
    { tipo: 'criado', amb: 'quarto2', x: 5.75, y: 8.25 },
    { tipo: 'escrivaninha', amb: 'quarto2', x: 3.92, y: 7.6, rot: PI / 2, w: 1.1, d: 0.5 },
    { tipo: 'armario', amb: 'quarto2', x: 6.3, y: 5.77, w: 1.6, d: 0.6 },
  ],
  ordem: ['sala', 'cozinha', 'hall', 'banho', 'entradaSuite', 'banhoSuite', 'suite', 'quarto2'],
  entradas: [0.95],
});

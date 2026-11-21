// E05 · Casa Estreita Suíte. 4,6 x 13,0 m = 60 m² (lote 6 x 30). Provisório até o arquiteto validar.
// Social na frente, quarto 2 no meio e a suíte nos fundos, longe da rua. A parede direita
// fica na divisa, sem janelas; o corredor corre por ela.
import { montar } from './montar.js';
const PI = Math.PI;

export default montar({
  id: 'E05',
  nome: 'Casa Estreita Suíte',
  ficha: '60 m² · 2 quartos (1 suíte) · 2 banhos',
  largura: 4.6,
  profundidade: 13.0,

  ambientes: [
    { id: 'sala', nome: 'Sala', x0: 0, y0: 0, x1: 4.6, y1: 3.2, piso: 'madeira' },
    { id: 'cozinha', nome: 'Cozinha', x0: 0, y0: 3.2, x1: 4.6, y1: 5.8, piso: 'porcelanato', rotulo: [2.1, 3.5] },
    { id: 'corredor', nome: 'Corredor', x0: 3.7, y0: 5.8, x1: 4.6, y1: 9.8, piso: 'madeira', rotulo: false, semJanela: true },
    { id: 'banho', nome: 'Banho', x0: 0, y0: 5.8, x1: 3.7, y1: 7.2, piso: 'ceramica', letra: 0.8, rotulo: [2.1, 6.3] },
    { id: 'quarto2', nome: 'Quarto 2', x0: 0, y0: 7.2, x1: 3.7, y1: 9.8, piso: 'madeira', letra: 0.9, rotulo: [2.0, 8.05] },
    { id: 'entradaSuite', nome: 'Suíte', x0: 3.0, y0: 9.8, x1: 4.6, y1: 11.2, piso: 'madeira', rotulo: false },
    { id: 'suite', nome: 'Suíte', x0: 0, y0: 9.8, x1: 3.0, y1: 13.0, piso: 'madeira', area: 11.84, rotulo: [1.5, 10.9] },
    { id: 'banhoSuite', nome: 'Banho', x0: 3.0, y0: 11.2, x1: 4.6, y1: 13.0, piso: 'ceramica', letra: 0.7, rotulo: [3.75, 12.05] },
  ],

  paredes: [
    [0, 0, 4.6, 0], [0, 13.0, 4.6, 13.0], [0, 0, 0, 13.0], [4.6, 0, 4.6, 13.0],
    [0, 5.8, 3.7, 5.8], [3.7, 5.8, 3.7, 9.8], [0, 7.2, 3.7, 7.2], [0, 9.8, 4.6, 9.8],
    [3.0, 11.2, 4.6, 11.2], [3.0, 11.2, 3.0, 13.0], // banho da suíte
  ],
  portas: [
    { id: 'entrada', x: 3.2, y: 0, larg: 0.9, eixo: 'h', abre: 1, dob: 'fim' },
    { id: 'banho', x: 3.7, y: 5.95, larg: 0.7, eixo: 'v', abre: -1, dob: 'ini' },
    { id: 'quarto2', x: 3.7, y: 7.3, larg: 0.8, eixo: 'v', abre: -1, dob: 'ini' },
    { id: 'suite', x: 3.75, y: 9.8, larg: 0.8, eixo: 'h', abre: 1, dob: 'fim' },
    { id: 'banhoSuite', x: 3.1, y: 11.2, larg: 0.7, eixo: 'h', abre: 1, dob: 'ini' },
  ],
  janelas: [
    { seg: [0.6, 0, 2.0, 0], peitoril: 1.0, verga: 2.2, id: 'sala' },
    { seg: [0, 3.8, 0, 5.0], peitoril: 1.1, verga: 2.2, id: 'cozinha' },
    { seg: [0, 6.2, 0, 6.8], peitoril: 1.6, verga: 2.2, id: 'banho' },
    { seg: [0, 7.5, 0, 8.5], peitoril: 1.0, verga: 2.2, id: 'quarto2' },
    { seg: [0, 10.8, 0, 12.0], peitoril: 1.0, verga: 2.2, id: 'suite' },
    { seg: [3.5, 13.0, 4.1, 13.0], peitoril: 1.6, verga: 2.2, id: 'banhoSuite' },
  ],

  moveis: [
    { tipo: 'tapete', amb: 'sala', x: 1.5, y: 1.75, w: 1.7, d: 2.1, cor: '#D9CBB4', borda: '#B49D7C' },
    { tipo: 'rack', amb: 'sala', x: 0.27, y: 1.75, rot: PI / 2, w: 1.6, d: 0.4 },
    { tipo: 'sofa', amb: 'sala', x: 2.75, y: 1.75, rot: -PI / 2, w: 2.0, d: 0.88, cor: '#8A9A86' },
    { tipo: 'mesaCentro', amb: 'sala', x: 1.5, y: 1.75, w: 0.55, d: 0.9 },
    { tipo: 'planta', amb: 'sala', x: 4.2, y: 2.8, s: 0.85 },
    { tipo: 'bancada', amb: 'cozinha', x: 0.38, y: 4.5, rot: PI / 2, w: 2.4, d: 0.62 },
    { tipo: 'geladeira', amb: 'cozinha', x: 4.18, y: 3.65, rot: -PI / 2, w: 0.72, d: 0.7 },
    { tipo: 'maquina', amb: 'cozinha', x: 4.22, y: 4.45, rot: -PI / 2 },
    { tipo: 'mesaJantar', amb: 'cozinha', x: 2.1, y: 4.5, rot: PI / 2, w: 0.75, d: 1.0 },
    { tipo: 'box', amb: 'banho', x: 0.5, y: 6.5, rot: PI / 2, w: 1.2, d: 0.86 },
    { tipo: 'vaso', amb: 'banho', x: 1.45, y: 6.8, rot: PI },
    { tipo: 'pia', amb: 'banho', x: 2.35, y: 6.92, rot: PI, w: 0.6, d: 0.42 },
    { tipo: 'camaSolteiro', amb: 'quarto2', x: 1.05, y: 9.25, rot: PI / 2, w: 0.9, d: 1.9, manta: '#E3B9A4' },
    { tipo: 'escrivaninha', amb: 'quarto2', x: 0.32, y: 7.85, rot: PI / 2, w: 1.0, d: 0.5 },
    { tipo: 'armario', amb: 'quarto2', x: 3.33, y: 9.05, rot: -PI / 2, w: 1.2, d: 0.6 },
    { tipo: 'planta', amb: 'entradaSuite', x: 3.35, y: 10.85, s: 0.75 },
    { tipo: 'tapete', amb: 'suite', x: 1.5, y: 11.8, w: 2.3, d: 1.6, cor: '#E4D6C3', borda: '#C9B59A' },
    { tipo: 'camaCasal', amb: 'suite', x: 1.5, y: 11.97, rot: PI, w: 1.4, d: 1.9, manta: '#B9C7D6' },
    { tipo: 'criado', amb: 'suite', x: 0.4, y: 12.7 },
    { tipo: 'criado', amb: 'suite', x: 2.6, y: 12.7 },
    { tipo: 'armario', amb: 'suite', x: 1.0, y: 10.17, w: 1.8, d: 0.6 },
    { tipo: 'box', amb: 'banhoSuite', x: 4.15, y: 12.55, rot: -PI / 2, w: 0.7, d: 0.74 },
    { tipo: 'vaso', amb: 'banhoSuite', x: 4.2, y: 11.7, rot: -PI / 2 },
    { tipo: 'pia', amb: 'banhoSuite', x: 3.28, y: 12.5, rot: PI / 2, w: 0.6, d: 0.42 },
  ],
  ordem: ['sala', 'cozinha', 'corredor', 'banho', 'quarto2', 'entradaSuite', 'suite', 'banhoSuite'],
  entradas: [3.65],
});

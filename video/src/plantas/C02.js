// C02 · Casa Studio. 5,0 x 6,4 m = 32 m². Provisório até o arquiteto validar.
// Um ambiente só (estar, cozinha e dormir), com serviço e banho fechados atrás da cozinha.
// Eixo x: largura. Eixo y: profundidade (0 = frente).
import { montar } from './montar.js';
const PI = Math.PI;

export default montar({
  id: 'C02',
  nome: 'Casa Studio',
  ficha: '32 m² · studio · 1 banho',
  largura: 5.0,
  profundidade: 6.4,

  ambientes: [
    { id: 'estar', nome: 'Estar', x0: 0, y0: 0, x1: 3.0, y1: 3.0, piso: 'madeira' },
    { id: 'cozinha', nome: 'Cozinha', x0: 3.0, y0: 0, x1: 5.0, y1: 3.0, piso: 'porcelanato', letra: 0.85 },
    { id: 'dormir', nome: 'Dormir', x0: 0, y0: 3.0, x1: 3.2, y1: 6.4, piso: 'madeira' },
    { id: 'servico', nome: 'Serviço', x0: 3.2, y0: 3.0, x1: 5.0, y1: 4.6, piso: 'porcelanato', letra: 0.8, rotulo: [3.75, 3.8] },
    { id: 'banho', nome: 'Banho', x0: 3.2, y0: 4.6, x1: 5.0, y1: 6.4, piso: 'ceramica', letra: 0.8, rotulo: [3.9, 5.85] },
  ],

  paredes: [
    [0, 0, 5.0, 0], [0, 6.4, 5.0, 6.4], [0, 0, 0, 6.4], [5.0, 0, 5.0, 6.4],
    [3.2, 3.0, 3.2, 6.4], // dormir | serviço e banho
    [3.2, 4.6, 5.0, 4.6], // serviço | banho
  ],
  portas: [
    { id: 'entrada', x: 0.4, y: 0, larg: 0.9, eixo: 'h', abre: 1, dob: 'ini' },
    { id: 'banho', x: 3.3, y: 4.6, larg: 0.7, eixo: 'h', abre: 1, dob: 'ini' },
  ],
  janelas: [
    { seg: [1.7, 0, 2.8, 0], peitoril: 1.0, verga: 2.2, id: 'estar' },
    { seg: [3.5, 0, 4.6, 0], peitoril: 1.1, verga: 2.2, id: 'cozinha' },
    { seg: [0, 4.4, 0, 5.6], peitoril: 1.0, verga: 2.2, id: 'dormir' },
    { seg: [5.0, 3.3, 5.0, 4.0], peitoril: 1.3, verga: 2.2, id: 'servico' },
    { seg: [5.0, 4.9, 5.0, 5.4], peitoril: 1.6, verga: 2.2, id: 'banho' },
  ],

  moveis: [
    { tipo: 'tapete', amb: 'estar', x: 1.3, y: 1.6, w: 1.6, d: 1.9, cor: '#D9CBB4', borda: '#B49D7C' },
    { tipo: 'rack', amb: 'estar', x: 0.27, y: 1.6, rot: PI / 2, w: 1.4, d: 0.4 },
    { tipo: 'sofa', amb: 'estar', x: 2.4, y: 1.6, rot: -PI / 2, w: 1.8, d: 0.85, cor: '#8A9A86' },
    { tipo: 'mesaCentro', amb: 'estar', x: 1.3, y: 1.6, w: 0.5, d: 0.85 },
    { tipo: 'estante', amb: 'estar', x: 1.6, y: 2.8, w: 1.4, d: 0.35 },
    { tipo: 'planta', amb: 'estar', x: 2.7, y: 0.4, s: 0.8 },
    { tipo: 'bancada', amb: 'cozinha', x: 4.62, y: 1.15, rot: -PI / 2, w: 2.0, d: 0.62 },
    { tipo: 'geladeira', amb: 'cozinha', x: 4.57, y: 2.6, rot: -PI / 2, w: 0.7, d: 0.68 },
    { tipo: 'planta', amb: 'cozinha', x: 3.35, y: 0.4, s: 0.7 },
    { tipo: 'maquina', amb: 'servico', x: 4.6, y: 3.45, rot: -PI / 2 },
    { tipo: 'tanque', amb: 'servico', x: 4.63, y: 4.17, rot: -PI / 2 },
    { tipo: 'tapete', amb: 'dormir', x: 1.5, y: 5.0, w: 2.2, d: 1.5, cor: '#E4D6C3', borda: '#C9B59A' },
    { tipo: 'camaCasal', amb: 'dormir', x: 1.5, y: 5.35, rot: PI, w: 1.4, d: 1.9, manta: '#B9C7D6' },
    { tipo: 'criado', amb: 'dormir', x: 0.38, y: 6.08 },
    { tipo: 'criado', amb: 'dormir', x: 2.62, y: 6.08 },
    { tipo: 'armario', amb: 'dormir', x: 2.82, y: 3.85, rot: -PI / 2, w: 1.2, d: 0.6 },
    { tipo: 'box', amb: 'banho', x: 4.56, y: 5.96, rot: -PI / 2, w: 0.7, d: 0.74 },
    { tipo: 'vaso', amb: 'banho', x: 4.62, y: 5.12, rot: -PI / 2 },
    { tipo: 'pia', amb: 'banho', x: 3.48, y: 5.9, rot: PI / 2, w: 0.6, d: 0.42 },
  ],
  ordem: ['estar', 'cozinha', 'servico', 'banho', 'dormir'],
  entradas: [0.85],
});

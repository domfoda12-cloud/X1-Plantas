// C03 · Casa Inicial. 6,0 x 7,0 m = 42 m². Provisório até o arquiteto validar.
// O corredor termina na parede dos fundos: é ali que entra a porta do 2º quarto
// quando a casa crescer para o fundo do lote (8 x 20 m).
import { montar } from './montar.js';
const PI = Math.PI;

export default montar({
  id: 'C03',
  nome: 'Casa Inicial',
  ficha: '42 m² · 1 quarto · 1 banho',
  largura: 6.0,
  profundidade: 7.0,

  ambientes: [
    { id: 'sala', nome: 'Sala', x0: 0, y0: 0, x1: 3.4, y1: 3.6, piso: 'madeira' },
    { id: 'cozinha', nome: 'Cozinha', x0: 3.4, y0: 0, x1: 6.0, y1: 3.6, piso: 'porcelanato' },
    { id: 'quarto', nome: 'Quarto', x0: 0, y0: 3.6, x1: 3.4, y1: 7.0, piso: 'madeira' },
    { id: 'hall', nome: 'Hall', x0: 3.4, y0: 3.6, x1: 4.4, y1: 7.0, piso: 'madeira', rotulo: false },
    { id: 'banho', nome: 'Banho', x0: 4.4, y0: 3.6, x1: 6.0, y1: 5.4, piso: 'ceramica', letra: 0.8, rotulo: [5.2, 4.55] },
    { id: 'servico', nome: 'Serviço', x0: 4.4, y0: 5.4, x1: 6.0, y1: 7.0, piso: 'porcelanato', letra: 0.8, rotulo: [5.05, 6.15] },
  ],

  paredes: [
    [0, 0, 6.0, 0], [0, 7.0, 6.0, 7.0], [0, 0, 0, 7.0], [6.0, 0, 6.0, 7.0],
    [0, 3.6, 3.4, 3.6], [4.4, 3.6, 6.0, 3.6], // sala | quarto, cozinha | banho
    [3.4, 3.6, 3.4, 7.0], [4.4, 3.6, 4.4, 7.0], // paredes do hall
    [4.4, 5.4, 6.0, 5.4], // banho | serviço
  ],
  portas: [
    { id: 'entrada', x: 0.5, y: 0, larg: 0.9, eixo: 'h', abre: 1, dob: 'ini' },
    { id: 'quarto', x: 3.4, y: 3.75, larg: 0.8, eixo: 'v', abre: -1, dob: 'ini' },
    { id: 'banho', x: 4.4, y: 4.5, larg: 0.7, eixo: 'v', abre: 1, dob: 'fim' },
    { id: 'servico', x: 4.4, y: 5.55, larg: 0.7, eixo: 'v', abre: 1, dob: 'ini' },
  ],
  janelas: [
    { seg: [1.9, 0, 3.0, 0], peitoril: 1.0, verga: 2.2, id: 'sala' },
    { seg: [4.1, 0, 5.2, 0], peitoril: 1.1, verga: 2.2, id: 'cozinha' },
    { seg: [0, 4.8, 0, 6.0], peitoril: 1.0, verga: 2.2, id: 'quarto' },
    { seg: [6.0, 4.5, 6.0, 5.0], peitoril: 1.6, verga: 2.2, id: 'banho' },
    { seg: [6.0, 6.2, 6.0, 6.8], peitoril: 1.3, verga: 2.2, id: 'servico' },
  ],

  moveis: [
    { tipo: 'tapete', amb: 'sala', x: 1.5, y: 2.1, w: 1.9, d: 2.2, cor: '#D9CBB4', borda: '#B49D7C' },
    { tipo: 'rack', amb: 'sala', x: 0.27, y: 2.2, rot: PI / 2, w: 1.6, d: 0.4 },
    { tipo: 'sofa', amb: 'sala', x: 2.75, y: 2.1, rot: -PI / 2, w: 2.0, d: 0.85, cor: '#7E8FA3' },
    { tipo: 'mesaCentro', amb: 'sala', x: 1.5, y: 2.1, w: 0.55, d: 0.95 },
    { tipo: 'planta', amb: 'sala', x: 3.1, y: 0.4, s: 0.85 },
    { tipo: 'bancada', amb: 'cozinha', x: 5.62, y: 1.5, rot: -PI / 2, w: 2.4, d: 0.62 },
    { tipo: 'geladeira', amb: 'cozinha', x: 5.58, y: 3.17, rot: -PI / 2, w: 0.72, d: 0.7 },
    { tipo: 'mesaJantar', amb: 'cozinha', x: 4.3, y: 1.6, rot: PI / 2, w: 0.75, d: 1.2 },
    { tipo: 'tapete', amb: 'quarto', x: 1.6, y: 5.6, w: 2.4, d: 1.6, cor: '#E4D6C3', borda: '#C9B59A' },
    { tipo: 'camaCasal', amb: 'quarto', x: 1.6, y: 5.95, rot: PI, w: 1.4, d: 1.9, manta: '#D7B9A0' },
    { tipo: 'criado', amb: 'quarto', x: 0.45, y: 6.73 },
    { tipo: 'criado', amb: 'quarto', x: 2.75, y: 6.73 },
    { tipo: 'armario', amb: 'quarto', x: 1.2, y: 3.97, w: 1.8, d: 0.6 },
    { tipo: 'planta', amb: 'quarto', x: 3.05, y: 5.2, s: 0.8 },
    { tipo: 'box', amb: 'banho', x: 5.55, y: 4.05, w: 0.7, d: 0.74 },
    { tipo: 'vaso', amb: 'banho', x: 5.6, y: 4.95, rot: -PI / 2 },
    { tipo: 'pia', amb: 'banho', x: 4.78, y: 3.88, w: 0.6, d: 0.42 },
    { tipo: 'maquina', amb: 'servico', x: 5.62, y: 5.78, rot: -PI / 2 },
    { tipo: 'tanque', amb: 'servico', x: 5.55, y: 6.66, rot: PI },
  ],
  ordem: ['sala', 'cozinha', 'hall', 'banho', 'servico', 'quarto'],
  entradas: [0.95],
});

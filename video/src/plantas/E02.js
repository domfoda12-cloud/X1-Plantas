// E02 · Casa Corredor. 4,2 x 12,4 m = 52 m² (lote 6 x 25). Provisório até o arquiteto validar.
// Cômodos em fila. A parede direita fica na divisa, sem janelas; o corredor corre por ela
// e todos os cômodos têm janela para o recuo do lado esquerdo.
import { montar } from './montar.js';
const PI = Math.PI;

export default montar({
  id: 'E02',
  nome: 'Casa Corredor',
  ficha: '52 m² · 2 quartos · 1 banho',
  largura: 4.2,
  profundidade: 12.4,

  ambientes: [
    { id: 'sala', nome: 'Sala', x0: 0, y0: 0, x1: 4.2, y1: 3.0, piso: 'madeira' },
    { id: 'cozinha', nome: 'Cozinha', x0: 0, y0: 3.0, x1: 4.2, y1: 5.4, piso: 'porcelanato', rotulo: [2.05, 3.25] },
    { id: 'corredor', nome: 'Corredor', x0: 3.3, y0: 5.4, x1: 4.2, y1: 9.5, piso: 'madeira', rotulo: false, semJanela: true },
    { id: 'banho', nome: 'Banho', x0: 0, y0: 5.4, x1: 3.3, y1: 6.9, piso: 'ceramica', letra: 0.8, rotulo: [1.9, 6.0] },
    { id: 'quarto2', nome: 'Quarto 2', x0: 0, y0: 6.9, x1: 3.3, y1: 9.5, piso: 'madeira', letra: 0.9, rotulo: [1.8, 7.75] },
    { id: 'quarto1', nome: 'Quarto 1', x0: 0, y0: 9.5, x1: 4.2, y1: 12.4, piso: 'madeira', rotulo: [3.0, 10.9] },
  ],

  paredes: [
    [0, 0, 4.2, 0], [0, 12.4, 4.2, 12.4], [0, 0, 0, 12.4], [4.2, 0, 4.2, 12.4],
    [0, 5.4, 3.3, 5.4], [3.3, 5.4, 3.3, 9.5], [0, 6.9, 3.3, 6.9], [0, 9.5, 4.2, 9.5],
  ],
  portas: [
    { id: 'entrada', x: 3.1, y: 0, larg: 0.9, eixo: 'h', abre: 1, dob: 'fim' },
    { id: 'banho', x: 3.3, y: 5.55, larg: 0.7, eixo: 'v', abre: -1, dob: 'ini' },
    { id: 'quarto2', x: 3.3, y: 7.0, larg: 0.8, eixo: 'v', abre: -1, dob: 'ini' },
    { id: 'quarto1', x: 3.35, y: 9.5, larg: 0.8, eixo: 'h', abre: 1, dob: 'fim' },
  ],
  janelas: [
    { seg: [0.6, 0, 1.9, 0], peitoril: 1.0, verga: 2.2, id: 'sala' },
    { seg: [0, 3.5, 0, 4.7], peitoril: 1.1, verga: 2.2, id: 'cozinha' },
    { seg: [0, 5.8, 0, 6.4], peitoril: 1.6, verga: 2.2, id: 'banho' },
    { seg: [0, 7.2, 0, 8.2], peitoril: 1.0, verga: 2.2, id: 'quarto2' },
    { seg: [0, 10.6, 0, 11.6], peitoril: 1.0, verga: 2.2, id: 'quarto1' },
    { seg: [1.5, 12.4, 2.3, 12.4], peitoril: 1.6, verga: 2.2, id: 'quarto1' },
  ],

  moveis: [
    { tipo: 'tapete', amb: 'sala', x: 1.45, y: 1.75, w: 1.5, d: 2.0, cor: '#D9CBB4', borda: '#B49D7C' },
    { tipo: 'rack', amb: 'sala', x: 0.27, y: 1.75, rot: PI / 2, w: 1.6, d: 0.4 },
    { tipo: 'sofa', amb: 'sala', x: 2.6, y: 1.75, rot: -PI / 2, w: 1.9, d: 0.85, cor: '#7E8FA3' },
    { tipo: 'mesaCentro', amb: 'sala', x: 1.45, y: 1.75, w: 0.5, d: 0.85 },
    { tipo: 'planta', amb: 'sala', x: 3.8, y: 2.6, s: 0.85 },
    { tipo: 'bancada', amb: 'cozinha', x: 0.38, y: 4.2, rot: PI / 2, w: 2.2, d: 0.62 },
    { tipo: 'geladeira', amb: 'cozinha', x: 3.78, y: 3.5, rot: -PI / 2, w: 0.72, d: 0.7 },
    { tipo: 'maquina', amb: 'cozinha', x: 3.82, y: 4.3, rot: -PI / 2 },
    { tipo: 'mesaJantar', amb: 'cozinha', x: 1.9, y: 4.2, rot: PI / 2, w: 0.7, d: 0.9 },
    { tipo: 'box', amb: 'banho', x: 0.5, y: 6.15, rot: PI / 2, w: 1.3, d: 0.86 },
    { tipo: 'vaso', amb: 'banho', x: 1.4, y: 6.5, rot: PI },
    { tipo: 'pia', amb: 'banho', x: 2.3, y: 6.62, rot: PI, w: 0.6, d: 0.42 },
    { tipo: 'camaSolteiro', amb: 'quarto2', x: 1.05, y: 8.9, rot: PI / 2, w: 0.9, d: 1.9, manta: '#E3B9A4' },
    { tipo: 'escrivaninha', amb: 'quarto2', x: 0.32, y: 7.5, rot: PI / 2, w: 1.0, d: 0.5 },
    { tipo: 'armario', amb: 'quarto2', x: 2.93, y: 8.75, rot: -PI / 2, w: 1.2, d: 0.6 },
    { tipo: 'tapete', amb: 'quarto1', x: 1.9, y: 11.2, w: 2.3, d: 1.5, cor: '#E4D6C3', borda: '#C9B59A' },
    { tipo: 'camaCasal', amb: 'quarto1', x: 1.9, y: 11.37, rot: PI, w: 1.4, d: 1.9, manta: '#B9C7D6' },
    { tipo: 'criado', amb: 'quarto1', x: 0.75, y: 12.1 },
    { tipo: 'criado', amb: 'quarto1', x: 3.05, y: 12.1 },
    { tipo: 'armario', amb: 'quarto1', x: 1.0, y: 9.87, w: 1.8, d: 0.6 },
    { tipo: 'planta', amb: 'quarto1', x: 3.85, y: 11.2, s: 0.75 },
  ],
  ordem: ['sala', 'cozinha', 'corredor', 'banho', 'quarto2', 'quarto1'],
  entradas: [3.55],
});

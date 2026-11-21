// E01 · Casa Estreita. 5,4 x 13,0 m = 70 m² (lote 8 x 30). Provisório até o arquiteto validar.
// Corredor lateral com janelas na parede direita; os cômodos ficam do lado esquerdo e
// cada um tem janela para fora. O serviço abre para o corredor, que é iluminado.
import { montar } from './montar.js';
const PI = Math.PI;

export default montar({
  id: 'E01',
  nome: 'Casa Estreita',
  ficha: '70 m² · 2 quartos · 2 banhos',
  largura: 5.4,
  profundidade: 13.0,

  ambientes: [
    { id: 'sala', nome: 'Sala', x0: 0, y0: 0, x1: 5.4, y1: 3.2, piso: 'madeira' },
    { id: 'cozinha', nome: 'Cozinha', x0: 0, y0: 3.2, x1: 4.4, y1: 5.9, piso: 'porcelanato' },
    { id: 'corredor', nome: 'Corredor', x0: 4.4, y0: 3.2, x1: 5.4, y1: 11.2, piso: 'madeira', rotulo: false },
    { id: 'banho', nome: 'Banho', x0: 0, y0: 5.9, x1: 2.3, y1: 7.5, piso: 'ceramica', letra: 0.8, rotulo: [1.3, 6.85] },
    { id: 'servico', nome: 'Serviço', x0: 2.3, y0: 5.9, x1: 4.4, y1: 7.5, piso: 'porcelanato', letra: 0.8, rotulo: [3.35, 7.0], semJanela: true },
    { id: 'quarto2', nome: 'Quarto 2', x0: 0, y0: 7.5, x1: 4.4, y1: 10.2, piso: 'madeira', rotulo: [2.9, 8.6] },
    { id: 'entradaQ1', nome: 'Quarto 1', x0: 3.6, y0: 10.2, x1: 4.4, y1: 11.2, piso: 'madeira', rotulo: false },
    { id: 'quarto1', nome: 'Quarto 1', x0: 0, y0: 10.2, x1: 3.6, y1: 13.0, piso: 'madeira', area: 10.88, rotulo: [2.4, 11.3] },
    { id: 'banho2', nome: 'Banho 2', x0: 3.6, y0: 11.2, x1: 5.4, y1: 13.0, piso: 'ceramica', letra: 0.7, rotulo: [4.5, 12.0] },
  ],

  paredes: [
    [0, 0, 5.4, 0], [0, 13.0, 5.4, 13.0], [0, 0, 0, 13.0], [5.4, 0, 5.4, 13.0],
    [0, 5.9, 4.4, 5.9], [0, 7.5, 4.4, 7.5], [2.3, 5.9, 2.3, 7.5], [0, 10.2, 3.6, 10.2],
    [4.4, 5.9, 4.4, 11.2], // parede do corredor
    [3.6, 11.2, 5.4, 11.2], [3.6, 11.2, 3.6, 13.0], // banho 2
  ],
  vaos: [{ x: 4.4, y: 6.0, larg: 1.4, eixo: 'v' }], // serviço aberto para o corredor
  portas: [
    { id: 'entrada', x: 0.4, y: 0, larg: 0.9, eixo: 'h', abre: 1, dob: 'ini' },
    { id: 'banho', x: 2.3, y: 6.6, larg: 0.7, eixo: 'v', abre: -1, dob: 'fim' },
    { id: 'quarto2', x: 4.4, y: 7.65, larg: 0.8, eixo: 'v', abre: -1, dob: 'ini' },
    { id: 'quarto1', x: 4.4, y: 10.3, larg: 0.8, eixo: 'v', abre: -1, dob: 'ini' },
    { id: 'banho2', x: 4.5, y: 11.2, larg: 0.7, eixo: 'h', abre: 1, dob: 'fim' },
  ],
  janelas: [
    { seg: [3.2, 0, 4.6, 0], peitoril: 1.0, verga: 2.2, id: 'sala' },
    { seg: [0, 1.0, 0, 2.4], peitoril: 1.0, verga: 2.2, id: 'sala' },
    { seg: [0, 3.6, 0, 4.8], peitoril: 1.1, verga: 2.2, id: 'cozinha' },
    { seg: [5.4, 4.2, 5.4, 5.2], peitoril: 1.0, verga: 2.2, id: 'corredor' },
    { seg: [5.4, 6.3, 5.4, 7.3], peitoril: 1.0, verga: 2.2, id: 'corredor' },
    { seg: [5.4, 8.6, 5.4, 9.6], peitoril: 1.0, verga: 2.2, id: 'corredor' },
    { seg: [0, 6.75, 0, 7.25], peitoril: 1.6, verga: 2.2, id: 'banho' },
    { seg: [0, 8.2, 0, 9.4], peitoril: 1.0, verga: 2.2, id: 'quarto2' },
    { seg: [0, 11.4, 0, 12.4], peitoril: 1.0, verga: 2.2, id: 'quarto1' },
    { seg: [4.0, 13.0, 4.6, 13.0], peitoril: 1.6, verga: 2.2, id: 'banho2' },
  ],

  moveis: [
    { tipo: 'tapete', amb: 'sala', x: 3.95, y: 1.7, w: 1.6, d: 2.2, cor: '#D9CBB4', borda: '#B49D7C' },
    { tipo: 'rack', amb: 'sala', x: 5.13, y: 1.7, rot: -PI / 2, w: 1.6, d: 0.4 },
    { tipo: 'sofa', amb: 'sala', x: 2.6, y: 1.7, rot: PI / 2, w: 2.0, d: 0.85, cor: '#8A9A86' },
    { tipo: 'mesaCentro', amb: 'sala', x: 3.9, y: 1.7, w: 0.55, d: 0.95 },
    { tipo: 'poltrona', amb: 'sala', x: 1.3, y: 2.55, rot: PI / 2, cor: '#C9A27A' },
    { tipo: 'planta', amb: 'sala', x: 0.4, y: 2.8, s: 0.85 },
    { tipo: 'bancada', amb: 'cozinha', x: 1.6, y: 5.52, rot: PI, w: 2.6, d: 0.62 },
    { tipo: 'geladeira', amb: 'cozinha', x: 3.4, y: 5.5, rot: PI, w: 0.72, d: 0.7 },
    { tipo: 'mesaJantar', amb: 'cozinha', x: 2.0, y: 4.0, w: 0.8, d: 1.2 },
    { tipo: 'box', amb: 'banho', x: 0.44, y: 6.34, rot: PI / 2, w: 0.7, d: 0.74 },
    { tipo: 'vaso', amb: 'banho', x: 0.4, y: 7.1, rot: PI / 2 },
    { tipo: 'pia', amb: 'banho', x: 1.35, y: 6.19, w: 0.6, d: 0.42 },
    { tipo: 'maquina', amb: 'servico', x: 2.75, y: 6.29 },
    { tipo: 'tanque', amb: 'servico', x: 3.45, y: 6.27 },
    { tipo: 'planta', amb: 'corredor', x: 4.9, y: 3.6, s: 0.7 },
    { tipo: 'camaCasal', amb: 'quarto2', x: 1.05, y: 8.85, rot: PI / 2, w: 1.4, d: 1.9, manta: '#E3B9A4' },
    { tipo: 'criado', amb: 'quarto2', x: 0.32, y: 7.87 },
    { tipo: 'criado', amb: 'quarto2', x: 0.32, y: 9.83 },
    { tipo: 'armario', amb: 'quarto2', x: 4.0, y: 9.45, rot: -PI / 2, w: 1.2, d: 0.6 },
    { tipo: 'tapete', amb: 'quarto1', x: 1.8, y: 11.8, w: 2.4, d: 1.6, cor: '#E4D6C3', borda: '#C9B59A' },
    { tipo: 'camaCasal', amb: 'quarto1', x: 1.8, y: 11.97, rot: PI, w: 1.4, d: 1.9, manta: '#B9C7D6' },
    { tipo: 'criado', amb: 'quarto1', x: 0.5, y: 12.7 },
    { tipo: 'criado', amb: 'quarto1', x: 3.1, y: 12.7 },
    { tipo: 'armario', amb: 'quarto1', x: 1.4, y: 10.57, w: 1.8, d: 0.6 },
    { tipo: 'box', amb: 'banho2', x: 4.95, y: 12.55, rot: -PI / 2, w: 0.7, d: 0.74 },
    { tipo: 'vaso', amb: 'banho2', x: 4.0, y: 12.6, rot: PI },
    { tipo: 'pia', amb: 'banho2', x: 3.88, y: 11.75, rot: PI / 2, w: 0.6, d: 0.42 },
  ],
  ordem: ['sala', 'cozinha', 'corredor', 'servico', 'banho', 'quarto2', 'entradaQ1', 'quarto1', 'banho2'],
  entradas: [0.85],
});

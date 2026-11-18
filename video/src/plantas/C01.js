// C01 · Casa Compacta. Dados da planta em metros. Provisório até o arquiteto validar.
// Eixo x: largura (0 a 6,5 m). Eixo y: profundidade (0 = frente, 8,5 = fundos).
// Formato de cada arquivo de planta: ver ../plantas/LEIA-ME.md
const PI = Math.PI;

export default {
  id: 'C01',
  nome: 'Casa Compacta',
  ficha: '55 m² · 2 quartos · 1 banho',
  largura: 6.5,
  profundidade: 8.5,

  ambientes: [
    { id: 'sala', nome: 'Sala', x0: 0, y0: 0, x1: 3.5, y1: 4.2, piso: 'madeira' },
    { id: 'cozinha', nome: 'Cozinha', x0: 3.5, y0: 0, x1: 6.5, y1: 4.2, piso: 'porcelanato' },
    { id: 'quarto1', nome: 'Quarto 1', x0: 0, y0: 4.2, x1: 3.2, y1: 8.5, piso: 'madeira' },
    { id: 'quarto2', nome: 'Quarto 2', x0: 3.2, y0: 5.8, x1: 6.5, y1: 8.5, piso: 'madeira' },
    { id: 'banho', nome: 'Banho', x0: 4.6, y0: 4.2, x1: 6.5, y1: 5.8, piso: 'ceramica' },
    { id: 'hall', nome: 'Hall', x0: 3.2, y0: 4.2, x1: 4.6, y1: 5.8, piso: 'madeira', rotulo: false },
  ],

  // Paredes como segmentos. As aberturas de porta são os vãos entre segmentos.
  paredes: [
    [0, 0, 1.0, 0], [1.9, 0, 6.5, 0], // frente, porta de entrada entre 1,0 e 1,9
    [0, 8.5, 6.5, 8.5], // fundos
    [0, 0, 0, 8.5], // lateral esquerda
    [6.5, 0, 6.5, 8.5], // lateral direita
    [0, 4.2, 3.2, 4.2], // sala / quarto 1
    [4.6, 4.2, 6.5, 4.2], // cozinha / banho
    [3.2, 4.2, 3.2, 4.4], [3.2, 5.2, 3.2, 8.5], // porta do quarto 1
    [3.2, 5.8, 3.4, 5.8], [4.2, 5.8, 6.5, 5.8], // porta do quarto 2
    [4.6, 4.2, 4.6, 4.5], [4.6, 5.3, 4.6, 5.8], // porta do banho
  ],

  // Janelas: trecho de parede com peitoril e verga (alturas em metros).
  janelas: [
    { seg: [2.2, 0, 3.2, 0], peitoril: 1.0, verga: 2.2, id: 'sala' },
    { seg: [4.2, 0, 5.6, 0], peitoril: 1.1, verga: 2.2, id: 'cozinha' },
    { seg: [0, 5.6, 0, 7.0], peitoril: 1.0, verga: 2.2, id: 'quarto1' },
    { seg: [4.2, 8.5, 5.6, 8.5], peitoril: 1.0, verga: 2.2, id: 'quarto2' },
    { seg: [6.5, 4.7, 6.5, 5.3], peitoril: 1.6, verga: 2.2, id: 'banho' },
  ],

  // Portas: dobradiça (x, y), raio da folha e ângulos de abertura (0 = +x, PI/2 = +y).
  portas: [
    { id: 'entrada', x: 1.0, y: 0, r: 0.9, a0: 0, a1: PI / 2 },
    { id: 'quarto1', x: 3.2, y: 4.4, r: 0.8, a0: PI / 2, a1: PI },
    { id: 'quarto2', x: 3.4, y: 5.8, r: 0.8, a0: 0, a1: PI / 2 },
    { id: 'banho', x: 4.6, y: 4.5, r: 0.8, a0: 0, a1: PI / 2 },
  ],

  // Móveis: centro em metros da planta, rotação em radianos (0 = frente do móvel para +y).
  moveis: [
    { tipo: 'tapete', amb: 'sala', x: 1.45, y: 2.2, w: 2.0, d: 2.5, cor: '#D9CBB4', borda: '#B49D7C' },
    { tipo: 'sofa', amb: 'sala', x: 2.78, y: 2.2, rot: -PI / 2, w: 2.1, d: 0.88, cor: '#8A9A86' },
    { tipo: 'rack', amb: 'sala', x: 0.3, y: 2.2, rot: PI / 2, w: 1.7, d: 0.4 },
    { tipo: 'mesaCentro', amb: 'sala', x: 1.55, y: 2.2, w: 0.6, d: 1.0 },
    { tipo: 'planta', amb: 'sala', x: 0.45, y: 0.5, s: 1.0 },
    { tipo: 'planta', amb: 'sala', x: 3.15, y: 3.85, s: 0.8 },
    { tipo: 'bancada', amb: 'cozinha', x: 6.12, y: 1.75, rot: -PI / 2, w: 3.0, d: 0.62 },
    { tipo: 'geladeira', amb: 'cozinha', x: 6.07, y: 3.72, rot: -PI / 2, w: 0.72, d: 0.7 },
    { tipo: 'mesaJantar', amb: 'cozinha', x: 4.55, y: 2.35, w: 0.85, d: 1.3 },
    { tipo: 'planta', amb: 'cozinha', x: 3.85, y: 0.5, s: 0.8 },
    { tipo: 'tapete', amb: 'quarto1', x: 1.6, y: 7.1, w: 2.3, d: 1.7, cor: '#E4D6C3', borda: '#C9B59A' },
    { tipo: 'camaCasal', amb: 'quarto1', x: 1.6, y: 7.42, rot: PI, w: 1.6, d: 2.0, manta: '#B9C7D6' },
    { tipo: 'criado', amb: 'quarto1', x: 0.5, y: 8.17 },
    { tipo: 'criado', amb: 'quarto1', x: 2.7, y: 8.17 },
    { tipo: 'armario', amb: 'quarto1', x: 1.05, y: 4.58, w: 1.8, d: 0.6 },
    { tipo: 'planta', amb: 'quarto1', x: 2.85, y: 5.95, s: 0.85 },
    { tipo: 'camaSolteiro', amb: 'quarto2', x: 5.45, y: 7.55, rot: -PI / 2, w: 0.95, d: 1.95, manta: '#E3B9A4' },
    { tipo: 'criado', amb: 'quarto2', x: 6.17, y: 6.8 },
    { tipo: 'escrivaninha', amb: 'quarto2', x: 3.95, y: 8.17, rot: PI, w: 1.1, d: 0.5 },
    { tipo: 'armario', amb: 'quarto2', x: 5.2, y: 6.17, w: 1.6, d: 0.55 },
    { tipo: 'box', amb: 'banho', x: 6.09, y: 4.64, w: 0.68, d: 0.74 },
    { tipo: 'vaso', amb: 'banho', x: 6.17, y: 5.42, rot: -PI / 2 },
    { tipo: 'pia', amb: 'banho', x: 5.15, y: 5.52, rot: PI, w: 0.6, d: 0.42 },
  ],

  // Ordem em que os cômodos ganham vida
  ordem: ['sala', 'cozinha', 'hall', 'banho', 'quarto1', 'quarto2'],

  // Jardim: x do centro de cada caminho até a rua; árvores [x, y, raio] (opcional: o motor gera em volta).
  entradas: [1.45],
  arvores: [[-2.6, -1.8, 1.5], [9.2, -1.2, 1.7], [-2.8, 4.5, 1.4], [9.4, 4.2, 1.5], [-2.5, 10.6, 1.8], [9.1, 10.9, 1.6], [3.4, 12.2, 1.9], [-4.6, 8.0, 1.6], [11.0, 7.6, 1.7], [0.6, 13.0, 1.4], [6.6, 13.6, 1.5]],
};

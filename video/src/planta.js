// Casa Compacta: dados da planta (em metros). Provisório até o arquiteto validar.
// Eixo x: largura (0 a 6,5 m). Eixo y: profundidade (0 = frente, 8,5 = fundos).

export const LARGURA = 6.5;
export const PROFUNDIDADE = 8.5;
export const PE_DIREITO = 2.8;
export const ESPESSURA = 0.15;

export const ambientes = [
  { id: 'sala', nome: 'Sala', x0: 0, y0: 0, x1: 3.5, y1: 4.2, cor: '#E8D7BC' },
  { id: 'cozinha', nome: 'Cozinha', x0: 3.5, y0: 0, x1: 6.5, y1: 4.2, cor: '#D5E0CF' },
  { id: 'quarto1', nome: 'Quarto 1', x0: 0, y0: 4.2, x1: 3.2, y1: 8.5, cor: '#EADCC6' },
  { id: 'quarto2', nome: 'Quarto 2', x0: 3.2, y0: 5.8, x1: 6.5, y1: 8.5, cor: '#EADCC6' },
  { id: 'banho', nome: 'Banho', x0: 4.6, y0: 4.2, x1: 6.5, y1: 5.8, cor: '#D3E2E6' },
  { id: 'hall', nome: 'Hall', x0: 3.2, y0: 4.2, x1: 4.6, y1: 5.8, cor: '#F1EBE0' },
];

// Paredes como segmentos. As aberturas de porta são os vãos entre segmentos.
export const paredes = [
  // Externas
  [0, 0, 1.0, 0], [1.9, 0, 6.5, 0], // frente, porta de entrada entre 1,0 e 1,9
  [0, 8.5, 6.5, 8.5], // fundos
  [0, 0, 0, 8.5], // lateral esquerda
  [6.5, 0, 6.5, 8.5], // lateral direita
  // Internas
  [0, 4.2, 3.2, 4.2], // sala / quarto 1
  [4.6, 4.2, 6.5, 4.2], // cozinha / banho
  [3.2, 4.2, 3.2, 4.4], [3.2, 5.2, 3.2, 8.5], // hall e quarto 2 / quarto 1, porta do quarto 1
  [3.2, 5.8, 3.4, 5.8], [4.2, 5.8, 6.5, 5.8], // hall e banho / quarto 2, porta do quarto 2
  [4.6, 4.2, 4.6, 4.5], [4.6, 5.3, 4.6, 5.8], // hall / banho, porta do banho
];

// Janelas: trecho de parede com peitoril e verga (alturas em metros).
export const janelas = [
  { seg: [2.2, 0, 3.2, 0], peitoril: 1.0, verga: 2.2, id: 'sala' },
  { seg: [4.2, 0, 5.6, 0], peitoril: 1.1, verga: 2.2, id: 'cozinha' },
  { seg: [0, 5.6, 0, 7.0], peitoril: 1.0, verga: 2.2, id: 'quarto1' },
  { seg: [4.2, 8.5, 5.6, 8.5], peitoril: 1.0, verga: 2.2, id: 'quarto2' },
  { seg: [6.5, 4.7, 6.5, 5.3], peitoril: 1.6, verga: 2.2, id: 'banho' },
];

export const areaTotal = () => LARGURA * PROFUNDIDADE; // ~55 m²

// Portas: dobradiça (x, y), raio da folha e ângulos de abertura (radianos, 0 = +x, PI/2 = +y).
export const portas = [
  { id: 'entrada', x: 1.0, y: 0, r: 0.9, a0: 0, a1: Math.PI / 2 },
  { id: 'quarto1', x: 3.2, y: 4.4, r: 0.8, a0: Math.PI / 2, a1: Math.PI },
  { id: 'quarto2', x: 3.4, y: 5.8, r: 0.8, a0: 0, a1: Math.PI / 2 },
  { id: 'banho', x: 4.6, y: 4.5, r: 0.8, a0: 0, a1: Math.PI / 2 },
];

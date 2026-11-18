// Planta usada pelo vídeo de anúncio (cena.js): a Casa Compacta (C01).
// Os dados de cada planta ficam em ./plantas/<ID>.js; este arquivo só reexporta a C01
// no formato antigo, para o vídeo continuar igual.
import C01 from './plantas/C01.js';

export const LARGURA = C01.largura;
export const PROFUNDIDADE = C01.profundidade;
export const PE_DIREITO = 2.8;
export const ESPESSURA = 0.15;
export const { ambientes, paredes, janelas, portas } = C01;
export const areaTotal = () => LARGURA * PROFUNDIDADE; // ~55 m²
export const planta = C01;

// Ajuda a escrever os dados de uma planta: as paredes entram inteiras e as portas e vãos
// cortam a abertura sozinhos. Devolve o formato que o motor (casa3d.js) lê.
//
// Porta: { id, x, y, larg, eixo, abre, dob }
//   (x, y)  início do vão (a menor coordenada ao longo da parede)
//   larg    largura da folha em metros (0,7 banho, 0,8 quartos, 0,9 entrada)
//   eixo    'h' para parede horizontal (y fixo) ou 'v' para vertical (x fixo)
//   abre    +1 abre para +y (eixo h) ou +x (eixo v); -1 para o outro lado
//   dob     'ini' dobradiça no início do vão, 'fim' no fim
// Vão sem porta (passagem): { x, y, larg, eixo }
const ANG = { '+x': 0, '+y': Math.PI / 2, '-x': Math.PI, '-y': -Math.PI / 2 };

function cortar(paredes, { x, y, larg, eixo }) {
  const h = eixo === 'h';
  let achou = false;
  const out = paredes.flatMap((p) => {
    const [x0, y0, x1, y1] = p;
    const ph = y0 === y1;
    if (ph !== h) return [p];
    const fixo = h ? y0 : x0; const a = h ? Math.min(x0, x1) : Math.min(y0, y1); const b = h ? Math.max(x0, x1) : Math.max(y0, y1);
    const ini = h ? x : y; const fim = ini + larg;
    if (Math.abs(fixo - (h ? y : x)) > 1e-6 || ini < a - 1e-6 || fim > b + 1e-6) return [p];
    achou = true;
    const seg = (u, v) => (h ? [u, fixo, v, fixo] : [fixo, u, fixo, v]);
    return [seg(a, ini), seg(fim, b)].filter((s) => Math.abs(h ? s[2] - s[0] : s[3] - s[1]) > 0.01);
  });
  if (!achou) throw new Error(`Vão em (${x}, ${y}) não cai inteiro sobre nenhuma parede ${eixo}`);
  return out;
}

export function montar(dados) {
  let paredes = dados.paredes.map((p) => [...p]);
  const portas = [];
  for (const v of dados.vaos || []) paredes = cortar(paredes, v);
  for (const d of dados.portas || []) {
    paredes = cortar(paredes, d);
    const h = d.eixo === 'h';
    const fim = d.dob === 'fim';
    const hx = h ? d.x + (fim ? d.larg : 0) : d.x; const hy = h ? d.y : d.y + (fim ? d.larg : 0);
    const a0 = ANG[(fim ? '-' : '+') + (h ? 'x' : 'y')];
    let a1 = ANG[(d.abre > 0 ? '+' : '-') + (h ? 'y' : 'x')];
    if (a1 - a0 > Math.PI) a1 -= 2 * Math.PI;
    if (a0 - a1 > Math.PI) a1 += 2 * Math.PI;
    portas.push({ id: d.id, x: hx, y: hy, r: d.larg, a0, a1 });
  }
  return { ...dados, paredes, portas, vaos: undefined };
}

// Ensaio dos fluxos fixos sem gastar nada (26/11/2026): roda cada .claude/workflows/*.js do começo ao fim com agentes
// de mentira, que devolvem um objeto na forma pedida. Pega o erro que a sintaxe não pega (variável sem declarar,
// campo que não existe), como o "passe is not defined" da primeira rodada do pagina-ebook.
// Uso: node ferramentas/fluxos-ensaio.cjs   (o checar.py roda)
const fs = require('fs');
const path = require('path');

const PASTA = path.join(__dirname, '..', '.claude', 'workflows');
const ARGS = {
  'texto-publico': { arquivo: 'a.md', pedido: 'ensaio' },
  'pagina-ebook': { pagina: 11, previa: '/tmp/ensaio', fonte: 'x.py', pedido: 'ensaio' },
  planta: { rascunho: 'r.py', casa: 'C01', objetivo: 'ensaio' },
  decisao: { proposta: 'p.md', pergunta: 'ensaio', motivo: 'vai ao público' },
  'prova-de-entrada': { papeis: ['redator'], tag: 'ensaio' },
};

// valor de mentira na forma do schema; "saida" de programa devolve um JSON plausível para cada comando
let QUEBRADO = false;  // 2ª passada: todo programa devolve lixo e a Vera diz SIM; nenhum fluxo pode aprovar
function falso(schema, prompt) {
  if (!schema) return 'ok';
  if (schema.enum) return QUEBRADO ? schema.enum[0] : (schema.enum[1] || schema.enum[0]);
  switch (schema.type) {
    case 'object': {
      const o = {};
      for (const [k, s] of Object.entries(schema.properties || {})) o[k] = falso(s, prompt);
      if ('saida' in o) o.saida = saidaDe(prompt);
      if ('codigo' in o) o.codigo = 0;
      return o;
    }
    case 'array': return Array.from({ length: Math.max(schema.minItems || 0, 2) }, () => falso(schema.items, prompt));
    case 'integer': return 1;
    case 'number': return 9;
    case 'boolean': return true;
    default: return 'x';
  }
}
function saidaDe(p) {
  if (QUEBRADO && !p.includes('registrar') && !p.includes('prova-')) return 'Traceback (most recent call last):\n  File x';
  if (p.includes('fluxo.py texto')) return 'Comando rodado.\n[{"linha": 3, "tipo": "erro", "msg": "frase vetada: x"}]';
  if (p.includes('fluxo.py pagina')) return '{"texto": "t", "achados": [{"linha": 1, "tipo": "erro", "msg": "m"}]}';
  if (p.includes('fluxo.py passe')) return '{"ok": false, "erros": ["e"]}';
  if (p.includes('fluxo.py juri')) return '{"completa": true, "erros": [], "notas": [8, 8, 8], "media": 8, "passa": false, "proximo": "reescrever uma vez"}';
  if (p.includes('fluxo.py registrar')) return 'lição gravada\n{"gravado": true}';
  if (p.includes('fluxo.py prova-estado')) return '{"redator": {"nivel": 2, "voltam": []}, "_niveis": {"2": "n"}}';
  if (p.includes('fluxo.py prova-nota')) return p.includes('confirmados') ? '{"redator": {"passou": true}}' : '{"_em_disputa": ["1:1"]}';
  return '[ERRO] porta que bate\nPassou nas conferências: 1 de 11 com erro.';
}

async function ensaiar(nome) {
  const src = fs.readFileSync(path.join(PASTA, nome + '.js'), 'utf8').replace('export const meta', 'const meta');
  let n = 0, gasto = 0;
  const agent = async (prompt, opts = {}) => { n++; gasto += 10; return falso(opts.schema, String(prompt)); };
  const parallel = async thunks => Promise.all(thunks.map(t => t()));
  const budget = { total: null, spent: () => gasto, remaining: () => Infinity };
  const fn = new Function('agent', 'parallel', 'pipeline', 'phase', 'log', 'budget', 'args', 'workflow',
    `"use strict"; return (async () => {\n${src}\n})()`);  // estrito como o fluxo de verdade
  const r = await fn(agent, parallel, null, () => {}, () => {}, budget, ARGS[nome], null);
  if (!r || typeof r !== 'object') throw new Error('não devolveu objeto');
  if (nome !== 'prova-de-entrada' && !r.registro) throw new Error('não montou o registro da rodada');
  if (QUEBRADO && /^(aprovad|pronto)/.test(String(r.resultado))) throw new Error(`aprovou com o programa quebrado: "${r.resultado}"`);
  return n;
}

(async () => {
  let falhou = 0;
  for (const f of fs.readdirSync(PASTA).filter(f => f.endsWith('.js')).sort()) {
    const nome = f.replace(/\.js$/, '');
    if (!ARGS[nome]) { console.log(`[ERRO] ${nome}: sem args de ensaio em ferramentas/fluxos-ensaio.cjs`); falhou++; continue; }
    try {
      QUEBRADO = false; const n = await ensaiar(nome);
      QUEBRADO = true; await ensaiar(nome);
      console.log(`[OK ] ${nome}: ensaio até o fim (${n} agentes de mentira) e falha fechada com o programa quebrado`);
    } catch (e) { console.log(`[ERRO] ${nome}${QUEBRADO ? ' (programa quebrado)' : ''}: ${e.message}`); falhou++; }
  }
  process.exit(falhou ? 1 : 0);
})();

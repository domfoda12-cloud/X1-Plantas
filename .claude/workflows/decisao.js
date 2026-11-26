export const meta = {
  name: 'decisao',
  description: 'Júri (CONSELHO.md 5b, regras de 25/11): 3 ângulos com régua, revisão anônima, presidente que não votou confere 5 fatos, programa recusa rodada incompleta',
  whenToUse: 'Só para decisão que custa dinheiro, vai ao público ou não se desfaz, com o motivo escrito na ficha. args: {proposta, pergunta, motivo, autor?, rodizio?, ficha?, calibracao?}',
  phases: [
    { title: 'Jurados', detail: '3 modelos, um ângulo cada (comprador, dinheiro, risco); 2 defeitos com arquivo e linha antes da nota' },
    { title: 'Revisão anônima', detail: 'cada jurado ordena as outras opiniões sem saber de quem são' },
    { title: 'Presidente', detail: 'o 4º modelo, que não votou, confere pelo menos 5 fatos no repositório' },
    { title: 'Programa', detail: 'fluxo.py juri: recusa rodada incompleta, piso 7, média 8,5, nota perdida por fato falso' },
    { title: 'Reescrita', detail: 'no máximo uma; se não chegar, vai ao dono com as duas notas' },
    { title: 'Colheita', detail: 'fluxo.py registrar: gasto e lições no arquivo do autor da proposta' },
  ],
}

const A = args || {}
if (!A.proposta || !A.pergunta || !A.motivo) throw new Error('args: {proposta: arquivo, pergunta: o que se decide, motivo: custa dinheiro / vai ao público / não se desfaz}')
const AUTOR = A.autor || 'maestro'
// Rodízio (regra 3): os 4 modelos giram; os 3 primeiros julgam, o 4º preside. Os ângulos giram junto (melhoria 1c).
const MODELOS = ['haiku', 'sonnet', 'opus', 'fable']
const ANG = ['comprador', 'dinheiro', 'risco']
const R = Number(A.rodizio || 0)
const gira = (xs, n) => xs.map((_, i) => xs[(i + n) % xs.length])

// Régua (regra 0): pedidos/anexos/juri-proximas-melhorias.md, parte 1a e 1b
const REGUA = {
  '3': 'Não dá para executar como está: falta a peça que faz funcionar, o fato central está errado ou fere uma regra que não muda. Ex.: plano de lançamento da rodada 6 (sem como receber o Pix).',
  '6': 'A ideia está certa e a estrutura serve, mas tem fato errado ou não testado, ou um passo anda antes do sim. Ex.: proposta v3 (3 fatos errados, passo 3 antes do sim).',
  '9': 'Pode ir ao dono ou ao público como está: todo número de ferramenta, nenhuma regra ferida, o comprador entende e ganha, nada antes do sim. Ex.: "cabe num lote de 8 x 15 m (no mínimo 8,0 x 13,0 m)".',
}
const COMO = 'Escreva as críticas primeiro; a nota vem por último. Escolha a âncora mais parecida (3, 6 ou 9) e suba ou desça no máximo 2 pontos, com o motivo. ' +
  '0 a 2: faz mal se executado. 10: vale 9 e já tem resultado medido. Tetos: fato central errado, no máximo 5; fere regra que não muda ou decisão do dono em vigor, no máximo 3; ' +
  'parte que depende de resposta que o dono não deu fica sem nota e vira pergunta.'
const PERGUNTA = {
  comprador: 'Você é quem tem o lote e vai construir com pedreiro, com dinheiro contado. Se isto for feito como está, você entende, confia e fica mais perto de achar a casa que cabe no seu lote? Aponte o trecho em que você se confunde, desconfia ou se decepciona. (Abra ebook/referencias/MERCADO.md e ESTRATEGIA.md, seção 9.)',
  dinheiro: 'Isto aproxima o primeiro Pix ou baixa o custo por venda (custo por contato ÷ conversão)? Diga qual dos dois números isto mexe, quanto custa (R$, tokens, horas do dono) e o que deixa de ser feito por causa disto. (Abra PAINEL.md, seções 4 e 7.)',
  risco: "O que aqui pode dar errado e não tem volta? Procure: promessa proibida, lei, licença, dado pessoal, gasto ou instalação sem o 'sim', suposição tratada como decisão do dono, e passo que falta. (Abra CLAUDE.md, 'Regras que não mudam'; ESTRATEGIA.md, seção 9; CONSELHO.md, seções 6 e 6b.)",
}

const CITA = { type: 'object', properties: { arquivo: { type: 'string' }, linha: { type: 'integer' }, texto: { type: 'string' } }, required: ['arquivo', 'linha', 'texto'] }
const OPINIAO = {
  type: 'object',
  properties: {
    defeitos: { type: 'array', items: CITA, minItems: 2, description: 'pelo menos 2, cada um com arquivo e linha' },
    criticas: { type: 'array', items: CITA },
    fatos_afirmados: { type: 'array', items: { type: 'object', properties: { fato: { type: 'string' }, arquivo: { type: 'string' }, linha: { type: 'integer' } }, required: ['fato', 'arquivo', 'linha'] } },
  perguntas_ao_dono: { type: 'array', items: { type: 'string' } },
    nota: { type: 'number' }, motivo_da_nota: { type: 'string' },
  },
  required: ['defeitos', 'criticas', 'fatos_afirmados', 'nota', 'motivo_da_nota'],
}
const ORDEM = { type: 'object', properties: { ordem: { type: 'array', items: { type: 'string' } }, porque: { type: 'string' } }, required: ['ordem', 'porque'] }
const PRES = {
  type: 'object',
  properties: {
    fatos: { type: 'array', minItems: 5, items: { type: 'object', properties: { fato: { type: 'string' }, de: { type: 'integer' }, arquivo: { type: 'string' }, linha: { type: 'integer' }, confirmado: { type: 'boolean' } }, required: ['fato', 'de', 'arquivo', 'linha', 'confirmado'] } },
    sintese: { type: 'string' },
    corrigir_ja: { type: 'array', items: { type: 'object', properties: { chave: { type: 'string' }, texto: { type: 'string' }, licao: { type: 'string' } }, required: ['chave', 'texto', 'licao'] } },
  },
  required: ['fatos', 'sintese', 'corrigir_ja'],
}
const SAIDA = { type: 'object', properties: { codigo: { type: 'integer' }, saida: { type: 'string' } }, required: ['codigo', 'saida'] }
// o agente às vezes embrulha a saída em frases: pega o último JSON inteiro que aparece nela
const lerJson = (s, padrao) => {
  const t = String(s || '')
  try { return JSON.parse(t) } catch (e) {}
  for (let i = t.length - 1; i >= 0; i--) {
    if (t[i] !== '}' && t[i] !== ']') continue
    const abre = t[i] === '}' ? '{' : '['
    for (let j = t.indexOf(abre); j >= 0 && j < i; j = t.indexOf(abre, j + 1)) {
      try { return JSON.parse(t.slice(j, i + 1)) } catch (e) {}
    }
  }
  return padrao
}

const ID_INICIO = budget.spent()  // identifica a rodada (o registrar recusa gravar duas vezes)
const gasto = {}, conf = {}, achados = []
async function medir(nome, tipo, fn) {
  const antes = budget.spent()
  const r = await fn()
  gasto[nome] = (gasto[nome] || 0) + (budget.spent() - antes)
  conf[nome] = conf[nome] || { nome, tipo, achados_proprios: 0 }
  return r
}

async function umaRodada(n, proposta) {
  const mods = gira(MODELOS, R + n - 1), angs = gira(ANG, R + n - 1)
  const jurados = angs.map((a, i) => ({ angulo: a, modelo: mods[i] }))
  const presidente = mods[3]
  phase('Jurados')
  const antesJ = budget.spent()
  const ops = await parallel(jurados.map((j, i) => () => agent(
    `Você é jurado do X1-Plantas (CONSELHO.md, seção 5b), rodada ${n}. Decisão: ${A.pergunta}\nProposta: ${proposta}. Motivo de ir ao júri: ${A.motivo}.\n\n` +
    `Seu ângulo é um só, "${j.angulo}": ${PERGUNTA[j.angulo]}\n\n` +
    `Régua: 3 = ${REGUA['3']}\n6 = ${REGUA['6']}\n9 = ${REGUA['9']}\n${COMO}\n\n` +
    `Antes da nota, aponte pelo menos 2 defeitos, cada um com arquivo e linha que existem; "está ótimo" sem prova não conta. ` +
    `Toda crítica cita arquivo e linha. Não rediscuta o que o dono já decidiu (pedidos/anexos/decisoes-do-dono-2026-11-23.md). ` +
    `Em fatos_afirmados, liste os fatos em que sua nota se apoia, com arquivo e linha: o presidente vai conferir, e fato falso tira a sua nota.`,
    { label: `jurado ${i + 1}: ${j.angulo} (${j.modelo})`, phase: 'Jurados', model: j.modelo, schema: OPINIAO })))
  gasto[`jurados r${n}`] = budget.spent() - antesJ
  phase('Revisão anônima')
  const rotulo = i => String.fromCharCode(65 + i)
  const antesR = budget.spent()
  const revs = await parallel(jurados.map((j, i) => () => agent(
    `Ordene, da mais útil para a menos útil para decidir "${A.pergunta}", estas opiniões anônimas de outros jurados (não são suas). ` +
    `Útil = defeito real, com arquivo e linha que conferem. Devolva os rótulos em ordem e o porquê em 2 frases.\n\n` +
    ops.map((o, k) => k === i || !o ? '' : `### Opinião ${rotulo(k)}\n${JSON.stringify({ defeitos: o.defeitos, criticas: o.criticas, nota: o.nota })}`).join('\n\n'),
    { label: `revisão anônima ${i + 1} (${j.modelo})`, phase: 'Revisão anônima', model: j.modelo, effort: 'low', schema: ORDEM })))
  gasto[`revisao r${n}`] = budget.spent() - antesR
  phase('Presidente')
  const fatos = ops.flatMap((o, i) => ((o && o.fatos_afirmados) || []).map(f => ({ ...f, de: i + 1 })))
  const pres = await medir(`presidente r${n}`, 'A', () => agent(
    `Você preside o júri (CONSELHO.md 5b, regra 3) e não opinou nesta rodada. Decisão: ${A.pergunta}; proposta: ${proposta}.\n` +
    `Confira no repositório pelo menos 5 dos fatos que os jurados afirmaram (abra cada arquivo na linha citada) e diga se se confirmou; ` +
    `"de" é o número do jurado que afirmou. Depois escreva a síntese e o que corrigir já na proposta (cada item com uma lição de uma linha para quem a escreveu). ` +
    `Ordem da revisão anônima (cada jurado ordenou as opiniões dos outros): ${JSON.stringify(revs.map((r, i) => ({ jurado: i + 1, ordem: r && r.ordem, porque: r && r.porque })))}\n` +
    `Fatos afirmados: ${JSON.stringify(fatos).slice(0, 12000)}\nOpiniões: ${JSON.stringify(ops.map(o => o && { defeitos: o.defeitos, nota: o.nota, motivo: o.motivo_da_nota })).slice(0, 12000)}`,
    { label: `presidente (${presidente})`, phase: 'Presidente', model: presidente, schema: PRES }))
  const rodada = {
    rodada: n, motivo: A.motivo, ficha: A.ficha || '-', regua: REGUA,
    jurados: jurados.map((j, i) => ({ ...j, nota: ops[i] ? ops[i].nota : null, defeitos: ops[i] ? ops[i].defeitos : [] })),
    revisao_anonima: revs.map(r => ({ ordem: r ? r.ordem : [] })),
    presidente: { modelo: presidente, fatos: pres ? pres.fatos : [] },
    gasto: { tokens_saida: (gasto[`jurados r${n}`] || 0) + (gasto[`revisao r${n}`] || 0) + (gasto[`presidente r${n}`] || 0) },
  }
  phase('Programa')
  const v = await medir('programa:juri', 'P', () => agent(
    `Rode exatamente este comando na raiz do repositório, sem mudar nada, e devolva o código de saída e, em "saida", SÓ o que o comando imprimiu, sem comentário seu:\n\npython3 ferramentas/fluxo.py juri - <<'FIM'\n${JSON.stringify(rodada)}\nFIM`,
    { label: 'programa:juri', phase: 'Programa', model: 'haiku', effort: 'low', schema: SAIDA }))
  const veredito = lerJson(v && v.saida, { completa: false, erros: ['saída ilegível do programa'], proximo: 'recusada: complete a rodada' })
  conf['programa:juri'].achados_proprios += (veredito.erros || []).length
  return { rodada, ops, pres, veredito }
}

const rodadas = []
let r1 = await umaRodada(1, A.proposta)
rodadas.push(r1)
let final = r1
for (const c of (r1.pres && r1.pres.corrigir_ja) || []) achados.push({ autor: AUTOR, ...c, achado_por: 'presidente' })
conf[`presidente r1`].achados_proprios = ((r1.pres && r1.pres.corrigir_ja) || []).length
if (r1.veredito.proximo === 'reescrever uma vez') {
  phase('Reescrita')
  const v2 = String(A.proposta).replace(/(\.\w+)?$/, '-v2$1')
  await medir('reescrita', 'F', () => agent(
    `Reescreva a proposta ${A.proposta} uma vez, em ${v2} (arquivo novo; não apague o original), aplicando o que o presidente do júri mandou corrigir ` +
    `e respondendo a cada defeito dos jurados. Não mude o que o dono já decidiu. O que depende do dono vira pergunta, não suposição.\n` +
    `Síntese: ${r1.pres ? r1.pres.sintese : ''}\nCorrigir já: ${JSON.stringify(r1.pres ? r1.pres.corrigir_ja : [])}\n` +
    `Defeitos: ${JSON.stringify(r1.ops.map(o => o && o.defeitos))}`.slice(0, 16000),
    { label: 'reescrita', phase: 'Reescrita', model: 'opus' }))
  final = await umaRodada(2, v2)
  rodadas.push(final)
}
let resultado = final.veredito.passa ? 'aprovada pelo júri' : final.veredito.completa ? `vai ao dono com as notas (${rodadas.map(r => r.veredito.media).join(' e ')})` : 'rodada recusada pelo programa: complete e rode de novo'

phase('Colheita')
// fecho por programa: o júri (e a reescrita) não pode ter mexido em ebook/saida/ nem em projetos.py (auditoria, 26/11)
const guarda = await medir('programa:guarda', 'P', () => agent(`Rode exatamente este comando na raiz do repositório, sem mudar nada, e devolva o código de saída e, em "saida", SÓ o que ele imprimiu:\n\ngit status --porcelain -- ebook/saida ebook/plantas/projetos.py; echo FIM_GUARDA`,
  { label: 'programa:guarda', phase: 'Colheita', model: 'haiku', effort: 'low', schema: SAIDA }))
if (!guarda || !/FIM_GUARDA/.test(String(guarda.saida)) || String(guarda.saida).split('FIM_GUARDA')[0].trim() !== '')
  resultado = 'PAROU: ebook/saida/ ou projetos.py mudaram (ou a conferência não respondeu); o Maestro olha antes de tudo'
const registro = {
  id: `${A.ficha || '-'}:${String(A.arquivo || A.fonte || A.rascunho || A.proposta).slice(0, 60)}:${ID_INICIO}`,
  fluxo: 'decisao', peca: A.proposta, ficha: A.ficha || '-', resultado, voltas: rodadas.length,
  gasto: { tokens_saida: Object.values(gasto).reduce((s, x) => s + x, 0), por_conferidor: gasto },
  conferidores: [...Object.values(conf), { nome: 'jurados', tipo: 'A', achados_proprios: rodadas.reduce((s, r) => s + r.ops.filter(Boolean).reduce((t, o) => t + o.defeitos.length, 0), 0) }],
  calibracao: !!A.calibracao,
  // rodada de calibração (erro plantado de propósito): o achado fica no registro, mas não vira lição de ninguém
  achados: (A.calibracao ? [] : achados).map(a => ({ autor: a.autor, chave: a.chave, texto: String(a.texto).slice(0, 300), licao: String(a.licao || '').slice(0, 300), achado_por: a.achado_por })),
  achados_da_calibracao: A.calibracao ? achados.map(a => ({ chave: a.chave, texto: String(a.texto).slice(0, 300) })) : [],
  n_achados: (A.calibracao ? [] : achados).length,
  perguntas_ao_dono: rodadas.flatMap(r => r.ops.filter(Boolean).flatMap(o => o.perguntas_ao_dono || [])),
  juri: rodadas.map(r => ({ rodada: r.rodada.rodada, notas: r.veredito.notas, media: r.veredito.media, perderam_a_nota: r.veredito.perderam_a_nota, erros: r.veredito.erros,
    jurados: r.rodada.jurados.map(j => ({ modelo: j.modelo, angulo: j.angulo, nota: j.nota, defeitos: (j.defeitos || []).map(d => `${d.arquivo}:${d.linha}`) })),
    presidente: r.rodada.presidente.modelo, fatos: (r.rodada.presidente.fatos || []).map(x => ({ de: x.de, onde: `${x.arquivo}:${x.linha}`, confirmado: x.confirmado })) })),
}
const reg = await agent(
  `Rode exatamente este comando na raiz do repositório e devolva, em "saida", SÓ o que o comando imprimiu, sem comentário seu:\n\npython3 ferramentas/fluxo.py registrar - <<'FIM'\n${JSON.stringify(registro)}\nFIM`,
  { label: 'registrar', phase: 'Colheita', model: 'haiku', effort: 'low', schema: SAIDA })
const gravado = lerJson(reg && reg.saida, null)
if (!gravado || !gravado.gravado) log('ATENÇÃO: o registro não gravou; o Maestro grava com o "registro" devolvido')
return { resultado, rodadas: rodadas.map(r => ({ veredito: r.veredito, sintese: r.pres && r.pres.sintese, notas: r.ops.map(o => o && o.nota) })), registro, gravado }

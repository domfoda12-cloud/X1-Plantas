export const meta = {
  name: 'texto-publico',
  description: 'Texto que vai ao público: programa confere, autor confere a própria lista, fatos por quem não escreveu, Vera uma vez, lições sozinhas',
  whenToUse: 'Anúncio, legenda, mensagem de WhatsApp ou texto de página antes de entrar no gerador. args: {arquivo, autor?, pedido, ficha?, fonte_diretor?}',
  phases: [
    { title: 'Programa', detail: 'fluxo.py texto: frases vetadas, promessas, números da casa (zero juízo)' },
    { title: 'Autor', detail: 'o autor conserta o que o programa achou e confere a própria lista' },
    { title: 'Fatos', detail: 'quem não escreveu confere cada afirmação no repositório (Opus)' },
    { title: 'Vera', detail: 'Revisora de risco, uma leitura, peça montada (Fable)' },
    { title: 'Colheita', detail: 'fluxo.py registrar: gasto, achados e lições no arquivo do autor' },
  ],
}

// Regras: pedidos/anexos/plano-fluxos-2026-11-26.md e mapa-conferencias-2026-11-26.md.
// Programa primeiro; agente só onde precisa de juízo; no máximo 2 voltas de conserto, depois vai ao dono.
const A = args || {}
if (!A.arquivo) throw new Error('args.arquivo: o arquivo que tem SÓ o texto que vai ao público')
const AUTOR = A.autor || 'redator'
const PEDIDO = A.pedido || '(sem descrição)'

const LISTA = { type: 'array', items: { type: 'string' } }
const PASSE = {
  type: 'object',
  properties: { feito: LISTA, suposicoes: LISTA, faltando: LISTA, arquivos: LISTA, perguntas_ao_dono: LISTA, fonte_diretor: { type: 'string' } },
  required: ['feito', 'suposicoes', 'faltando', 'arquivos', 'perguntas_ao_dono', 'fonte_diretor'],
}
const SAIDA = { type: 'object', properties: { codigo: { type: 'integer' }, saida: { type: 'string' } }, required: ['codigo', 'saida'] }
const ACHADO = {
  type: 'object',
  properties: {
    chave: { type: 'string', description: 'categoria curta em kebab-case, ex. numero-sem-fonte' },
    texto: { type: 'string', description: 'o problema, com o trecho' },
    arquivo: { type: 'string' }, linha: { type: 'integer' },
    licao: { type: 'string', description: 'uma linha, imperativa, para o autor não repetir' },
  },
  required: ['chave', 'texto', 'licao'],
}
const ACHADOS = { type: 'object', properties: { achados: { type: 'array', items: ACHADO }, nota: { type: 'string' } }, required: ['achados'] }
const CONDICAO = { type: 'object', properties: { ...ACHADO.properties,
  por: { type: 'string', description: 'o texto novo, palavra por palavra, como vai ficar no arquivo' },
  corte: { type: 'string', description: 'o trecho exato que sai (quando a condição é cortar)' } }, required: ACHADO.required }
const VERA = {
  type: 'object',
  properties: { veredito: { type: 'string', enum: ['SIM', 'SIM SE', 'NÃO'] }, condicoes: { type: 'array', items: CONDICAO }, nota: { type: 'string' } },
  required: ['veredito', 'condicoes'],
}

const ID_INICIO = budget.spent()  // identifica a rodada (o registrar recusa gravar duas vezes)
const gasto = {}
const conf = {}
async function medir(nome, tipo, fn) {
  const antes = budget.spent()
  const r = await fn()
  gasto[nome] = (gasto[nome] || 0) + (budget.spent() - antes)
  conf[nome] = conf[nome] || { nome, tipo, achados_proprios: 0 }
  return r
}
const rodar = (nome, cmd) => medir(nome, 'P', () => agent(
  `Rode exatamente este comando na raiz do repositório, sem mudar nada, e devolva o código de saída e, em "saida", SÓ o que o comando imprimiu, sem comentário seu:\n\n${cmd}`,
  { label: nome, phase: 'Programa', model: 'haiku', effort: 'low', schema: SAIDA }))
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

const achados = []
const passes = []

// 1. Programa
phase('Programa')
let prog = await rodar('programa:texto', `python3 ferramentas/fluxo.py texto ${A.arquivo} --json`)
const ILEGIVEL = [{ linha: 0, tipo: 'erro', msg: 'saída do programa ilegível: conferência não feita' }]  // falha fechada (auditoria)
let lista = lerJson(prog && prog.saida, ILEGIVEL)
const errosIniciais = lista.filter(x => x.tipo === 'erro')
conf['programa:texto'].achados_proprios = lista.length
for (const e of errosIniciais) achados.push({ autor: AUTOR, chave: 'programa-' + e.msg.split(':')[0].replace(/[^a-z]+/gi, '-').toLowerCase(), texto: `linha ${e.linha}: ${e.msg}`, licao: `antes de entregar, rode python3 ferramentas/fluxo.py texto no arquivo: ${e.msg}`, achado_por: 'programa:texto' })
log(`programa: ${errosIniciais.length} erro(s), ${lista.length - errosIniciais.length} aviso(s)`)

// 2. Autor: conserta e confere a própria lista ("Antes de mandar ao Revisor", contexto/<autor>.md)
let voltas = -1  // a primeira passada do autor é a conferência dele, não volta de conserto
async function autor(oque) {
  voltas++
  const rotulo = voltas === 0 ? 'conferência própria' : `conserto ${voltas}`
  return medir('autor', 'F', () => agent(
    `Você é o autor deste texto público (${PEDIDO}). Arquivo: ${A.arquivo}. Só pode editar esse arquivo.\n\n` +
    `O que conferir e consertar agora:\n${oque}\n\n` +
    `Depois, confira o texto contra a sua lista "Antes de mandar ao Revisor" em contexto/${AUTOR}.md, item por item, e conserte o que falhar. ` +
    `Nunca diga que a planta dispensa pedreiro, engenheiro ou arquiteto; nunca prometa aprovação, prazo ou custo de obra; número só o que o arquivo traz. ` +
    `A ideia principal de todo conteúdo é do Diretor (MinoAI Frontier): em fonte_diretor, diga de onde veio (ficha, anexo ou a busca na MinoAI Frontier que você fez agora)` +
    (A.fonte_diretor ? `; o Maestro indicou: ${A.fonte_diretor}` : '') + '.\n' +
    `Devolva o passe: feito, suposicoes (o que você supôs sem o dono dizer), faltando, arquivos (caminho relativo), perguntas_ao_dono, fonte_diretor.`,
    { label: `autor:${AUTOR} (${rotulo})`, phase: 'Autor', agentType: AUTOR, schema: PASSE }))
}
let passe = await autor(lista.length ? lista.map(x => `- linha ${x.linha} (${x.tipo}): ${x.msg}`).join('\n') : '- o programa não achou nada; só a sua lista.')
passes.push(passe)

// 2b. Programa de novo: texto e passe (forma fixa, arquivos salvos, Diretor com fonte)
async function conferirDeNovo() {
  const t = await rodar('programa:texto', `python3 ferramentas/fluxo.py texto ${A.arquivo} --json`)
  const p = await rodar('programa:passe', `python3 ferramentas/fluxo.py passe - --publico <<'FIM'\n${JSON.stringify(passe)}\nFIM`)
  return { erros: lerJson(t && t.saida, ILEGIVEL).filter(x => x.tipo === 'erro'), passe: lerJson(p && p.saida, { ok: false, erros: ['saída ilegível'] }) }
}
let depois = await conferirDeNovo()
if ((depois.erros.length || !depois.passe.ok) && voltas < 2) {
  conf['programa:passe'].achados_proprios += (depois.passe.erros || []).length
  passe = await autor([...depois.erros.map(x => `- linha ${x.linha}: ${x.msg}`), ...(depois.passe.erros || []).map(e => `- passe: ${e}`)].join('\n'))
  passes.push(passe)
  depois = await conferirDeNovo()
}

// 3. Fatos: quem não escreveu confere cada afirmação
phase('Fatos')
const fatos = await medir('fatos:opus', 'A', () => agent(
  `Confira os fatos de um texto público que você não escreveu: ${A.arquivo} (${PEDIDO}).\n` +
  `Liste cada afirmação que pode ser conferida (número, medida, o que a peça tem, o que o comprador recebe, regra, lei) e abra o arquivo que a sustenta ` +
  `(ebook/plantas/PLANTAS.md para números da casa; CONTEXTO.md para o que está decidido; pedidos/anexos/decisoes-do-dono-2026-11-23.md para o que o dono disse). ` +
  `Devolva SÓ o que falhou: afirmação sem apoio, maior que a peça, ou contra o arquivo, com arquivo e linha da prova. ` +
  `O programa já pegou isto (não repita): ${JSON.stringify(lista.map(x => x.msg))}. Para cada achado, uma lição de uma linha para o autor.`,
  { label: 'fatos (quem não escreveu)', phase: 'Fatos', model: 'opus', schema: ACHADOS }))
for (const a of (fatos && fatos.achados) || []) achados.push({ autor: AUTOR, ...a, achado_por: 'fatos:opus' })
conf['fatos:opus'].achados_proprios = ((fatos && fatos.achados) || []).length

if (fatos && fatos.achados && fatos.achados.length && voltas < 2) {
  passe = await autor(fatos.achados.map(a => `- ${a.texto}`).join('\n'))
  passes.push(passe)
  depois = await conferirDeNovo()
}

// 4. Vera: uma leitura, com a peça montada (decisão do dono, 26/11)
phase('Vera')
const vera = await medir('vera', 'A', () => agent(
  `Leia uma vez, como vai ao público, o texto em ${A.arquivo} (${PEDIDO}). Dê o veredito (SIM, SIM SE, NÃO). ` +
  `Em SIM SE ou NÃO, cada condição com o trecho, o motivo, a troca pronta ("por": o texto novo palavra por palavra; ou "corte": o trecho que sai) e uma lição de uma linha para o autor. ` +
  `O programa, na última passada: ${depois.erros.length} erro(s) ${JSON.stringify(depois.erros.map(x => x.msg)).slice(0, 1500)}; passe ${depois.passe.ok ? 'certo' : 'com erro: ' + JSON.stringify(depois.passe.erros)}. ` +
  `Programa e fatos não pegam tudo: leia como se ninguém tivesse lido antes. Passe do autor: ${JSON.stringify(passe)}.`,
  { label: 'vera (revisora de risco)', phase: 'Vera', agentType: 'revisor-de-risco', schema: VERA }))
for (const c of (vera && vera.condicoes) || []) achados.push({ autor: AUTOR, ...c, achado_por: 'vera' })
conf['vera'].achados_proprios = ((vera && vera.condicoes) || []).length
const limpo = () => !depois.erros.length && depois.passe.ok  // aprovado só com prova positiva do programa
let resultado = !vera ? 'vai ao dono (Vera não respondeu)' : vera.veredito === 'SIM' ? (limpo() ? 'aprovado' : 'vai ao dono (Vera disse SIM, mas o programa tem erro em aberto)') : vera.veredito === 'NÃO' ? 'vetado: vai ao dono' : 'SIM SE'
if (vera && vera.veredito === 'SIM SE') {
  if (voltas < 2) {
    passe = await autor('Aplique as condições da Vera, uma por uma, sem mudar mais nada:\n' + vera.condicoes.map(c => `- ${c.texto}`).join('\n'))
    passes.push(passe)
    depois = await conferirDeNovo()
    const tc = lerJson((await rodar('programa:trocas', `python3 ferramentas/fluxo.py trocas ${A.arquivo} - <<'FIM'\n${JSON.stringify(vera.condicoes.map(c => ({ por: c.por, corte: c.corte })))}\nFIM`)).saida, { ok: false, falta: ['saída ilegível'] })
    if (!tc.ok) depois.erros.push(...(tc.falta || []).map(m => ({ linha: 0, tipo: 'erro', msg: 'troca da Vera: ' + m })))
    resultado = !limpo() ? 'vai ao dono (conserto não passou no programa)' : 'aprovado com as condições da Vera aplicadas'
  } else {
    resultado = 'vai ao dono (2 voltas gastas; condições da Vera em aberto)'
  }
}

// 5. Colheita: registro, gasto e lições, sozinhos
phase('Colheita')

// fecho por programa: o fluxo não pode ter mexido em ebook/saida/ nem em projetos.py (auditoria, 26/11)
const guarda = await rodar('programa:guarda', 'git status --porcelain -- ebook/saida ebook/plantas/projetos.py; echo FIM_GUARDA')
const mexeu = !guarda || !/FIM_GUARDA/.test(String(guarda.saida)) || String(guarda.saida).split('FIM_GUARDA')[0].trim() !== ''
if (mexeu) resultado = 'PAROU: ebook/saida/ ou projetos.py mudaram (ou a conferência não respondeu); o Maestro olha antes de tudo'
const registro = {
  id: `${A.ficha || '-'}:${String(A.arquivo || A.fonte || A.rascunho || A.proposta).slice(0, 60)}:${ID_INICIO}`,
  fluxo: 'texto-publico', peca: A.arquivo, ficha: A.ficha || '-', resultado, voltas,
  gasto: { tokens_saida: Object.values(gasto).reduce((s, x) => s + x, 0), por_conferidor: gasto },
  conferidores: Object.values(conf),
  achados: achados.map(a => ({ autor: a.autor, chave: a.chave, texto: String(a.texto).slice(0, 300), licao: String(a.licao || '').slice(0, 300), achado_por: a.achado_por })),
  n_achados: achados.length,
  perguntas_ao_dono: passe ? passe.perguntas_ao_dono : [],
}
const reg = await agent(
  `Rode exatamente este comando na raiz do repositório e devolva, em "saida", SÓ o que o comando imprimiu, sem comentário seu:\n\npython3 ferramentas/fluxo.py registrar - <<'FIM'\n${JSON.stringify(registro)}\nFIM`,
  { label: 'registrar', phase: 'Colheita', model: 'haiku', effort: 'low', schema: SAIDA })
const gravado = lerJson(reg && reg.saida, null)
if (!gravado || !gravado.gravado) log('ATENÇÃO: o registro não gravou; o Maestro grava com o "registro" devolvido abaixo')
return { resultado, voltas, passe, vera, programa_final: depois, registro, gravado }

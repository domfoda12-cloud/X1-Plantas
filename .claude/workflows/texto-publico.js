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
const VERA = {
  type: 'object',
  properties: { veredito: { type: 'string', enum: ['SIM', 'SIM SE', 'NÃO'] }, condicoes: { type: 'array', items: ACHADO }, nota: { type: 'string' } },
  required: ['veredito', 'condicoes'],
}

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
  `Rode exatamente este comando na raiz do repositório, sem mudar nada, e devolva o código de saída e a saída inteira:\n\n${cmd}`,
  { label: nome, phase: 'Programa', model: 'haiku', effort: 'low', schema: SAIDA }))
const lerJson = (s, padrao) => { try { return JSON.parse(s) } catch (e) { return padrao } }

const achados = []
const passes = []

// 1. Programa
phase('Programa')
let prog = await rodar('programa:texto', `python3 ferramentas/fluxo.py texto ${A.arquivo} --json`)
let lista = lerJson(prog && prog.saida, [])
const errosIniciais = lista.filter(x => x.tipo === 'erro')
conf['programa:texto'].achados_proprios = lista.length
for (const e of errosIniciais) achados.push({ autor: AUTOR, chave: 'programa-' + e.msg.split(':')[0].replace(/[^a-z]+/gi, '-').toLowerCase(), texto: `linha ${e.linha}: ${e.msg}`, licao: `antes de entregar, rode python3 ferramentas/fluxo.py texto no arquivo: ${e.msg}`, achado_por: 'programa:texto' })
log(`programa: ${errosIniciais.length} erro(s), ${lista.length - errosIniciais.length} aviso(s)`)

// 2. Autor: conserta e confere a própria lista ("Antes de mandar ao Revisor", contexto/<autor>.md)
let voltas = 0
async function autor(oque) {
  voltas++
  return medir('autor', 'A', () => agent(
    `Você é o autor deste texto público (${PEDIDO}). Arquivo: ${A.arquivo}. Só pode editar esse arquivo.\n\n` +
    `O que conferir e consertar agora:\n${oque}\n\n` +
    `Depois, confira o texto contra a sua lista "Antes de mandar ao Revisor" em contexto/${AUTOR}.md, item por item, e conserte o que falhar. ` +
    `Nunca diga que a planta dispensa pedreiro, engenheiro ou arquiteto; nunca prometa aprovação, prazo ou custo de obra; número só o que o arquivo traz. ` +
    `A ideia principal de todo conteúdo é do Diretor (MinoAI Frontier): em fonte_diretor, diga de onde veio (ficha, anexo ou a busca na MinoAI Frontier que você fez agora)` +
    (A.fonte_diretor ? `; o Maestro indicou: ${A.fonte_diretor}` : '') + '.\n' +
    `Devolva o passe: feito, suposicoes (o que você supôs sem o dono dizer), faltando, arquivos (caminho relativo), perguntas_ao_dono, fonte_diretor.`,
    { label: `autor:${AUTOR} (volta ${voltas})`, phase: 'Autor', agentType: AUTOR, schema: PASSE }))
}
let passe = await autor(lista.length ? lista.map(x => `- linha ${x.linha} (${x.tipo}): ${x.msg}`).join('\n') : '- o programa não achou nada; só a sua lista.')
passes.push(passe)

// 2b. Programa de novo: texto e passe (forma fixa, arquivos salvos, Diretor com fonte)
async function conferirDeNovo() {
  const t = await rodar('programa:texto', `python3 ferramentas/fluxo.py texto ${A.arquivo} --json`)
  const p = await rodar('programa:passe', `python3 ferramentas/fluxo.py passe - --publico <<'FIM'\n${JSON.stringify(passe)}\nFIM`)
  return { erros: lerJson(t && t.saida, []).filter(x => x.tipo === 'erro'), passe: lerJson(p && p.saida, { ok: false, erros: ['saída ilegível'] }) }
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
  `Em SIM SE ou NÃO, cada condição com o trecho, o motivo e uma lição de uma linha para o autor. ` +
  `Já passou pelo programa de frases vetadas e pela conferência de fatos; o passe do autor: ${JSON.stringify(passe)}.`,
  { label: 'vera (revisora de risco)', phase: 'Vera', agentType: 'revisor-de-risco', schema: VERA }))
for (const c of (vera && vera.condicoes) || []) achados.push({ autor: AUTOR, ...c, achado_por: 'vera' })
conf['vera'].achados_proprios = ((vera && vera.condicoes) || []).length
let resultado = !vera ? 'vai ao dono (Vera não respondeu)' : vera.veredito === 'SIM' ? 'aprovado' : vera.veredito === 'NÃO' ? 'vetado: vai ao dono' : 'SIM SE'
if (vera && vera.veredito === 'SIM SE') {
  if (voltas < 2) {
    passe = await autor('Aplique as condições da Vera, uma por uma, sem mudar mais nada:\n' + vera.condicoes.map(c => `- ${c.texto}`).join('\n'))
    passes.push(passe)
    depois = await conferirDeNovo()
    resultado = depois.erros.length || !depois.passe.ok ? 'vai ao dono (conserto não passou no programa)' : 'aprovado com as condições da Vera aplicadas'
  } else {
    resultado = 'vai ao dono (2 voltas gastas; condições da Vera em aberto)'
  }
}

// 5. Colheita: registro, gasto e lições, sozinhos
phase('Colheita')
const registro = {
  fluxo: 'texto-publico', peca: A.arquivo, ficha: A.ficha || '-', resultado, voltas,
  gasto: { tokens_saida: Object.values(gasto).reduce((s, x) => s + x, 0), por_conferidor: gasto },
  conferidores: Object.values(conf),
  achados: achados.map(a => ({ autor: a.autor, chave: a.chave, texto: String(a.texto).slice(0, 300), licao: String(a.licao || '').slice(0, 300), achado_por: a.achado_por })),
  perguntas_ao_dono: passe ? passe.perguntas_ao_dono : [],
}
const reg = await agent(
  `Rode exatamente este comando na raiz do repositório e devolva a saída inteira:\n\npython3 ferramentas/fluxo.py registrar - <<'FIM'\n${JSON.stringify(registro)}\nFIM`,
  { label: 'registrar', phase: 'Colheita', model: 'haiku', effort: 'low', schema: SAIDA })
const gravado = lerJson(reg && reg.saida, null)
if (!gravado || !gravado.gravado) log('ATENÇÃO: o registro não gravou; o Maestro grava com o "registro" devolvido abaixo')
return { resultado, voltas, passe, vera, programa_final: depois, registro, gravado }

export const meta = {
  name: 'planta',
  description: 'Rascunho de planta: Nilo desenha, programa roda todas as conferências da oficial, segundo olhar de obra, lições sozinhas',
  whenToUse: 'Antes de dizer que um rascunho de planta está "pronto para aplicar". Não toca em ebook/plantas/projetos.py. args: {rascunho, casa, objetivo, variante?, ficha?}',
  phases: [
    { title: 'Autor', detail: 'Nilo (arquiteto) escreve ou conserta o rascunho' },
    { title: 'Programa', detail: 'conferir-rascunho.py: validador e 3D, rascunho e oficial lado a lado' },
    { title: 'Obra', detail: 'segundo olhar, de quem não desenhou: dá para construir e morar? (Opus)' },
    { title: 'Colheita', detail: 'fluxo.py registrar: gasto, achados e lições no arquivo do Nilo' },
  ],
}

const A = args || {}
if (!A.rascunho || !A.casa || !A.objetivo) throw new Error('args: {rascunho: caminho do .py, casa: C01, objetivo: o que muda}')
const AUTOR = 'arquiteto'
const VAR = A.variante ? ` ${A.variante}` : ''

const LISTA = { type: 'array', items: { type: 'string' } }
const PASSE = {
  type: 'object',
  properties: { feito: LISTA, suposicoes: LISTA, faltando: LISTA, arquivos: LISTA, perguntas_ao_dono: LISTA },
  required: ['feito', 'suposicoes', 'faltando', 'arquivos', 'perguntas_ao_dono'],
}
const SAIDA = { type: 'object', properties: { codigo: { type: 'integer' }, saida: { type: 'string' } }, required: ['codigo', 'saida'] }
const ACHADO = {
  type: 'object',
  properties: { chave: { type: 'string' }, texto: { type: 'string' }, arquivo: { type: 'string' }, linha: { type: 'integer' }, licao: { type: 'string' } },
  required: ['chave', 'texto', 'licao'],
}
const ACHADOS = { type: 'object', properties: { achados: { type: 'array', items: ACHADO }, nota: { type: 'string' } }, required: ['achados'] }

const gasto = {}, conf = {}, achados = []
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

let voltas = -1  // a primeira passada do autor é a conferência dele, não volta de conserto, passe = null
async function autor(oque) {
  voltas++
  const rotulo = voltas === 0 ? 'conferência própria' : `conserto ${voltas}`
  return medir('autor', 'A', () => agent(
    `Rascunho de planta da ${A.casa}: ${A.rascunho}${VAR}. Objetivo: ${A.objetivo}.\n` +
    `Escreva ou conserte SÓ o rascunho (um .py que monta a planta num dicionário com "comodos" e "portas", como pede ferramentas/conferir-rascunho.py; ` +
    `parta da oficial em ebook/plantas/projetos.py). Nunca edite projetos.py, ebook/saida/ nem as prévias. ` +
    `Antes de devolver, rode python3 ferramentas/conferir-rascunho.py ${A.rascunho}${VAR} até sair limpo, e confira contra a sua lista em contexto/arquiteto.md.\n\n` +
    `O que fazer agora:\n${oque}\n\nDevolva o passe (em suposicoes, o que você decidiu sem o dono dizer).`,
    { label: `nilo (${rotulo})`, phase: 'Autor', agentType: AUTOR, schema: PASSE }))
}
phase('Autor')
passe = await autor('- desenhe o rascunho para o objetivo acima.')

phase('Programa')
async function programa() {
  const r = await rodar('programa:rascunho', `python3 ferramentas/conferir-rascunho.py ${A.rascunho}${VAR}; echo "=== oficial"; python3 ferramentas/conferir-rascunho.py ${A.casa}`)
  return r || { codigo: 1, saida: 'programa não respondeu' }
}
let prog = await programa()
const falhou = p => /\[ERRO|Traceback|: [1-9]\d* de \d+ com erro|^\s*ERRO/m.test(String(p.saida).split('=== oficial')[0])
if (falhou(prog)) {
  conf['programa:rascunho'].achados_proprios += 1
  achados.push({ autor: AUTOR, chave: 'rascunho-nao-passou', texto: String(prog.saida).slice(0, 300), licao: 'rode conferir-rascunho.py até sair limpo antes de entregar o rascunho', achado_por: 'programa:rascunho' })
  if (voltas < 2) { passe = await autor('O programa falhou; conserte:\n' + String(prog.saida).slice(0, 3000)); prog = await programa() }
}

phase('Obra')
const obra = await medir('obra:opus', 'A', () => agent(
  `Você não desenhou este rascunho. Leia ${A.rascunho}${VAR} (${A.casa}; objetivo: ${A.objetivo}) e compare com a oficial em ebook/plantas/projetos.py. ` +
  `Olhe como pedreiro e como morador: dá para construir sem gambiarra? a porta, o móvel e a passagem funcionam? o aviso que vai ao comprador é verdade? ` +
  `O programa já passou nisto: ${String(prog.saida).slice(0, 1500)}. Devolva só o que falhou, com arquivo e linha e uma lição de uma linha para o arquiteto.`,
  { label: 'obra (quem não desenhou)', phase: 'Obra', model: 'opus', schema: ACHADOS }))
for (const a of (obra && obra.achados) || []) achados.push({ autor: AUTOR, ...a, achado_por: 'obra:opus' })
conf['obra:opus'].achados_proprios = ((obra && obra.achados) || []).length
if (obra && obra.achados.length && voltas < 2) {
  passe = await autor(obra.achados.map(a => `- ${a.texto}`).join('\n'))
  prog = await programa()
}
const resultado = falhou(prog) ? 'vai ao dono (o programa ainda falha)' :
  (obra && obra.achados.length && voltas >= 2) ? 'pronto para aplicar, com achados de obra em aberto' : 'pronto para aplicar (aplicar é outro passo: plantas.py validar e checar.py)'

phase('Colheita')
const registro = {
  fluxo: 'planta', peca: `${A.rascunho}${VAR}`, ficha: A.ficha || '-', resultado, voltas,
  gasto: { tokens_saida: Object.values(gasto).reduce((s, x) => s + x, 0), por_conferidor: gasto },
  conferidores: Object.values(conf),
  achados: achados.map(a => ({ autor: a.autor, chave: a.chave, texto: String(a.texto).slice(0, 300), licao: String(a.licao || '').slice(0, 300), achado_por: a.achado_por })),
  perguntas_ao_dono: passe ? passe.perguntas_ao_dono : [],
}
const reg = await agent(
  `Rode exatamente este comando na raiz do repositório e devolva, em "saida", SÓ o que o comando imprimiu, sem comentário seu:\n\npython3 ferramentas/fluxo.py registrar - <<'FIM'\n${JSON.stringify(registro)}\nFIM`,
  { label: 'registrar', phase: 'Colheita', model: 'haiku', effort: 'low', schema: SAIDA })
const gravado = lerJson(reg && reg.saida, null)
if (!gravado || !gravado.gravado) log('ATENÇÃO: o registro não gravou; o Maestro grava com o "registro" devolvido')
return { resultado, voltas, passe, programa_final: prog, registro, gravado }

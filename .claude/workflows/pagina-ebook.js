export const meta = {
  name: 'pagina-ebook',
  description: 'Página do e-book na prévia: programa gera e confere, autor conserta, Nilo confere a técnica, Bia o visual, Vera uma vez, lições sozinhas',
  whenToUse: 'Antes de dizer que uma página do e-book está pronta. Nunca grava ebook/saida/. args: {pagina, previa (pasta fora do repositório), fonte (arquivos do texto), autor?, opcoes?, pedido, ficha?}',
  phases: [
    { title: 'Programa', detail: 'livro.py --previa e fluxo.py pagina (texto da página contra as regras e o PLANTAS.md)' },
    { title: 'Autor', detail: 'quem fez a página confere a própria lista e conserta' },
    { title: 'Técnica e visual', detail: 'Nilo (números e afirmações técnicas) e Bia (visual), cada um uma leitura' },
    { title: 'Vera', detail: 'Revisora de risco, uma leitura, página montada' },
    { title: 'Colheita', detail: 'fluxo.py registrar: gasto, achados e lições no arquivo do autor' },
  ],
}

const A = args || {}
if (!A.pagina || !A.previa || !A.fonte) throw new Error('args: {pagina: número, previa: pasta fora do repositório, fonte: arquivo(s) de onde sai o texto}')
if (String(A.previa).includes('ebook/saida')) throw new Error('a prévia nunca vai a ebook/saida/ (só o dono manda gerar o oficial)')
const AUTOR = A.autor || 'designer'
const PEDIDO = A.pedido || `página ${A.pagina}`
const NN = String(A.pagina).padStart(2, '0')
const PNG = `${A.previa}/pagina-${NN}.png`
const GERAR = `python3 ebook/gerador/livro.py --previa ${A.previa} ${A.opcoes || ''}`.trim()

const LISTA = { type: 'array', items: { type: 'string' } }
const PASSE = {
  type: 'object',
  properties: { feito: LISTA, suposicoes: LISTA, faltando: LISTA, arquivos: LISTA, perguntas_ao_dono: LISTA, fonte_diretor: { type: 'string' } },
  required: ['feito', 'suposicoes', 'faltando', 'arquivos', 'perguntas_ao_dono', 'fonte_diretor'],
}
const SAIDA = { type: 'object', properties: { codigo: { type: 'integer' }, saida: { type: 'string' } }, required: ['codigo', 'saida'] }
const ACHADO = {
  type: 'object',
  properties: { chave: { type: 'string' }, texto: { type: 'string' }, arquivo: { type: 'string' }, linha: { type: 'integer' }, licao: { type: 'string' } },
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
const gasto = {}, conf = {}, achados = []
async function medir(nome, tipo, fn) {
  const antes = budget.spent()
  const r = await fn()
  gasto[nome] = (gasto[nome] || 0) + (budget.spent() - antes)
  conf[nome] = conf[nome] || { nome, tipo, achados_proprios: 0 }
  return r
}
const rodar = (nome, cmd) => medir(nome, 'P', () => agent(
  `Rode exatamente estes comandos na raiz do repositório, nesta ordem, sem mudar nada, e devolva o código de saída do último e, em "saida", SÓ o que o último imprimiu, sem comentário seu:\n\n${cmd}`,
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

async function programa() {
  const r = await rodar('programa:pagina', `${GERAR} > /dev/null && python3 ferramentas/fluxo.py pagina ${A.previa}/ebook.pdf ${A.pagina} --json`)
  return lerJson(r && r.saida, { texto: '', achados: [{ linha: 0, tipo: 'erro', msg: 'prévia não gerou ou saída ilegível: ' + String(r && r.saida).slice(0, 300) }] })
}

phase('Programa')
let prog = await programa()
conf['programa:pagina'].achados_proprios = prog.achados.length
for (const e of prog.achados.filter(x => x.tipo === 'erro'))
  achados.push({ autor: AUTOR, chave: 'programa-pagina', texto: `pág. ${A.pagina}: ${e.msg}`, licao: `antes de dizer pronta, gere a prévia e rode fluxo.py pagina: ${e.msg}`, achado_por: 'programa:pagina' })

let voltas = -1, passe = null  // a primeira passada do autor é a conferência dele, não volta de conserto
async function autor(oque) {
  voltas++
  const rotulo = voltas === 0 ? 'conferência própria' : `conserto ${voltas}`
  return medir('autor', 'F', () => agent(
    `Você fez a página ${A.pagina} do e-book (${PEDIDO}). O texto sai de: ${A.fonte}. Só edite esses arquivos; nunca grave ebook/saida/. ` +
    `Para ver a página: ${GERAR} e abra ${PNG}.\n\nO que conferir e consertar agora:\n${oque}\n\n` +
    `Depois, confira a página contra a sua lista em contexto/${AUTOR}.md e conserte o que falhar. Número só o que o PLANTAS.md traz. ` +
    `Devolva o passe (fonte_diretor: de onde veio a ideia principal desta página).`,
    { label: `autor:${AUTOR} (${rotulo})`, phase: 'Autor', agentType: AUTOR, schema: PASSE }))
}
phase('Autor')
passe = await autor(prog.achados.length ? prog.achados.map(x => `- (${x.tipo}) ${x.msg}`).join('\n') : '- o programa não achou nada; só a sua lista.')
prog = await programa()

// Técnica e visual: uma leitura de cada, em paralelo (ângulos diferentes; cada um sabe o que o programa já pegou)
phase('Técnica e visual')
const jaPego = JSON.stringify(prog.achados.map(x => x.msg))
// o paralelo é medido por fora (medir dentro do parallel contava em dobro; auditoria)
const antesTV = budget.spent()
conf.nilo = { nome: 'nilo', tipo: 'A', achados_proprios: 0 }; conf.bia = { nome: 'bia', tipo: 'A', achados_proprios: 0 }
const [nilo, bia] = await parallel([
  () => (agent(
    `Confira a parte técnica da página ${A.pagina} (imagem ${PNG}; texto extraído: ${JSON.stringify(prog.texto).slice(0, 4000)}). ` +
    `Cada número, medida, lado do sol, ventilação, divisa, lei: contra ebook/plantas/PLANTAS.md e ebook/referencias/ARQUITETO.md. ` +
    `Devolva só o que falhou, com arquivo e linha da prova e uma lição de uma linha para quem fez a página. O programa já pegou: ${jaPego}.`,
    { label: 'nilo (técnica)', phase: 'Técnica e visual', agentType: 'arquiteto', schema: ACHADOS })),
  () => (agent(
    `Olhe a página ${A.pagina} (${PNG}) com o método da skill design-editorial: a Placa no lugar certo (a voz do Lote Carente só nas placas), ` +
    `hierarquia, leitura no celular, nada cortado, nada genérico. Devolva só o que falhou, com o trecho e uma lição de uma linha para quem fez a página.`,
    { label: 'bia (visual)', phase: 'Técnica e visual', agentType: 'designer', schema: ACHADOS })),
])
gasto['nilo e bia'] = budget.spent() - antesTV
for (const [nome, r] of [['nilo', nilo], ['bia', bia]]) {
  const xs = (r && r.achados) || []
  conf[nome].achados_proprios = xs.length
  for (const a of xs) achados.push({ autor: AUTOR, ...a, achado_por: nome })
}
const tecvis = [...((nilo && nilo.achados) || []), ...((bia && bia.achados) || [])]
if (tecvis.length && voltas < 2) {
  passe = await autor(tecvis.map(a => `- ${a.texto}`).join('\n'))
  prog = await programa()
}

phase('Vera')
const vera = await medir('vera', 'A', () => agent(
  `Leia uma vez, como vai ao comprador, a página ${A.pagina} do e-book (${PNG}; texto: ${JSON.stringify(prog.texto).slice(0, 4000)}). ` +
  `Veredito SIM, SIM SE ou NÃO; cada condição com o trecho, o motivo, a troca pronta ("por": o texto novo palavra por palavra; ou "corte": o trecho que sai) e uma lição de uma linha para quem fez a página. Passe do autor: ${JSON.stringify(passe)}.`,
  { label: 'vera (revisora de risco)', phase: 'Vera', agentType: 'revisor-de-risco', schema: VERA }))
for (const c of (vera && vera.condicoes) || []) achados.push({ autor: AUTOR, ...c, achado_por: 'vera' })
conf['vera'].achados_proprios = ((vera && vera.condicoes) || []).length
const limpa = () => !prog.achados.some(x => x.tipo === 'erro')  // aprovada só com prova positiva do programa
let resultado = !vera ? 'vai ao dono (Vera não respondeu)' : vera.veredito === 'SIM' ? (limpa() ? 'aprovada na prévia' : 'vai ao dono (Vera disse SIM, mas o programa tem erro em aberto)') : vera.veredito === 'NÃO' ? 'vetada: vai ao dono' : 'SIM SE'
if (vera && vera.veredito === 'SIM SE') {
  if (voltas < 2) {
    passe = await autor('Aplique as condições da Vera, uma por uma, sem mudar mais nada:\n' + vera.condicoes.map(c => `- ${c.texto}`).join('\n'))
    prog = await programa()
    // a página sai do gerador: a troca da Vera é conferida no texto extraído da página montada
    const tc = lerJson((await rodar('programa:trocas', `python3 - <<'FIM'\nimport json,sys\nsys.path.insert(0,'ferramentas')\nimport fluxo\nprint(json.dumps({'falta': fluxo.conferir_trocas(${JSON.stringify(JSON.stringify(prog.texto))}, json.loads(${JSON.stringify(JSON.stringify(vera.condicoes.map(c => ({ por: c.por, corte: c.corte }))))}))}))\nFIM`)).saida, { falta: ['saída ilegível'] })
    if ((tc.falta || []).length) prog.achados.push(...tc.falta.map(m => ({ linha: 0, tipo: 'erro', msg: 'troca da Vera: ' + m })))
    resultado = !limpa() ? 'vai ao dono (conserto não passou no programa)' : 'aprovada na prévia, com as condições da Vera'
  } else resultado = 'vai ao dono (2 voltas gastas; condições da Vera em aberto)'
}

phase('Colheita')
// o passe também passa pelo programa: forma fixa, arquivos que o git guarda, ideia do Diretor com a fonte
const pp = lerJson((await rodar('programa:passe', `python3 ferramentas/fluxo.py passe - --publico <<'FIM'\n${JSON.stringify(passe)}\nFIM`)).saida, { ok: false, erros: ['saída ilegível'] })
if (!pp.ok && resultado.startsWith('aprovada')) resultado = 'vai ao dono (passe fora da forma: ' + (pp.erros || []).join('; ').slice(0, 200) + ')'

// fecho por programa: o fluxo não pode ter mexido em ebook/saida/ nem em projetos.py (auditoria, 26/11)
const guarda = await rodar('programa:guarda', 'git status --porcelain -- ebook/saida ebook/plantas/projetos.py; echo FIM_GUARDA')
const mexeu = !guarda || !/FIM_GUARDA/.test(String(guarda.saida)) || String(guarda.saida).split('FIM_GUARDA')[0].trim() !== ''
if (mexeu) resultado = 'PAROU: ebook/saida/ ou projetos.py mudaram (ou a conferência não respondeu); o Maestro olha antes de tudo'
const registro = {
  id: `${A.ficha || '-'}:${String(A.arquivo || A.fonte || A.rascunho || A.proposta).slice(0, 60)}:${ID_INICIO}`,
  fluxo: 'pagina-ebook', peca: `${A.fonte} (página ${A.pagina})`, ficha: A.ficha || '-', resultado, voltas,
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
if (!gravado || !gravado.gravado) log('ATENÇÃO: o registro não gravou; o Maestro grava com o "registro" devolvido')
return { resultado, voltas, passe, vera, programa_final: prog.achados, registro, gravado }

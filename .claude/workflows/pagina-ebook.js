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
const VERA = {
  type: 'object',
  properties: { veredito: { type: 'string', enum: ['SIM', 'SIM SE', 'NÃO'] }, condicoes: { type: 'array', items: ACHADO }, nota: { type: 'string' } },
  required: ['veredito', 'condicoes'],
}

const gasto = {}, conf = {}, achados = []
async function medir(nome, tipo, fn) {
  const antes = budget.spent()
  const r = await fn()
  gasto[nome] = (gasto[nome] || 0) + (budget.spent() - antes)
  conf[nome] = conf[nome] || { nome, tipo, achados_proprios: 0 }
  return r
}
const rodar = (nome, cmd) => medir(nome, 'P', () => agent(
  `Rode exatamente estes comandos na raiz do repositório, nesta ordem, sem mudar nada, e devolva o código de saída do último e a saída inteira do último:\n\n${cmd}`,
  { label: nome, phase: 'Programa', model: 'haiku', effort: 'low', schema: SAIDA }))
const lerJson = (s, padrao) => { try { return JSON.parse(s) } catch (e) { return padrao } }

async function programa() {
  const r = await rodar('programa:pagina', `${GERAR} > /dev/null && python3 ferramentas/fluxo.py pagina ${A.previa}/ebook.pdf ${A.pagina} --json`)
  return lerJson(r && r.saida, { texto: '', achados: [{ linha: 0, tipo: 'erro', msg: 'prévia não gerou ou saída ilegível: ' + String(r && r.saida).slice(0, 300) }] })
}

phase('Programa')
let prog = await programa()
conf['programa:pagina'].achados_proprios = prog.achados.length
for (const e of prog.achados.filter(x => x.tipo === 'erro'))
  achados.push({ autor: AUTOR, chave: 'programa-pagina', texto: `pág. ${A.pagina}: ${e.msg}`, licao: `antes de dizer pronta, gere a prévia e rode fluxo.py pagina: ${e.msg}`, achado_por: 'programa:pagina' })

let voltas = 0, passe = null
async function autor(oque) {
  voltas++
  return medir('autor', 'A', () => agent(
    `Você fez a página ${A.pagina} do e-book (${PEDIDO}). O texto sai de: ${A.fonte}. Só edite esses arquivos; nunca grave ebook/saida/. ` +
    `Para ver a página: ${GERAR} e abra ${PNG}.\n\nO que conferir e consertar agora:\n${oque}\n\n` +
    `Depois, confira a página contra a sua lista em contexto/${AUTOR}.md e conserte o que falhar. Número só o que o PLANTAS.md traz. ` +
    `Devolva o passe (fonte_diretor: de onde veio a ideia principal desta página).`,
    { label: `autor:${AUTOR} (volta ${voltas})`, phase: 'Autor', agentType: AUTOR, schema: PASSE }))
}
phase('Autor')
passe = await autor(prog.achados.length ? prog.achados.map(x => `- (${x.tipo}) ${x.msg}`).join('\n') : '- o programa não achou nada; só a sua lista.')
prog = await programa()

// Técnica e visual: uma leitura de cada, em paralelo (ângulos diferentes; cada um sabe o que o programa já pegou)
phase('Técnica e visual')
const jaPego = JSON.stringify(prog.achados.map(x => x.msg))
const [nilo, bia] = await parallel([
  () => medir('nilo', 'A', () => agent(
    `Confira a parte técnica da página ${A.pagina} (imagem ${PNG}; texto extraído: ${JSON.stringify(prog.texto).slice(0, 4000)}). ` +
    `Cada número, medida, lado do sol, ventilação, divisa, lei: contra ebook/plantas/PLANTAS.md e ebook/referencias/ARQUITETO.md. ` +
    `Devolva só o que falhou, com arquivo e linha da prova e uma lição de uma linha para quem fez a página. O programa já pegou: ${jaPego}.`,
    { label: 'nilo (técnica)', phase: 'Técnica e visual', agentType: 'arquiteto', schema: ACHADOS })),
  () => medir('bia', 'A', () => agent(
    `Olhe a página ${A.pagina} (${PNG}) com o método da skill design-editorial: a Placa no lugar certo (a voz do Lote Carente só nas placas), ` +
    `hierarquia, leitura no celular, nada cortado, nada genérico. Devolva só o que falhou, com o trecho e uma lição de uma linha para quem fez a página.`,
    { label: 'bia (visual)', phase: 'Técnica e visual', agentType: 'designer', schema: ACHADOS })),
])
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
  `Veredito SIM, SIM SE ou NÃO; cada condição com o trecho, o motivo e uma lição de uma linha para quem fez a página. Passe do autor: ${JSON.stringify(passe)}.`,
  { label: 'vera (revisora de risco)', phase: 'Vera', agentType: 'revisor-de-risco', schema: VERA }))
for (const c of (vera && vera.condicoes) || []) achados.push({ autor: AUTOR, ...c, achado_por: 'vera' })
conf['vera'].achados_proprios = ((vera && vera.condicoes) || []).length
let resultado = !vera ? 'vai ao dono (Vera não respondeu)' : vera.veredito === 'SIM' ? 'aprovada na prévia' : vera.veredito === 'NÃO' ? 'vetada: vai ao dono' : 'SIM SE'
if (vera && vera.veredito === 'SIM SE') {
  if (voltas < 2) {
    passe = await autor('Aplique as condições da Vera, uma por uma, sem mudar mais nada:\n' + vera.condicoes.map(c => `- ${c.texto}`).join('\n'))
    prog = await programa()
    resultado = prog.achados.some(x => x.tipo === 'erro') ? 'vai ao dono (conserto não passou no programa)' : 'aprovada na prévia, com as condições da Vera'
  } else resultado = 'vai ao dono (2 voltas gastas; condições da Vera em aberto)'
}

phase('Colheita')
const registro = {
  fluxo: 'pagina-ebook', peca: `${A.fonte} (página ${A.pagina})`, ficha: A.ficha || '-', resultado, voltas,
  gasto: { tokens_saida: Object.values(gasto).reduce((s, x) => s + x, 0), por_conferidor: gasto },
  conferidores: Object.values(conf),
  achados: achados.map(a => ({ autor: a.autor, chave: a.chave, texto: String(a.texto).slice(0, 300), licao: String(a.licao || '').slice(0, 300), achado_por: a.achado_por })),
  perguntas_ao_dono: passe ? passe.perguntas_ao_dono : [],
}
const reg = await agent(
  `Rode exatamente este comando na raiz do repositório e devolva a saída inteira:\n\npython3 ferramentas/fluxo.py registrar - <<'FIM'\n${JSON.stringify(registro)}\nFIM`,
  { label: 'registrar', phase: 'Colheita', model: 'haiku', effort: 'low', schema: SAIDA })
const gravado = lerJson(reg && reg.saida, null)
if (!gravado || !gravado.gravado) log('ATENÇÃO: o registro não gravou; o Maestro grava com o "registro" devolvido')
return { resultado, voltas, passe, vera, programa_final: prog.achados, registro, gravado }

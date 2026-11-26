export const meta = {
  name: 'prova-de-entrada',
  description: 'Prova de entrada que endurece: casos com problema plantado tirados dos erros reais, gabarito fora do repositório, nota por programa, nível sobe para quem passa',
  whenToUse: 'A cada 3 rodadas de júri (CONSELHO.md 5b, regra 5) ou quando o Maestro quiser medir um papel. args: {papeis: [...], tag: "AAAAMMDD-HHMM", n_casos?: 10, n_problemas?: 5}',
  phases: [
    { title: 'Estado', detail: 'fluxo.py prova-estado: nível de cada papel e os erros que voltaram' },
    { title: 'Montar', detail: 'Opus monta os casos do nível, dos erros reais (pedidos/LICOES.md)' },
    { title: 'Conferir gabarito', detail: 'outro Opus confere cada problema plantado e cada caso limpo; o gabarito vai para fora do repositório' },
    { title: 'Prova', detail: 'cada papel responde do seu lugar, com as 3 perguntas do júri, sem ver o gabarito' },
    { title: 'Nota', detail: 'fluxo.py prova-nota: nota por programa; item que todos perderam vai à árbitra (Olga) antes; nível, lições e casos que voltam' },
  ],
}

const A = args || {}
if (!A.papeis || !A.papeis.length || !A.tag) throw new Error('args: {papeis: ["redator", ...], tag: "AAAAMMDD-HHMM"}')
const N = A.n_casos || 10, P = A.n_problemas || 5
const GAB = `/tmp/x1-provas/gabarito-${A.tag}.json`  // fora do repositório até a nota (provas 1 e 2)
const SAIDA = { type: 'object', properties: { codigo: { type: 'integer' }, saida: { type: 'string' } }, required: ['codigo', 'saida'] }
const PROB = { type: 'object', properties: { linha: { type: 'integer' }, categoria: { type: 'string' }, porque: { type: 'string', description: 'a regra ferida, com arquivo e linha' }, nivel: { type: 'integer', description: 'o nível do problema (1 a 6), pela tabela de níveis' } }, required: ['linha', 'categoria', 'porque', 'nivel'] }
const CASOS = {
  type: 'object',
  properties: { casos: { type: 'array', items: { type: 'object', properties: { id: { type: 'integer' }, linhas: { type: 'array', items: { type: 'string' } }, problemas: { type: 'array', items: PROB }, iscas: { type: 'array', items: { type: 'integer' }, description: 'linhas que parecem erro e não são' } }, required: ['id', 'linhas', 'problemas', 'iscas'] } } },
  required: ['casos'],
}
const RESP = {
  type: 'object',
  properties: {
    respostas: { type: 'array', items: { type: 'object', properties: {
      id: { type: 'integer' }, comprador: { type: 'string' }, dinheiro: { type: 'string' }, risco: { type: 'string' },
      problemas: { type: 'array', items: { type: 'object', properties: { linha: { type: 'integer' }, categoria: { type: 'string' }, porque: { type: 'string' } }, required: ['linha', 'porque'] } },
    }, required: ['id', 'problemas'] } },
  },
  required: ['respostas'],
}
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
const rodar = (label, phase, cmd) => agent(`Rode exatamente este comando na raiz do repositório e devolva o código de saída e, em "saida", SÓ o que o comando imprimiu, sem comentário seu:\n\n${cmd}`,
  { label, phase, model: 'haiku', effort: 'low', schema: SAIDA })
const numerar = c => c.linhas.map((l, i) => `${i + 1}| ${l}`).join('\n')

const gastoAntes = budget.spent()
phase('Estado')
const est = lerJson((await rodar('programa:estado', 'Estado', 'python3 ferramentas/fluxo.py prova-estado')).saida, {})
const niveis = est._niveis || {}
const nivelDe = p => (est[p] && est[p].nivel) || 1
const porNivel = {}
for (const p of A.papeis) (porNivel[nivelDe(p)] = porNivel[nivelDe(p)] || []).push(p)
log('níveis: ' + A.papeis.map(p => `${p} ${nivelDe(p)}`).join(', '))

const todos = [], respostas = {}
let proximoId = 1
for (const [nivel, papeis] of Object.entries(porNivel)) {
  const regra = niveis[nivel] || `${niveis['6']}; ${nivel - 5} iscas por caso e o problema no meio de um texto mais longo`
  const voltam = papeis.flatMap(p => ((est[p] && est[p].voltam) || []).map(v => ({ papel: p, ...v })))
  phase('Montar')
  const montado = await agent(
    `Monte ${N} casos para a prova de entrada do X1-Plantas, nível ${nivel}: ${regra}.\n` +
    `Cada caso é um trecho curto do trabalho real (mensagem de WhatsApp, página do e-book, plano, anúncio, decisão), de 4 a 12 linhas, em português do Brasil. ` +
    `${P} casos têm problema plantado; os outros ${N - P} são limpos de verdade (cuidado: na prova 1, 3 "limpos" não eram). ` +
    `Tire os problemas dos erros reais: pedidos/LICOES.md, pedidos/PROVAS.md, pedidos/anexos/veto-*.md, contexto/redator.md (frases vetadas), CLAUDE.md (regras que não mudam), ` +
    `ebook/plantas/PLANTAS.md (números), pedidos/anexos/decisoes-do-dono-2026-11-23.md (o que o dono decidiu). ` +
    (voltam.length ? `Inclua, reescritos com outras palavras, estes erros que voltaram: ${JSON.stringify(voltam).slice(0, 4000)}. ` : '') +
    `Para cada problema: a linha (1 = primeira linha do caso), a categoria, o porquê (arquivo e linha da regra) e o nível dele na tabela (${JSON.stringify(niveis)}); ` +
    `todo problema é do nível ${nivel} ou abaixo, e pelo menos metade é do nível ${nivel}. Em "iscas", as linhas que parecem erro e não são (obrigatório a partir do nível 5). Ids de ${proximoId} a ${proximoId + N - 1}. Não grave nada.`,
    { label: `montar nível ${nivel}`, phase: 'Montar', model: 'opus', schema: CASOS })
  phase('Conferir gabarito')
  const conferido = await agent(
    `Confira o gabarito desta prova sem confiar em quem montou. Para cada caso com problema, abra a regra citada e confirme que a linha indicada fere a regra ` +
    `(se a linha estiver errada, corrija; se não houver problema de verdade, deixe "problemas" vazio; confira o nível de cada um e se cada isca é mesmo limpa). Para cada caso limpo, procure problema real ` +
    `contra CLAUDE.md, contexto/redator.md, ebook/plantas/PLANTAS.md e as decisões do dono; se achar, ponha no gabarito. Devolva os casos corrigidos, mesmos ids.\n\n` +
    JSON.stringify(montado ? montado.casos : []),
    { label: `conferir gabarito nível ${nivel}`, phase: 'Conferir gabarito', model: 'opus', schema: CASOS })
  const casos = (conferido || montado || { casos: [] }).casos
  proximoId += N
  todos.push(...casos.map(c => ({ id: c.id, texto: numerar(c), problemas: c.problemas, iscas: c.iscas || [] })))
  phase('Prova')
  const rs = await parallel(papeis.map(p => () => agent(
    `Prova de entrada do seu papel (nível ${nivel}). Para cada caso, responda às 3 perguntas do júri do seu lugar: ` +
    `comprador (quem tem o lote entende e confia?), dinheiro (aproxima o Pix ou baixa o custo por venda?), risco (o que dá errado e não tem volta, e que passo falta?). ` +
    `Depois aponte cada problema com o número da linha e a regra (arquivo e linha). Caso sem problema: "problemas" vazio; apontar problema em caso limpo conta contra. ` +
    `Pode abrir o repositório para conferir, menos pedidos/provas/ e /tmp.\n\n` +
    casos.map(c => `### Caso ${c.id}\n${numerar(c)}`).join('\n\n'),
    { label: `prova: ${p}`, phase: 'Prova', agentType: p, schema: RESP })))
  papeis.forEach((p, i) => { respostas[p] = rs[i] ? rs[i].respostas.map(r => ({ id: r.id, problemas: r.problemas })) : [] })
}

phase('Nota')
const gravaGab = await rodar('gabarito fora do repositório', 'Nota', `mkdir -p /tmp/x1-provas && cat > ${GAB} <<'FIM'\n${JSON.stringify({ casos: todos })}\nFIM\necho gravado`)
const notaCom = extra => rodar('programa:nota', 'Nota', `python3 ferramentas/fluxo.py prova-nota - <<'FIM'\n${JSON.stringify({ gabarito_arquivo: GAB, respostas, gasto_tokens: budget.spent() - gastoAntes, ...extra })}\nFIM`)
let resultado = lerJson((await notaCom({})).saida, null)
// item que todos deixaram passar fica em disputa (o gabarito pode estar errado, como na prova 1): a Olga, que não montou
// nem conferiu o gabarito, decide; só então a nota é gravada
let arbitro = null
if (resultado && resultado._em_disputa && resultado._em_disputa.length) {
  const ARB = { type: 'object', properties: { confirmados: { type: 'array', items: { type: 'string' } }, anulados: { type: 'array', items: { type: 'string' } }, porque: { type: 'string' } }, required: ['confirmados', 'anulados', 'porque'] }
  const itens = resultado._em_disputa.map(k => { const [cid, ln] = k.split(':').map(Number); const c = todos.find(x => x.id === cid); return { chave: k, caso: c && c.texto, problema: c && c.problemas.find(g => g.linha === ln) } })
  arbitro = await agent(
    `Você é árbitro da prova de entrada. Todos os papéis deixaram passar estes itens do gabarito, e o gabarito pode estar errado (na prova 1 errou em 3 planos). ` +
    `Para cada item, abra a regra citada e decida: "confirmados" se a linha fere mesmo uma regra escrita, aplicada ao caso como está; "anulados" se a regra não alcança o caso ou é leitura larga. ` +
    `Use as chaves exatas. Uma frase de porquê por item.\n\n${JSON.stringify(itens).slice(0, 8000)}`,
    { label: 'árbitro: Olga', phase: 'Nota', agentType: 'supervisor', schema: ARB })
  resultado = lerJson((await notaCom({ confirmados: arbitro ? arbitro.confirmados : [], anulados: arbitro ? arbitro.anulados : [] })).saida, null)
}
if (!resultado) log('ATENÇÃO: a nota não saiu; o Maestro roda prova-nota com "casos" e "respostas" devolvidos')
return { resultado, arbitro, gabarito_em: GAB, gravou_gabarito: gravaGab && gravaGab.saida, casos: todos, respostas }

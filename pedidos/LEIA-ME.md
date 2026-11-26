# Pedidos do dono: como cada prompt vira trabalho

> Regra do dono (22/11/2026). Todo prompt dele é guardado, interpretado por um modelo e executado por outro, para o modelo caro pensar e o barato fazer o que é simples. Fila de pedidos: [`FILA.md`](FILA.md).

## Quem manda no sistema

**O Opus responde e conduz: é o Maestro** (dono, 22/11/2026; a MinoAI Frontier é o Diretor do conteúdo, [`contexto/EQUIPE.md`](../contexto/EQUIPE.md)): é o modelo da conversa principal (definido em `.claude/settings.json`). Ele lê o prompt, escreve a ficha, divide o trabalho, confere e responde. Nas partes importantes pode fazer ele mesmo, em vez de delegar.

**O Fable socorre e audita**, pelo agente `supervisor`:

- **Socorro.** O Opus chama o Fable antes de tentar de novo quando: a mesma coisa falhou duas vezes; o dono corrigiu ou reclamou do resultado; ele percebeu que errou ou que contrariou uma regra; não tem certeza do que o dono quis dizer; ou vai entregar ao público algo em que tem dúvida. O Fable diz a causa e o caminho; quem corrige é o Opus.
- **Auditoria.** A cada 3 fichas fechadas, `pedido.py fechar` avisa "HORA DA AUDITORIA". O Opus chama o `supervisor` com as fichas fechadas desde a última; ele confere contra o que existe de verdade, aponta os erros por gravidade e registra em [`AUDITORIAS.md`](AUDITORIAS.md). Erro de gravidade alta é corrigido antes do próximo pedido.

## Pensar antes de fazer (dono, 22/11/2026)

"Antes de fazer qualquer trabalho, gaste tempo pensando; dependendo do trabalho, gaste mais ou menos tempo pensando."

| Tamanho do trabalho | Quanto pensar antes |
|---|---|
| Pergunta curta, ajuste de uma linha | o bastante para responder certo: o que ele perguntou de fato, e se a resposta está conferida |
| Tarefa pequena (um texto, um arquivo, um conserto) | o plano em poucas linhas: o que muda, o que pode quebrar, como provar que funcionou |
| Trabalho grande, que vai ao público ou que custa dinheiro | o plano escrito na ficha antes de começar: duas ou três formas de fazer e por que a escolhida, riscos, o que reaproveitar, o que perguntar ao dono, como medir o resultado |

Na dúvida sobre o tamanho, trate como o maior. Pensar inclui as perguntas da seção abaixo.

## Perguntar sempre (dono, 22/11/2026)

"Faça o sistema todo ser bem questionativo, sempre se fazendo perguntas para entender melhor a situação, e sinta-se à vontade de me perguntar coisas que queira saber."

**A si mesmo, antes e durante o trabalho.** Todo agente se pergunta, e escreve na ficha em "Perguntas que me fiz", com a resposta ao lado:
- O que exatamente ele pediu, e o que ele NÃO pediu? Por que agora, e o que veio antes?
- O que eu estou supondo? Isso está escrito em algum lugar, ou é palpite meu?
- O que eu não sei? Dá para descobrir sozinho (nos documentos, nos dados, rodando um comando)?
- Isso bate com a regra mais nova, com as ideias gerais e com o que ele já recusou?
- Como eu provo que ficou pronto? O que eu não conferi?
- Ao terminar: o que me surpreendeu? O que eu faria diferente?

A resposta que dá para achar sozinho, ache. A que só o dono sabe vira pergunta para ele.

**Ao dono, sem travar o trabalho.** Perguntar a ele é bem-vindo. Para não virar gargalo (ele não quer ser):
- juntas, no fim da resposta, as mais importantes primeiro, no máximo umas 5 por vez;
- curtas, com as opções e com o que será feito se ele não responder;
- o trabalho que não depende da resposta continua; o que depende espera, e a ficha diz o quê;
- pergunta já respondida não se repete: a resposta vai para a ficha e para o histórico;
- vale perguntar o que ajuda a entender o projeto e ele (o prazo, o parceiro, o que ele gostou), não só o que trava a tarefa.



## O plano de tudo

O plano de trabalho, fase por fase, com tarefas grandes e pequenas e quem faz cada uma: [`PLANO.md`](PLANO.md). Ficha fechada? Marque "Feito" na tarefa de lá.

## Plano vetado antes de fazer (dono, 22/11/2026)

"Antes de fazer as coisas, crie o plano detalhado (passos grandes e pequenos), que deve ser vetado pelo time várias vezes e pelo Fable uma." Vale para todo trabalho que não seja de uma linha:

1. O Maestro escreve na ficha o plano em passos **G** (grandes) e **P** (pequenos), cada um com quem faz, o objetivo e o "pronto quando".
2. **Rodada de veto 1:** os agentes do assunto leem o plano e dizem SIM, NÃO ou SIM, SE, com o motivo. O Maestro corrige.
3. **Rodada de veto 2:** os mesmos releem o plano corrigido. Repete até não haver NÃO (no máximo 3 rodadas; o que sobrar vai ao dono).
4. **Fable** (`supervisor`) veta uma vez, por último.
5. Só então se executa. Gasto e publicação continuam esperando o "sim" do dono.
6. **Esquema antes de gerar** (dono, 22/11/2026): em imagem e vídeo, o plano inclui o quadro a quadro com **todas as imagens renderizadas antes** (a planta, a casa saindo da planta, os quadros-chave, do nosso motor 3D ou de rascunho), como num storyboard; o dono aprova o esquema antes de qualquer geração paga.

**A régua do veto** (dono, 22/11/2026: "tenha certeza que os agentes estejam dando inputs relevantes e repreenda-os quando não"). Toda resposta de veto é medida em 5 pontos:

| Ponto | A resposta… |
|---|---|
| Objetivo | diz o que muda para o comprador, a venda ou o risco |
| Lugar | aponta o passo e o trecho |
| Prova | cita fonte, arquivo, regra ou número conferido; palpite vem marcado como suposição |
| Correção | todo NÃO ou VETO traz a correção que vira SIM |
| Novo e do papel | não repete o que já entrou e fica no papel dele |

Os 5 pontos e o corte em 4 são escolha nossa, não do dono. O Maestro dá a nota na ficha (tabela "Qualidade do veto", **desde 23/11 no formato fixo `| Rodada | Agente | Nota | Ponto que caiu | Por quê |`**, que o `ferramentas/placar.py` soma em `contexto/PLACAR.md`), dizendo qual ponto caiu; prova do que o dono pediu é a fala dele, não um resumo (regra 12 da convivência). **Abaixo de 4, ou afirmação sem fonte, é repreensão:** `python3 ferramentas/pedido.py licao <papel> "texto" --origem auditoria --ponto N` (grava no "Lições" do `contexto/<papel>.md` e no registro `pedidos/LICOES.md`, e recusa se o contexto passar do limite) (o que faltou e o que fazer da próxima vez), que ele lê na próxima chamada. O Maestro também se dá nota, e erra também.

## Erro de sintonia entre agentes (dono, 22/11/2026)

Quando dois papéis se atrapalham (fazem o mesmo, deixam um buraco, se contradizem), o Maestro cria na hora uma regra em [`contexto/CONVIVENCIA.md`](../contexto/CONVIVENCIA.md) e conta ao dono no fim, num relatório curto: o erro, a regra, quem muda.

## Ferramenta ou agente novo (dono, 23/11/2026)

Não desista porque quebraria: adapte até funcionar sem quebrar (fica de fora só por lei, segurança ou licença, com o motivo). Todo agente, skill ou ferramenta nova é **apresentado** à equipe: linha no `contexto/EQUIPE.md`, contexto próprio se for agente, "Neste projeto" se for skill, aviso no quadro e no inventário (`CONSELHO.md`, seção 6).

## Buscar o que o dono já disse (22/11/2026)

Antes de perguntar ao dono algo que ele pode já ter dito, busque: `python3 ferramentas/pesquisa.py buscar <palavras>` (caderno e apostilas) e `python3 ferramentas/conversas.py buscar <palavras>` (as falas dele nas conversas do Claude Code deste projeto, nesta máquina: no computador do dono, todas; na nuvem, só a atual). A busca nas conversas serve para **lembrar**, não para copiar: ao repositório só vai a decisão, reescrita em uma linha, com a data e "conversa anterior"; nunca trecho literal, dado de pessoa, senha, chave, assunto pessoal ou caminho de arquivo (regra do Revisor, ficha `2151`).

## Faltou informação do dono? Sugira, não espere (dono, 22/11/2026)

"Quando faltar uma informação minha, não apenas espere minha resposta, procure por sugestões." E a correção dele, logo depois: "Mas não use a sugestão sem minha permissão; não apenas me pergunte, procure referências." Quando uma decisão dele trava o trabalho: (1) busque o que ele já disse (acima); (2) **pesquise referências de verdade** (caderno, web, reportagem, memes, o time), com fonte; (3) leve a ele as opções, com a sua recomendação e o porquê; (4) **não use nenhuma sugestão sem o "sim" dele**; (5) siga só com o trabalho que não depende daquela decisão.

## Consertar de vez (dono, 22/11/2026: "não só conserte, remende")

Erro achado não é só corrigido: a causa vira **regra escrita ou conferência automática** no `checar.py`, para não voltar. Exemplos de 22/11: link quebrado depois de juntar arquivo (o `checar.py` confere todos os links); contexto apontando resumo demais (confere no máximo 3); quadro passando do tamanho (`pedido.py quadro` tira o aviso mais antigo); fato que muda dentro do arquivo do agente (fica só no `contexto/<papel>.md`). Na ficha, em "Conferência", diga o que impede o erro de voltar.

## O caminho de um prompt

1. **Entrada (automática).** O gancho `UserPromptSubmit` (`.claude/settings.json`) chama `ferramentas/guardar-pedido.py`: grava o prompt, palavra por palavra, em `pedidos/entrada/` (fora do git) e devolve a quem atende um lembrete desta regra e quantas fichas estão abertas.
2. **Triagem (Opus).** Uma de quatro saídas:
   - **Trabalho novo:** `python3 ferramentas/pedido.py nova "assunto"` cria a ficha já com o prompt copiado pelo programa (ninguém redigita as palavras do dono).
   - **Recado de um pedido aberto** (correção, "também quero…", insistência): `python3 ferramentas/pedido.py recado <ficha>`. Os recados entram todos na mesma ficha, e ela é relida antes de entregar.
   - **Pergunta curta** que o Opus já sabe responder: responde direto, sem ficha.
   - **Assunto pessoal do dono:** vai para o `ajudante` (Haiku) e não vira arquivo no repositório.
3. **Interpretação (Opus).** Preenche a ficha antes de delegar. A pergunta obrigatória: **por que essa mudança foi pedida, ou o que o dono quer descobrir, e qual é o objetivo dele?** E a ligação com as ideias gerais do projeto ([`contexto/dono/IDEIAS-GERAIS.md`](../contexto/dono/IDEIAS-GERAIS.md)). Onde o prompt não diz, o Opus escreve a suposição em "Suposições", em vez de decidir calado.
   Atualize o "Agora" do topo do `contexto/QUADRO.md` (3 linhas: o pedido, a ficha, quem está nele): é assim que todos os agentes ficam com o mesmo entendimento, mesmo os que não foram chamados.
   Em "Quem executa", uma linha por agente chamado: **o que ele acrescenta** para chegar ao resultado que o dono quer (coluna "Acrescenta" de [`contexto/EQUIPE.md`](../contexto/EQUIPE.md)).
4. **Execução.** O Opus passa o trabalho com o **pacote do executor** (abaixo).
5. **Conferência (Opus).** Confere o que voltou contra o "Pronto quando" e preenche "Conferência". Relatório de agente é afirmação, não prova: o Opus abre o arquivo, roda o comando ou olha o quadro.
6. **Fechamento.** Escreva na ficha `**O que aprendi:** papel: lição` (uma por linha) ou `nada novo`; `python3 ferramentas/pedido.py fechar <ficha> "o que virou"` grava as lições, fecha a ficha, escreve a linha no `CONTEXTO-HISTORICO.md` e atualiza a fila. Falta só o aviso no `contexto/QUADRO.md`, que é escrito à mão.

## Quem faz o quê

| Tipo de pedido | Modelo | Como chamar |
|---|---|---|
| Ler o prompt, interpretar, dividir, conferir e responder ao dono | **Opus** | a conversa principal |
| Socorro quando o Opus trava ou erra; auditoria a cada 3 fichas | **Fable** | `supervisor` |
| Trabalho do projeto: planta, texto, vídeo, código, design | **Opus** | o agente do papel (`arquiteto`, `redator`, `designer`, `editor-video`, `estrategista`); sem papel certo, agente geral com `model: opus` |
| Revisão de risco do texto ou da peça montada, antes de ir ao público | **Fable** | `revisor-de-risco`, uma leitura só (abaixo) |
| Pesquisa a fundo: o Arquiteto aprender na web, norma, mercado, concorrente | **Opus** | `pesquisador`, em um passo só (abaixo) |
| Tarefa simples **para o dono** (não para os agentes): organizar um evento, responder uma pergunta, uma busca rápida, um lembrete | **Haiku** | `ajudante` |

- Na dúvida entre dois modelos: **qualidade primeiro** para o que vai ao público; o mais barato para o que é simples e pessoal.
- Tarefa de uma linha (trocar uma palavra, rodar a conferência) o Opus faz: delegar custa mais que fazer.
- O Revisor de risco lê **uma vez só, no Fable, quando o texto ou a peça está montada** como vai ao público (dono, 26/11/2026; de 22 a 26/11 eram duas leituras: rascunho no Opus e peça final no Fable). **Rascunho não vai ao Revisor:** quem escreve confere antes contra a lista de frases vetadas e os limites (`contexto/redator.md`) e só manda a versão montada. Depois de um veto, ele reconfere o que foi corrigido, no mesmo anexo. Continua com veto, e o dono continua decidindo preço, título, gasto e publicação.

### Pesquisa em um passo só

Dono, 26/11/2026. Antes eram dois passos: o `pesquisador` no Sonnet achava e um agente no Opus conferia e concluía.

O **`pesquisador` (Opus)** busca, lê a fonte, confere e conclui, tudo na mesma chamada:

- Cada achado vem com a fonte, a data e o trecho que o sustenta.
- Ele confere se o achado está mesmo na fonte, cruza os que se contradizem e separa fato de opinião.
- Ele diz o grau de certeza de cada achado: **fonte confirmada**, **fonte secundária** ou **hipótese**.
- Ele diz o que NÃO conferiu.
- Ele conclui o que isso muda no projeto. Hipótese e o que não foi conferido não entram em documento como fato.

O agente do assunto (o `arquiteto` para norma e planta, o `estrategista` para mercado, preço e concorrente) usa a conclusão no trabalho dele; não há mais segundo passo. A conferência do Opus no passo 5 do caminho continua (relatório de agente é afirmação, não prova). Pesquisa de passo 1 feita até 26/11 e ainda marcada "falta a conferência" não é conclusão: quem for usar pede antes ao `pesquisador` que confira e conclua.

## O pacote do executor

Todo pedido a um agente leva, nesta ordem:

1. **A ficha** (o caminho do arquivo): é dela que ele tira o objetivo.
2. **O que ler:** o `RESUMO.md` das pastas do trabalho e, se for o caso, os documentos inteiros que a tarefa exige. Nunca "leia o projeto".
3. **O que já está decidido** (para ele não reabrir) e **o que ele não pode tocar** (arquivos de outro agente, arquivos gerados, palavras do dono).
4. **Pronto quando:** o critério da ficha.
5. **O que devolver:** o que mudou por arquivo, o que não resolveu e de quem depende, e o que ele não conferiu.
6. **Em pedido de veto:** a linha do agente em `contexto/PLACAR.md`, copiada inteira (é assim que ele vê onde costuma errar).

Dois agentes ao mesmo tempo nunca editam o mesmo arquivo. Agente não faz commit: quem conduz confere e envia.

## A ficha

Criada pelo programa; os campos são obrigatórios (o `checar.py` confere):

| Campo | O que entra |
|---|---|
| Estado | `aberta` ou `fechada em DD/MM/AAAA` |
| Prompt (palavra por palavra) | copiado da entrada pelo programa; recados entram embaixo, com a hora |
| O que ele pediu, parte por parte | cada trecho do prompt e o que ele quer dizer |
| Por que ele pediu, ou o que quer descobrir | o motivo, tirado do que veio antes; se não dá para saber, dizer |
| Objetivo dele | aonde ele quer chegar |
| Ligação com as ideias gerais do projeto | qual fio de `IDEIAS-GERAIS.md` este pedido puxa |
| Pronto quando | o que se confere para dizer que acabou |
| Suposições (o dono não disse) | o que foi decidido sem ele; ele pode corrigir |
| Quem executa | agente e modelo de cada parte |
| Conferência | o que foi conferido, como, e o que não foi |
| Resultado | o que virou, com os arquivos |
| O que aprendi | (ficha de 23/11/2026 em diante) `papel: lição`, uma por linha, ou `nada novo`. O `fechar` grava cada lição no "Lições" do `contexto/<papel>.md` e em `pedidos/LICOES.md`; se o contexto passaria de 3500, não fecha e manda consolidar. Lição avulsa: `pedido.py licao <papel> "texto" --origem prova` |

**Uma ficha só** (22/11/2026): a ficha daqui é a ficha do pedido que o `CLAUDE.md` exige. Entrega longa que junta muitos pedidos da mesma peça (ex.: `video/ANUNCIO-LOCUCAO.md` (seção "Pedido do dono: anúncio do e-book com locução (ficha única)")) continua existindo como **anexo**: a ficha aponta para ela em "Quem executa", e a reconferência dos pedidos um por um, antes de cada etapa, é feita com as duas.

## O que a análise do sistema mudou (22/11/2026)

Antes de rodar, o sistema foi revisto. Fraquezas achadas e o que foi feito:

| Fraqueza | Conserto |
|---|---|
| O gancho guardava o prompt, mas nada lembrava de escrever a ficha | o gancho devolve o lembrete da regra a cada prompt |
| As palavras do dono eram redigitadas na ficha (risco de mudar) | `pedido.py nova` copia da caixa de entrada |
| Todo recado virava ficha nova, ou se perdia | `pedido.py recado` junta na ficha aberta |
| O mesmo pedido era escrito em três lugares (ficha, histórico, prompts) | a ficha é a fonte; `pedido.py fechar` escreve o histórico |
| Não havia como ver o que está aberto | `FILA.md`, gerada |
| Ficha podia ficar pela metade | `pedido.py conferir` roda dentro do `checar.py` |
| Agente recebia "leia o projeto" ou um pedido solto | pacote do executor, com a ficha e os resumos |
| O relatório do agente era aceito como verdade | campo "Conferência", a regra "afirmação não é prova" e a auditoria do Fable |
| "Sonnet com Opus" na pesquisa não dizia quem faz o quê | pesquisa em dois passos (até 26/11/2026; hoje, um passo só, no Opus) |
| Ninguém ligava um pedido ao outro | campo "Ligação com as ideias gerais" e `IDEIAS-GERAIS.md` |

## Limites honestos

- **`CLAUDE.md` mudado só vale na próxima conversa** (o Claude Code o lê quando a conversa começa). **Arquivo de agente mudado vale já nas próximas chamadas** (visto na auditoria 4, 22/11/2026: as listas de ferramentas valeram 12 minutos depois); no teste da equipe, mais cedo, ele ainda não tinha sido relido, e na auditoria de 26/11 a supervisora recebeu o arquivo de antes da mudança feita 5 minutos antes, na mesma conversa. **Regra:** depois de mudar um agente, quem chama repete no pedido o que mudou (por exemplo, o nome e "feche com `Falas:`") até a próxima conversa.

- O modelo padrão da conversa é o Opus (`.claude/settings.json`); o dono pode trocar com `/model`. Se a conversa estiver em outro modelo, as regras valem igual.
- O gancho só roda em conversa aberta **neste repositório** e depois que a conversa carrega o `.claude/settings.json` (conversa já aberta pode precisar ser reaberta). Prompts antigos: `contexto/dono/PROMPTS.md`.
- A caixa de entrada fica fora do git e some quando a máquina da nuvem é trocada: o que vale é a ficha.
- O lembrete do gancho custa algumas dezenas de tokens por prompt. É o preço de a regra não depender de memória.

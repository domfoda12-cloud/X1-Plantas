# Pedidos do dono: como cada prompt vira trabalho

> Regra do dono (22/11/2026). Todo prompt dele é guardado, interpretado por um modelo e executado por outro, para o modelo caro pensar e o barato fazer o que é simples. Fila de pedidos: [`FILA.md`](FILA.md).

## Quem manda no sistema

**O Opus responde e conduz** (dono, 22/11/2026): é o modelo da conversa principal (definido em `.claude/settings.json`). Ele lê o prompt, escreve a ficha, divide o trabalho, confere e responde. Nas partes importantes pode fazer ele mesmo, em vez de delegar.

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



## O caminho de um prompt

1. **Entrada (automática).** O gancho `UserPromptSubmit` (`.claude/settings.json`) chama `ferramentas/guardar-pedido.py`: grava o prompt, palavra por palavra, em `pedidos/entrada/` (fora do git) e devolve a quem atende um lembrete desta regra e quantas fichas estão abertas.
2. **Triagem (Opus).** Uma de quatro saídas:
   - **Trabalho novo:** `python3 ferramentas/pedido.py nova "assunto"` cria a ficha já com o prompt copiado pelo programa (ninguém redigita as palavras do dono).
   - **Recado de um pedido aberto** (correção, "também quero…", insistência): `python3 ferramentas/pedido.py recado <ficha>`. Os recados entram todos na mesma ficha, e ela é relida antes de entregar.
   - **Pergunta curta** que o Opus já sabe responder: responde direto, sem ficha.
   - **Assunto pessoal do dono:** vai para o `ajudante` (Haiku) e não vira arquivo no repositório.
3. **Interpretação (Opus).** Preenche a ficha antes de delegar. A pergunta obrigatória: **por que essa mudança foi pedida, ou o que o dono quer descobrir, e qual é o objetivo dele?** E a ligação com as ideias gerais do projeto ([`contexto/dono/IDEIAS-GERAIS.md`](../contexto/dono/IDEIAS-GERAIS.md)). Onde o prompt não diz, o Opus escreve a suposição em "Suposições", em vez de decidir calado.
4. **Execução.** O Opus passa o trabalho com o **pacote do executor** (abaixo).
5. **Conferência (Opus).** Confere o que voltou contra o "Pronto quando" e preenche "Conferência". Relatório de agente é afirmação, não prova: o Opus abre o arquivo, roda o comando ou olha o quadro.
6. **Fechamento.** `python3 ferramentas/pedido.py fechar <ficha> "o que virou"` fecha a ficha, escreve a linha no `CONTEXTO-HISTORICO.md` e atualiza a fila. Falta só o aviso no `contexto/QUADRO.md`, que é escrito à mão.

## Quem faz o quê

| Tipo de pedido | Modelo | Como chamar |
|---|---|---|
| Ler o prompt, interpretar, dividir, conferir e responder ao dono | **Opus** | a conversa principal |
| Socorro quando o Opus trava ou erra; auditoria a cada 3 fichas | **Fable** | `supervisor` |
| Trabalho do projeto: planta, texto, vídeo, código, design, revisão de risco | **Opus** | o agente do papel (`arquiteto`, `redator`, `designer`, `editor-video`, `estrategista`, `revisor-de-risco`); sem papel certo, agente geral com `model: opus` |
| Pesquisa a fundo: o Arquiteto aprender na web, norma, mercado, concorrente | **Sonnet + Opus** | em dois passos (abaixo) |
| Tarefa simples **para o dono** (não para os agentes): organizar um evento, responder uma pergunta, uma busca rápida, um lembrete | **Haiku** | `ajudante` |

- Na dúvida entre dois modelos: **qualidade primeiro** para o que vai ao público; o mais barato para o que é simples e pessoal.
- Tarefa de uma linha (trocar uma palavra, rodar a conferência) o Opus faz: delegar custa mais que fazer.
- O Revisor de risco continua com veto, e o dono continua decidindo preço, título, gasto e publicação.

### Pesquisa em dois passos

1. **`pesquisador` (Sonnet)** busca e lê as fontes e devolve uma lista: cada achado com a fonte, a data, o trecho que o sustenta e o que ele NÃO conseguiu confirmar.
2. **Um agente no Opus** recebe essa lista e as fontes: confere se cada achado está mesmo na fonte, cruza os que se contradizem, separa fato de opinião e conclui o que isso muda no projeto. Só o resultado do passo 2 entra em documento.

## O pacote do executor

Todo pedido a um agente leva, nesta ordem:

1. **A ficha** (o caminho do arquivo): é dela que ele tira o objetivo.
2. **O que ler:** o `RESUMO.md` das pastas do trabalho e, se for o caso, os documentos inteiros que a tarefa exige. Nunca "leia o projeto".
3. **O que já está decidido** (para ele não reabrir) e **o que ele não pode tocar** (arquivos de outro agente, arquivos gerados, palavras do dono).
4. **Pronto quando:** o critério da ficha.
5. **O que devolver:** o que mudou por arquivo, o que não resolveu e de quem depende, e o que ele não conferiu.

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

**Uma ficha só** (22/11/2026): a ficha daqui é a ficha do pedido que o `CLAUDE.md` exige. Entrega longa que junta muitos pedidos da mesma peça (ex.: `video/PEDIDO-anuncio-locucao.md`) continua existindo como **anexo**: a ficha aponta para ela em "Quem executa", e a reconferência dos pedidos um por um, antes de cada etapa, é feita com as duas.

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
| "Sonnet com Opus" na pesquisa não dizia quem faz o quê | pesquisa em dois passos |
| Ninguém ligava um pedido ao outro | campo "Ligação com as ideias gerais" e `IDEIAS-GERAIS.md` |

## Limites honestos

- O modelo padrão da conversa é o Opus (`.claude/settings.json`); o dono pode trocar com `/model`. Se a conversa estiver em outro modelo, as regras valem igual.
- O gancho só roda em conversa aberta **neste repositório** e depois que a conversa carrega o `.claude/settings.json` (conversa já aberta pode precisar ser reaberta). Prompts antigos: `contexto/dono/PROMPTS.md`.
- A caixa de entrada fica fora do git e some quando a máquina da nuvem é trocada: o que vale é a ficha.
- O lembrete do gancho custa algumas dezenas de tokens por prompt. É o preço de a regra não depender de memória.

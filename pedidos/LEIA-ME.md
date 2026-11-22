# Pedidos do dono: como cada prompt vira trabalho

> Regra do dono (22/11/2026). Todo prompt dele é guardado, interpretado por um modelo e executado por outro, para o modelo caro pensar e o barato fazer o que é simples. Fila de pedidos: [`FILA.md`](FILA.md).

## Quem manda no sistema

**O Fable roda o sistema e é o supervisor principal.** Ele decide a divisão do trabalho, confere tudo o que os outros entregam e responde pelo resultado. Nas partes importantes do projeto ele pode pôr a mão e fazer ele mesmo, em vez de delegar.

## O caminho de um prompt

1. **Entrada (automática).** O gancho `UserPromptSubmit` (`.claude/settings.json`) chama `ferramentas/guardar-pedido.py`: grava o prompt, palavra por palavra, em `pedidos/entrada/` (fora do git) e devolve a quem atende um lembrete desta regra e quantas fichas estão abertas.
2. **Triagem (Fable).** Uma de quatro saídas:
   - **Trabalho novo:** `python3 ferramentas/pedido.py nova "assunto"` cria a ficha já com o prompt copiado pelo programa (ninguém redigita as palavras do dono).
   - **Recado de um pedido aberto** (correção, "também quero…", insistência): `python3 ferramentas/pedido.py recado <ficha>`. Os recados entram todos na mesma ficha, e ela é relida antes de entregar.
   - **Pergunta curta** que o Fable já sabe responder: responde direto, sem ficha.
   - **Assunto pessoal do dono:** vai para o `ajudante` (Haiku) e não vira arquivo no repositório.
3. **Interpretação (Fable).** Preenche a ficha antes de delegar. A pergunta obrigatória: **por que essa mudança foi pedida, ou o que o dono quer descobrir, e qual é o objetivo dele?** E a ligação com as ideias gerais do projeto ([`contexto/dono/IDEIAS-GERAIS.md`](../contexto/dono/IDEIAS-GERAIS.md)). Onde o prompt não diz, o Fable escreve a suposição em "Suposições", em vez de decidir calado.
4. **Execução (outro modelo).** O Fable passa o trabalho com o **pacote do executor** (abaixo).
5. **Conferência (Fable).** Confere o que voltou contra o "Pronto quando" e preenche "Conferência do Fable". Relatório de agente é afirmação, não prova: o Fable abre o arquivo, roda o comando ou olha o quadro.
6. **Fechamento.** `python3 ferramentas/pedido.py fechar <ficha> "o que virou"` fecha a ficha, escreve a linha no `CONTEXTO-HISTORICO.md` e atualiza a fila. Falta só o aviso no `contexto/QUADRO.md`, que é escrito à mão.

## Quem faz o quê

| Tipo de pedido | Modelo | Como chamar |
|---|---|---|
| Ler o prompt, interpretar, dividir, conferir e responder ao dono | **Fable** | a conversa principal |
| Trabalho do projeto: planta, texto, vídeo, código, design, revisão de risco | **Opus** | o agente do papel (`arquiteto`, `redator`, `designer`, `editor-video`, `estrategista`, `revisor-de-risco`); sem papel certo, agente geral com `model: opus` |
| Pesquisa a fundo: o Arquiteto aprender na web, norma, mercado, concorrente | **Sonnet + Opus** | em dois passos (abaixo) |
| Tarefa simples **para o dono** (não para os agentes): organizar um evento, responder uma pergunta, uma busca rápida, um lembrete | **Haiku** | `ajudante` |

- Na dúvida entre dois modelos: **qualidade primeiro** para o que vai ao público; o mais barato para o que é simples e pessoal.
- Tarefa de uma linha (trocar uma palavra, rodar a conferência) o Fable faz: delegar custa mais que fazer.
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
| Conferência do Fable | o que foi conferido, como, e o que não foi |
| Resultado | o que virou, com os arquivos |

A ficha de entrega longa de vídeo (`video/PEDIDO-<entrega>.md`, que junta muitos pedidos da mesma peça) continua existindo: a ficha daqui aponta para ela.

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
| O relatório do agente era aceito como verdade | campo "Conferência do Fable" e a regra "afirmação não é prova" |
| "Sonnet com Opus" na pesquisa não dizia quem faz o quê | pesquisa em dois passos |
| Ninguém ligava um pedido ao outro | campo "Ligação com as ideias gerais" e `IDEIAS-GERAIS.md` |

## Limites honestos

- A conversa principal só é o Fable se o dono a deixar nesse modelo (`/model`). A regra de delegar vale com qualquer modelo na conversa principal.
- O gancho só roda em conversa aberta **neste repositório** e depois que a conversa carrega o `.claude/settings.json` (conversa já aberta pode precisar ser reaberta). Prompts antigos: `contexto/dono/PROMPTS.md`.
- A caixa de entrada fica fora do git e some quando a máquina da nuvem é trocada: o que vale é a ficha.
- O lembrete do gancho custa algumas dezenas de tokens por prompt. É o preço de a regra não depender de memória.

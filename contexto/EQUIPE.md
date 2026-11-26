# A equipe: quem faz o quê e o que cada um acrescenta

> Dono, 22/11/2026: cada agente sabe a sua função e o que acrescentar a cada prompt; todos com o mesmo entendimento; tudo junto e organizado; gastando o mínimo de token e tempo. Agente: `.claude/agents/<nome>.md` e `contexto/<nome>.md`. Skills de cada um: [`ECOSSISTEMA.md`](../ECOSSISTEMA.md), seção 2b.

## A cada prompt

1. O **Maestro** (a conversa principal, Opus) abre a ficha e atualiza o "Agora" do [quadro](QUADRO.md): **todos leem o mesmo**, chamados ou não.
2. Chama **só** quem importa; na ficha, uma linha por agente: o que ele acrescenta. Tarefa de uma linha, ele faz.
3. O agente lê o quadro, o seu contexto e a ficha; devolve o que não é dele dizendo de quem é. Agente não chama agente.
4. O Maestro junta, confere e decide; em conteúdo, o Diretor opina primeiro.

## Os papéis

| Quem (modelo) | Faz | Acrescenta a cada prompt |
|---|---|---|
| **Maestro** (Opus) | Decide e rege | Quem chamar; a decisão final |
| **Diretor**, MinoAI | Ideia principal do conteúdo | Para, comenta, paga? Com a fonte |
| `redator` (Opus) | Texto público | O atributo que faz pagar |
| `estrategista` (Opus) | Oferta, preço | Efeito no custo por venda |
| `arquiteto` (Opus) | Planta, técnica | Validador; o que o profissional confere |
| `designer` (Opus) | Imagem parada | Genérico? Bate com a planta? |
| `editor-video` (Opus) | O que se move | Segura 3 segundos? |
| `pesquisador` (Opus) | Pesquisa a fundo, num passo | Achado conferido, fonte, certeza, o que não conferiu |
| `revisor-de-risco` (Fable, veto) | Honestidade, lei: uma leitura, peça montada | Promessa sem lastro? A correção |
| `supervisor` (Fable) | Socorro, auditoria, referências | A causa; o que falta |
| `ajudante` (Haiku) | Pessoal do dono | O resultado, curto |
| `planejador` (Opus) | Passo a passo; monte em grupos (desde 26/11) | Agora, depois, esperando o dono; grupos de 3 a 7, com ordem |

## Veto

Toda resposta de veto passa pela régua de 5 pontos (objetivo, lugar, prova, correção, novo e do papel; `pedidos/LEIA-ME.md`). Nota abaixo de 4 ou afirmação sem fonte vira repreensão em "Lições". **Quem chama o veto cola no pedido a linha do agente no [placar](PLACAR.md)**; ele lê antes de vetar.

## Fronteiras

Regras de convivência (o que já deu errado entre os papéis): [`CONVIVENCIA.md`](CONVIVENCIA.md).


- Designer e Editor usam o Diretor; geração no OpenArt só com o "sim" do dono.
- Web: todos buscam (menos o Revisor, que só lê), num caderno só: `ferramentas/pesquisa.py`. Pesquisa a fundo: o `pesquisador` (Opus) busca, confere e conclui, num passo só (dono, 26/11).
- Revisor de risco: **uma leitura só, no Fable, com a peça montada** como vai ao público (dono, 26/11). Rascunho não vai a ele: quem escreve confere antes contra a lista de frases vetadas e os limites (`contexto/redator.md`).
- Peça pública: Redator, Arquiteto e Revisor. Preço, título, gasto e publicação: o dono.

## Economia

- Menos agentes, o modelo mais barato que dá a qualidade; resumo, não documento; ficha, não conversa.
- O `CLAUDE.md` já chega a todos. `ULTIMO.md` só se a tarefa continua. Antes da web, `pesquisa.py buscar`; antes de perguntar ao dono, `conversas.py buscar`.
- Faltou decisão do dono? Pesquise referências e leve opções com recomendação; **nada se usa sem o "sim" dele** (`pedidos/LEIA-ME.md`).

## Tempo livre

Sem tarefa concreta, o Maestro deixa a equipe mais inteligente: lições, testes, método, cortar repetido, medir o gasto (`pedidos/PLANO.md`, "Tempo livre").

## Prompt sem papel

Geral no Opus (pessoal: `ajudante`). Tipo que volta em 2 ou 3 fichas vira proposta de papel novo ([`CONSELHO.md`](../CONSELHO.md), seção 6); papel parado, proposta de juntar.

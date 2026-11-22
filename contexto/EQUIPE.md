# A equipe: quem faz o quê e o que cada um acrescenta

> Dono, 22/11/2026: cada agente sabe a sua função e, a cada prompt, o que acrescentar para o resultado que ele quer; tudo resumido junto; um dia, ajuda em qualquer coisa, gastando o mínimo de token e tempo. Cada agente: `.claude/agents/<nome>.md` e `contexto/<nome>.md`. Modelos e ficha: [`pedidos/LEIA-ME.md`](../pedidos/LEIA-ME.md).

## A cada prompt

1. O Opus abre a ficha e chama **só** quem tem a ver (tabela). Tarefa de uma linha, ele faz.
2. Na ficha, em "Quem executa", uma linha por agente: o que ele acrescenta.
3. O agente lê o quadro, o seu contexto e a ficha; devolve o que não é dele dizendo de quem é. Agente não chama agente.
4. O Opus junta, confere e responde, com o Maestro primeiro.

## Os papéis

| Agente (modelo) | Faz | Acrescenta a cada prompt |
|---|---|---|
| Maestro, MinoAI Frontier | Preside; edita vídeo e gera imagem | Para, comenta, manda o Pix? Com a fonte |
| `redator` (Opus) | Texto público | O atributo que faz o Marcos pagar |
| `estrategista` (Opus) | Oferta, preço, ângulo | Efeito no custo por venda; teste mais barato |
| `arquiteto` (Opus) | Plantas, verdade técnica | Validador e o que o profissional confere |
| `designer` (Opus) | Imagem parada | Genérico? Bate com a planta? |
| `editor-video` (Opus) | O que se move | Segura os 3 primeiros segundos? |
| `pesquisador` (Sonnet) | Acha a fonte | Achado, fonte, data, o que não confirmou |
| `revisor-de-risco` (Opus, veto) | Honestidade e lei | Promete o que não cumpre? A correção |
| `supervisor` (Fable) | Socorro, auditoria | A causa e o primeiro passo |
| `ajudante` (Haiku) | Pessoal do dono | O resultado, curto |

## Fronteiras

- Imagem parada: Designer. O que se move: Editor. Geração pela MinoAI (OpenArt), com o "sim" do dono.
- Pesquisa: o `pesquisador` acha; conclui o Arquiteto (norma, planta), o Estrategista (mercado, preço) ou um geral no Opus.
- Peça pública: Redator, Arquiteto e Revisor. Preço, título, gasto e publicação: o dono.

## Economia (dono, 22/11)

- Chamar o menor número de agentes; o modelo mais barato que dá a qualidade da peça.
- Ler o resumo, não o documento; passar a ficha, não a conversa.
- O `CLAUDE.md` já chega a todo agente: ninguém abre de novo. O `ULTIMO.md` só quando a tarefa continua a anterior.

## Prompt sem papel

Geral no Opus (pessoal: `ajudante`). Tipo que volta em 2 ou 3 fichas vira proposta de papel novo ao dono ([`CONSELHO.md`](../CONSELHO.md), seção 6); papel parado, proposta de juntar.

# Fluxos fixos: como usar

> Pedido do dono, 26/11/2026: "YESSS, thats exactly what im looking for but a version ultra max" (ficha `2026-11-26-0721`; plano em `pedidos/anexos/plano-fluxos-2026-11-26.md`; mapa das conferências em `pedidos/anexos/mapa-conferencias-2026-11-26.md`).

## A ideia

Tudo é conferido, mas pela conferência mais barata que pega o erro: **programa primeiro** (`ferramentas/fluxo.py`, zero juízo), depois o **autor confere a própria lista**, depois **um agente por ângulo**, só onde precisa de juízo, e no fim a **Vera, uma vez**, com a peça montada. No máximo 2 voltas de conserto; depois disso, a peça vai ao dono. Toda rodada grava o gasto e os achados, e **as lições entram sozinhas** no `contexto/<papel>.md` de quem errou (no máximo 3 por autor e por rodada; as outras ficam no registro).

## Os 5 fluxos (`.claude/workflows/`)

| Fluxo | Quando | args |
|---|---|---|
| `texto-publico` | anúncio, legenda, WhatsApp, texto de página | `{arquivo, autor?, pedido, ficha?, fonte_diretor?}` |
| `pagina-ebook` | página do e-book na prévia (nunca `ebook/saida/`) | `{pagina, previa, fonte, autor?, opcoes?, pedido, ficha?}` |
| `planta` | rascunho de planta até "pronto para aplicar" | `{rascunho, casa, objetivo, variante?, ficha?}` |
| `decisao` | júri (`CONSELHO.md`, 5b): só o que custa dinheiro, vai ao público ou não se desfaz | `{proposta, pergunta, motivo, autor?, rodizio?, ficha?, calibracao?}` |
| `prova-de-entrada` | a cada 3 rodadas de júri, ou para medir um papel | `{papeis, tag, n_casos?, n_problemas?}` |

Rodar: `Workflow({name: "texto-publico", args: {...}})`. Numa conversa aberta antes de o fluxo existir, use `Workflow({scriptPath: "<raiz>/.claude/workflows/texto-publico.js", args: {...}})`.

## O que fica gravado

- `RODADAS.md`: uma linha por rodada (resultado, voltas, tokens de saída, achados, lições). O detalhe fica em `rodadas/`.
- `licoes-colhidas.json`: o que já virou lição. Se o mesmo erro volta, ele não vira lição de novo: vai para `pedidos/provas/voltam.json` e entra na próxima prova, com outras palavras.
- `pedidos/provas/`: o nível de cada papel (`NIVEIS.json`) e cada prova, com o gabarito revelado depois da nota. Quem passa (acha tudo, sem alarme falso) sobe de nível, e a próxima prova fica mais difícil. Se todos os papéis deixam passar o mesmo item, a Olga arbitra antes da nota (o gabarito pode estar errado).
- `python3 ferramentas/fluxo.py relatorio`: gasto por fluxo e por conferidor. Conferidor de juízo com 5 rodadas sem achado próprio é candidato a corte.

## Quem confere os fluxos

O `checar.py` roda `fluxo.py testar` (cada conferência pega o erro plantado), `fluxos-ensaio.cjs` (cada fluxo do começo ao fim com agentes de mentira) e confere que toda rodada gravada tem a forma certa. Rodada de calibração (`calibracao: true`) não vira lição: o erro foi plantado.

---
name: redacao-que-vende
description: Método do Redator do X1-Plantas para escrever qualquer texto de venda (anúncio, legenda, página do e-book, WhatsApp, capa) partindo dos atributos que fazem o comprador pagar. Use sempre que for escrever ou revisar texto para o público.
---

# Redação que vende

Siga o método do agente `redator` (`.claude/agents/redator.md`): banco de atributos em `ebook/vendas/atributos-que-vendem.md`, escada característica → vantagem → benefício → dinheiro ou alívio, nota de desejo, prova e exclusividade, atributo campeão na primeira linha, entrega no formato com "o que medir" e a variação para teste. Termine passando a peça pelo `revisor-de-risco`.

## Neste projeto (X1-Plantas)

Antes de usar esta skill aqui, alcance o projeto:
- Leia `CLAUDE.md` (regras que não mudam) e `CONTEXTO.md` (o resumo: o que nunca muda e o que está em aberto) e o último resumo, `contexto/entregas/ULTIMO.md`.
- Responda e escreva em português do Brasil, com palavras simples.
- O objetivo é a alegria do comprador, que vira venda. Qualidade vem antes de economia.
- Uma coisa por vez, na ordem e-book → animações → vídeo.
- Ela é membro do Conselho (`CONSELHO.md`): a decisão de usá-la segue as regras de lá, e o Revisor de risco tem veto em tudo que toca honestidade e lei.
- Nunca corte nem enfraqueça os avisos de "planta de referência", que dizem que o projeto é do profissional habilitado. Também não corte nenhum texto que o Revisor exigiu.
- Antes de entregar, rode `python3 ferramentas/checar.py` e `python3 ferramentas/atualizar-painel.py`. Acrescente uma linha no fim de `CONTEXTO-HISTORICO.md` (não no `CONTEXTO.md`, que é resumo com limite de tamanho), faça o commit e o push na branch `planta-de-casas-anuncio`.
- Tudo o que esta skill escreve para o público passa pelo Revisor de risco antes de sair.
- **Prompt de entrada:** parta de `ebook/vendas/atributos-que-vendem.md` e dos números do validador, arredondados como no PDF (0,5 sobe). A lista de frases vetadas está no agente `redator`. Entregue no formato da skill e passe pelo Revisor antes de sair.

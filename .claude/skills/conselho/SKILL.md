---
name: conselho
description: Reúne o Conselho do X1-Plantas (Maestro, Redator, Estrategista, Arquiteto, Revisor de risco, Designer, Pesquisador, Editor de vídeo) para decidir quais skills, agentes e ferramentas usar numa tarefa, e depois executa só o que foi aprovado. Use no começo de qualquer entrega que vai ao público ou que custa dinheiro, ou quando o dono digitar /conselho.
---

# Conselho

Regras completas: `CONSELHO.md` na raiz do projeto. Siga estes passos.

1. **Enquadre a tarefa** em 3 linhas: o que é, para quem, qual alavanca de venda ela mexe (ver `PAINEL.md`, seção 4).
2. **Escolha o modo.** Vai ao público ou custa dinheiro → completo. Senão → de bolso.
3. **Chame os membros que importam** (tabela em `CONSELHO.md`, seção 2). Revisor de risco entra sempre que algo vai ao público.
   - De bolso: escreva você mesmo uma linha por membro, no formato da seção 3.
   - Completo: abra os agentes de `.claude/agents/` em paralelo, cada um com a tarefa e a pergunta "qual skill ou ferramenta você propõe, e vale a pena?". Peça a resposta no formato de uma linha.
4. **Mostre a mesa** ao dono: as linhas de cada membro e a decisão pela regra da seção 4 (maioria, sem veto, empate pelo maior efeito em venda, depois o mais barato).
5. **Itens reservados ao dono** (preço, título, gasto, publicação, contratação, ferramenta paga): pare e peça o "sim".
6. **Execute** só o aprovado, na ordem que o Maestro definir. Depois da execução, o Revisor confere a peça final.
7. **Registre** em `CONSELHO.md`, seção 7 (data, tarefa, votos, decisão, o que medir), rode `python3 ferramentas/atualizar-painel.py` e faça commit.

## Neste projeto (X1-Plantas)

Antes de usar esta skill aqui, alcance o projeto:
- Leia `CLAUDE.md` (regras que não mudam) e `CONTEXTO.md` (tudo o que o dono pediu e o que está em aberto).
- Responda e escreva em português do Brasil, com palavras simples.
- O objetivo é a alegria do comprador, que vira venda. Qualidade vem antes de economia.
- Uma coisa por vez, na ordem e-book → animações → vídeo.
- Ela é membro do Conselho (`CONSELHO.md`): a decisão de usá-la segue as regras de lá, e o Revisor de risco tem veto em tudo que toca honestidade e lei.
- Nunca corte nem enfraqueça os avisos de "planta de referência", que dizem que o projeto é do profissional habilitado. Também não corte nenhum texto que o Revisor exigiu.
- Antes de entregar, rode `python3 ferramentas/checar.py` e `python3 ferramentas/atualizar-painel.py`. Acrescente uma linha no `CONTEXTO.md`, faça o commit e o push na branch `planta-de-casas-anuncio`.
- Toda skill ou agente novo passa pelo roteiro de entrada da seção 6 do `CONSELHO.md` antes do primeiro uso.

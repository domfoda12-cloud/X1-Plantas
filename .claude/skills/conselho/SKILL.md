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
7. **Registre** em `CONSELHO.md`, seção 6 (data, tarefa, votos, decisão, o que medir), rode `python3 ferramentas/atualizar-painel.py` e faça commit.

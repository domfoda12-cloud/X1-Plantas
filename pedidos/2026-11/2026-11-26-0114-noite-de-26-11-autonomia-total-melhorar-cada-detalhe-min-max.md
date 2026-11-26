# noite de 26/11: autonomia total, melhorar cada detalhe (min-maxing)

**Estado:** aberta

**Prompt (palavra por palavra):** Im going to sleep now, for this night i want you to go crazy, dont ask me for permission for ANYTHING, only rules: dont fuck me up and dont spend my money
This doesnt apply only for the ads and ebook, i still want to decide on the final but feel free to keep tweaking it and improving
Always remember, I M P R O V E M E N T, get every single detail, every single component that makes something and make it better, thats how you masterize things. A term for it: Min maxing except we can max everything.

**O que ele pediu, parte por parte:** 1) Esta noite, não pedir permissão para nada. 2) Duas regras: não prejudicar ele e não gastar o dinheiro dele. 3) Exceção: anúncios e o final do e-book ele decide; pode continuar ajustando e melhorando. 4) Melhorar cada detalhe e cada componente ("min maxing, except we can max everything").

**Por que ele pediu, ou o que quer descobrir:** Vai dormir e quer acordar com tudo melhor, sem ser parado por perguntas.

**Objetivo dele:** Maestria: cada peça melhorada parte por parte.

**Ligação com as ideias gerais do projeto:** Qualidade em primeiro lugar; e-book primeiro; decisão final do produto e do anúncio é dele.

**Perguntas que me fiz:** O que é "não me prejudicar"? Escrevi a lista em `pedidos/anexos/noite-2026-11-26-fila.md`: nada público, nada enviado, nada apagado sem volta, nada pago, nenhuma trava contornada. O CLAUDE.md pode mudar? Pode, com parcimônia e registro.

**Pronto quando:** De manhã existe o resumo do que mudou, com como desfazer; `ebook/saida/` intacto; nenhum gasto.

**Suposições (o dono não disse):** A lista do que "dont fuck me up" proíbe é leitura minha.

**Quem executa:** Maestro e a equipe, em fluxos.

**Conferência:** checar.py verde a cada salvar; git log; o resumo da manhã.

**Resultado:** (a preencher)

**O que aprendi:** (a preencher)

**Papéis afetados:** todos

**Segunda olhada (item 11, mover arquivos de `contexto/`):** primeira ideia: mover `contexto/dono/` inteiro e o `REGISTRO.md` para uma pasta nova `historico/` na raiz. Alternativa: deixar em `contexto/dono/` o que ainda é lido como contexto vivo (`IDEIAS-GERAIS.md`, `TEXTOS-DESATUALIZADOS.md`, citados por 7 papéis) e pôr só o histórico em `pedidos/historico/`, junto dos pedidos do dono, sem pasta nova para registrar. O que provaria o erro: link quebrado, papel que lê o arquivo movido ao começar, programa que procura o caminho antigo. A conferência: `checar.py` (links entre documentos) verde; nenhum `.claude/agents/` cita os arquivos movidos; só o `resumos.py` citava o caminho e foi ajustado; `REGISTRO.md` continua no lugar (o `pedido.py` e o `CLAUDE.md` apontam para ele). Ficou a alternativa.

**Segunda olhada (item 3, lado do sol):** primeira ideia: o Nilo errou a convenção (o desenho poderia ser visto de dentro da casa). Alternativa: a tabela `ORIENTACAO` está espelhada. O que provaria o erro dele: a planta desenhada com a rua no alto, ou o x crescendo para a esquerda. A conferência: `svg_lote` e a planta põem a rua embaixo (`y = LD + .15`) e o x cresce para a direita; com a frente ao norte embaixo, a direita do desenho é o oeste; as 4 linhas da tabela estavam trocadas. Refiz a conta: C01 passa de "melhor norte" (15,5) a "melhor sul" (11,5, pior leste); E03 de norte a sul (11,4, pior norte); F01 continua sul. Ficou o conserto, com prova no `checar.py`.


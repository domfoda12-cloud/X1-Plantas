# Fluxos fixos, ultra max (plano, 26/11/2026)

> Ficha `pedidos/2026-11/2026-11-26-0721-fluxos-fixos-ultra-max-e-licoes-automaticas.md`. Dono, 26/11: "YESSS, thats exactly what im looking for but a version ultra max"; lições "Automatically"; "most of the things id like for you to have the free will to do"; gate test "making the questions harder each time, testing the knowledge of the agents and challenging them"; "we're missing checks in a bunch of places"; "In theory everything should always be getting checked but idk how the usage would be".

## Ideia central

Tudo é conferido, mas pela conferência mais barata que pega o erro:
1. **Programa primeiro** (zero token): tudo o que se confere por regra (medida, número citado contra o arquivo, frase vetada, campo faltando, página cortada, link quebrado, arquivo em pasta ignorada, hora contra `date -u`) vira conferência no `checar.py` ou num conferidor do fluxo.
2. **Agente só onde precisa de juízo**, uma leitura, no modelo que basta (mecânico: Haiku; juízo: Opus; veto: Vera no Fable, uma vez, peça montada).
3. **Medir:** cada rodada grava o gasto que a ferramenta devolve (`budget.spent()`) e os achados de cada conferidor; conferidor que nunca acha nada sozinho é cortado.

## O que se constrói (branch `sistema/fluxos`, depois `main`)

1. **Mapa das conferências que faltam:** cada passo de cada trabalho (texto, página, planta, vídeo, Canteiro, salvar, passagem), o que pode dar errado, quem confere hoje, quem deveria (programa ou agente). Fonte: lições em `pedidos/LICOES.md`, auditorias, vetos da Vera.
2. **Conferências por programa** para tudo o que o mapa mostrar que é regra.
3. **Fluxos salvos** em `.claude/workflows/`: `texto-publico`, `pagina-ebook`, `planta`, `decisao` (regras do júri de 25/11 + conferência de fatos por quem não votou + as 3 perguntas de entrada). Cada passo entrega um **passe** com forma fixa (feito, suposições, faltando, arquivos, perguntas ao dono). Autor confere a própria lista antes do revisor. No máximo 2 voltas de conserto, depois vai ao dono.
4. **Colheita de lições** no fim de cada fluxo: achado repetido vira lição no arquivo do autor, sozinha (`pedido.py licao`); arquivo cheio: consolida as antigas, não descarta. Vai ao resumo da manhã.
5. **Prova de entrada que fica mais difícil** (dono): banco de casos com gabarito fora do repositório, em níveis; cada agente responde do seu papel; acertou o nível, o próximo fica mais difícil; errou, vira lição e o caso volta na próxima. Casos tirados dos erros reais (lições). Começa pelas 3 perguntas do júri (10 casos, 5 com problema plantado).
6. **Programa que recusa rodada de júri incompleta** (régua, arquivo e linha, 2 defeitos, 5 fatos, gasto).
7. `checar.py` confere que os fluxos existem, estão no `MAPA-DO-SISTEMA.md` e no `ECOSSISTEMA.md`, e que cada rodada deixou registro.

## Ordem

Mapa → conferências por programa → fluxos → colheita → prova que endurece → conferidor do júri. Cada fluxo roda uma vez sobre peça real (funil do sócio, uma página, uma planta, um pedido de júri de teste). Olga audita no fim. Nada pago, nada publicado, nada em `ebook/saida/`.

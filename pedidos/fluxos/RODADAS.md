# Rodadas dos fluxos fixos

> Gerado por `python3 ferramentas/fluxo.py` (`registrar` e `gasto`) a partir de `rodadas/`. Não edite à mão. Tokens: os de saída que o `budget.spent()` devolve e o total de subagentes que a ferramenta Workflow devolve ao terminar (o Paydon anota com `fluxo.py gasto`; sem ele, o `checar.py` fica vermelho).

| Quando (UTC) | Fluxo | Peça | Resultado | Voltas | Tokens de saída | Tokens da ferramenta | Achados | Lições novas | Erro que voltou |
|---|---|---|---|---|---|---|---|---|---|
| 26/11 08:04 | texto-publico | `pedidos/anexos/funil-textos-rascunho-2026-11-26.md` | vai ao dono (2 voltas gastas; condições da Vera em aberto) | 2 | 108710 | 929300 | 7 | 7 | 0 |
| 26/11 08:31 | pagina-ebook | `ebook/gerador/paginas.py (dicionário COMODO e os textos cômodo a cômodo da C01) e ebook/ge` | aprovada na prévia, com as condições da Vera | 2 | 73502 | 819136 | 7 | 3 | 0 |
| 26/11 08:40 | planta | `ebook/plantas/rascunhos/C01V.py` | pronto para aplicar (aplicar é outro passo: plantas.py validar e checar.py) | 1 | 32848 | 510641 | 1 | 1 | 0 |
| 26/11 08:53 | decisao | `pedidos/anexos/juri-teste-fluxo-2026-11-26.md` | calibração: os 3 erros plantados pegos pelos 3 jurados na 1ª rodada (notas 4, 4 e 2); não vai ao dono | 2 | 124142 | 1806457 | 6 | 0 | 0 |

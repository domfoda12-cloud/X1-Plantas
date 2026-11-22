# Resumo: Pedidos do dono

> Como cada prompt vira trabalho: quem interpreta, quem executa e as fichas dos pedidos. **Leia este resumo primeiro**; abra um documento inteiro só quando a tarefa pedir. Índice geral: [`INDICE.md`](../INDICE.md). Quem lê: todos.

## O essencial

<!-- essencial: escrito à mão, o gerador não apaga -->
- O Fable roda o sistema e é o supervisor principal: divide, confere e responde; nas partes importantes pode fazer ele mesmo (`LEIA-ME.md`).
- Todo prompt do dono é gravado sozinho em `pedidos/entrada/` (fora do git) pelo gancho, que também devolve o lembrete da regra (`LEIA-ME.md`).
- Trabalho novo: `python3 ferramentas/pedido.py nova "assunto"` cria a ficha com o prompt copiado; recado de pedido aberto: `pedido.py recado <ficha>`; fechar: `pedido.py fechar <ficha> "o que virou"`, que também escreve o histórico (`LEIA-ME.md`).
- A ficha responde: por que ele pediu, qual o objetivo e qual a ligação com `contexto/dono/IDEIAS-GERAIS.md`, antes de qualquer delegação (`LEIA-ME.md`).
- Modelos: Opus executa o trabalho do projeto; pesquisa em dois passos (Sonnet busca, Opus confere e conclui); Haiku (`ajudante`) faz a tarefa simples e pessoal do dono (`LEIA-ME.md`).
- Todo pedido a agente leva o pacote do executor: ficha, o que ler, o que já está decidido, pronto quando e o que devolver (`LEIA-ME.md`).
- Relatório de agente é afirmação, não prova: o Fable confere e escreve em "Conferência do Fable" (`LEIA-ME.md`).
- O que está aberto: `FILA.md`, gerada (`FILA.md`).
<!-- /essencial -->

## Os 2 documentos

### [Auditorias do Supervisor (Fable)](AUDITORIAS.md)

Uma linha por auditoria, escrita pelo agente `supervisor` (regras em `LEIA-ME.md`). A cada 3 fichas fechadas, `ferramentas/pedido.py` avisa que é hora da próxima.

Tamanho: 46 palavras.

### [Pedidos do dono: como cada prompt vira trabalho](LEIA-ME.md)

Regra do dono (22/11/2026). Todo prompt dele é guardado, interpretado por um modelo e executado por outro, para o modelo caro pensar e o barato fazer o que é simples. Fila de pedidos: `FILA.md`.

Seções: Quem manda no sistema; Perguntar sempre (dono, 22/11/2026); Quem faz o quê; O pacote do executor; A ficha; O que a análise do sistema mudou (22/11/2026); Limites honestos.

Tamanho: 1729 palavras.

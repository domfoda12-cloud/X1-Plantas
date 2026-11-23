# Resumo: Pedidos do dono

> Como cada prompt vira trabalho: quem interpreta, quem executa e as fichas dos pedidos. **Leia este resumo primeiro**; abra um documento inteiro só quando a tarefa pedir. Índice geral: [`INDICE.md`](../INDICE.md). Quem lê: todos.

## O essencial

<!-- essencial: escrito à mão, o gerador não apaga -->
- O Opus responde, divide, executa e confere; o Fable (`supervisor`) socorre quando ele trava ou erra e audita a cada 3 fichas (`LEIA-ME.md`).
- Todo prompt do dono é gravado sozinho em `pedidos/entrada/` (fora do git) pelo gancho, que também devolve o lembrete da regra (`LEIA-ME.md`).
- Trabalho novo: `python3 ferramentas/pedido.py nova "assunto"` cria a ficha com o prompt copiado; recado de pedido aberto: `pedido.py recado <ficha>`; fechar: `pedido.py fechar <ficha> "o que virou"`, que também escreve o histórico (`LEIA-ME.md`).
- A ficha responde: por que ele pediu, qual o objetivo e qual a ligação com `contexto/dono/IDEIAS-GERAIS.md`, antes de qualquer delegação (`LEIA-ME.md`).
- Modelos: Opus executa o trabalho do projeto; pesquisa em dois passos (Sonnet busca, Opus confere e conclui); Haiku (`ajudante`) faz a tarefa simples e pessoal do dono (`LEIA-ME.md`).
- Todo pedido a agente leva o pacote do executor: ficha, o que ler, o que já está decidido, pronto quando e o que devolver (`LEIA-ME.md`).
- Relatório de agente é afirmação, não prova: quem conduz confere e escreve em "Conferência" (`LEIA-ME.md`).
- O que está aberto: `FILA.md`, gerada (`FILA.md`).
<!-- /essencial -->

## Os 5 documentos

### [Auditorias do Supervisor (Fable)](AUDITORIAS.md)

Uma linha por auditoria, escrita pelo agente `supervisor` (regras em `LEIA-ME.md`). A cada 3 fichas fechadas, `ferramentas/pedido.py` avisa que é hora da próxima.

Tamanho: 1979 palavras.

### [Pedidos do dono: como cada prompt vira trabalho](LEIA-ME.md)

Regra do dono (22/11/2026). Todo prompt dele é guardado, interpretado por um modelo e executado por outro, para o modelo caro pensar e o barato fazer o que é simples. Fila de pedidos: `FILA.md`.

Seções: Quem manda no sistema; Pensar antes de fazer (dono, 22/11/2026); Perguntar sempre (dono, 22/11/2026); O plano de tudo; Plano vetado antes de fazer (dono, 22/11/2026); Erro de sintonia entre agentes (dono, 22/11/2026); Buscar o que o dono já disse (22/11/2026); Faltou informação do dono? Sugira, não espere (dono, 22/11/2026); Consertar de vez (dono, 22/11/2026: "não só conserte, remende"); O caminho de um prompt; Quem faz o quê; O pacote do executor; A ficha; O que a análise do sistema mudou (22/11/2026); ….

Tamanho: 2810 palavras.

### [Plano de trabalho: o que a equipe faz, em que ordem, e para quê](PLANO.md)

Pedido do dono (22/11/2026): "sempre dê um objetivo à equipe; um plano passo a passo, separado em tarefas grandes e pequenas, entre os agentes". Quem mantém: o Maestro (a conversa principal). Toda tarefa daqui vira ou já é ficha em `pedidos/`; ao terminar uma, marque feito e atualize o "Agora" do…

Seções: O objetivo da equipe; Fase 1 · Organizar a base (ficha `1529-organizar-os-arquivos`); Fase 2 · O plano mestre da equipe (ficha `1944-plano-mestre`); Fase 3 · E-book: as casas refeitas (frente atual); Fase 4 · Animações e imagens (abre só quando a fase 3 fechar); Fase 5 · Vídeo; Fase 6 · Vender e medir (o objetivo é o Pix); Tempo livre: deixar a equipe mais inteligente (dono, 22/11/2026); Sempre, em toda fase.

Tamanho: 1920 palavras.

### [Rascunho: e-mail ao autor do cass (para o dono mandar)](anexos/email-autor-cass.md)

Ficha `2026-11-22-2237-busca-nas-conversas-propria-opcao-c-e-e-mail-ao-autor-do-cas.md`. O dono troca os campos entre colchetes e manda do e-mail dele, em particular (não como issue pública). Esta sessão não manda e-mail. O endereço do autor não está aqui: pegue no perfil dele no GitHub…

Tamanho: 499 palavras.

### [Proposta de integração das 5 adições do dono (versão 1, 23/11/2026)](anexos/integracao-novos-v1.md)

Para o júri criticar, rodada após rodada (pedido do dono: "make the jury criticise it a lot of times, and improve at each time"). Cada rodada gera uma versão nova. Contexto: o próprio júri, no veredito de 23/11 (ficha `2026-11-23-0156`), disse que o sistema já cresceu demais e que falta vender; o…

Seções: O que cada adição é, e o que propomos; Mudanças concretas da v1; O que não muda.

Tamanho: 562 palavras.

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

## Os 12 documentos

### [Auditorias do Supervisor (Fable)](AUDITORIAS.md)

Uma linha por auditoria, escrita pelo agente `supervisor` (regras em `LEIA-ME.md`). A cada 3 fichas fechadas, `ferramentas/pedido.py` avisa que é hora da próxima.

Tamanho: 1979 palavras.

### [Pedidos do dono: como cada prompt vira trabalho](LEIA-ME.md)

Regra do dono (22/11/2026). Todo prompt dele é guardado, interpretado por um modelo e executado por outro, para o modelo caro pensar e o barato fazer o que é simples. Fila de pedidos: `FILA.md`.

Seções: Quem manda no sistema; Pensar antes de fazer (dono, 22/11/2026); Perguntar sempre (dono, 22/11/2026); O plano de tudo; Plano vetado antes de fazer (dono, 22/11/2026); Erro de sintonia entre agentes (dono, 22/11/2026); Ferramenta ou agente novo (dono, 23/11/2026); Buscar o que o dono já disse (22/11/2026); Faltou informação do dono? Sugira, não espere (dono, 22/11/2026); Consertar de vez (dono, 22/11/2026: "não só conserte, remende"); O caminho de um prompt; Quem faz o quê; O pacote do executor; A ficha; ….

Tamanho: 2870 palavras.

### [Plano de trabalho: o que a equipe faz, em que ordem, e para quê](PLANO.md)

Pedido do dono (22/11/2026): "sempre dê um objetivo à equipe; um plano passo a passo, separado em tarefas grandes e pequenas, entre os agentes". Quem mantém: o Maestro (a conversa principal). Toda tarefa daqui vira ou já é ficha em `pedidos/`; ao terminar uma, marque feito e atualize o "Agora" do…

Seções: O objetivo da equipe; Fase 1 · Organizar a base (ficha `1529-organizar-os-arquivos`); Fase 2 · O plano mestre da equipe (ficha `1944-plano-mestre`); Fase 3 · E-book: as casas refeitas (frente atual); Fase 4 · Animações e imagens (abre só quando a fase 3 fechar); Fase 5 · Vídeo; Fase 6 · Vender e medir (o objetivo é o Pix); Tempo livre: deixar a equipe mais inteligente (dono, 22/11/2026); Sempre, em toda fase.

Tamanho: 1920 palavras.

### [Plano de integração do everything-claude-code (vetado, 23/11/2026)](anexos/ecc-plano.md)

Saída do workflow wkfowrx4b (5 leitores, Revisor e compatibilidade por grupo, plano, Fable). Ficha `0209`. Texto dos agentes, sem edição; as correções do Fable valem sobre o plano.

Seções: Entra (adaptado); Não entra; Ganchos; Passos; Testes; Veto do Fable: SIM, SE; Não conferido.

Tamanho: 8430 palavras.

### [Rascunho: e-mail ao autor do cass (para o dono mandar)](anexos/email-autor-cass.md)

Ficha `2026-11-22-2237-busca-nas-conversas-propria-opcao-c-e-e-mail-ao-autor-do-cas.md`. O dono troca os campos entre colchetes e manda do e-mail dele, em particular (não como issue pública). Esta sessão não manda e-mail. O endereço do autor não está aqui: pegue no perfil dele no GitHub…

Tamanho: 499 palavras.

### [Proposta de integração das 5 adições do dono (versão 1, 23/11/2026)](anexos/integracao-novos-v1.md)

Para o júri criticar, rodada após rodada (pedido do dono: "make the jury criticise it a lot of times, and improve at each time"). Cada rodada gera uma versão nova. Contexto: o próprio júri, no veredito de 23/11 (ficha `2026-11-23-0156`), disse que o sistema já cresceu demais e que falta vender; o…

Seções: O que cada adição é, e o que propomos; Mudanças concretas da v1; O que não muda.

Tamanho: 562 palavras.

### [Proposta de integração das 5 adições do dono (versão 2, 23/11/2026)](anexos/integracao-novos-v2.md)

Rodada 1 do júri sobre a v1: notas 4, 5 e 5 (e a do Fable a chegar). O que mudou da v1 para a v2, em uma linha cada: - Conflito explicitado: o veredito de 23/11 mandou parar de criar sistema por 7 dias; o dono, depois, pediu estas 5 adições. Regra da v2: o que o dono pediu pelo nome entra ou vira…

Seções: As cinco, ligadas como num cérebro; Cada adição, com medida, custo e saída; Perguntas ao dono (uma linha cada, com a recomendação); O que não muda.

Tamanho: 771 palavras.

### [Proposta de integração das 5 adições do dono (versão 3, 23/11/2026)](anexos/integracao-novos-v3.md)

O que mudou da v2 para a v3 (escrita com as 8 críticas do júri; médias: rodada 1, 4,75; rodada 2, 6,1) - Regra nova sua (02:13 e 02:14): "não desista porque quebraria, faça funcionar sem quebrar", e apresentar direito cada agente novo. Cada adição ganhou uma parte que entra adaptada; fica de fora…

Seções: O cérebro: por onde um pedido passa; Cada adição; Perguntas para você; Ordem, quem faz e quando o júri para.

Tamanho: 1421 palavras.

### [Proposta de integração das 6 adições do dono (5 do pedido e a sexta, da ficha `0209`): versão 4, 23/11/2026](anexos/integracao-novos-v4.md)

O que mudou da v3 para a v4 (escrita com as críticas das rodadas 1, 2 e 3) - Página de decisões em dois blocos: primeiro o que destrava o Pix; depois as ferramentas, com "aceito todas as recomendações". - Ordem corrigida: nada que depende do seu sim acontece antes dele. - Fatos refeitos com o…

Seções: O cérebro: por onde um pedido passa; Cada adição; Perguntas para você; Ordem, quem faz e quando o júri para.

Tamanho: 2579 palavras.

### [Integração das 6 adições do dono (5 do pedido e a sexta, da ficha `0209`): versão 5, 23/11/2026](anexos/integracao-novos-v5.md)

Escrita com as críticas das rodadas 1 e 2 (por extenso), as notas da rodada 3 (estão na ficha `0156`: Haiku 6, Sonnet 7, Opus 6,5; média 6,5; presidiu o Fable) e a síntese do presidente da rodada 4. As críticas por extenso das rodadas 3 e 4 não estão no repositório. O que mudou da v4 para a v5 - A…

Seções: O cérebro: por onde um pedido passa; Página de decisões, versão 1; Cada adição (para o júri conferir); As outras opções (para quem disser "quero ver"); Ordem, quem faz e quando o júri para.

Tamanho: 2911 palavras.

### [Integração das 6 adições: versão 6, curta (23/11/2026)](anexos/integracao-novos-v6.md)

O que mudou da v5 para a v6

Seções: 1. O estado verdadeiro; 2. Página de decisões (pode responder só esta); 3. Uma linha por ferramenta.

Tamanho: 880 palavras.

### [Júri: síntese dos presidentes, rodadas 3 a 5 (23/11/2026)](anexos/juri-rodadas-3-a-5.md)

Saída do laço do júri (ficha `0156`), sem edição. Base da v6 curta, que é o último passo do júri.

Seções: v3: média 6.5 (presidente: fable); v4: média 6.3 (presidente: haiku); v5: média 6 (presidente: sonnet).

Tamanho: 10600 palavras.

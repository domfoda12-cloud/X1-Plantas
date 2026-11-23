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

## Os 28 documentos

### [Auditorias do Supervisor (Fable)](AUDITORIAS.md)

Uma linha por auditoria, escrita pelo agente `supervisor` (regras em `LEIA-ME.md`). A cada 3 fichas fechadas, `ferramentas/pedido.py` avisa que é hora da próxima.

Tamanho: 1979 palavras.

### [Pedidos do dono: como cada prompt vira trabalho](LEIA-ME.md)

Regra do dono (22/11/2026). Todo prompt dele é guardado, interpretado por um modelo e executado por outro, para o modelo caro pensar e o barato fazer o que é simples. Fila de pedidos: `FILA.md`.

Seções: Quem manda no sistema; Pensar antes de fazer (dono, 22/11/2026); Perguntar sempre (dono, 22/11/2026); O plano de tudo; Plano vetado antes de fazer (dono, 22/11/2026); Erro de sintonia entre agentes (dono, 22/11/2026); Ferramenta ou agente novo (dono, 23/11/2026); Buscar o que o dono já disse (22/11/2026); Faltou informação do dono? Sugira, não espere (dono, 22/11/2026); Consertar de vez (dono, 22/11/2026: "não só conserte, remende"); O caminho de um prompt; Quem faz o quê; O pacote do executor; A ficha; ….

Tamanho: 3003 palavras.

### [Lições da equipe (registro único, só acréscimo)](LICOES.md)

Gravado por `python3 ferramentas/pedido.py licao` e pelo `fechar`. Não edite à mão: a lição também está no "Lições" do `contexto/<papel>.md`.

Tamanho: 923 palavras.

### [Plano de trabalho: o que a equipe faz, em que ordem, e para quê](PLANO.md)

Pedido do dono (22/11/2026): "sempre dê um objetivo à equipe; um plano passo a passo, separado em tarefas grandes e pequenas, entre os agentes". Quem mantém: o Maestro (a conversa principal). Toda tarefa daqui vira ou já é ficha em `pedidos/`; ao terminar uma, marque feito e atualize o "Agora" do…

Seções: O objetivo da equipe; Fase 1 · Organizar a base (ficha `1529-organizar-os-arquivos`); Fase 2 · O plano mestre da equipe (ficha `1944-plano-mestre`); Fase 3 · E-book: as casas refeitas (frente atual); Fase 4 · Animações e imagens (abre só quando a fase 3 fechar); Fase 5 · Vídeo; Fase 6 · Vender e medir (o objetivo é o Pix); Tempo livre: deixar a equipe mais inteligente (dono, 22/11/2026); Sempre, em toda fase.

Tamanho: 1921 palavras.

### [Provas da equipe](PROVAS.md)

Fila da noite (ficha `2026-11-23-0144`), tarefa A0: a régua que diz se a equipe aprende. Planos com erro plantado e gabarito guardado fora do repositório até a nota; os agentes vetam sem ver o gabarito; o Fable dá a nota. Nenhuma regra muda com n menor que 5 (condição do Fable).

Seções: Prova 1, base (23/11/2026, 04:47 a 04:55 UTC); Prova 2 (23/11/2026, 14:10 a 14:40 UTC).

Tamanho: 1144 palavras.

### [A4: correções antigas do dono, conferidas (23/11/2026)](anexos/a4-correcoes-do-dono.md)

Fila da noite, tarefa A4 (ficha `2026-11-23-0144`). Três leitores (Sonnet) em `contexto/dono/PROMPTS.md`, `contexto/dono/intencoes/` e `pedidos/entrada/` + `conversas.py`; um agente juntou e conferiu o que já existia; Revisor e Fable vetaram (Fable SIM, SE, 7). Tudo nas nossas palavras. 81 achados…

Seções: Já eram lição ou regra (correções do Fable aplicadas às citações); Viraram lição (texto final, depois do veto); Tiradas pelo veto.

Tamanho: 1717 palavras.

### [O que vai de graça: 2 opções de amostra](anexos/amostra-gratis-opcoes.md)

Pedido do dono no quadro (23/11/2026): "uma amostra grátis bem impressionante do que vamos oferecer a eles, talvez um guia também". Ainda não decidido. Feito pelo Estrategista. Nenhum número abaixo foi medido: ainda não há venda.

Seções: Opção A: a Casa Compacta completa, caprichada (5 páginas); Opção B: a Casa Compacta + o guia "Seu lote cabe?" (8 a 9 páginas); O teste de preço (R$ 47 x R$ 67).

Tamanho: 913 palavras.

### [Decisões do dono, 23/11/2026 (respostas às perguntas pendentes)](anexos/decisoes-do-dono-2026-11-23.md)

Respondidas pelo dono nesta data, em 6 blocos de perguntas (ficha `pedidos/2026-11/2026-11-23-0947-testar-as-ferramentas-novas-achar-funcoes-que-faltam-na-equi.md`). As palavras entre aspas são dele. Vale até ele dizer o contrário.

Tamanho: 2443 palavras.

### [E07 e a parede na divisa: o que fazer com a parede sem janela](anexos/e07-parede-na-divisa-ideias.md)

Pedido do dono (23/11, comentário no quadro; `decisoes-do-dono-2026-11-23.md`, linha 86): "Crie uma solução criativa para o que pode ser feito ou acontecer naquele quarto/área, pode ser ideia de vídeo e/ou parte do e-book." Autor: Editor de vídeo, 23/11/2026. Rascunho de ideias: nada aqui é texto…

Seções: O que encosta na divisa (lido no rascunho, não suposto); 1. Cinco usos de verdade para a parede sem janela; 2. Duas páginas de e-book: "A parede sem janela trabalha para você"; 3. Dois roteiros de vídeo, de 15 a 25 s; Em aberto (perguntas ao dono, uma de cada vez).

Tamanho: 2124 palavras.

### [Plano de integração do everything-claude-code (vetado, 23/11/2026)](anexos/ecc-plano.md)

Saída do workflow wkfowrx4b (5 leitores, Revisor e compatibilidade por grupo, plano, Fable). Ficha `0209`. Texto dos agentes, sem edição; as correções do Fable valem sobre o plano.

Seções: Entra (adaptado); Não entra; Ganchos; Passos; Testes; Veto do Fable: SIM, SE; Não conferido.

Tamanho: 8430 palavras.

### [E-mail ao autor do cass: ENVIADO em 23/11/2026 do Gmail do dono, com o sim dele, assinado "Dominic de Lima, a solo founder"](anexos/email-autor-cass.md)

Ficha `2026-11-22-2237-busca-nas-conversas-propria-opcao-c-e-e-mail-ao-autor-do-cas.md`. O dono troca os campos entre colchetes e manda do e-mail dele, em particular (não como issue pública). Esta sessão não manda e-mail. O endereço do autor não está aqui: pegue no perfil dele no GitHub…

Tamanho: 517 palavras.

### [Perfil novo do Instagram: material para o dono escolher (rascunho)](anexos/instagram-perfil-novo.md)

Redator, 23/11/2026, noite. Pedido do dono: "Um novo" (comentário no quadro, `pedidos/anexos/decisoes-do-dono-2026-11-23.md`, linha "Instagram"): perfil novo, só do negócio. Quem cria a conta é ele; aqui fica o material para ele escolher. Rascunho: nada vai ao público antes do Revisor de risco.…

Seções: 1. Nome de usuário (@): 6 opções; 2. Bio: 3 opções (limite de 150 caracteres); 3. Nome de exibição e categoria; 4. Os 9 primeiros posts (a grade de quem abre o perfil); 5. Destaques fixos (stories): 3; 6. O que só o dono faz; Para o Revisor de risco; Perguntas ao dono (curtas).

Tamanho: 2874 palavras.

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

### [Júri: as próximas melhorias (23/11/2026, Supervisor)](anexos/juri-proximas-melhorias.md)

Pedido do dono: "continuar melhorando o júri é essencial". Ficha de origem do júri: `pedidos/2026-11/2026-11-23-0156-adicionar-o-llm-council-karpathy-e-pedir-a-opiniao-dele-sobr.md` (abaixo, "ficha 0156"). Regras em vigor: `CONSELHO.md`, seção 5b. Este documento é proposta. Nada aqui foi rodado,…

Seções: Em 7 linhas; 1. A régua (cole inteira em toda rodada); 2. Modelos de pedido, prontos para copiar; 3. As 5 próximas melhorias, em ordem de ganho; 4. Prova 3: a primeira prova do júri com erro plantado; 5. O que a pesquisa pública diz sobre júri de modelos; 6. Perguntas ao dono; 7. O que eu não conferi.

Tamanho: 5431 palavras.

### [Júri: síntese dos presidentes, rodadas 3 a 5 (23/11/2026)](anexos/juri-rodadas-3-a-5.md)

Saída do laço do júri (ficha `0156`), sem edição. Base da v6 curta, que é o último passo do júri.

Seções: v3: média 6.5 (presidente: fable); v4: média 6.3 (presidente: haiku); v5: média 6 (presidente: sonnet).

Tamanho: 10600 palavras.

### [Prova de base: 10 planos curtos para vetar (23/11/2026)](anexos/prova-A0-planos.md)

Cada plano é um rascunho de trabalho da equipe do X1-Plantas. Vete cada um como faria de verdade: o plano pode ter problema ou estar certo. Não suponha que todos têm erro.

Seções: Plano 1: legenda do post da Casa Compacta (Redator); Plano 2: ângulo do primeiro anúncio (Estrategista); Plano 3: cena do vídeo principal (Editor de vídeo); Plano 4: conserto no gerador do PDF (Maestro); Plano 5: teste do last30days (Pesquisador); Plano 6: edição do vídeo com a MinoAI (Editor de vídeo); Plano 7: página do e-book da Casa Compacta (Arquiteto e Redator); Plano 8: roteiro dos dois vídeos (Editor de vídeo); Plano 9: conferência nova no checar.py (Maestro); Plano 10: legenda do post da planta grátis (Redator).

Tamanho: 733 palavras.

### [Quadrinhos cômicos do e-book: 3 roteiros e 1 vídeo](anexos/quadrinhos-roteiros.md)

Redator, 23/11/2026, noite. Pedido do dono: quadrinhos cômicos no e-book ("Como ler esta planta" em quadrinhos e a obra em passos), no modo humor pelo absurdo (`video/referencias/GANCHOS-VISUAIS.md`, "Referência de humor do dono"; fim de `ebook/referencias/visual-ref/EDITORIAL.md`). Ficha…

Seções: A fórmula e o nosso jeito de dizer; Roteiro 1 · O formigueiro e meio (medir o lote); Roteiro 2 · A planta lavada (a casa que não cabe); Roteiro 3 · Você está aqui (ensina a ler a planta); Versão em vídeo (24 segundos, toda em IA): A planta lavada; Para o Revisor de risco.

Tamanho: 2209 palavras.

### [Skills candidatas para design criativo (passo 1 da pesquisa)](anexos/skills-candidatas-design.md)

Pesquisador, 23/11/2026. Passo 1: achados com fonte. Quem conclui é o Opus (Designer e Maestro) e o Conselho. Nada foi baixado, instalado nem executado; só páginas públicas, nada pago, sem commit. Falta a ficha e o veto do Conselho para qualquer uma entrar (CONSELHO.md, seção 6). Para que serve: o…

Seções: As 3 melhores no topo; Mapa rápido (as 12 lidas); Fichas; Lidas e descartadas; O que ainda precisa de decisão (nada disso eu fiz); O que não consegui confirmar; Fontes lidas (todas em 23/11/2026); Reconferência da ficha (tarefa recebida).

Tamanho: 3188 palavras.

### [Skills candidatas para a venda do e-book (WhatsApp, Instagram, anúncio)](anexos/skills-candidatas-venda.md)

Pesquisa do Pesquisador, passo 1 de 2. Lida em 23/11/2026, só em páginas públicas do GitHub (arquivos "raw"), pelo TinyFish (busca e leitura, grátis). Nada foi baixado, instalado nem executado. Quem confere e conclui é o Opus; o Revisor de risco tem veto. Todas as leituras foram da branch `main`…

Seções: As 3 melhores (para o primeiro Pix); Tabela das 12 candidatas; Descartadas (li o suficiente para dizer não); O que isto significa para a ordem de entrada (sugestão, quem decide é o Conselho e o dono); O que não consegui confirmar.

Tamanho: 2263 palavras.

### [Entrada de 6 skills: passo 1 do roteiro (ler o que ela roda)](anexos/skills-entrada-passo1.md)

Pesquisador, 23/11/2026. Passo 1 de `CONSELHO.md`, seção 6. Só leitura de páginas públicas (TinyFish: GitHub raw, blob e a API pública de commits e pastas). Nada foi baixado, clonado, instalado nem executado; nada pago; sem commit. O `gh` e o `curl` do shell continuam sem acesso a esses…

Seções: Resumo em uma tabela; 1. meta-click-to-message-ads (Insightful-Pipe/meta-ads-skills); Neste projeto (X1-Plantas); 2. copy-thief (thalesholleben/copy-thief); Neste projeto (X1-Plantas); 3. offers (coreyhaines31/marketingskills, pasta `skills/offers/`); Neste projeto (X1-Plantas); 4. frontend-design (anthropics/skills, pasta `skills/frontend-design/`); Neste projeto (X1-Plantas); 5. canvas-design (anthropics/skills, pasta `skills/canvas-design/`); Neste projeto (X1-Plantas); 6. pdf-design (Georgi45/pdf-design); Neste projeto (X1-Plantas); Riscos transversais (para o Revisor de risco); ….

Tamanho: 7353 palavras.

### [Primeiro uso das duas skills novas (roteiro de entrada, passo "rodar uma vez sobre o que já existe")](anexos/skills-primeiro-uso.md)

23/11/2026. Skills: `.claude/skills/oferta-e-whatsapp/` e `.claude/skills/design-editorial/` (leitura das 6 fontes em `skills-entrada-passo1.md`). Nenhum arquivo do e-book ou da venda foi editado: são achados para o Redator, o Designer e o dono. Até 5 por peça. Números aqui são só os que um comando…

Seções: 1. `oferta-e-whatsapp` sobre `ebook/vendas/RESPOSTAS-RAPIDAS.md`; 2. `design-editorial` sobre a página da Casa Compacta (`ebook/plantas/rascunhos/estilo-final-C01.png`).

Tamanho: 1028 palavras.

### [Teste de preço R$ 47 x R$ 67: como medir](anexos/teste-de-preco-como-medir.md)

Para o dono. Decisão dele em 23/11/2026 (decisões): dois preços, em semanas alternadas, começando pelo R$ 47. Feito pelo Estrategista. Ainda não há nenhuma venda medida: nenhum número abaixo é resultado, só exemplo de conta.

Seções: 1. A regra em uma linha; 2. O que anotar, por pessoa; 3. O modelo de planilha (só os nomes das colunas); 4. A venda conta na semana da oferta; 5. Quantas conversas antes de concluir; 6. A conta: qual preço ganha; 7. Perguntas que só você responde.

Tamanho: 743 palavras.

### [Opções de título do e-book (Redator, 23/11/2026)](anexos/titulos-opcoes.md)

Pedido do dono, 23/11: "Título meio sem graça, tem que ser mais chamativo e atraente" (provisório: "Que casa cabe no seu lote?"). Ficha: `pedidos/2026-11/2026-11-23-0947-testar-as-ferramentas-novas-achar-funcoes-que-faltam-na-equi.md`. O dono escolhe; nada foi aplicado no `ebook/config.json`. Todas…

Seções: Opção 1 (a que eu recomendo); Opção 2; Opção 3; Passada da marketing-psychology (vontade, facilidade, pedido claro); O que ficou de fora, e por quê; Perguntas ao dono (curtas).

Tamanho: 749 palavras.

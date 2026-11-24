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

## Os 58 documentos

### [Auditorias do Supervisor (Fable)](AUDITORIAS.md)

Uma linha por auditoria, escrita pelo agente `supervisor` (regras em `LEIA-ME.md`). A cada 3 fichas fechadas, `ferramentas/pedido.py` avisa que é hora da próxima.

Seções: Auditoria das regras, 24/11/2026; Auditoria de 24/11/2026 (tarde): as 3 fichas que escaparam (passo F17 do plano).

Tamanho: 6681 palavras.

### [Pedidos do dono: como cada prompt vira trabalho](LEIA-ME.md)

Regra do dono (22/11/2026). Todo prompt dele é guardado, interpretado por um modelo e executado por outro, para o modelo caro pensar e o barato fazer o que é simples. Fila de pedidos: `FILA.md`.

Seções: Quem manda no sistema; Pensar antes de fazer (dono, 22/11/2026); Perguntar sempre (dono, 22/11/2026); O plano de tudo; Plano vetado antes de fazer (dono, 22/11/2026); Erro de sintonia entre agentes (dono, 22/11/2026); Ferramenta ou agente novo (dono, 23/11/2026); Buscar o que o dono já disse (22/11/2026); Faltou informação do dono? Sugira, não espere (dono, 22/11/2026); Consertar de vez (dono, 22/11/2026: "não só conserte, remende"); O caminho de um prompt; Quem faz o quê; O pacote do executor; A ficha; ….

Tamanho: 3003 palavras.

### [Lições da equipe (registro único, só acréscimo)](LICOES.md)

Gravado por `python3 ferramentas/pedido.py licao` e pelo `fechar`. Não edite à mão: a lição também está no "Lições" do `contexto/<papel>.md`.

Seções: Saídas do contexto/maestro.md por falta de espaço (24/11/2026).

Tamanho: 1254 palavras.

### [Plano de trabalho: o que a equipe faz, em que ordem, e para quê](PLANO.md)

Pedido do dono (22/11/2026): "sempre dê um objetivo à equipe; um plano passo a passo, separado em tarefas grandes e pequenas, entre os agentes". Quem mantém, desde 24/11: o `planejador`. Quarta rodada: 24/11/2026, 16h05 UTC, conferida contra o repositório nesta hora (`git log` até `ca5b47b`, `git…

Seções: O objetivo da equipe; Onde estamos (24/11, 16h05, conferido); O caminho mais curto até o primeiro Pix; Agora (pode começar já, sem esperar ninguém); Depois: o júri decide e mostra depois (dono, cartão v6); Depois (em ordem; cada um diz de qual passo ou decisão depende); Depois: fila da equipe (para o Agora nunca ficar vazio); Depois: feitos que outros passos citam; Esperando o dono; Não fazer (parece o próximo passo, mas não é); Histórico: feitos de 24/11 que nenhum passo aberto cita; Histórico: o plano de 22/11 (fases antigas); Tempo livre: deixar a equipe mais inteligente (dono, 22/11/2026); Sempre, em toda fase.

Tamanho: 11900 palavras.

### [Provas da equipe](PROVAS.md)

Fila da noite (ficha `2026-11-23-0144`), tarefa A0: a régua que diz se a equipe aprende. Planos com erro plantado e gabarito guardado fora do repositório até a nota; os agentes vetam sem ver o gabarito; o Fable dá a nota. Nenhuma regra muda com n menor que 5 (condição do Fable).

Seções: Prova 1, base (23/11/2026, 04:47 a 04:55 UTC); Prova 2 (23/11/2026, 14:10 a 14:40 UTC); Prova 3: o júri (23/11/2026, 22:10 UTC, a 24/11, 00:55 UTC); Prova 4: planejador e organizador (24/11/2026, 12:20 a 13:00 UTC).

Tamanho: 3450 palavras.

### [A4: correções antigas do dono, conferidas (23/11/2026)](anexos/a4-correcoes-do-dono.md)

Fila da noite, tarefa A4 (ficha `2026-11-23-0144`). Três leitores (Sonnet) em `contexto/dono/PROMPTS.md`, `contexto/dono/intencoes/` e `pedidos/entrada/` + `conversas.py`; um agente juntou e conferiu o que já existia; Revisor e Fable vetaram (Fable SIM, SE, 7). Tudo nas nossas palavras. 81 achados…

Seções: Já eram lição ou regra (correções do Fable aplicadas às citações); Viraram lição (texto final, depois do veto); Tiradas pelo veto.

Tamanho: 1717 palavras.

### [O que vai de graça: 2 opções de amostra](anexos/amostra-gratis-opcoes.md)

Pedido do dono no quadro (23/11/2026): "uma amostra grátis bem impressionante do que vamos oferecer a eles, talvez um guia também". Ainda não decidido. Feito pelo Estrategista. Nenhum número abaixo foi medido: ainda não há venda.

Seções: Opção A: a Casa Compacta completa, caprichada (5 páginas); Opção B: a Casa Compacta + o guia "Seu lote cabe?" (8 a 9 páginas); O teste de preço (R$ 47 x R$ 67).

Tamanho: 913 palavras.

### [Bônus 1: Checklist da obra por fase (rascunho técnico)](anexos/bonus-checklist-da-obra.md)

Status: rascunho do Arquiteto, 24/11/2026, para o Redator e o Designer fazerem a página e o Revisor de risco conferir. Ainda não vai ao público. Pedido do dono: os 2 bônus de "Antes do primeiro tijolo" (`ebook/config.json`, chave `bonus`; decisão de 23/11 em…

Seções: Aviso que abre a página (texto-base para o Redator); Os momentos de chamar o engenheiro (resumo para o topo da página); Nota sobre a ordem das fases; Fase 0a. Antes de começar: o lote, o projeto e o profissional; Fase 0b. Antes de começar: alvará, ligações e cadastro da obra; Fase 1. Locação: a casa marcada no chão do lote; Fase 2. Fundação e baldrame; Fase 3. Impermeabilização; Fase 4. Paredes, vergas e contravergas; Fase 5. Pilares, vigas e laje ou forro; Fase 6. Telhado; Fase 7. Água, esgoto e luz antes de fechar a parede; Fase 8. Chapisco, reboco e contrapiso; Fase 9. Esquadrias (portas e janelas); ….

Tamanho: 3526 palavras.

### [Bônus 2: Perguntas para levar ao engenheiro (rascunho)](anexos/bonus-perguntas-ao-engenheiro.md)

Estado: rascunho do Redator, 24/11/2026. Nada aqui vai ao público antes do Arquiteto (conteúdo técnico) e do Revisor de risco (veto). A página é do Designer. Pedido do dono: o e-book "Antes do primeiro tijolo" tem 2 bônus, "Checklist da obra por fase" e "Perguntas para levar ao engenheiro"…

Seções: A folha (texto para o público); Para a equipe (não vai ao público).

Tamanho: 2888 palavras.

### [Como mobiliar as 3 casas do lançamento (conteúdo técnico)](anexos/como-mobiliar-as-3-casas.md)

Medidas conferidas em 24/11/2026, segunda conferência, cômodo por cômodo, pela face de dentro da parede, contra `ebook/plantas/dados/<ID>.json`, `video/src/plantas/<ID>.js` (móveis, portas e janelas do desenho 3D) e `python3 ferramentas/plantas.py validar` (C01, E03 e F01: zero erros). Mudou desde…

Seções: Como ler as contas; 1. C01 · Casa Compacta (6,50 x 8,50 m, 51 m², 2 quartos; cabe num lote de 8 x 15 m); 2. E03 · Casa Fita (3,50 x 16,10 m, 56 m², 2 quartos; cabe num lote de 5 x 25 m); 3. F01 · Casa Família Compacta (8,50 x 8,30 m, 71 m², 3 quartos; cabe num lote de 10 x 15 m); 4. Medidas de móveis comuns no Brasil (as usadas nas contas); 5. Para a equipe (não vai ao público).

Tamanho: 4995 palavras.

### [Cômodo a cômodo: o próximo passo depois da planta (C01, E03, F01)](anexos/comodo-a-comodo-3-casas.md)

Pedido do dono (24/11/2026, ficha `pedidos/2026-11/2026-11-24-1119-casas-comodo-a-comodo-...`), palavra por palavra: "continue trabalhando nas casas, podem estar desenhadas corretas mas qual o próximo passo? Planejar cada quarto, ideias do que fazer em lugares da casa etc". Continua dois pedidos de…

Seções: Como ler; 1. C01 · Casa Compacta (6,50 x 8,50 m, 51 m², 2 quartos; lote de 8 x 15 m, mínimo 8 x 13); 2. E03 · Casa Fita (3,50 x 16,10 m, 56 m², 2 quartos; lote de 5 x 25 m, mínimo 5 x 20,6); 3. F01 · Família Compacta (8,50 x 8,30 m, 71 m², 3 quartos; lote de 10 x 15 m, mínimo 10 x 12,8); 4. O que disso vira o quê (recomendação; quem decide é o dono); 5. Para a equipe (não vai ao público); 6. O que ainda não pode virar página.

Tamanho: 9711 palavras.

### [Conferência técnica do Arquiteto: página "A parede que não pode ter janela" (passo D19), 24/11/2026](anexos/conferencia-arquiteto-parede-sem-janela-2026-11-24.md)

Conferido contra os dados da C01, E03 e F01 (recuo esquerdo 0,0 m = divisa; móveis por posição) e as prévias; o validador dá 0 erros nas 3 casas. Texto conferido: `pagina-parede-sem-janela-texto.md`.

Tamanho: 594 palavras.

### [Decisões do dono, 23/11/2026 (respostas às perguntas pendentes)](anexos/decisoes-do-dono-2026-11-23.md)

Respondidas pelo dono nesta data, em 6 blocos de perguntas (ficha `pedidos/2026-11/2026-11-23-0947-testar-as-ferramentas-novas-achar-funcoes-que-faltam-na-equi.md`). As palavras entre aspas são dele. Vale até ele dizer o contrário.

Seções: 24/11/2026, comentários no quadro de tarefas (11:07 UTC); 24/11/2026, mais comentários no quadro (11:09 a 11:15 UTC; lidos às 12:00, na reforma do Canteiro); 24/11/2026, respostas no Canteiro novo (13:15 a 13:39 UTC; lidas às 15:45, depois do limite de uso).

Tamanho: 3866 palavras.

### [Decisões pendentes do dono, em grupos (24/11/2026, tarde)](anexos/decisoes-pendentes-em-grupos.md)

Proposta do `organizador`, segunda versão (passo F2 do `pedidos/PLANO.md`; a primeira é da ficha `2026-11-24-1027`, manhã de 24/11). Só propõe: não mexe no quadro de tarefas, não decide nada pelo dono, não muda prioridade que ele deu. Fontes novas desta versão: as duas seções de 24/11 de…

Seções: O que mudou desde a manhã; Contagem; Decisões do dono, na ordem em que ele deveria tratar; Saíram da lista de decisões; Cartão → grupo (para o Maestro atualizar o Canteiro).

Tamanho: 3876 palavras.

### [E07 e a parede na divisa: o que fazer com a parede sem janela](anexos/e07-parede-na-divisa-ideias.md)

Pedido do dono (23/11, comentário no quadro; `decisoes-do-dono-2026-11-23.md`, linha 86): "Crie uma solução criativa para o que pode ser feito ou acontecer naquele quarto/área, pode ser ideia de vídeo e/ou parte do e-book." Autor: Editor de vídeo, 23/11/2026. Rascunho de ideias: nada aqui é texto…

Seções: O que encosta na divisa (lido no rascunho, não suposto); 1. Cinco usos de verdade para a parede sem janela; 2. Duas páginas de e-book: "A parede sem janela trabalha para você"; 3. Dois roteiros de vídeo, de 15 a 25 s; Em aberto (perguntas ao dono, uma de cada vez).

Tamanho: 2124 palavras.

### [Plano de integração do everything-claude-code (vetado, 23/11/2026)](anexos/ecc-plano.md)

Saída do workflow wkfowrx4b (5 leitores, Revisor e compatibilidade por grupo, plano, Fable). Ficha `0209`. Texto dos agentes, sem edição; as correções do Fable valem sobre o plano.

Seções: Entra (adaptado); Não entra; Ganchos; Passos; Testes; Veto do Fable: SIM, SE; Não conferido.

Tamanho: 8430 palavras.

### [E-mail ao autor do cass: ENVIADO em 23/11/2026 do Gmail do dono, com o sim dele, assinado "[nome do dono], a solo founder"](anexos/email-autor-cass.md)

Ficha `2026-11-22-2237-busca-nas-conversas-propria-opcao-c-e-e-mail-ao-autor-do-cas.md`. O dono troca os campos entre colchetes e manda do e-mail dele, em particular (não como issue pública). Esta sessão não manda e-mail. O endereço do autor não está aqui: pegue no perfil dele no GitHub…

Tamanho: 517 palavras.

### [Guia "Seu lote cabe?": o texto real (RASCUNHO)](anexos/guia-seu-lote-cabe-texto.md)

Conferido pelo Arquiteto em 24/11/2026. As trocas já estão nas tabelas abaixo; o que mudou e por quê, item por item, está em "Resposta do Arquiteto", depois da lista dele. A lista do Revisor de risco não foi tocada e continua valendo para o texto novo.

Seções: Antes de escrever (skills `redacao-que-vende` e `oferta-e-whatsapp`); Página 1 (B-p1): "Meça o lote com a trena, de muro a muro."; Página 2 (B-p2): "Recuo é o espaço que a casa deixa livre no lote."; Página 3 (B-p3): "Anote de que lado o sol nasce no seu lote."; Página 4 (B-p4): "Anote a sua medida e mande no WhatsApp."; Entrega no formato do Redator; O Arquiteto precisa conferir; Resposta do Arquiteto (24/11/2026); O Revisor de risco precisa ver; Em aberto (para quem conduz levar ao dono).

Tamanho: 4137 palavras.

### [Perfil novo do Instagram, 3ª rodada: a identidade do Lote Carente (24/11/2026)](anexos/instagram-identidade-lote-carente-2026-11-24.md)

Pedido do dono (no quadro, 24/11, sobre a 2ª rodada, `instagram-nomes-e-bios-absurdos-2026-11-24.md`). Sobre os nomes: "Todas nao tem um senso de identidade meio grande, parece generico dms. lote carente foi a melhor opcao". Sobre as bios: "Quis dizer basica no sentido que so está explicando o que…

Seções: O que a MinoAI Frontier devolveu (só isto; a leitura minha vem marcada); 1. O personagem em 6 linhas; 2. Cinco bios na voz dele; 3. Três nomes de exibição (o campo ao lado do @); 4. O que fica fixo fora da bio (lei e honestidade); 5. Seis ideias de post na voz dele (uma linha cada); 6. Se @lotecarente estiver ocupado; 7. Recomendação do Redator: @lotecarente + nome "Plantas térreas de referência" + Bio 1; Para o Revisor de risco; O que não conferi.

Tamanho: 2594 palavras.

### [Perfil novo do Instagram: 8 nomes e 4 bios no humor pelo absurdo (24/11/2026)](anexos/instagram-nomes-e-bios-absurdos-2026-11-24.md)

Pedido do dono (comentários no quadro, 24/11): recusou os 6 nomes de `instagram-perfil-novo.md` ("Não gostei de nenhuma opção, lembre, coisas absurdas prendem a atenção") e as 3 bios ("Todas um pouco básico"). Rascunho do Redator. Ainda não passou pelo Revisor de risco. Quem escolhe o @ e a bio é o…

Seções: O que a MinoAI Frontier devolveu (só isto; leitura minha marcada como tal); 1. Oito nomes (@), em 3 linhas de humor; 2. Quatro bios (até 150 caracteres); 3. Recomendação do Redator: @lotecarente + Bio 1; Para o Revisor de risco; O que não conferi; Veto do Revisor de risco (24/11, rascunho).

Tamanho: 2230 palavras.

### [Perfil novo do Instagram: material para o dono escolher (rascunho)](anexos/instagram-perfil-novo.md)

Redator, 23/11/2026, noite. Pedido do dono: "Um novo" (comentário no quadro, `pedidos/anexos/decisoes-do-dono-2026-11-23.md`, linha "Instagram"): perfil novo, só do negócio. Quem cria a conta é ele; aqui fica o material para ele escolher. Rascunho: nada vai ao público antes do Revisor de risco.…

Seções: 1. Nome de usuário (@): 6 opções; 2. Bio: 3 opções (limite de 150 caracteres); 3. Nome de exibição e categoria; 4. Os 9 primeiros posts (a grade de quem abre o perfil); 5. Destaques fixos (stories): 3; 6. O que só o dono faz; Para o Revisor de risco; Perguntas ao dono (curtas).

Tamanho: 2922 palavras.

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

### [Kit do anúncio pago que abre o WhatsApp (rascunho)](anexos/kit-anuncio-whatsapp.md)

24/11/2026. Escrito pelo Redator com a skill `oferta-e-whatsapp` (passo a passo) e a `redacao-que-vende`, conferido com a `marketing-psychology` (vontade, facilidade, um pedido só). Origem: achados 1, 2 e 5 de `skills-primeiro-uso.md`. RASCUNHO: nada aqui vai ao público. Antes, três coisas: o…

Seções: 0. Quais anúncios podem rodar e quais esperam; 1. Diagnóstico antes de escrever (skill, seções 1 e 2); 2. O que é igual nos 3 anúncios; 3. Anúncio A: Casa Fita (lote de 5 x 25); 4. Anúncio B: Família Compacta (lote de 10 x 15); 5. Cuidado do anúncio B: quem chega com 8 ou 9 m de frente; 6. Anúncio C: Casa Compacta (lote de 8 x 15). ESPERA A DECISÃO DO DONO; 7. Como anotar a origem, sem dado pessoal no repositório; 8. O que medir por anúncio, e quando parar; 9. Para o Revisor de risco (frases, uma por linha); 10. Perguntas ao dono (uma por linha); 11. Conformidade (skill, seção 4).

Tamanho: 5730 palavras.

### [Leis e regras conferidas no texto oficial (23/11/2026)](anexos/leis-conferidas-2026-11-23.md)

Pesquisador, passo 1. Cada item: o que o texto diz (citação curta), o link lido, o que não se confirmou e "muda algo nos nossos textos?". Não editei texto de venda. Quem conclui: o Revisor de risco (lei) e o Redator (texto). Todos os achados estão no caderno (`pesquisas/normas.md` e…

Seções: 1. Lei 6.766/1979, art. 4º, II (lote mínimo); 2. Decreto 7.962/2013 (comércio eletrônico); 3. CDC, Lei 8.078/1990; 4. Código Civil, arts. 1.301 e 1.302; 5. LGPD, Lei 13.709/2018; 6. WhatsApp Business, ajuda oficial; 7. Instagram e Meta; Reconferência do pedido.

Tamanho: 2331 palavras.

### [Letras com identidade para o projeto: 10 opções em 6 famílias (24/11/2026)](anexos/letras-com-identidade-2026-11-24.md)

Pedido do dono (quadro, 24/11/2026), palavra por palavra: "Procure na rede e me mostre as opcoes, o alienigena so foi um exemplo de algo com identidade e original". Antes (23/11) ele tinha dito "caligrafia meio alienígena". O que se quer: uma letra com identidade para os títulos do e-book e para o…

Seções: Como ler as marcações; Família 1: letreiro de obra e de placa pintada à mão (letreiramento popular, "abridor de letras"); Família 2: estêncil e carimbo de caixote; Família 3: letra de planta técnica e de normógrafo; Família 4: letra "estranha" ou alienígena (forma inventada, ainda legível); Família 5: letra de quadrinho e de gibi; Família 6: display gorda e engraçada; Quais 3 eu levaria ao Designer para testar no nome "Lote Carente" (leitura minha, não decisão); O que não consegui conferir; Reconferência do pedido (um por um).

Tamanho: 2923 palavras.

### [Mapa das duas partes do e-book (passo A10, 24/11/2026)](anexos/mapa-duas-partes-do-ebook-2026-11-24.md)

Pedido do dono (24/11, resposta à decisão 8 no quadro): o e-book terá "uma parte falando de cada casa específica, e outra parte falando de casas no geral"; a página da parede sem janela "pode ir pro geral". Autor: Designer, 24/11/2026. É proposta: quem decide a ordem é o Maestro…

Seções: 1. As 17 páginas de hoje e para onde vão; 2. A ordem proposta: a casa primeiro, o geral depois; 3. Onde entram as páginas novas; 4. Como o leitor sabe em que parte está (sem trocar a identidade); 5. Esboço do sumário novo; 6. O que muda no gerador (para o D17; eu não mexi); 7. Perguntas; 8. O que não conferi.

Tamanho: 2786 palavras.

### [Página "A parede sem janela" (parte geral do e-book): texto (passo D19)](anexos/pagina-parede-sem-janela-texto.md)

Pedido do dono. 23/11: "Crie uma solução criativa para o que pode ser feito ou acontecer naquele quarto/área, pode ser ideia de vídeo e/ou parte do e-book." 24/11, decisão 8: o e-book terá "uma parte falando de cada casa específica, e outra parte falando de casas no geral"; esta página "pode ir pro…

Seções: 1. A ideia principal (Diretor, MinoAI Frontier, 24/11); 2. Atributos (escada e nota); 3. O texto da página (pronto para o Designer); 4. Formato de entrega; 5. O que foi conferido e o que não foi.

Tamanho: 2200 palavras.

### [Página de prova "cômodo a cômodo": Casa Fita (E03), texto](anexos/pagina-prova-comodo-a-comodo-E03-texto.md)

Passo A9 do `pedidos/PLANO.md`. Autor: Redator, 24/11/2026. Rascunho para o Designer montar e para o Revisor de risco e o Arquiteto conferirem (D15). Não está aprovado e não vai ao público. Pedido do dono (24/11), palavra por palavra: "Planejar cada quarto, ideias do que fazer em lugares da casa".…

Seções: Ideia principal (Diretor, MinoAI Frontier); Atributos (escada e nota D/P/E); TEXTO DA PÁGINA; Para o Designer e para quem confere (não vai ao público).

Tamanho: 1698 palavras.

### [Prova de base: 10 planos curtos para vetar (23/11/2026)](anexos/prova-A0-planos.md)

Cada plano é um rascunho de trabalho da equipe do X1-Plantas. Vete cada um como faria de verdade: o plano pode ter problema ou estar certo. Não suponha que todos têm erro.

Seções: Plano 1: legenda do post da Casa Compacta (Redator); Plano 2: ângulo do primeiro anúncio (Estrategista); Plano 3: cena do vídeo principal (Editor de vídeo); Plano 4: conserto no gerador do PDF (Maestro); Plano 5: teste do last30days (Pesquisador); Plano 6: edição do vídeo com a MinoAI (Editor de vídeo); Plano 7: página do e-book da Casa Compacta (Arquiteto e Redator); Plano 8: roteiro dos dois vídeos (Editor de vídeo); Plano 9: conferência nova no checar.py (Maestro); Plano 10: legenda do post da planta grátis (Redator).

Tamanho: 733 palavras.

### [Quadrinhos cômicos do e-book: 3 roteiros e 1 vídeo](anexos/quadrinhos-roteiros.md)

Redator, 23/11/2026, noite. Pedido do dono: quadrinhos cômicos no e-book ("Como ler esta planta" em quadrinhos e a obra em passos), no modo humor pelo absurdo (`video/referencias/GANCHOS-VISUAIS.md`, "Referência de humor do dono"; fim de `ebook/referencias/visual-ref/EDITORIAL.md`). Ficha…

Seções: A fórmula e o nosso jeito de dizer; Roteiro 1 · O formigueiro e meio (medir o lote); Roteiro 2 · A planta lavada (a casa que não cabe); Roteiro 3 · Você está aqui (ensina a ler a planta); Versão em vídeo (24 segundos, toda em IA): A planta lavada; Para o Revisor de risco.

Tamanho: 2209 palavras.

### [Referências para a visita 3D por dentro das casas (mais móveis, quadros, detalhe e personalização)](anexos/referencias-visita-3d-2026-11-24.md)

Pedido do dono (24/11/2026), palavra por palavra: "Adicione mais móveis, quadros, o mais detalhado possível, referências legais também. Se puder deixar personalizável pro usuário também é legal." Autor: Pesquisador (passo 1 da pesquisa em dois passos). Só leitura e só grátis: nada foi baixado nem…

Seções: 1. Passeios 3D de casa pequena e configuradores de planta, na web; 2. Estilo "maquete" e low-poly de interiores: o que dá vida; 3. Como a casa brasileira de classe C é mobiliada de verdade (50 a 70 m²); 4. Personalização que ajuda a decidir; 5. As 10 ideias que mais valem a pena, da mais barata de fazer à mais cara; 6. O que eu não consegui confirmar ou não fiz; Reconferência dos pedidos do dono (24/11/2026).

Tamanho: 4490 palavras.

### [A regra de honestidade: o que é nosso e o que é da lei](anexos/regra-de-honestidade-para-o-dono-2026-11-24.md)

Revisor de risco, 24/11/2026 (Opus). Pedido do dono no quadro: "Quero dar uma olhada na regra de honestidade, nao roubando ou entregando produto de baixa qualidade, nao me importo de exagerar as coisas ou mentir". Quem decide é o dono. Só não dá para mudar o que é lei.

Seções: (a) O que a regra de hoje proíbe; (b) O que pode soltar sem risco; (c) O que continua proibido, e por quê; (d) Onde o dono quer a linha (três perguntas, uma por cartão); Conferência; Nota do Maestro.

Tamanho: 966 palavras.

### [Skills candidatas, 24/11/2026: júri, casas, cooperação e venda (passo 1 da pesquisa)](anexos/skills-candidatas-2026-11-24.md)

Pesquisador (Sonnet), 24/11/2026. Pedido do dono: "procure mais skills, talvez o júri precise de ajuda com uma". Passo 1 de 2: achados com fonte. Quem conclui é o Opus; o Revisor de risco tem veto. Nada foi baixado, instalado nem executado. Só páginas públicas lidas pelo TinyFish (busca e leitura,…

Seções: Em 15 linhas (o que o Maestro precisa); Quadro rápido (11 candidatas); Frente 1: para o júri; Frente 2: para as casas; Frente 3: cooperação com o dono; Frente 4: venda (só o que é novo); O que levar ao Conselho (recomendação, quem decide é o Maestro); Reconferência do pedido (ficha em `pedidos/`: não recebi o número; reconferi contra o texto do pedido); O que não consegui conferir.

Tamanho: 5337 palavras.

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

Tamanho: 805 palavras.

### [Título do e-book: 3 opções no lugar de "Antes do primeiro tijolo" (24/11/2026)](anexos/titulos-opcoes-2026-11-24.md)

Pedido do dono (quadro de tarefas, cartão p14, 24/11): "B", ou seja, 3 opções de título novo. Motivo: "Antes do primeiro tijolo" abre a legenda de um vídeo de referência com 5,2 milhões de visualizações e pode parecer cópia. O título atual fica até ele escolher. Quem escolhe é o dono. Rascunho do…

Seções: Cabe na capa?; Opção 1: o lote; Opção 2: o medo de errar; Opção 3: ver a casa antes; Já existe com esse nome? (busca de 24/11/2026); Recomendação (quem escolhe é o dono); Vontade, facilidade e pedido (conferência da marketing-psychology, feita por mim, sem rodar a skill inteira); Se o título mudar, revisar também; Veto do Revisor de risco (24/11, rascunho): os três passam com troca; Opinião do Diretor (MinoAI Frontier), 24/11.

Tamanho: 2734 palavras.

### [Opções de título do e-book (Redator, 23/11/2026)](anexos/titulos-opcoes.md)

Pedido do dono, 23/11: "Título meio sem graça, tem que ser mais chamativo e atraente" (provisório: "Que casa cabe no seu lote?"). Ficha: `pedidos/2026-11/2026-11-23-0947-testar-as-ferramentas-novas-achar-funcoes-que-faltam-na-equi.md`. O dono escolhe; nada foi aplicado no `ebook/config.json`. Todas…

Seções: Opção 1 (a que eu recomendo); Opção 2; Opção 3; Passada da marketing-psychology (vontade, facilidade, pedido claro); O que ficou de fora, e por quê; Perguntas ao dono (curtas).

Tamanho: 749 palavras.

### [Veto do Revisor de risco: os 2 bônus (24/11/2026)](anexos/veto-bonus-2026-11-24.md)

Texto do Revisor, como ele entregou. As trocas são aplicadas pelo Redator.

Tamanho: 1057 palavras.

### [Veto do Revisor de risco: `comodo-a-comodo-3-casas.md` (24/11/2026)](anexos/veto-comodo-a-comodo-2026-11-24.md)

VETO em 3 pontos, cada um com a troca que vira SIM; o resto passa com troca ou como está. L = linha do documento na versão lida. Conferido contra os dados das 3 casas e `PLANTAS.md`: medidas livres, perímetros, janelas, portas, folga no fundo e distâncias da tomada ao box batem. Não há promessa de…

Seções: Vetos; Trocas que passam (sem veto); As 5 mais seguras e úteis para abrir a página; Reconferência do Revisor, 24/11 (depois das trocas do Arquiteto).

Tamanho: 1093 palavras.

### [Veredito do Revisor de risco: rascunho do lançamento (24/11/2026)](anexos/veto-ebook-lancamento-2026-11-24.md)

Passo A1 do `pedidos/PLANO.md`. O Revisor leu o PDF direto: 17 páginas do e-book e 3 da planta grátis. SIM (rascunho): nada é veto. Nenhuma página promete aprovação, prazo ou custo; nenhuma dá a entender que dispensa profissional.

Seções: Trocas que não dependiam do dono; Depende do dono; Não conferido pelo Revisor.

Tamanho: 350 palavras.

### [Revisor de risco: identidade "Lote Carente" do Instagram, 24/11/2026 · Opus, rascunho](anexos/veto-instagram-lote-carente-2026-11-24.md)

SIM SE. Arquivo lido: `instagram-identidade-lote-carente-2026-11-24.md`.

Tamanho: 269 palavras.

### [Parecer do Revisor de risco: vender o e-book sem os 2 bônus (decisão 33, passo A5), 24/11/2026](anexos/veto-opcao-sem-bonus-2026-11-24.md)

[Revisor] SIM SE. A escolha é do dono; o parecer só diz se a opção é honesta. Vender sem bônus é honesto e dentro da lei se o comprador nunca ler "bônus" antes de o bônus existir. CDC, art. 30: a oferta vincula; o que não foi oferecido não obriga. Promessa sem data descumpre o Decreto 7.962/2013,…

Seções: Trocas, só se o dono disser sim.

Tamanho: 513 palavras.

### [Revisor de risco: página de prova "cômodo a cômodo" da Casa Fita (passo D15), 24/11/2026](anexos/veto-pagina-prova-E03-2026-11-24.md)

[Revisor] SIM SE, com 4 trocas pequenas. Não há veto. Rodou no Opus, sobre o rascunho; a peça final pede nova leitura no Fable. Imagens lidas: `ebook/plantas/rascunhos/comodo-a-comodo/E03-pagina-1.png` e `E03-pagina-2.png`.

Seções: Conferência do Arquiteto (24/11): SIM SE; Decisão do Maestro sobre os dois pareceres (24/11).

Tamanho: 757 palavras.

### [Veto: página "A parede que não pode ter janela" (passo D19), 24/11/2026 · Revisor de risco, Opus (rascunho)](anexos/veto-parede-sem-janela-2026-11-24.md)

Vale como SIM do rascunho; a página montada no PDF ainda pede a leitura no Fable.

Tamanho: 305 palavras.

### [Revisor de risco: posts 2, 4 e 7 reescritos (passo F19), 24/11/2026](anexos/veto-posts-2-4-7-2026-11-24.md)

[Revisor] SIM no post 2; SIM SE nos posts 4 e 7 e nas notas. Rodou no Opus, em rascunho; a peça final passa pelo Fable. Conferido contra `PLANTAS.md`, os dados da E03 e da F01, o `config.json` e as imagens 3D paradas. Os números batem (E03: 56 m², 2 quartos, 1 banheiro, 5 x 25, mínimo 5,0 x 20,6;…

Seções: Post 4 (Casa Fita): SIM SE; Post 7 (Casa Família Compacta): SIM SE; Notas e outros arquivos: SIM SE; Telas dos posts 2, 4 e 7 (rascunho do Designer, passo F20): SIM SE · Revisor, 24/11, Opus.

Tamanho: 844 palavras.

### [Veto do Revisor de risco: porta, Casa Fita, kit do anúncio, guia, pôster C e "como mobiliar" (24/11/2026)](anexos/veto-rascunhos-2026-11-24.md)

Texto do Revisor, como ele entregou.

Tamanho: 842 palavras.

### [Revisor de risco: textos de venda contra as decisões de 24/11 (passo F1), 24/11/2026](anexos/veto-textos-de-venda-2026-11-24.md)

[Revisor] VETO em pontos de gravidade alta (bônus que não existe e casas fora do lançamento) → fazer as trocas da parte A. Rodou no Opus, em rascunho. Conferido contra `PLANTAS.md`: C01 51 m², 8 x 15 (mín. 8,0 x 13,0); E03 56 m², 5 x 25 (mín. 5,0 x 20,6); F01 71 m², 3 quartos, 10 x 15 (mín. 10,0 x…

Seções: A. Pode corrigir já (não depende do dono); B. Espera o dono.

Tamanho: 687 palavras.

### [Revisor de risco: veneziana da Casa Compacta (passo D1), 24/11/2026 · Opus, rascunho](anexos/veto-veneziana-C01-2026-11-24.md)

SIM SE. Conferido nos dados: `veneziana_sobre_porta: fundos`; 0,90 x 0,50 = 0,45 m²; 0,45 / 3,4 = 13%. A página não estoura; os avisos aparecem nas páginas 8 e 9 e na planta grátis. O veto 3 do cômodo a cômodo (serviço da C01) fica levantado, com as condições abaixo.

Tamanho: 340 palavras.

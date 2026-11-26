# Registro dos resumos de passagem

> Todos os resumos de passagem, do mais antigo ao mais novo. O mais recente também fica em `ULTIMO.md`, que é o que os agentes leem. Juntado em 22/11/2026 (ficha de organizar os arquivos): cada seção é um documento antigo, inteiro.

> As passagens de 20/11 até a manhã de 24/11 foram movidas para [`pedidos/historico/REGISTRO-ate-2026-11-24.md`](../../pedidos/historico/REGISTRO-ate-2026-11-24.md) em 26/11 (nada apagado).

## 2026-11-24-0750-vitrines-para-o-amigo-do-dono

**Tarefa:** o dono pediu um artifact bonito para mostrar o sistema a um amigo que acha tudo de IA genérico.
**Feito:** 1) página de texto "A Obra do X1-Plantas" (ele recusou: queria peça para ver, não para ler); 2) casa 3D que se constrói na tela, "Antes do Primeiro Tijolo", com o motor `video/src/casa3d.js` e as 3 casas do lançamento. Links nas fichas `2026-11-24-0646` e `2026-11-24-0726`; página guardada em `pedidos/anexos/vitrines/maquete-viva.html`. Auditoria de 24/11 (manhã) em `pedidos/AUDITORIAS.md`; consertei os números errados da primeira página, os links, a fonte da lição "uma pergunta por cartão" e o `pedidos/LICOES.md`.
**Como conferir:** `python3 ferramentas/checar.py`; abrir os dois links das fichas.
**Não feito / ressalva:** a página 3D publicada não foi revista depois de eu virar a câmera (o Supervisor testou só a cópia local, as 3 casas abrem). No celular o nome da Casa Fita quebra em duas linhas. Nada disso mexe no e-book.
**Decisão do dono pendente:** amostra grátis (A, B, ou A agora e B depois; protótipo em `ebook/plantas/rascunhos/amostra/`) e o que ganha quem já recebeu a C01; CNPJ ou CPF, endereço e e-mail de quem vende; preço no PDF ou PDF sem preço; janela da C01; roteiros de quadrinho e bordão; pôster A ou B; @ e bio do Instagram; 2 skills nossas ou as 6; everything-claude-code inteiro ou 6 peças; "grátis" e "publicar" saem da lista dele?; a tarefa de hora em hora continua?
Novas de 24/11: se a primeira página (mostra rascunho do e-book e 3 erros internos) pode ser vista por alguém de fora; se a tarefa de hora em hora continua.
**Próximo passo:** ler os comentários do quadro de tarefas. Sem resposta do dono, não criar rascunho novo em cima de rascunho.

## 2026-11-24-1800-juri-mecanismos-e-pagina-da-parede

**Tarefa:** tocar o plano enquanto o dono não responde: júri das decisões fáceis, mecanismos de regra e a página da parede sem janela no gerador.
**Feito:** 1) júri J1, J2, J3, J5, J7, J8, J9 em 2 rodadas (`pedidos/anexos/juri-decisoes-faceis-2026-11-24.md`): nenhuma nota chegou a 8,5; as propostas reescritas têm cartão no Canteiro. 2) `pedido.py fechar` recusa ficha sem aviso de 3 partes no quadro e avisa contexto parado; `checar.py` avisa `ULTIMO.md` velho; `plano.py feito J<n>` exige "mostrado ao dono: sim"; `plano.py conferir` barra vídeo em "Agora" antes do D13. 3) página "A parede que não pode ter janela" no gerador, página 21 do modo `--duas-partes` (só prévia); o Revisor (Fable) deu SIM SE e as trocas estão sendo aplicadas. 4) @lotecarente: sem perfil público no Instagram e no TikTok (indício, não prova).
**Como conferir:** `python3 ferramentas/checar.py`; `python3 ferramentas/plano.py agora`; `python3 ebook/gerador/livro.py --previa <pasta> --duas-partes`.
**Não feito / ressalva:** os passos J seguem abertos: só fecham quando o dono responder aos cartões (o mecanismo recusa antes). A revisão anônima do júri não rodou. A frase "60% e-book, 40% sistema" não entrou no `CLAUDE.md` (espera o dono). Fichas abertas de 24/11 (peça livre, 1103, 1119, 1144) agora precisam de aviso de 3 partes no quadro para fechar.
**Decisão do dono pendente:** título (p14), validade do preço (p10), formato da prévia (i5), os 4 cartões "decidimos" (j1, j3, j7, j9), endereço (40), profissional (41), "sim" do anúncio (46).
**Próximo passo:** ler os comentários do Canteiro; conferir as páginas cômodo a cômodo da Família Compacta e da Casa Compacta que o Designer está montando e levá-las à aba Ver.

## 2026-11-25-1610-passagem-para-a-conversa-nova

**Tarefa:** o dono pediu uma conversa nova (esta ficou longa e cara) e definiu a ordem: primeiro o e-book, assim que o limite semanal renovar; até lá, só planejar, pensar e melhorar.
**Feito nesta conversa (24 e 25/11):** cômodo a cômodo das 3 casas no gerador (prévia `--duas-partes`); PDF dos bônus sai do gerador junto do e-book, com selo de rascunho até o profissional ler; página da parede sem janela; mapa dor e saída (`pedidos/anexos/mapa-dor-solucao-do-ebook-2026-11-24.md`); separação do que vai ao cliente (`pedidos/anexos/o-que-vai-ao-cliente-2026-11-24.md`); prompt audit aplicado (`pedidos/anexos/prompt-audit-2026-11-25.md`); `plano.py` com no máximo 2 em "Agora"; `salvar.py` assina pelo modelo da sessão (`X1_MODELO`). Tarefa de hora em hora **pausada** pelo dono.
**Como conferir:** `python3 ferramentas/checar.py`; `python3 ferramentas/plano.py agora`.
**Decisões do dono de 25/11:** cômodo a cômodo entra no pago ("2 ok"); pausar a tarefa de hora em hora; e-book é a primeira tarefa quando o limite renovar.
**Decisão do dono pendente (o e-book para aqui):** (1) quantas das 5 páginas do mapa mudar (8, 12, 17, 22, 23), e se antes do PDF final ("vou olhar quando o limite resetar"); (2) "gera o PDF" (geração oficial grava `ebook/saida/`); depois título (cartão p14), profissional do checklist, pasta no Drive.
**Projeto novo, depois do e-book:** um Instagram 100% feito por IA, estudado a partir de @science_in_8bit (não copiar o nicho dele, ciência em 8 bits; nada de "AI slop"). O dono decidiu: criar a conta e postar sozinho (precisa de e-mail/telefone dele para criar a conta); **só ferramentas grátis**; língua e público pelo estudo; ferramenta nova grátis pode entrar sem perguntar, mas com licença lida e teste; júri forte antes de publicar. Recomendado: repositório e conversa próprios (a pedir ao dono), para as regras do X1-Plantas não se misturarem.
**Próximo passo:** até o reset, planejar sem gastar: ler o mapa dor e saída e preparar as frases das 5 páginas como plano (não texto final); esboçar o plano do estudo do perfil. Nada de agente em paralelo.

## 2026-11-26-0250-passagem-noite-itens-1-e-2

**Tarefa:** fila da noite de 26/11 (`pedidos/anexos/noite-2026-11-26-fila.md`), com autonomia total dada pelo dono, menos gastar dinheiro, publicar e decidir o final do e-book e dos anúncios. O Maestro agora se chama **Paydon Clabett**.
**Feito:** item 1 (configuração dos agentes: 4 mudanças, ficha 0105 fechada; diagnóstico do júri em `pedidos/anexos/diagnostico-do-juri-2026-11-26.md`). Item 2 (Canteiro refeito do zero, no mesmo link https://claude.ai/artifact/R8SSzqnZxR6XafEP5uXBtX: 54 cartões criados ou migrados, 99 antigos arquivados com `nivel: "arquivo"`, nada apagado; cópia em `ebook/plantas/rascunhos/quadro-tarefas.html`; fonte e dados em scratchpad, que some).
**Como conferir:** `python3 ferramentas/checar.py`; o Registro no fim da fila da noite.
**Não feito / ressalva:** o rtk não foi instalado (a trava da sessão recusou; não contornar). Na prova do júri (item 4) gastam-se ~1,6 M tokens: só com o "sim" do dono. O banco do Canteiro só deixa o dono escrever (o sócio ainda não).
**Decisão do dono pendente:** identidade (Trena, Placa ou Porta acesa), as 5 frases de dor, o título (p14), "gera o PDF", o "sim" da prova do júri, se decisão irreversível vai ao júri, as perguntas Q1 a Q8 do grill-me do Instagram, o sócio escrever no Canteiro e a instalação do rtk.
**Próximo passo:** seguir a fila pelo item 10 (nomes e conversa da equipe em `contexto/EQUIPE.md`, `contexto/CONVERSA.md` e nos agentes), depois o 11 (`contexto/` enxuto), o 3 (e-book página por página, só em prévia), o 5, o 6, o 7 e o 8, e por último o 9 (resumo da manhã). Um fluxo grande por hora, para racionar o limite. Não gravar `ebook/saida/`, não publicar nada, não gastar nada.

## 2026-11-26-0255-nomes-e-conversa-da-equipe

**Tarefa:** fila da noite, item 10: nome para cada agente e a equipe conversando como colegas (ficha 0116).
**Feito:** nome e jeito no topo dos 10 agentes (`.claude/agents/`) e em `contexto/EQUIPE.md`; `contexto/CONVERSA.md` criado; regra do Paydon copiar as falas em `contexto/maestro.md`; aviso no quadro; fala nova no Canteiro; `checar.py` acusa agente sem nome ou sem a conversa.
**Como conferir:** `python3 ferramentas/checar.py`; `grep -l "Seu nome é" .claude/agents/*.md`.
**Não feito / ressalva:** nenhum agente rodou ainda com a regra nova (a primeira prova é o item 3). A cópia do Canteiro em `ebook/plantas/rascunhos/` é ignorada pelo git: a fonte de verdade é o artifact.
**Decisão do dono pendente:** as mesmas de antes (identidade, 5 frases, título p14, "gera", prova do júri, rtk); ele pode trocar qualquer nome.
**Próximo passo:** auditoria da Olga (3 fichas fechadas), depois o item 11 (`contexto/` enxuto).

## 2026-11-26-0305-auditoria-da-olga-e-consertos

**Tarefa:** auditoria de rotina das fichas 1027, 0105 e 0116 (a Olga, no Fable) e os consertos que ela pediu.
**Feito:** resultado em `pedidos/AUDITORIAS.md` (0 alta, 6 média, 10 baixa). Consertos: `CONSELHO.md` 5b com as 3 escolhas do aplicador marcadas "espera o sim"; `pedidos/LEIA-ME.md` ("Limites honestos": quem chama repete no pedido o que mudou no agente até a conversa seguinte); `contexto/maestro.md` abaixo de 5.000, com a lição nova; ficha 0116 com data e a primeira prova das falas (as 3 da Olga, em `contexto/CONVERSA.md` e no Canteiro); ficha 0105 com a nota dos 5 achados não gravados; nomes "escolhidos pelo Paydon"; fala do dono como ele escreveu; fonte do Canteiro agora em `pedidos/canteiro/quadro-tarefas.html`, que o git acompanha.
**Como conferir:** `python3 ferramentas/checar.py`; `python3 ferramentas/pedido.py auditar` (0).
**Não feito / ressalva:** os 5 achados e a proposta do "Aplique" se perderam com a conversa anterior. O nome do Maestro no `CONTEXTO.md` fica para o item 11 (o arquivo está no teto).
**Decisão do dono pendente:** "júri também para o que não se desfaz, mesmo sem custo e sem público: sim ou não?"; o passo J pelo conselho de bolso; ele precisa saber que uma linha do `CLAUDE.md` mudou na 0105 ("a pesquisa vai ao Opus").
**Próximo passo:** item 11 (`contexto/` enxuto). Em todo pedido a agente nesta conversa, escrever o nome dele e "feche com `Falas:`".

## 2026-11-26-0400-passada-do-ebook

**Tarefa:** fila da noite, item 3: passada de melhoria do e-book página por página, em prévia (24 páginas, duas partes).
**Feito:** Bia (Designer e comprador) e Nilo (técnica) olharam as 24 páginas; Vera leu uma vez, no Fable, com a peça montada: SIM. Consertos no gerador: lado do sol espelhado em `ferramentas/plantas.py` (C01 e E03 melhores com a rua ao sul; prova no `checar.py`), frente do lote na faixa da rua, rodapé fora da fita, varanda da C01 (págs. 9 e 11), "parte do sol", vão da F01, "área construída", "Melhor com a rua: ao sul", textos de venda e de post. As 5 frases na prévia marcada em amarelo.
**Como conferir:** `pedidos/anexos/passada-do-ebook-2026-11-26.md` e `veto-passada-do-ebook-2026-11-26.md`; imagens em `pedidos/anexos/previa-noite-2026-11-26/`; `python3 ferramentas/checar.py`.
**Não feito / ressalva:** 12 propostas guardadas (a maior: a casa no lote ilegível no celular); a parede da varanda da C01 não está desenhada; `ebook/saida/` e `ebook/revisao/` têm a orientação antiga até o "gera" do dono.
**Decisão do dono pendente:** as 5 frases (quais páginas), identidade, título, "gera"; o "sim" do júri para o que não se desfaz.
**Próximo passo:** item 5 da fila (3 reels piloto do Instagram de IA), na próxima hora (um fluxo grande por hora).

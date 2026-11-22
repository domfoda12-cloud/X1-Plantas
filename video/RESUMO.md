# Resumo: Vídeo e anúncio

> Pedidos do dono, roteiros, planos, referências de edição e textos de anúncio. **Leia este resumo primeiro**; abra um documento inteiro só quando a tarefa pedir. Índice geral: [`INDICE.md`](../INDICE.md). Quem lê: editor-video, maestro, redator, revisor-de-risco.

## O essencial

<!-- essencial: escrito à mão, o gerador não apaga -->
- Antes de mexer em vídeo, leia `PEDIDOS-DO-DONO.md` inteiro; ordem nova do dono entra lá na hora (22/11/2026). (`CLAUDE.md`)
- Antes de montar vídeo ou gastar crédito do OpenArt: mande o resumo e a lista de instruções e espere o dono confirmar. OpenArt não é proibido; pede o "sim" dele a cada uso (22/11/2026). (`PEDIDOS-DO-DONO.md`)
- Destino do anúncio com locução: WhatsApp e Facebook Ads, não Instagram nem TikTok (22/11/2026). (`PEDIDO-anuncio-locucao.md`)
- Aviso legal pequeno, no canto, parado. Sem o selo "Imagem ilustrativa" no vídeo: o dono tirou (22/11/2026). Os roteiros `.json` antigos ainda trazem o selo; sai na próxima montagem. (`CLAUDE.md`, `VIDEO.md`)
- Montar: `python3 video/montar.py video/roteiros/<nome>.json`. Escaneamento: `python3 video/scan.py ID`. Passeio: `node render-passeio.cjs --planta ID`. 3D: `node render-planta.cjs --planta ID`. (`CLAUDE.md`)
- `saida/` hoje: `previa-whatsapp/` e `principal/` são de 21/11, com a C01 antiga (remontar); `principal-condor/` e `convite/` são rascunhos; `principal-e07/` tem a versão antiga e a montagem com a voz do dono sobre a E07 em fila; `v1` a `v5` (R$ 1.000 do arquiteto) são antigos, não publicar. (`VIDEO.md`)
- Todo clipe usa os prompts de câmera de `principal-e07/PROMPTS.md` e parte de imagem nossa. (`principal-e07/PROMPTS.md`)
- Edição final: MinoAI Frontier, no Mac do dono. Música: faixa licenciada ou a trilha nossa de 128 BPM. Até 12 MB; WhatsApp até 5 MB. (`CLAUDE.md`, `plano-anuncio-locucao.md`)
- Em aberto: o plano do anúncio com locução espera o dono aprovar a planta nova da E07 (na fila do redesenho) e o plano; nada foi gerado. (`plano-anuncio-locucao.md`)
- `plano-principal-e07.md` é registro da versão de 21/11, substituído por `plano-anuncio-locucao.md`. (`plano-principal-e07.md`)
<!-- /essencial -->

## Os 14 documentos

### [Vídeo: regras desta pasta](CLAUDE.md)

O Claude Code carrega este arquivo sozinho quando trabalha aqui. As regras gerais estão no `CLAUDE.md` da raiz.

Tamanho: 365 palavras.

### [Pedido do dono: anúncio do e-book com locução (ficha única)](PEDIDO-anuncio-locucao.md)

Parte da frente Vídeo. Plano: `plano-anuncio-locucao.md`. Regras da pasta: `CLAUDE.md`. Para que serve: é o lugar único com tudo o que o dono pediu para este vídeo, o que foi pedido a cada agente e o que eu supus sem ele dizer. Todo agente recebe este arquivo inteiro no pedido. Antes de cada etapa,…

Seções: 1. O que o dono pediu (nas palavras dele, resumidas); 2. O que eu supus sem o dono dizer; 3. O que foi pedido a cada agente, e o que voltou; 4. Ciclo de reconferência; 5. Reconferência de 22/11, antes de fechar o plano.

Tamanho: 1512 palavras.

### [Vídeo: tudo o que o dono pediu (não se perde)](PEDIDOS-DO-DONO.md)

Regra do dono (22/11/2026): "Para todo vídeo, quando eu acrescentar uma informação, garanta que ela fique lá e não se perca na conversa." Por isso: toda instrução dele sobre vídeo entra aqui na hora, com as palavras dele, antes de qualquer edição. Quem edita lê este arquivo inteiro antes de mexer…

Seções: Ordens gerais (valem para todo vídeo); Prompt base para tomadas realistas (22/11/2026); Próximo vídeo: o convite (22/11/2026); Vídeo principal.

Tamanho: 2379 palavras.

### [Referência de edição: CONDOR XIII (Payton Talbott)](REFERENCIA-CONDOR.md)

Pedido do dono (20/11/2026): "melhor edição que já vi, meu vídeo favorito do YouTube; absorva os conceitos e aplique no vídeo curto". Parte da frente vídeo (a última da fila: e-book → animações → vídeo). Guia do editor: `../instagram/MINOAI-FRONTIER.md`.

Seções: 1. O que deu para ver (e o que não deu); 1b. O que o `analyze_hook` da MinoAI Frontier viu (reels da mesma dupla de edição); 1c. B-roll e música: o coração do estilo (pedido do dono: "preste muita atenção"); 2. Os conceitos, levados para o reel de planta (30 a 60 s, vertical); 3. Conselho de bolso; 4. Próximo uso.

Tamanho: 3125 palavras.

### [Referência: como um formato viraliza (oferta e demanda)](REFERENCIA-VIRAL.md)

Era o agente `editor` da `main` (16/11/2026). Virou referência do Editor de vídeo (`.claude/agents/editor-video.md`) para não haver dois editores. O texto abaixo é o original; o público dele é rede social em geral, e o nosso anúncio vai para WhatsApp e Facebook Ads (ver `video/CLAUDE.md`).

Seções: Core thesis: going viral is not luck, it is supply and demand; Three ways to win a format; Arbitrage decays; Summary; How to work.

Tamanho: 1132 palavras.

### [Vídeo: o que existe hoje](VIDEO.md)

Parte do projeto X1-Plantas. Painel geral: `../PAINEL.md`. Regras desta pasta: `CLAUDE.md`. Antes de mexer em vídeo, leia `PEDIDOS-DO-DONO.md` inteiro. Reorganizado em 22/11/2026 para dizer a verdade de hoje. O guia antigo do vídeo "Os R$ 1.000 do arquiteto" (teleprompter, gravação do apresentador,…

Seções: 1. As regras que valem (dono, 22/11/2026); 2. O que está em `saida/` (conferido em 22/11/2026); 3. Nesta pasta; 4. Como montar e gerar; 5. Decisões que ficam com o dono.

Tamanho: 1021 palavras.

### [Anúncios para o Facebook Ads](anuncios/anuncio-facebook.md)

Parte da pasta Vídeo: `../VIDEO.md`. Antes de escrever ou mudar um anúncio, leia a estratégia de marketing (público, ângulos e tom de voz). Fluxo: anúncio → pessoa comenta "PLANTA" ou chama no WhatsApp → recebe a planta grátis → o parceiro pergunta o tamanho do lote → oferta do e-book. Campos entre…

Seções: Regras para todos os anúncios; Ângulo 1: pelo lote (o mais promissor); Ângulo 2: erro caro; Ângulo 3: casa que cresce; Ângulo 4: pedreiro; Ângulo 5: economia com arquiteto (vídeo antigo, não subir); Ângulo 6: oferta direta (só para quem já interagiu); Como testar.

Tamanho: 998 palavras.

### [Brief criativo: anúncios de plantas de casas](anuncios/brief-criativo.md)

Rascunho para revisão. Os trechos entre [colchetes] dependem do vídeo de referência que você vai enviar.

Seções: 1. Objetivo; 2. Mensagem central; 3. Formatos; 4. Estrutura do vídeo (roteiro de 20 segundos); 5. Estilo visual; 6. Variações para testar; 7. Checklist antes de publicar; 8. Perguntas para você responder.

Tamanho: 747 palavras.

### [Checklist de revisão antes de subir o anúncio](anuncios/checklist-revisao.md)

Use antes de publicar. Confira as regras atuais da Meta para anúncios de imóveis e construção no Gerenciador de Anúncios, porque elas mudam.

Seções: Conteúdo; Imagem ou vídeo; Público e oferta; Depois de publicar.

Tamanho: 300 palavras.

### [Plano de criação: anúncio do e-book com locução, com a planta nova](plano-anuncio-locucao.md)

Parte da frente Vídeo. Guia: `VIDEO.md`. Regras da pasta: `CLAUDE.md`. Prompts: `principal-e07/PROMPTS.md`. Situação (22/11/2026): para o dono mudar e aprovar. Nada foi gerado. Destino confirmado por ele: WhatsApp e Facebook Ads. Ficha com todos os pedidos e suposições: `PEDIDO-anuncio-locucao.md`.…

Seções: 1. O que muda em relação ao vídeo que o dono já viu; 2. As quatro paradas para aprovação; 3. Cena a cena; 4. Formato, legendas e aviso (destino: WhatsApp e Facebook Ads); 5. Gancho do primeiro quadro: três versões para testar; 6. Prompt cinematográfico (condição do dono); 7. Custo; 8. Instruções que estou seguindo; 9. O que falta o dono responder.

Tamanho: 1862 palavras.

### [Plano: vídeo principal "3 quartos em 8 m" (E07), quadro a quadro](plano-principal-e07.md)

E07 na fila do redesenho: o dono chamou de erro os 3 quartos em fila (22/11/2026). Registro da versão de 21/11, substituído. O plano que vale é `plano-anuncio-locucao.md`, com a ficha `PEDIDO-anuncio-locucao.md`. Depois deste plano o dono mudou: o vídeo abre na casa pronta e o blueprint vai para o…

Seções: 1. A casa que o vídeo segue (fonte única); 2. Ritmo; 3. Quadro a quadro; 4. Referências brasileiras (sem marca, sem personagem de terceiros); 5. Passos e custo; 6. Decisões que ficam com o dono; 7. Decisão do Conselho (21/11/2026); 8. Versão 3 "Grupo da família" (roteiro esperando o dono).

Tamanho: 1718 palavras.

### [Prompts do vídeo da E07 (OpenArt)](principal-e07/PROMPTS.md)

E07 na fila do redesenho: o dono chamou de erro os 3 quartos em fila (22/11/2026); as imagens de partida da E07 mudam com a planta nova. Os prompts de câmera continuam valendo. Parte da frente Vídeo. Plano que vale agora: `../plano-anuncio-locucao.md` (o antigo: `../plano-principal-e07.md`).…

Seções: 1. Movimento de câmera da casa (imagem → vídeo); 2. Imagens (Nano Banana 2.1, imagem → imagem, 9:16, 2K); 3. Peso dos arquivos.

Tamanho: 1006 palavras.

### [Pacote para a edição da MinoAI Frontier: anúncio do e-book (E07)](principal-e07/kit-minoai/LEIA-ME.md)

E07 na fila do redesenho: o dono chamou de erro os 3 quartos em fila (22/11/2026); os clipes deste pacote mostram a planta antiga e serão refeitos pelo plano novo, `../../plano-anuncio-locucao.md`. Parte da frente Vídeo. Plano desta versão: `../../plano-principal-e07.md`; plano que vale agora:…

Seções: 1. O que tem aqui (20 MB); 2. Roteiro para gravar (aprovado pelo Revisor de risco); 3. Plano de corte (128 BPM: 1 compasso = 1,875 s); 4. Regras da edição; 5. O que dizer para a MinoAI no Mac.

Tamanho: 1346 palavras.

### [Roteiro: vídeo de aquecimento do lançamento ("casas na mala")](roteiro-lancamento.md)

Parte da pasta Vídeo: `VIDEO.md`. Estratégia: `../ESTRATEGIA.md` (fase de aquecimento, seção 10). Editor: MinoAI Frontier. Canal: vídeo do perfil do Instagram (orgânico). Não confundir com o anúncio com locução, que vai para WhatsApp e Facebook Ads (`PEDIDO-anuncio-locucao.md`). Objetivo:…

Seções: 1. O roteiro original; 2. Versão recomendada (cerca de 38 s); 3. Cinco ganchos para os reels de teste; 4. Como gravar; 5. Edição com a MinoAI Frontier; 6. Série até o lançamento.

Tamanho: 1265 palavras.

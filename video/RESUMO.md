# Resumo: Vídeo e anúncio

> Pedidos do dono, roteiros, planos, referências de edição e textos de anúncio. **Leia este resumo primeiro**; abra um documento inteiro só quando a tarefa pedir. Índice geral: [`INDICE.md`](../INDICE.md). Quem lê: editor-video, diretor, redator, revisor-de-risco.

## O essencial

<!-- essencial: escrito à mão, o gerador não apaga -->
- Antes de mexer em vídeo, leia `VIDEO.md` (seção "Vídeo: tudo o que o dono pediu (não se perde)") inteiro; ordem nova do dono entra lá na hora (22/11/2026). (`CLAUDE.md`)
- Antes de montar vídeo ou gastar crédito do OpenArt: mande o resumo e a lista de instruções e espere o dono confirmar. OpenArt não é proibido; pede o "sim" dele a cada uso (22/11/2026). (`VIDEO.md` (seção "Vídeo: tudo o que o dono pediu (não se perde)"))
- Destino do anúncio com locução: WhatsApp e Facebook Ads, não Instagram nem TikTok (22/11/2026). (`ANUNCIO-LOCUCAO.md` (seção "Pedido do dono: anúncio do e-book com locução (ficha única)"))
- Aviso legal pequeno, no canto, parado. Sem o selo "Imagem ilustrativa" no vídeo: o dono tirou (22/11/2026). Os roteiros `.json` antigos ainda trazem o selo; sai na próxima montagem. (`CLAUDE.md`, `VIDEO.md`)
- Montar: `python3 video/montar.py video/roteiros/<nome>.json`. Escaneamento: `python3 video/scan.py ID`. Passeio: `node render-passeio.cjs --planta ID`. 3D: `node render-planta.cjs --planta ID`. (`CLAUDE.md`)
- `saida/` hoje: `previa-whatsapp/` e `principal/` são de 21/11, com a C01 antiga (remontar); `principal-condor/` e `convite/` são rascunhos; `principal-e07/` tem a versão antiga e a montagem com a voz do dono sobre a E07 em fila; `v1` a `v5` (R$ 1.000 do arquiteto) são antigos, não publicar. (`VIDEO.md`)
- Todo clipe usa os prompts de câmera de `principal-e07/PROMPTS.md` e parte de imagem nossa. (`principal-e07/PROMPTS.md`)
- Edição final: MinoAI Frontier, no Mac do dono. Música: faixa licenciada ou a trilha nossa de 128 BPM. Até 12 MB; WhatsApp até 5 MB. (`CLAUDE.md`, `ANUNCIO-LOCUCAO.md` (seção "Plano de criação: anúncio do e-book com locução, com a planta nova"))
- Em aberto: o plano do anúncio com locução espera o dono aprovar a planta nova da E07 (na fila do redesenho) e o plano; nada foi gerado. (`ANUNCIO-LOCUCAO.md` (seção "Plano de criação: anúncio do e-book com locução, com a planta nova"))
- `PRINCIPAL-E07.md` (seção "Plano: vídeo principal "3 quartos em 8 m" (E07), quadro a quadro") é registro da versão de 21/11, substituído por `ANUNCIO-LOCUCAO.md` (seção "Plano de criação: anúncio do e-book com locução, com a planta nova"). (`PRINCIPAL-E07.md` (seção "Plano: vídeo principal "3 quartos em 8 m" (E07), quadro a quadro"))
<!-- /essencial -->

## Os 7 documentos

### [Anúncio com a locução do dono](ANUNCIO-LOCUCAO.md)

A peça do anúncio com a voz do dono: o pedido (ficha anexa), o plano, o brief e o texto do Facebook. Juntado em 22/11/2026 (ficha de organizar os arquivos): cada seção é um documento antigo, inteiro.

Seções: Pedido do dono: anúncio do e-book com locução (ficha única); Plano de criação: anúncio do e-book com locução, com a planta nova; Brief criativo: anúncios de plantas de casas; Anúncios para o Facebook Ads.

Tamanho: 5233 palavras.

### [Vídeo: regras desta pasta](CLAUDE.md)

O Claude Code carrega este arquivo sozinho quando trabalha aqui. As regras gerais estão no `CLAUDE.md` da raiz.

Tamanho: 377 palavras.

### [Vídeo principal da E07 e roteiro de lançamento](PRINCIPAL-E07.md)

O plano do vídeo principal e o roteiro de lançamento. Juntado em 22/11/2026 (ficha de organizar os arquivos): cada seção é um documento antigo, inteiro.

Seções: Plano: vídeo principal "3 quartos em 8 m" (E07), quadro a quadro; Roteiro: vídeo de aquecimento do lançamento ("casas na mala").

Tamanho: 3026 palavras.

### [Referências de vídeo](REFERENCIAS.md)

A referência de edição favorita do dono (CONDOR) e a oferta e demanda de formatos virais. Juntado em 22/11/2026 (ficha de organizar os arquivos): cada seção é um documento antigo, inteiro.

Seções: Referência de edição: CONDOR XIII (Payton Talbott); Referência: como um formato viraliza (oferta e demanda).

Tamanho: 4301 palavras.

### [Vídeo: regras, pedidos do dono e conferência](VIDEO.md)

Tudo o que vale para qualquer vídeo: o guia, as instruções do dono (palavra por palavra, na seção dele) e a lista de revisão. Juntado em 22/11/2026 (ficha de organizar os arquivos): cada seção é um documento antigo, inteiro.

Seções: Vídeo: o que existe hoje; Vídeo: tudo o que o dono pediu (não se perde); Checklist de revisão antes de subir o anúncio.

Tamanho: 4390 palavras.

### [Prompts do vídeo da E07 (OpenArt)](principal-e07/PROMPTS.md)

E07 na fila do redesenho: o dono chamou de erro os 3 quartos em fila (22/11/2026); as imagens de partida da E07 mudam com a planta nova. Os prompts de câmera continuam valendo. Parte da frente Vídeo. Plano que vale agora: `../ANUNCIO-LOCUCAO.md` (o antigo: `../PRINCIPAL-E07.md`). Guardados para…

Seções: 1. Movimento de câmera da casa (imagem → vídeo); 2. Imagens (Nano Banana 2.1, imagem → imagem, 9:16, 2K); 3. Peso dos arquivos.

Tamanho: 1006 palavras.

### [Pacote para a edição da MinoAI Frontier: anúncio do e-book (E07)](principal-e07/kit-minoai/LEIA-ME.md)

E07 na fila do redesenho: o dono chamou de erro os 3 quartos em fila (22/11/2026); os clipes deste pacote mostram a planta antiga e serão refeitos pelo plano novo, `../../ANUNCIO-LOCUCAO.md`. Parte da frente Vídeo. Plano desta versão: `../../PRINCIPAL-E07.md`; plano que vale agora:…

Seções: 1. O que tem aqui (20 MB); 2. Roteiro para gravar (aprovado pelo Revisor de risco); 3. Plano de corte (128 BPM: 1 compasso = 1,875 s); 4. Regras da edição; 5. O que dizer para a MinoAI no Mac.

Tamanho: 1346 palavras.

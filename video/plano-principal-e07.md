# Plano: vídeo principal "3 quartos em 8 m" (E07), quadro a quadro

> **E07 na fila do redesenho:** o dono chamou de erro os 3 quartos em fila (22/11/2026).
>
> **Registro da versão de 21/11, substituído.** O plano que vale é [`plano-anuncio-locucao.md`](plano-anuncio-locucao.md), com a ficha [`PEDIDO-anuncio-locucao.md`](PEDIDO-anuncio-locucao.md). Depois deste plano o dono mudou: o vídeo **abre na casa pronta** e o blueprint vai para o meio, como prova; **sem o selo "Imagem ilustrativa"** (aviso legal pequeno, no canto, parado); **nada de morango do amor**; destino **WhatsApp e Facebook Ads**. Fica aqui porque documenta o vídeo `saida/principal-e07/x1-plantas-e07.mp4` e a decisão do Conselho que o código (`principal-e07/montar_e07.cjs`, `blueprint.html`) segue.

> Pedido do dono (21/11/2026): vídeo curto, cada quadro pensado, começando do blueprint com efeito (o azul não fica parado), referências populares do Brasil dentro da casa, OpenArt com as ferramentas novas (plano Pro, 24.000 créditos), casa detalhada antes de gerar (serve depois para o e-book), Conselho aprova antes, "capricha", estilo CONDOR ([`REFERENCIA-CONDOR.md`](REFERENCIA-CONDOR.md)). Música: [`musica/`](musica/) (original, 128 BPM).
> **Situação:** aprovado pelo Conselho em 21/11/2026, com as condições da seção 7. **Versão 2 pronta e aprovada pelo Revisor (21/11/2026; a v1 levou veto por marcas na sala e na cozinha, corrigido):** `video/saida/principal-e07/x1-plantas-e07.mp4` (15 s, 11,5 MB). Para montar de novo: `node video/principal-e07/render_blueprint.cjs` e `node video/principal-e07/montar_e07.cjs`.

## 1. A casa que o vídeo segue (fonte única)

**E07 Casa Estreita 3 Quartos**: 72 m², 3 quartos (1 suíte), 2 banheiros, 5,00 x 17,90 m, lote a partir de 8 x 25 m, recuos de 1,5 m dos dois lados, 3 m na frente e 1,5 m nos fundos; corredor coberto de 1 m na direita, dentro dos 5 m (é a passagem para todos os cômodos). Validada (`python3 ferramentas/plantas.py validar`). Da frente para os fundos: sala 15,2 m² → cozinha 11,2 m² → banheiro 4,4 m² + serviço 3,6 m² → quarto 12,0 m² → quarto 12,0 m² → suíte 8,9 m² + banho da suíte 4,3 m².

Tudo o que aparece no vídeo sai dessa planta: a prévia `ebook/plantas/previas/E07.png`, o 3D do motor próprio (`video/src/plantas/E07.js`, `broll/clipes/e07-3d.mp4`). As imagens realistas do OpenArt partem **sempre** de uma imagem nossa como referência (imagem → imagem), para portas, janelas e cômodos ficarem no mesmo lugar. Serve depois para a página da E07 no e-book.

## 2. Ritmo

128 BPM: 1 tempo = 0,469 s, 1 compasso = 1,875 s. **15 s = 8 compassos.** A trilha entra no compasso 3 dela (3,75 s), então o drop cai em **7,5 s** do vídeo. Todo corte cai num tempo.

## 3. Quadro a quadro

| Tempo | Música | Imagem | Texto na tela | Fonte |
|---|---|---|---|---|
| 0,00 | kick 1 | **Primeiro quadro:** folha de blueprint azul profundo com grade, papel com textura, e já com a pergunta. Uma linha de luz ciano varre a folha de cima para baixo (scanner), a grade tem paralaxe leve e o papel "respira" | **"3 quartos em 8 m de frente?"** (texto no 1º quadro, regra do CONDOR) | Nosso (blueprint animado em código) |
| 0,00–1,88 | intro | As paredes da E07 **se desenham no tempo do kick**: uma caneta de luz com faíscas risca cada parede; a cada batida entra um trecho. Cota "8 m" do lote pisca em amarelo | pergunta fica | Nosso |
| 1,88–3,75 | intro | Portas abrem o arco, janelas acendem em ciano. Câmera desliza da frente aos fundos | "5 m de construção" (cota cresce) | Nosso |
| 3,75–7,50 | subida | Nomes dos cômodos **pulam um por tempo**: SALA, COZINHA, BANHO, QUARTO, QUARTO, SUÍTE. Na caixa acelerando, os três quartos acendem em amarelo em sequência; a folha começa a tremer e a grade se curva | "3 quartos." *(batida)* "8 metros." *(batida)* | Nosso |
| 7,50 | **drop** | **A folha levanta:** o blueprint vira a casa em 3D, paredes sobem, a luz azul vira luz de fim de tarde | "Cabe em lote 8 x 25 m." | OpenArt vídeo (quadro inicial = blueprint nosso, final = humanizada) |
| 7,50–9,38 | drop | Voo de cima pela casa mobiliada (planta humanizada realista), da sala à suíte | "72 m² · 3 quartos · 2 banheiros" | OpenArt imagem→imagem + vídeo |
| 9,38–11,25 | drop | **2 detalhes de 2 tempos** (mudança do Editor: 0,94 s cada, para o público de 25 a 50 anos): (1) vira-lata caramelo deitado no sofá da sala; (2) filtro de barro, garrafa térmica de café e air fryer na bancada da cozinha (o morango do amor que estava aqui foi vetado pelo dono em 21/11) | sem texto (respiro) | OpenArt |
| 11,25–13,13 | drop | Fachada ao entardecer no lote de 8 m, com rede e bandeirinhas verde e amarelo no recuo (nunca no corredor de 1 m, que é a passagem), câmera recua até mostrar o lote inteiro | "Lote a partir de 8 x 25 m" | OpenArt (a partir do 3D nosso) |
| 13,13–15,00 | drop | Corte seco para o blueprint de novo, agora com a logo (versão de perfil, sem os nomes) e o carimbo "CASA VII" no canto; igual ao quadro 0 para o vídeo repetir sem salto (emenda o fim no começo, para o vídeo repetir) | **"Comenta PLANTA"** | Nosso |

**Em todas as cenas (versão de 21/11):** selo "Imagem ilustrativa" nas imagens geradas (o dono tirou o selo em 22/11; não repetir) e rodapé "Planta de referência. O projeto para a prefeitura é assinado por arquiteto ou engenheiro habilitado." (já sai do `montar.py`).

## 4. Referências brasileiras (sem marca, sem personagem de terceiros)

Vira-lata caramelo, air fryer, filtro de barro, garrafa térmica, rede, bandeirinhas verde e amarelo, futebol na TV (sem logo de time nem de canal), espada-de-são-jorge no vaso. Nada de marca, logo de clube ou personagem licenciado. Nada de morango do amor nem de batata (dono, 21/11). O Pesquisador confere se ainda estão em alta.

## 5. Passos e custo

| # | Passo | Ferramenta | Créditos (estimado) |
|---|---|---|---|
| 1 | Blueprint animado (0–7,5 s) e cartão final | Código nosso (Playwright + ffmpeg) | 0 |
| 2 | Planta humanizada realista da E07, vista de cima, a partir de `E07.png` | OpenArt imagem→imagem, modelo com até 14 referências e 4K (Nano Banana 2.1 ou Pro) | ~50–100 |
| 3 | 4 detalhes de interior + fachada, a partir do 3D nosso | OpenArt imagem→imagem 4K | ~250 |
| 4 | Transição blueprint → casa, voo pela casa e recuo da fachada | OpenArt imagem→vídeo com quadro inicial e final (Kling 3 Omni / Veo 3.1) | ~600–900 |
| 5 | Montagem no tempo da música, selos e rodapé | `video/montar.py` | 0 |
| 6 | Revisão: Arquiteto (bate com a planta), Revisor (aviso legal e promessa) | Subagentes | 0 |
| | **Total** | | **~1.000–1.300 de 24.000** |

Rascunho barato antes, final na melhor configuração (regra de qualidade do `CLAUDE.md`). As imagens finais vão para as pastas do OpenArt `X1 · Vídeo principal` e `X1 · E-book imagens`.

## 6. Decisões que ficam com o dono

Publicar; palavra da chamada (PLANTA ou LOTE). A E07 é planta do e-book (rascunho 1); a promessa "essa planta" segue a decisão em aberto no `CONTEXTO.md`.

## 7. Decisão do Conselho (21/11/2026)

```text
[Maestro MinoAI] SIM, SE o 1º segundo for contido e a pergunta ficar 5 s ou mais · fonte: "Mastering Viral Text Hooks" (texto de 5 a 10 s); coaching call 21/07/2026 (carga cognitiva no começo); call 18/03/2025 (montagem curta, som forte na transição)
[Editor]         SIM, SE a planta ficar parada e legível 1,5 s antes do drop e nenhum detalhe durar menos de 0,94 s · Kling (quadro inicial e final)
[Arquiteto]      SIM, SE corrigir "5 m de casa", "corredor externo" e a rede, e as imagens seguirem a lista de cômodos
[Revisor]        SIM, SE "Cabe" vier com o lote, selo em toda imagem gerada (inclusive vídeo), rodapé nunca coberto, sem marca/escudo/jogador, áudio dos modelos de vídeo removido
[Designer]       SIM, SE conferir quadro a quadro contra a E07 e o fim voltar ao 1º quadro · sem ciano neon; papel heliográfico com dobra, grade de 1 m, luz rasante
DECISÃO: aprovado com as condições. Nenhum veto.
```

**O que mudou por causa da mesa:**
- **0,00–0,94:** só a folha (papel respirando) e a pergunta. Luz rasante entra em 0,47; brilho da tinta em 0,94; paralaxe em 1,88.
- **Paleta:** fundo #0B4FA8 escurecendo para #06306A nas bordas, traço branco-giz 85%, destaque só #FFC857. Sem ciano. Grade de 1 m em escala real.
- **0,00–5,63:** a pergunta fica no alto; em 3,75 encolhe e "3 quartos." e "8 metros." entram embaixo.
- **3,75–6,56:** planta parada e legível; tremor e grade curvando só em 6,56–7,50; a luz esquenta para emendar com o fim de tarde.
- **7,50:** um "8" gigante e estreito abre como janela (conceito 3 do CONDOR) e a casa aparece por dentro dele.
- **Interior:** luz lateral de fim de tarde (3.500–4.000 K), lente 24–28 mm a 1,5 m, piso cerâmico bege, parede branco-gelo, MDF amadeirado, janela de alumínio com grade, sinais de casa vivida; nada de catálogo.
- **Cada imagem gerada** segue a lista de cômodos do Arquiteto (porta, janela e móveis no lugar da planta; suíte não aparece maior). Áudio dos clipes gerados é descartado; a trilha é a nossa.
- **Logo no vídeo:** versão de perfil (sem os nomes). "DOMINIC & DAVI" só com autorização por escrito dos dois.

## 8. Versão 3 "Grupo da família" (roteiro esperando o dono)

Pedido do dono (21/11, noite): ironia com a família brasileira e referências o mais recentes possível. Roteiro completo, fontes e cuidados: [documento do dono](https://claude.ai/artifact/Lr8SvUJPmvcZ5JAZvzywNU).

- **Abertura:** balão genérico "GRUPO DA FAMÍLIA · Tio Zé: 3 quartos em 8 m de frente? Não cabe nem a família no Natal kkkk" sobre o blueprint (já feito no `blueprint.html`).
- **Cenas novas no drop:** almoço de domingo na cozinha (5 pessoas e o caramelo), onigiri na bancada (trend de novembro; sai o morango do amor, que é de 2025), fachada com luz rosa de GTA (sem nada do jogo).
- **Fecho:** "Cabe. Print enviado no grupo", depois "Comenta PLANTA".
- **Falta:** aprovação do dono, animar 3 cenas (~525 créditos), montar, Revisor.


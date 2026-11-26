# Os 9 primeiros posts, prontos para o editor

> **22/11/2026:** as imagens, clipes e renders citados aqui foram apagados para refazer do zero com a C01 nova (ficam no histórico do git). Os nomes de arquivo abaixo ficaram como referência, sem link.

> Parte da pasta Instagram. Guia da frente: [`../INSTAGRAM.md`](../INSTAGRAM.md). Plano do perfil: [`../INSTAGRAM.md`](../INSTAGRAM.md#plano-de-conteúdo-perfil-de-arquitetura-no-instagram). Calendário: [`../INSTAGRAM.md`](../INSTAGRAM.md#calendário-as-2-primeiras-semanas-do-perfil).
>
> Para cada post: legenda final (copiar e colar), texto de cada tela, imagens e, nos reels, o roteiro.
> As imagens dos carrosséis já estão geradas em `imagens/`. Onde falta a planta em 3D, a tela sai com um aviso amarelo **FALTA O 3D**.

## C01 redesenhada em 22/11/2026: o que vale agora

- **Casa Compacta (C01): 51 m², 2 quartos, 1 banheiro, cabe num lote de 8 x 15 m (no mínimo 8,0 x 13,0 m), melhor com a rua ao sul** ([`PLANTAS.md`](../../ebook/plantas/PLANTAS.md)). Sem corredor comprido: um hall curto distribui, a varanda recebe e o banheiro passa de 1,80 m de largura. A varanda encosta na divisa da esquerda; o banheiro tem prumada própria (custa mais).
- **Toda imagem da C01 nesta pasta é do desenho antigo** (`imagens/`, gerada em 20/11, antes do redesenho): posts 2 (tela 2), 3, 6, 8, 9 e a reserva estão marcados **refazer: C01 redesenhada**. Gere as imagens 2D da C01 de novo e rode o gerador antes de publicar. Os textos das telas que ficam dentro do `gerar-imagens.cjs` também são do desenho antigo.

## Ajustes depois da estratégia (20/11/2026)

Estes posts foram feitos antes das 24 plantas validadas. O que mudou:

- **Os números das plantas agora vêm do validador** ([`../../ebook/plantas/PLANTAS.md`](../../ebook/plantas/PLANTAS.md)): Casa Compacta 51 m², 2 quartos, 1 banheiro, cabe num lote de 8 x 15 m (no mínimo 8,0 x 13,0 m) (desde 23/11); Casa Fita 56 m², 2 quartos, 1 banheiro, cabe num lote de 5 x 25 m (no mínimo 5,0 x 20,6 m); Casa Família Compacta 71 m², 3 quartos, 1 banheiro, cabe num lote de 10 x 15 m (no mínimo 10,0 x 12,8 m). Os textos do gerador ainda são da E01 e da F03 (passo F20). **Confira cada legenda abaixo contra a ficha antes de publicar.**
- **As imagens dos carrosséis agora saem das plantas validadas em 2D** (`animacoes-3d/plantas-2d/`, geradas por `python3 ferramentas/imagens2d.py C01 E03 F01`), em 2160 x 2700. O 3D antigo da Casa Compacta não é mais usado.
- **Os vídeos 3D da Casa Compacta (posts 1 e 6) são do desenho antigo**, que tem outro layout. Não publique até o 3D novo sair (último passo). Use no lugar as páginas do e-book: [`../../ebook/visual/mockups/`](../../ebook/visual/mockups) e o B-roll `../../video/broll/clipes/ebook-folheando.mp4`.
- **"O que o arquiteto pensou" não se usa mais** (decisão do Revisor de risco): diga "por que esta planta é assim" até um arquiteto assinar as plantas.
- **Post novo sugerido pelo Diretor (MinoAI Frontier):** reel com o gancho "Me fala a frente do seu lote que em 10 segundos eu te mostro quais casas cabem nele", mostrando a fita métrica da capa e o B-roll do e-book.
- **Imagens geradas (fachada realista, ambientes):** feitas pela MinoAI com o OpenArt ([`../../animacoes-3d/OPENART-MINOAI.md`](../../animacoes-3d/OPENART-MINOAI.md)).

## Resumo

| # | Formato | Tema | Imagens | Situação |
|---|---|---|---|---|
| 1 | Reel | Passeio 3D da Casa Compacta | `animacao.mp4` + capa | **Espera o vídeo:** use o B-roll `video/broll/clipes/ebook-folheando.mp4` ou espere o 3D novo |
| 2 | Carrossel (6) | Três plantas lado a lado | `imagens/post-02-tres-plantas/` | **Refazer imagem:** tela 2 (C01 redesenhada) e telas 1, 3 e 4 (Casa Fita E03 e Casa Família Compacta F01 no lugar de E01 e F03) |
| 3 | Carrossel (7) | Como ler uma planta baixa | `imagens/post-03-como-ler-planta/` | **Refazer: C01 redesenhada** (as 7 telas usam a planta antiga) |
| 4 | Reel | Passeio 3D da Casa Fita | capa em `imagens/capas-reels/` | **Espera o vídeo:** idem. **Refazer imagem:** a capa é da E01 |
| 5 | Carrossel (5) | Checklist antes de contratar o pedreiro | `imagens/post-05-checklist-pedreiro/` | **Pronto** |
| 6 | Reel | Bastidor: a planta virando 3D | imagens da Casa Compacta + capa | **Espera o 3D novo** (é um reel de bastidor do 3D) |
| 7 | Imagem | Casa Família Compacta, vista 3D | `imagens/post-07-casa-familia/` | **Refazer: F01** (refazer imagem: a que existia era da F03) |
| 8 | Carrossel (5) | 3 erros comuns na planta | `imagens/post-08-erros-comuns/` | **Refazer: C01 redesenhada** (recortes da planta antiga) |
| 9 | Reel | O material gratuito | imagens da Casa Compacta + capa | **Refazer: C01 redesenhada** (as imagens e a animação são da casa antiga) |
| R | Carrossel (6) | Reserva: Casa Compacta completa | `imagens/reserva-casa-compacta/` | **Refazer: C01 redesenhada** |

A 3D parada da E03 Casa Fita e da F01 Casa Família Compacta já existe (`ebook/visual/3d/E03.jpg`, `F01.jpg`); falta a animação de cada uma (chat de Animações 3D) e o gerador ler as 3 casas (F20).

> O post 3 estava como "Imagem" no plano, mas o plano também pede "uma dica por slide". Virou carrossel.
> O post 7 pede a "fachada". O motor 3D hoje faz a casa com as paredes cortadas a 1,1 m, vista de cima. Usamos a `03-perspectiva.png`. Uma fachada de verdade (vista da rua, paredes inteiras, telhado) exige ajuste no motor: pedir ao chat de **Animações 3D** se quiser.

## Como gerar as imagens de novo

Na raiz do projeto:

```bash
NODE_PATH=$(npm root -g) node instagram/posts/gerar-imagens.cjs
```

Para gerar um post só, passe parte do nome: `... gerar-imagens.cjs post-02`. Os textos das telas estão no próprio [`gerar-imagens.cjs`](gerar-imagens.cjs). No fim, o script lista as imagens de planta que ainda faltam.

Telas de 1080 x 1350 (4:5, o tamanho máximo do feed). Capas de reel com 1080 x 1920; o texto fica no meio, dentro da parte que aparece na grade do perfil.

## Regras que valem para todas as legendas

- Sempre área, quartos e banheiros quando falar de uma planta.
- Nada de prazo de obra, economia exata ou aprovação na prefeitura.
- Até 5 hashtags. Base: `#plantadecasa #plantabaixa #casapropria #construcao #arquitetura`.
- Todo post com planta leva a linha: *Planta de referência, não é projeto executivo. A obra precisa de responsável técnico.* (as telas já trazem essa linha em letra miúda).
- Chamada final sempre igual: **Comente PLANTA**. Quem responde no WhatsApp é o parceiro ([`../../ebook/vendas/WHATSAPP.md`](../../ebook/vendas/WHATSAPP.md)). Combine com ele a resposta automática ao comentário antes de publicar o primeiro post.

---

## Post 1 · Reel · Passeio 3D da Casa Compacta

**Material:** `animacao.mp4` (12 s, vertical) e `03-perspectiva.png`. Capa: `imagens/capas-reels/post-01-reel-passeio-compacta.png`.

**Texto fixo no alto (o vídeo todo):** Você consegue ver a casa antes de construir?

**Roteiro (15 s, sem apresentador; só texto e música baixa sem letra):**

| Tempo | Na tela | Legenda no meio (blocos de 2 a 3 palavras, chave em amarelo) |
|---|---|---|
| 0:00 a 0:04 | `animacao.mp4` do início: o blueprint se desenhando | "essa é a **planta**" · "de 51 m²" |
| 0:04 a 0:06 | Cômodos ganhando piso e móveis | "agora ela" · "**ganha vida**" |
| 0:06 a 0:12 | Câmera deslizando sobre a casa 3D | "2 quartos" · "1 banheiro" · "sala e cozinha **juntas**" |
| 0:12 a 0:15 | `03-perspectiva.png` parada, zoom lento, ficha embaixo: "Casa Compacta · 51 m² · cabe num lote de 8 x 15 m (no mínimo 8,0 x 13,0 m)" | "quer ver a sua **antes**?" · "comente **PLANTA**" |

Se o apresentador já tiver gravado, a versão com rosto é melhor: ele fala por cima "Antes de gastar um tijolo, olha a casa pronta. Comenta PLANTA que eu te mando essa planta de graça."

**Legenda:**

```
Dá pra ver a casa pronta antes do primeiro tijolo. 🏠

Essa é a Casa Compacta:
📐 51 m²
🛏️ 2 quartos
🚿 1 banheiro
📏 cabe num lote de 8 x 15 m (no mínimo 8,0 x 13,0 m)

Sem corredor comprido: um hall curto distribui, a varanda cobre a porta da sala e o banheiro passa de 1,80 m de largura. Tudo em escala, com os móveis no lugar.

Quer receber essa planta humanizada de graça? Comente PLANTA que eu te mando no WhatsApp.

Planta de referência, não é projeto executivo. A obra precisa de responsável técnico.

#plantadecasa #plantabaixa #casapropria #construcao #arquitetura
```

---

## Post 2 · Carrossel · Três plantas lado a lado

**Imagens:** `imagens/post-02-tres-plantas/` (01 a 06). **Refazer imagem** (telas 1, 3 e 4): o gerador `gerar-imagens.cjs` ainda desenha a E01 Casa Estreita e a F03 Casa Família, fora do lançamento, e as imagens foram apagadas em 22/11; trocar pela E03 e pela F01.

| Tela | Texto |
|---|---|
| 1 | *compare antes de escolher* · **3 casas, 3 terrenos. Qual cabe no seu?** · miniaturas com o lote: 8 x 15 (51 m²), 5 x 25 (56 m²), 10 x 15 (71 m²) · "Área, quartos e o terreno mínimo de cada uma." |
| 2 | *planta 1 de 3 · C01* · **Casa Compacta** · 51 m² · 2 quartos · 1 banheiro · cabe num lote de 8 x 15 m (no mínimo 8,0 x 13,0 m) · Destaque: sem corredor comprido, um hall curto distribui e a varanda recebe. **Refazer: C01 redesenhada** (imagem da planta antiga) |
| 3 | *planta 2 de 3 · E03* · **Casa Fita** · 56 m² · 2 quartos · 1 banheiro · cabe num lote de 5 x 25 m (no mínimo 5,0 x 20,6 m) · Destaque: um quarto em cada ponta, sala e copa no meio, banheiro dentro de casa. |
| 4 | *planta 3 de 3 · F01* · **Casa Família Compacta** · 71 m² · 3 quartos · 1 banheiro · cabe num lote de 10 x 15 m (no mínimo 10,0 x 12,8 m) · Destaque: os 3 quartos nos fundos, longe da rua, e sala com mesa de 4. |
| 5 | *lado a lado* · **Qual combina com o seu terreno?** · tabela: área, quartos, banheiros, lote mínimo, para quem · "Os recuos mudam de cidade para cidade: confira na sua prefeitura." |
| 6 | *planta grátis* · **Quer essa planta?** · Comente PLANTA · "e eu te mando a planta humanizada da Casa Compacta de graça no WhatsApp." |

**Legenda:**

```
Antes de escolher a planta, olhe o terreno. 📏

Casa Compacta: 51 m², 2 quartos, 1 banheiro. Cabe num lote de 8 x 15 m (no mínimo 8,0 x 13,0 m).
Casa Fita: 56 m², 2 quartos, 1 banheiro. Cabe num lote de 5 x 25 m (no mínimo 5,0 x 20,6 m).
Casa Família Compacta: 71 m², 3 quartos, 1 banheiro. Cabe num lote de 10 x 15 m (no mínimo 10,0 x 12,8 m).

Arrasta para ver cada uma e a comparação no final.

Qual dessas cabe no seu terreno? Me conta nos comentários a frente e o fundo do seu lote.

Quer a planta humanizada da Casa Compacta de graça? Comente PLANTA.

Plantas de referência, não são projeto executivo. A obra precisa de responsável técnico. Os recuos mudam de cidade para cidade.

#plantadecasa #plantabaixa #casapropria #terreno #arquitetura
```

---

## Post 3 · Carrossel · Como ler uma planta baixa

**Imagens:** `imagens/post-03-como-ler-planta/` (01 a 07). Todas com o blueprint e a planta humanizada da Casa Compacta. **Refazer: C01 redesenhada** (as telas mostram a planta antiga).

| Tela | Texto | Imagem |
|---|---|---|
| 1 | *salve para consultar* · **Como ler uma planta baixa em 1 minuto** | Blueprint inteiro |
| 2 | *dica 1 de 5* · **A cota é a medida** · "A linha azul embaixo da casa, com um traço em cada ponta, mostra a largura em metros: aqui, 6,50 m. A linha do lado mostra o fundo: 8,50 m." | Recorte da cota de baixo (a da largura), em amarelo |
| 3 | *dica 2 de 5* · **Amarelo é a porta de entrada** · "É por ali que você entra da rua. Na planta com móveis, o arco de cada porta mostra para que lado ela abre: esse espaço fica livre, nada de móvel ali." | Porta de entrada (o retângulo amarelo) marcada |
| 4 | *dica 3 de 5* · **Azul é janela** · "Cada retângulo azul na parede é uma janela. Confira se cada quarto tem a sua." | Janelas da sala e da cozinha marcadas |
| 5 | *dica 4 de 5* · **O m² é a área do cômodo** · "9,4 m² quer dizer um quarto de cerca de 2,90 x 3,20 m. Compare com o quarto onde você dorme hoje." | Quarto casal em amarelo (medidas livres do validador, `ebook/plantas/dados/C01.json`) |
| 6 | *dica 5 de 5* · **Planta humanizada** · "É a mesma planta com piso e móveis em escala. Fica fácil ver como cada cômodo vai ser usado." | Planta humanizada |
| 7 | *planta grátis* · **Quer treinar numa planta de verdade?** · Comente PLANTA | Miniaturas |

**Legenda:**

```
Planta baixa parece desenho de engenheiro, mas dá pra ler em 1 minuto. 📐

1. A cota é a medida
2. Amarelo é a porta de entrada (e, na planta com móveis, o arco mostra para onde cada porta abre)
3. Azul é janela
4. O m² é a área de cada cômodo
5. A planta humanizada mostra os móveis em escala

Salve para olhar de novo quando receber a planta da sua casa.

A planta do exemplo é a Casa Compacta: 51 m², 2 quartos, 1 banheiro.
Quer ela inteira, de graça? Comente PLANTA que eu te mando no WhatsApp.

Planta de referência, não é projeto executivo. A obra precisa de responsável técnico.

#plantadecasa #plantabaixa #casapropria #construcao #arquitetura
```

---

## Post 4 · Reel · Passeio 3D da Casa Fita

**Refazer imagem:** o gerador `gerar-imagens.cjs` ainda desenha a E01 Casa Estreita e a F03 Casa Família, fora do lançamento, e as imagens foram apagadas em 22/11 (a capa `imagens/capas-reels/post-04-reel-casa-estreita.png` é da E01); trocar pela E03 Casa Fita (casa em 3D parada: `ebook/visual/3d/E03.jpg`). Não existe animação de nenhuma casa: o `animacao.mp4` do roteiro ainda não existe.

**Formato:** "É possível…?" ([`../MINOAI-FRONTIER.md`](../MINOAI-FRONTIER.md#referências-de-vídeo-mino-lee-minoleemp4), reel 1).

**Texto fixo no alto:** É possível 2 quartos num lote de 5 metros de frente?

**Roteiro (15 s):**

| Tempo | Na tela | Legenda |
|---|---|---|
| 0:00 a 0:03 | Retângulo do lote 5 x 25 m se desenhando, a frente de 5 m destacada em amarelo | "**5 metros**" · "de frente" · "por 25 de fundo" |
| 0:03 a 0:06 | `animacao.mp4`: o blueprint se desenha dentro do lote | "2 quartos" · "1 banheiro" · "**cabe?**" |
| 0:06 a 0:12 | A casa ganha vida; câmera desliza da frente aos fundos | "um quarto" · "em **cada ponta**" · "sala e copa **no meio**" |
| 0:12 a 0:15 | Perspectiva parada + ficha: "Casa Fita · 56 m² · cabe num lote de 5 x 25 m (no mínimo 5,0 x 20,6 m)" | "cabe, com os" · "recuos de referência" · "comente **PLANTA**" |

Canto da tela, o vídeo todo, parado: Planta de referência, não é projeto executivo. A obra precisa de responsável técnico.

**Legenda:**

```
Terreno estreito não precisa virar casa apertada. 📏

Casa Fita:
📐 56 m²
🛏️ 2 quartos
🚿 1 banheiro
📏 cabe num lote de 5 x 25 m (no mínimo 5,0 x 20,6 m), com os recuos de referência

O segredo é um quarto em cada ponta, com a sala e a copa no meio. Sala, cozinha e quartos têm janela para fora, mesmo com só 5 m de frente.

Tem terreno estreito? Me conta a medida nos comentários.
Quer a planta humanizada da Casa Compacta de graça? Comente PLANTA.

Planta de referência, não é projeto executivo. A obra precisa de responsável técnico. Os recuos mudam de cidade para cidade: confira na sua prefeitura.

#plantadecasa #terrenoestreito #casapropria #construcao #arquitetura
```

---

## Post 5 · Carrossel · Checklist antes de contratar o pedreiro

**Imagens:** `imagens/post-05-checklist-pedreiro/` (01 a 05). Só texto, não depende de planta.

| Tela | Texto |
|---|---|
| 1 | *salve para usar na obra* · **Antes de contratar o pedreiro, confira estes 8 itens** |
| 2 | *documentos* · 1. Projeto com responsável técnico: arquiteto ou engenheiro, com ART ou RRT. · 2. Alvará da prefeitura: antes de começar a obra, não depois. · 3. Recuos do seu lote conferidos: cada prefeitura tem a sua regra. |
| 3 | *escolher quem faz* · 4. 3 orçamentos com a mesma planta: só assim dá para comparar preço. · 5. Uma obra dele visitada: converse com o dono da casa. · 6. Contrato escrito: o que está incluído, o prazo e o que acontece se atrasar. |
| 4 | *pagamento e material* · 7. Pagamento por etapa pronta: nunca a obra toda adiantada. · 8. Quem compra o material: e quem confere o que chegou. |
| 5 | *lista completa* · **Tire print e leve para a conversa** · os 8 itens · Comente PLANTA |

**Legenda:**

```
Salve esse post antes de fechar com o pedreiro. ✅

1. Projeto com responsável técnico (ART ou RRT)
2. Alvará da prefeitura antes de começar
3. Recuos do seu lote conferidos
4. 3 orçamentos com a mesma planta
5. Uma obra dele visitada
6. Contrato escrito, com prazo
7. Pagamento por etapa pronta
8. Combinar quem compra e quem confere o material

Faltou algum item que você aprendeu na prática? Escreve nos comentários.

Ainda não tem a planta? Comente PLANTA que eu te mando uma planta humanizada de graça no WhatsApp.

#construcao #obra #casapropria #plantadecasa #reforma
```

---

## Post 6 · Reel · Bastidor: a planta virando 3D

**Refazer: C01 redesenhada.** **Material:** as 4 imagens e a animação da Casa Compacta em `../../animacoes-3d/plantas/casa-compacta/` (do desenho antigo: gere de novo com `node render-planta.cjs --planta C01`). Opcional: gravação de tela do arquivo de dados `../../video/src/planta.js` aberto no editor de código (10 s rolando a tela bastam). Capa: `imagens/capas-reels/post-06-reel-bastidor.png`.

**Formato:** POV bastidor ([`../MINOAI-FRONTIER.md`](../MINOAI-FRONTIER.md#referências-de-vídeo-mino-lee-minoleemp4), reel 3).

**Texto fixo no alto:** POV: transformando uma planta em casa 3D

**Roteiro (15 s, cortes rápidos com movimento de câmera entre as etapas):**

| Tempo | Na tela | Legenda |
|---|---|---|
| 0:00 a 0:03 | Gravação de tela de `planta.js` rolando (ou o blueprint com zoom rápido) | "tudo começa" · "com **medidas**" |
| 0:03 a 0:06 | `01-blueprint.png`, zoom lento | "vira o **blueprint**" · "com as cotas" |
| 0:06 a 0:09 | `02-planta-humanizada.png` | "ganha piso" · "e **móveis**" |
| 0:09 a 0:13 | `animacao.mp4` dos 6 aos 10 s (câmera deslizando) | "e vira **casa 3D**" |
| 0:13 a 0:15 | `04-perspectiva-lateral.png` | "comente **PLANTA**" · "e receba essa" |

**Legenda:**

```
De um arquivo de medidas a uma casa 3D. 🧱➡️🏠

É assim que cada planta é feita: primeiro as medidas, depois o blueprint com cotas, depois piso e móveis em escala, e por fim a casa em 3D.

Essa é a Casa Compacta: 51 m², 2 quartos, 1 banheiro, cabe num lote de 8 x 15 m (no mínimo 8,0 x 13,0 m).

Quer receber essa planta de graça? Comente PLANTA.

Planta de referência, não é projeto executivo. A obra precisa de responsável técnico.

#plantadecasa #arquitetura #projeto3d #casapropria #construcao
```

---

## Post 7 · Imagem · Casa Família Compacta

**Imagem:** `imagens/post-07-casa-familia/01.png`. **Refazer imagem:** o gerador `gerar-imagens.cjs` ainda desenha a E01 Casa Estreita e a F03 Casa Família, fora do lançamento, e as imagens foram apagadas em 22/11; trocar pela F01 Casa Família Compacta (casa em 3D: `ebook/visual/3d/F01.jpg`).

| Tela | Texto |
|---|---|
| 1 | Perspectiva 3D em tela cheia; faixa embaixo: **Casa Família Compacta** · 71 m² · 3 quartos · 1 banheiro · cabe num lote de 10 x 15 m (no mínimo 10,0 x 12,8 m), com os recuos de referência · no canto: Planta de referência, não é projeto executivo. A obra precisa de responsável técnico. · selo **Imagem ilustrativa** |

**Legenda:**

```
Casa Família Compacta: 3 quartos em 71 m². 🏡

📐 71 m²
🛏️ 3 quartos
🚿 1 banheiro
📏 cabe num lote de 10 x 15 m (no mínimo 10,0 x 12,8 m), com os recuos de referência

Os 3 quartos ficam nos fundos, longe da rua. Na sala cabe a mesa de 4, e o serviço tem porta para fora, para a faixa livre de 1,5 m ao lado da casa (recuo de referência).

Você moraria nessa? Comenta aqui o que mudaria.
Quer a planta humanizada da Casa Compacta de graça? Comente PLANTA.

Planta de referência, não é projeto executivo. A obra precisa de responsável técnico.

#plantadecasa #casapropria #casa3quartos #construcao #arquitetura
```

---

## Post 8 · Carrossel · 3 erros comuns na planta

**Imagens:** `imagens/post-08-erros-comuns/` (01 a 05). Recortes do blueprint da Casa Compacta, com a solução em amarelo. **Refazer: C01 redesenhada** (os recortes são da planta antiga; o texto abaixo já segue a nova).

| Tela | Texto | Imagem |
|---|---|---|
| 1 | *e como evitar cada um* · **3 erros na planta que saem caro na obra** | Blueprint inteiro |
| 2 | *erro 1 de 3* · **Corredor comprido** · ✕ Corredor custa por metro, e ninguém mora nele. · ✓ Na Casa Compacta não há corredor comprido: um hall curto distribui para os quartos e o banheiro. | Sala e passagem em amarelo |
| 3 | *erro 2 de 3* · **Banheiro de frente pra sala** · ✕ Quem está na sala vê a porta do banheiro. · ✓ A porta do banheiro não abre para a sala. | Porta do banho em amarelo |
| 4 | *erro 3 de 3* · **Banheiro sem janela** · ✕ Sem ventilação natural, o mofo aparece rápido. · ✓ Janela alta na parede de fora: ventila e mantém a privacidade. | Janela do banho em amarelo |
| 5 | *planta grátis* · **Quer a planta inteira, sem esses erros?** · Comente PLANTA | Miniaturas |

**Legenda:**

```
3 erros de planta que você só percebe depois da obra pronta. 👇

1. Corredor comprido: custa por metro e ninguém mora nele.
2. Banheiro de frente pra sala: o melhor é a porta não abrir pra sala.
3. Banheiro sem janela: sem ventilação natural, aparece mofo.

Na Casa Compacta (51 m², 2 quartos, 1 banheiro) os três estão resolvidos. Arrasta para ver onde.

Quer essa planta de graça? Comente PLANTA que eu te mando no WhatsApp.

Planta de referência, não é projeto executivo. A obra precisa de responsável técnico.

#plantadecasa #plantabaixa #casapropria #construcao #arquitetura
```

---

## Post 9 · Reel · O material gratuito

**Refazer: C01 redesenhada.** **Material:** as 4 imagens e a animação da Casa Compacta (gerar de novo: as atuais são do desenho antigo). Capa: `imagens/capas-reels/post-09-reel-material-gratis.png`. O que a pessoa recebe está em [`../../ebook/vendas/WHATSAPP.md`](../../ebook/vendas/WHATSAPP.md#planta-grátis-o-que-a-pessoa-recebe-depois-do-comentário-planta): o reel mostra exatamente isso, nada a mais.

**Texto fixo no alto:** Comente PLANTA e receba isto de graça

**Roteiro (18 s; com apresentador, se já tiver gravado; senão, só texto):**

| Tempo | Na tela | Fala / legenda |
|---|---|---|
| 0:00 a 0:03 | `02-planta-humanizada.png` entrando com zoom | "Essa planta é **sua**, de graça." |
| 0:03 a 0:06 | `01-blueprint.png` | "Vem com o **blueprint** e as medidas," |
| 0:06 a 0:10 | `03-perspectiva.png` e `04-perspectiva-lateral.png`, troca a cada 2 s | "a casa em **3D** dos dois lados," |
| 0:10 a 0:14 | `animacao.mp4` dos 6 aos 10 s | "e a animação da casa **ganhando vida**." |
| 0:14 a 0:18 | Ficha "Casa Compacta · 51 m² · 2 quartos · 1 banheiro" + botão amarelo "PLANTA" pulsando | "Comente **PLANTA** que eu te mando no WhatsApp." |

**Legenda:**

```
Tá aqui o que você recebe de graça. 🎁

✅ Planta humanizada, com móveis em escala
✅ Blueprint com as medidas principais (cotas)
✅ A casa em 3D, de dois ângulos
✅ A animação da casa ganhando vida

É a Casa Compacta: 51 m², 2 quartos, 1 banheiro, cabe num lote de 8 x 15 m (no mínimo 8,0 x 13,0 m).

Comente PLANTA que eu te mando no WhatsApp.

Planta de referência, não é projeto executivo. A obra precisa de responsável técnico.

#plantadecasa #plantabaixa #casapropria #construcao #arquitetura
```

---

## Reserva · Carrossel · Casa Compacta completa

**Imagens:** `imagens/reserva-casa-compacta/` (01 a 06). **Refazer: C01 redesenhada** (as 6 telas são da planta antiga). Use no lugar do post 2 ou do 7 se o 3D da Casa Fita ou da Casa Família Compacta não chegar a tempo.

| Tela | Texto |
|---|---|
| 1 | *planta da semana · C01* · **Casa Compacta: 51 m², 2 quartos** · ficha · planta humanizada |
| 2 | *a planta com medidas* · **Blueprint com cotas** |
| 3 | *a casa em 3D* · **Como ela fica por dentro** |
| 4 | *o outro lado* · **Sala, cozinha e quartos** |
| 5 | *por que funciona* · Sem corredor comprido: um hall curto distribui · Varanda cobrindo a porta da sala · Banheiro com mais de 1,80 m de largura |
| 6 | *planta grátis* · **Quer essa planta?** · Comente PLANTA |

**Legenda:**

```
Planta da semana: Casa Compacta. 🏠

📐 51 m²
🛏️ 2 quartos
🚿 1 banheiro
📏 cabe num lote de 8 x 15 m (no mínimo 8,0 x 13,0 m)

Por que ela funciona:
• sem corredor comprido: um hall curto distribui
• a varanda cobre a porta da sala, protegida da chuva e do sol
• o banheiro passa de 1,80 m de largura

Arrasta para ver o blueprint e a casa em 3D.
Quer receber de graça? Comente PLANTA.

Planta de referência, não é projeto executivo. A obra precisa de responsável técnico.

#plantadecasa #plantabaixa #casapropria #construcao #arquitetura
```

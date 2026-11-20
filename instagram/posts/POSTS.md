# Os 9 primeiros posts, prontos para o editor

> Parte da pasta Instagram. Guia da frente: [`../INSTAGRAM.md`](../INSTAGRAM.md). Plano do perfil: [`../plano-perfil.md`](../plano-perfil.md). Calendário: [`../calendario.md`](../calendario.md).
>
> Para cada post: legenda final (copiar e colar), texto de cada tela, imagens e, nos reels, o roteiro.
> As imagens dos carrosséis já estão geradas em [`imagens/`](imagens/). Onde falta a planta em 3D, a tela sai com um aviso amarelo **FALTA O 3D**.

## Ajustes depois da estratégia (20/11/2026)

Estes posts foram feitos antes das 24 plantas validadas. O que mudou:

- **Os números das plantas agora vêm do validador** ([`../../ebook/plantas/PLANTAS.md`](../../ebook/plantas/PLANTAS.md)): Casa Compacta 55 m² em lote a partir de 8 x 15; Casa Estreita 58 m², 2 quartos (1 suíte), lote a partir de 8 x 25; Casa Família 78 m², 3 quartos (1 suíte), lote a partir de 11 x 15. Os dados do gerador já foram corrigidos; **confira cada legenda abaixo contra a ficha antes de publicar.**
- **As imagens 3D da Casa Compacta (posts 1, 6, 9 e reserva) são do desenho antigo**, que tem outro layout. Não publique até o 3D novo sair (último passo). Use no lugar as páginas do e-book: [`../../ebook/visual/mockups/`](../../ebook/visual/mockups/) e o B-roll [`../../video/broll/ebook-folheando.mp4`](../../video/broll/ebook-folheando.mp4).
- **"O que o arquiteto pensou" não se usa mais** (decisão do Revisor de risco): diga "por que esta planta é assim" até um arquiteto assinar as plantas.
- **Post novo sugerido pelo maestro (MinoAI Frontier):** reel com o gancho "Me fala a frente do seu lote que em 10 segundos eu te mostro quais casas cabem nele", mostrando a fita métrica da capa e o B-roll do e-book.
- **Imagens geradas (fachada realista, ambientes):** feitas pela MinoAI com o OpenArt ([`../../animacoes-3d/OPENART-MINOAI.md`](../../animacoes-3d/OPENART-MINOAI.md)).

## Resumo

| # | Formato | Tema | Imagens | Situação |
|---|---|---|---|---|
| 1 | Reel | Passeio 3D da Casa Compacta | `animacao.mp4` + capa | **Pronto para editar** |
| 2 | Carrossel (6) | Três plantas lado a lado | [`imagens/post-02-tres-plantas/`](imagens/post-02-tres-plantas/) | **Falta 3D:** E01 Casa Estreita e F03 Casa Família |
| 3 | Carrossel (7) | Como ler uma planta baixa | [`imagens/post-03-como-ler-planta/`](imagens/post-03-como-ler-planta/) | **Pronto** |
| 4 | Reel | Passeio 3D da Casa Estreita | capa em [`imagens/capas-reels/`](imagens/capas-reels/) | **Falta 3D:** E01 Casa Estreita |
| 5 | Carrossel (5) | Checklist antes de contratar o pedreiro | [`imagens/post-05-checklist-pedreiro/`](imagens/post-05-checklist-pedreiro/) | **Pronto** |
| 6 | Reel | Bastidor: a planta virando 3D | imagens da Casa Compacta + capa | **Pronto para editar** |
| 7 | Imagem | Casa Família, vista 3D | [`imagens/post-07-casa-familia/`](imagens/post-07-casa-familia/) | **Falta 3D:** F03 Casa Família |
| 8 | Carrossel (5) | 3 erros comuns na planta | [`imagens/post-08-erros-comuns/`](imagens/post-08-erros-comuns/) | **Pronto** |
| 9 | Reel | O material gratuito | imagens da Casa Compacta + capa | **Pronto para editar** |
| R | Carrossel (6) | Reserva: Casa Compacta completa | [`imagens/reserva-casa-compacta/`](imagens/reserva-casa-compacta/) | **Pronto.** Entra no lugar do 2 ou do 7 se o 3D atrasar |

**O que falta de outra frente** (pedir ao chat de **Animações 3D**): gerar as plantas **E01 Casa Estreita** e **F03 Casa Família** em `animacoes-3d/plantas/casa-estreita/` e `animacoes-3d/plantas/casa-familia/`, com os 5 arquivos de sempre. Quando existirem, rode o gerador de novo (abaixo) e as telas saem com as imagens no lugar do aviso.

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
- Chamada final sempre igual: **Comente PLANTA**. Quem responde no WhatsApp é o parceiro ([`../../ebook/vendas/sequencia-whatsapp.md`](../../ebook/vendas/sequencia-whatsapp.md)). Combine com ele a resposta automática ao comentário antes de publicar o primeiro post.

---

## Post 1 · Reel · Passeio 3D da Casa Compacta

**Material:** [`animacao.mp4`](../../animacoes-3d/plantas/casa-compacta/animacao.mp4) (12 s, vertical) e [`03-perspectiva.png`](../../animacoes-3d/plantas/casa-compacta/03-perspectiva.png). Capa: [`imagens/capas-reels/post-01-reel-passeio-compacta.png`](imagens/capas-reels/post-01-reel-passeio-compacta.png).

**Texto fixo no alto (o vídeo todo):** Você consegue ver a casa antes de construir?

**Roteiro (15 s, sem apresentador; só texto e música baixa sem letra):**

| Tempo | Na tela | Legenda no meio (blocos de 2 a 3 palavras, chave em amarelo) |
|---|---|---|
| 0:00 a 0:04 | `animacao.mp4` do início: o blueprint se desenhando | "essa é a **planta**" · "de 55 m²" |
| 0:04 a 0:06 | Cômodos ganhando piso e móveis | "agora ela" · "**ganha vida**" |
| 0:06 a 0:12 | Câmera deslizando sobre a casa 3D | "2 quartos" · "1 banheiro" · "sala e cozinha **juntas**" |
| 0:12 a 0:15 | `03-perspectiva.png` parada, zoom lento, ficha embaixo: "Casa Compacta · 55 m² · lote a partir de 8 x 15 m" | "quer ver a sua **antes**?" · "comente **PLANTA**" |

Se o apresentador já tiver gravado, a versão com rosto é melhor: ele fala por cima "Antes de gastar um tijolo, olha a casa pronta. Comenta PLANTA que eu te mando essa planta de graça."

**Legenda:**

```
Dá pra ver a casa pronta antes do primeiro tijolo. 🏠

Essa é a Casa Compacta:
📐 55 m²
🛏️ 2 quartos
🚿 1 banheiro
📏 lote a partir de 8 x 15 m

Dois quartos do mesmo tamanho, serviço coberto e só 10% de corredor. Tudo em escala, com os móveis no lugar.

Quer receber essa planta humanizada de graça? Comente PLANTA que eu te mando no WhatsApp.

Planta de referência, não é projeto executivo. A obra precisa de responsável técnico.

#plantadecasa #plantabaixa #casapropria #construcao #arquitetura
```

---

## Post 2 · Carrossel · Três plantas lado a lado

**Imagens:** [`imagens/post-02-tres-plantas/`](imagens/post-02-tres-plantas/) (01 a 06). **Falta 3D:** E01 Casa Estreita e F03 Casa Família (telas 1, 3 e 4).

| Tela | Texto |
|---|---|
| 1 | *compare antes de escolher* · **3 casas, 3 terrenos. Qual cabe no seu?** · miniaturas com o lote: 8 x 15 (55 m²), 8 x 25 (58 m²), 11 x 15 (78 m²) · "Área, quartos e o terreno mínimo de cada uma." |
| 2 | *planta 1 de 3 · C01* · **Casa Compacta** · 55 m² · 2 quartos · 1 banheiro · lote a partir de 8 x 15 m · Destaque: 2 quartos iguais e serviço coberto, com pouco corredor. |
| 3 | *planta 2 de 3 · E01* · **Casa Estreita** · 58 m² · 2 quartos (1 suíte) · 2 banheiros · lote a partir de 8 x 25 m · Destaque: garagem na frente e todos os cômodos abrindo para o corredor coberto. |
| 4 | *planta 3 de 3 · F03* · **Casa Família** · 78 m² · 3 quartos (1 suíte) · 2 banheiros · lote a partir de 11 x 15 m · Destaque: suíte para o casal e varanda na frente. |
| 5 | *lado a lado* · **Qual combina com o seu terreno?** · tabela: área, quartos, banheiros, lote mínimo, para quem · "Os recuos mudam de cidade para cidade: confira na sua prefeitura." |
| 6 | *planta grátis* · **Quer essa planta?** · Comente PLANTA · "e eu te mando a planta humanizada da Casa Compacta de graça no WhatsApp." |

**Legenda:**

```
Antes de escolher a planta, olhe o terreno. 📏

Casa Compacta: 55 m², 2 quartos, 1 banheiro. Lote a partir de 8 x 15 m.
Casa Estreita: 58 m², 2 quartos (1 suíte), 2 banheiros. Lote a partir de 8 x 25 m.
Casa Família: 78 m², 3 quartos (1 suíte), 2 banheiros. Lote a partir de 11 x 15 m.

Arrasta para ver cada uma e a comparação no final.

Qual dessas cabe no seu terreno? Me conta nos comentários a frente e o fundo do seu lote.

Quer a planta humanizada da Casa Compacta de graça? Comente PLANTA.

Plantas de referência, não são projeto executivo. Os recuos mudam de cidade para cidade.

#plantadecasa #plantabaixa #casapropria #terreno #arquitetura
```

---

## Post 3 · Carrossel · Como ler uma planta baixa

**Imagens:** [`imagens/post-03-como-ler-planta/`](imagens/post-03-como-ler-planta/) (01 a 07). Todas com o blueprint e a planta humanizada da Casa Compacta.

| Tela | Texto | Imagem |
|---|---|---|
| 1 | *salve para consultar* · **Como ler uma planta baixa em 1 minuto** | Blueprint inteiro |
| 2 | *dica 1 de 5* · **A cota é a medida** · "A linha com um traço em cada ponta mostra a medida, em metros. Aqui, a casa tem 6,50 m de largura." | Recorte da cota de cima, em amarelo |
| 3 | *dica 2 de 5* · **O arco é a porta** · "Ele mostra para que lado a porta abre. Esse espaço precisa ficar livre: nada de móvel ali." | Porta de entrada em amarelo |
| 4 | *dica 3 de 5* · **Linha fina na parede é janela** · "Onde a parede vira linhas finas e duplas, há uma janela. Confira se cada quarto tem a sua." | Janelas da sala e da cozinha em amarelo |
| 5 | *dica 4 de 5* · **O m² é a área do cômodo** · "8,9 m² quer dizer um quarto de 3,30 x 2,70 m. Compare com o quarto onde você dorme hoje." | Quarto 2 em amarelo |
| 6 | *dica 5 de 5* · **Planta humanizada** · "É a mesma planta com piso e móveis em escala. Fica fácil ver como cada cômodo vai ser usado." | Planta humanizada |
| 7 | *planta grátis* · **Quer treinar numa planta de verdade?** · Comente PLANTA | Miniaturas |

**Legenda:**

```
Planta baixa parece desenho de engenheiro, mas dá pra ler em 1 minuto. 📐

1. A cota é a medida
2. O arco é a porta (e o espaço que ela precisa)
3. Linha fina na parede é janela
4. O m² é a área de cada cômodo
5. A planta humanizada mostra os móveis em escala

Salve para olhar de novo quando receber a planta da sua casa.

A planta do exemplo é a Casa Compacta: 55 m², 2 quartos, 1 banheiro.
Quer ela inteira, de graça? Comente PLANTA que eu te mando no WhatsApp.

#plantadecasa #plantabaixa #casapropria #construcao #arquitetura
```

---

## Post 4 · Reel · Passeio 3D da Casa Estreita

**Falta 3D:** E01 Casa Estreita (`animacao.mp4` e `03-perspectiva.png` em `animacoes-3d/plantas/casa-estreita/`). Capa já desenhada: [`imagens/capas-reels/post-04-reel-casa-estreita.png`](imagens/capas-reels/post-04-reel-casa-estreita.png) (sai com aviso até a planta existir).

**Formato:** "É possível…?" ([`../referencias-mino-lee.md`](../referencias-mino-lee.md), reel 1).

**Texto fixo no alto:** É possível 2 quartos e 2 banheiros em 8 m de frente?

**Roteiro (15 s):**

| Tempo | Na tela | Legenda |
|---|---|---|
| 0:00 a 0:03 | Retângulo do lote 8 x 25 m se desenhando, a frente de 8 m destacada em amarelo | "**8 metros**" · "de frente" |
| 0:03 a 0:06 | `animacao.mp4`: o blueprint se desenha dentro do lote | "2 quartos" · "2 banheiros" · "**cabe?**" |
| 0:06 a 0:12 | A casa ganha vida; câmera desliza ao longo do corredor lateral | "corredor **do lado**" · "luz natural" · "em **todos** os cômodos" |
| 0:12 a 0:15 | Perspectiva parada + ficha: "Casa Estreita · 58 m² · lote a partir de 8 x 25 m" | "cabe sim" · "comente **PLANTA**" |

**Legenda:**

```
Terreno estreito não precisa virar casa apertada. 📏

Casa Estreita:
📐 58 m²
🛏️ 2 quartos
🚿 2 banheiros
📏 lote a partir de 8 x 25 m

O segredo é o corredor na lateral: todos os cômodos ganham janela e luz natural, mesmo com só 8 m de frente.

Tem terreno estreito? Me conta a medida nos comentários.
Quer uma planta humanizada de graça? Comente PLANTA.

Planta de referência, não é projeto executivo. A obra precisa de responsável técnico.

#plantadecasa #terrenoestreito #casapropria #construcao #arquitetura
```

---

## Post 5 · Carrossel · Checklist antes de contratar o pedreiro

**Imagens:** [`imagens/post-05-checklist-pedreiro/`](imagens/post-05-checklist-pedreiro/) (01 a 05). Só texto, não depende de planta.

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

**Material:** as 4 imagens e a animação da Casa Compacta em [`../../animacoes-3d/plantas/casa-compacta/`](../../animacoes-3d/plantas/casa-compacta/). Opcional: gravação de tela do arquivo de dados [`../../video/src/planta.js`](../../video/src/planta.js) aberto no editor de código (10 s rolando a tela bastam). Capa: [`imagens/capas-reels/post-06-reel-bastidor.png`](imagens/capas-reels/post-06-reel-bastidor.png).

**Formato:** POV bastidor ([`../referencias-mino-lee.md`](../referencias-mino-lee.md), reel 3).

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

Essa é a Casa Compacta: 55 m², 2 quartos, 1 banheiro, lote a partir de 8 x 15 m.

Quer receber essa planta de graça? Comente PLANTA.

Planta de referência, não é projeto executivo. A obra precisa de responsável técnico.

#plantadecasa #arquitetura #projeto3d #casapropria #construcao
```

---

## Post 7 · Imagem · Casa Família

**Imagem:** [`imagens/post-07-casa-familia/01.png`](imagens/post-07-casa-familia/01.png). **Falta 3D:** F03 Casa Família (`03-perspectiva.png`). Até lá, a tela sai com aviso.

| Tela | Texto |
|---|---|
| 1 | Perspectiva 3D em tela cheia; faixa embaixo: **Casa Família** · 78 m² · 3 quartos (1 suíte) · 2 banheiros · lote a partir de 11 x 15 m |

**Legenda:**

```
Casa Família: espaço para todo mundo. 🏡

📐 78 m²
🛏️ 3 quartos
🚿 2 banheiros
📏 lote a partir de 11 x 15 m

Dois quartos perto do banheiro social e varanda nos fundos.

Você moraria nessa? Comenta aqui o que mudaria.
Quer uma planta humanizada de graça? Comente PLANTA.

Planta de referência, não é projeto executivo. A obra precisa de responsável técnico.

#plantadecasa #casapropria #casa3quartos #construcao #arquitetura
```

---

## Post 8 · Carrossel · 3 erros comuns na planta

**Imagens:** [`imagens/post-08-erros-comuns/`](imagens/post-08-erros-comuns/) (01 a 05). Recortes do blueprint da Casa Compacta, com a solução em amarelo. Os 3 erros são os itens 2, 3 e 4 do vídeo de anúncio, para o perfil e o anúncio falarem a mesma língua.

| Tela | Texto | Imagem |
|---|---|---|
| 1 | *e como evitar cada um* · **3 erros na planta que saem caro na obra** | Blueprint inteiro |
| 2 | *erro 1 de 3* · **Corredor comprido** · ✕ Corredor custa por metro, e ninguém mora nele. · ✓ Na Casa Compacta, só 10% da área é circulação: ela liga os quartos e o banheiro. | Hall em amarelo |
| 3 | *erro 2 de 3* · **Banheiro de frente pra sala** · ✕ Quem está na sala vê a porta do banheiro. · ✓ A porta do banho abre para a circulação, longe da sala. | Porta do banho em amarelo |
| 4 | *erro 3 de 3* · **Banheiro sem janela** · ✕ Sem ventilação natural, o mofo aparece rápido. · ✓ Janela alta na parede de fora: ventila e mantém a privacidade. | Janela do banho em amarelo |
| 5 | *planta grátis* · **Quer a planta inteira, sem esses erros?** · Comente PLANTA | Miniaturas |

**Legenda:**

```
3 erros de planta que você só percebe depois da obra pronta. 👇

1. Corredor comprido: custa por metro e ninguém mora nele.
2. Banheiro de frente pra sala: a porta tem que abrir pro hall.
3. Banheiro sem janela: sem ventilação natural, aparece mofo.

Na Casa Compacta (55 m², 2 quartos, 1 banheiro) os três estão resolvidos. Arrasta para ver onde.

Quer essa planta de graça? Comente PLANTA que eu te mando no WhatsApp.

Planta de referência, não é projeto executivo. A obra precisa de responsável técnico.

#plantadecasa #plantabaixa #casapropria #construcao #arquitetura
```

---

## Post 9 · Reel · O material gratuito

**Material:** as 4 imagens e a animação da Casa Compacta. Capa: [`imagens/capas-reels/post-09-reel-material-gratis.png`](imagens/capas-reels/post-09-reel-material-gratis.png). O que a pessoa recebe está em [`../../ebook/vendas/material-gratuito.md`](../../ebook/vendas/material-gratuito.md): o reel mostra exatamente isso, nada a mais.

**Texto fixo no alto:** Comente PLANTA e receba isto de graça

**Roteiro (18 s; com apresentador, se já tiver gravado; senão, só texto):**

| Tempo | Na tela | Fala / legenda |
|---|---|---|
| 0:00 a 0:03 | `02-planta-humanizada.png` entrando com zoom | "Essa planta é **sua**, de graça." |
| 0:03 a 0:06 | `01-blueprint.png` | "Vem com o **blueprint** e as medidas," |
| 0:06 a 0:10 | `03-perspectiva.png` e `04-perspectiva-lateral.png`, troca a cada 2 s | "a casa em **3D** dos dois lados," |
| 0:10 a 0:14 | `animacao.mp4` dos 6 aos 10 s | "e a animação da casa **ganhando vida**." |
| 0:14 a 0:18 | Ficha "Casa Compacta · 55 m² · 2 quartos · 1 banheiro" + botão amarelo "PLANTA" pulsando | "Comenta **PLANTA** que eu te mando no WhatsApp." |

**Legenda:**

```
Tá aqui o que você recebe de graça. 🎁

✅ Planta humanizada, com móveis em escala
✅ Blueprint com todas as medidas
✅ A casa em 3D, de dois ângulos
✅ A animação da casa ganhando vida

É a Casa Compacta: 55 m², 2 quartos, 1 banheiro, lote a partir de 8 x 15 m.

Comente PLANTA que eu te mando no WhatsApp.

Planta de referência, não é projeto executivo. A obra precisa de responsável técnico.

#plantadecasa #plantabaixa #casapropria #construcao #arquitetura
```

---

## Reserva · Carrossel · Casa Compacta completa

**Imagens:** [`imagens/reserva-casa-compacta/`](imagens/reserva-casa-compacta/) (01 a 06). Use no lugar do post 2 ou do 7 se o 3D da Casa Estreita ou da Casa Família não chegar a tempo.

| Tela | Texto |
|---|---|
| 1 | *planta da semana · C01* · **Casa Compacta: 55 m², 2 quartos** · ficha · planta humanizada |
| 2 | *a planta com medidas* · **Blueprint com cotas** |
| 3 | *a casa em 3D* · **Como ela fica por dentro** |
| 4 | *o outro lado* · **Sala, cozinha e quartos** |
| 5 | *por que funciona* · Sala e cozinha integradas · Hall de 2,2 m² em vez de corredor · Banheiro abre para o hall |
| 6 | *planta grátis* · **Quer essa planta?** · Comente PLANTA |

**Legenda:**

```
Planta da semana: Casa Compacta. 🏠

📐 55 m²
🛏️ 2 quartos
🚿 1 banheiro
📏 lote a partir de 8 x 15 m

Por que ela funciona:
• sala e cozinha integradas, a casa parece maior
• hall de 2,2 m² no lugar do corredor
• o banheiro abre para o hall, não para a sala

Arrasta para ver o blueprint e a casa em 3D.
Quer receber de graça? Comente PLANTA.

Planta de referência, não é projeto executivo. A obra precisa de responsável técnico.

#plantadecasa #plantabaixa #casapropria #construcao #arquitetura
```

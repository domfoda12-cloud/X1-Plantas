# Referência visual

> A linguagem visual e de animação, os livros de plantas com 3D e a análise de catálogos. Juntado em 22/11/2026 (ficha de organizar os arquivos): cada seção é um documento antigo, inteiro.

<!-- era: ebook/referencias/linguagem-visual-e-animacao.md -->
## Linguagem, visual e animação do e-book

> Parte da pasta E-book ([`../EBOOK.md`](../EBOOK.md)). Público e tom: [`MERCADO.md`](MERCADO.md) e [`../../ESTRATEGIA.md`](../../ESTRATEGIA.md). Formato de referência: [`VISUAL.md`](VISUAL.md).

### 1. Linguagem que convence sem enrolar

**Princípio:** falar com o Marcos como um vizinho que entende. Frase curta, número concreto, uma ideia por frase. Nada de "solução inovadora" nem "sonho da casa própria". Nada que prometa o que a planta não entrega.

| Em vez de | Escreva |
|---|---|
| "Realize o sonho da casa própria" | "Descubra que casa cabe no seu lote antes de gastar com laje" |
| "Plantas exclusivas e inovadoras" | "24 casas, cada uma conferida contra as medidas mínimas de quarto, cozinha e banheiro" |
| "Economize milhares com arquiteto" | "Chegue no seu engenheiro sabendo que casa você quer" |
| "Projeto completo para construir" | "Planta de referência para conversar com o seu engenheiro e o seu pedreiro" |
| "Casa barata" | "Casa compacta, que cabe no seu lote" ("por etapas" sai até as etapas serem desenhadas: dono, 23/11/2026) |
| "Aprovado" / "garantido" | Nunca. Aprovação é da prefeitura |

**Estrutura de cada página de casa** (cada frase abaixo deve caber em uma linha de celular):

1. **Gancho:** "8 m de frente. 2 quartos, varanda e banheiro largo. 50 m²." (C01; os ganchos de todas estão em [`../fichas/textos.py`](../fichas/textos.py), e o gerador recusa gancho que não bate com o validador)
2. **Promessa honesta:** "A casa que cabe no lote que você tem."
3. **Por que esta planta é assim** (3 pontos, de [`../plantas/PLANTAS.md`](../plantas/PLANTAS.md)).
4. **Para quem serve** e **para quem não serve** (honestidade vende: na C01, "Para quem não serve: quem quer suíte. Veja a C06").
5. **Leve ao seu engenheiro:** o que perguntar a ele (laje, fundação, recuo da sua cidade).

**Capa (como está no PDF):** "Que casa cabe no seu lote?" (provisório: o título é decisão do dono), "24 plantas de casas térreas" e "Casas organizadas pela frente do terreno". Aviso fixo no rodapé de cada casa: "Plantas de referência. O projeto para a prefeitura é assinado por arquiteto ou engenheiro habilitado."

**Ganchos de anúncio** (para testar, um por vídeo):
- "Tem um lote de 8 x 25? Essa casa cabe."
- "O erro de planta que o pedreiro não te conta: o corredor."
- "Antes de comprar a laje, veja se a cozinha cabe." (a cozinha precisa de 1,50 m livres)
- "Por que cozinha, banheiro e serviço ficam juntos?" (uma prumada só)
- "Antes do primeiro tijolo, mede a frente do seu lote. A casa certa começa nessa medida." (no lugar de "A casa que cresce… sem quebrar nada", da C03: em espera até ela ser redesenhada; dono, 23/11/2026)

### 2. Visual

Identidade: azul de projeto `#0B4FA8`, amarelo `#FFC857`, fundo quadriculado, títulos em Bricolage Grotesque, texto em Inter. É a que o gerador usa hoje (`../gerador/livro.css`).

| Elemento | Regra |
|---|---|
| **Planta de dados** (as prévias de [`../plantas/previas/`](../plantas/previas)) | Base da página: cada cômodo com nome e m², cotas externas, portas em amarelo, janelas em azul claro |
| **Planta mobiliada** | Mesmo desenho com móveis em escala, feito pelo gerador (`livro.py`) a partir do dado, nas 24 |
| **Vista da rua e casa em 3D** | Vista da rua: foto ilustrativa em 4 casas, desenho nas outras 20. Casa em 3D: imagem do nosso motor (`../visual/3d/`), do mesmo dado, nas 24. Nunca imagem com texto dentro |
| **Cotas** | Todas as medidas em metros, na própria imagem (como nos catálogos de porcelanato) |
| **Ícones** | Um sol, uma gota, uma seta de vento, na margem de cada ponto de "por que esta planta é assim" |
| **Cor por cômodo** | Mesma em todas as plantas (sala bege, cozinha verde, banheiro azul, quarto areia). O leitor aprende uma vez |

### 3. Animação: como incluir

Um PDF não toca vídeo. Opções, da mais simples para a mais completa:

| Opção | O que é | Esforço | Quando |
|---|---|---|---|
| **QR code por página** | Em cada casa, um QR que abre a animação de 12 s (blueprint que ganha vida) numa página simples | Médio. Nenhuma casa tem animação hoje: o vídeo antigo da C01 é do desenho de antes de 22/11/2026 | Frente de animações, depois do e-book |
| **Edição web** | O mesmo e-book em HTML (páginas que viram), com a animação tocando no lugar da imagem | Médio | Depois do 1º mês, se o QR funcionar |
| **GIF ou WebP curto** | O blueprint se desenhando em 3 s, para Instagram e anúncio | Baixo | Já, para anúncio |
| **Passeio 3D da casa** | Câmera dentro dos cômodos, para o anúncio | Alto | Só para a casa mais pedida |

**Como o motor 3D gera cada casa:** o dado de cada planta está em `ebook/plantas/dados/ID.json` (cômodos, janelas, portas). A imagem 3D parada já sai para qualquer casa (`python3 ferramentas/imagens3d.py ID`); a animação é da frente de animações. Ver [`../../animacoes-3d/ANIMACOES-3D.md`](../../animacoes-3d/ANIMACOES-3D.md).

**Roteiro de 12 s para cada casa** (testado na C01 antiga): 0–3 s o blueprint se desenha com as cotas; 3–7 s as paredes sobem; 7–10 s os móveis entram; 10–12 s a planta humanizada com o nome e a área.

### 4. O que ainda é decisão sua

- Título e preço (R$ 67 é recomendação da [estratégia](../../ESTRATEGIA.md), não decisão).
- Se o 1º lançamento sai com 12 ou com as 24 que já estão no PDF.
- Quem é o arquiteto que revisa e assina a declaração de revisão.

<!-- era: ebook/referencias/livros-de-plantas-com-3d.md -->
## Referência: livros de plantas com 3D e um guia de apresentação

> Pedido do dono (20/11/2026): "use a referência de um e-book famoso de qualidade, com animações 3D, como o que eu quero fazer; anote o que funciona, o que não funciona e o que deve ficar mais parecido. Se não for um e-book, um conjunto de instruções que você possa seguir." Última tarefa da frente **e-book**.

### 1. As referências (só o que as fontes mostraram)

| Referência | O que é | Fonte |
|---|---|---|
| **Ultimate Book of Home Plans**, 4ª ed. (Creative Homeowner) | Catálogo de 680 plantas, 609 páginas, 1.600 ilustrações. Tem uma seção com o app **3D Design America**, que "traz a planta da página para a vida no seu celular, em 3D". Na Amazon, nota 4,4 de 5 em 513 avaliações | [Amazon](https://amazon.com/Ultimate-Plans-Completely-Updated-Revised-ebook/dp/B09MWNXD4Q) |
| **The One-Story Barndominium Plan Book** (J. McDowell) | "50 plantas térreas em 3D com medidas reais e um guia para evitar erros de layout que saem caros". Aparece em 5º nos lançamentos mais vendidos de House Plans na Amazon. É o conceito mais parecido com o nosso. Não deu para ler o miolo: a Amazon bloqueou a leitura | [Amazon](https://www.amazon.com/One-Story-Barndominium-Plan-Book-Single-Level-ebook/dp/B0HNT6C1BC), [lista de lançamentos](https://amazon.com/gp/new-releases/books/5326) |
| **Guia de apresentação de plantas da Cedreo** | O conjunto de instruções: quais vistas mostrar, em que ordem e por quê, para quem não sabe ler planta | [Cedreo](https://cedreo.com/blog/floor-plan-presentation) |
| **Técnicas de apresentação da SMAARCHVIZ** | O que uma planta 2D boa precisa ter, e quando a planta 3D resolve | [SMAARCHVIZ](https://smaarchviz.com/floor-plan-presentation-techniques-for-architects) |

### 2. O que os leitores do Ultimate Book elogiam e criticam

Vem do resumo das avaliações na Amazon:

| Elogio | Crítica |
|---|---|
| Variedade ("tem para todo gosto") | **Plantas pequenas demais** na página (6 menções negativas de 7) |
| Detalhe e informação ("ótimo para construir do zero") | **Sem organização** por tamanho ou estilo: "a gente tem que folhear tudo" |
| As seções de dicas (fachada, área externa) | **Poucas casas pequenas** (85% acima de 2.000 pés², cerca de 186 m²) |
| | "Devia ter várias páginas para uma casa só" |

**Onde o nosso e-book já ganha:** as quatro críticas são exatamente o que ele resolve.
- A planta ocupa a página inteira.
- O livro é organizado pela frente do lote e pelo jeito da família.
- As 24 casas são pequenas, de 32 a 91 m².
- Cada casa tem duas páginas.

### 3. O conjunto de instruções (Cedreo e SMAARCHVIZ) e como o e-book cumpre cada uma

| # | Instrução | No e-book (rascunho 1) |
|---|---|---|
| 1 | Contar uma história, do geral ao detalhe: **o terreno, depois a planta, depois a imagem que dá vida** | Cumpre. O livro abre por "Ache pelo seu lote"; cada casa traz a planta e a casa no lote, com a ficha |
| 2 | Planta 2D com medidas, nome dos cômodos, **espessura de parede**, móveis em escala, **seta do norte** e cotas | Cumpre. Desde o rascunho 1 as paredes têm espessura (medida por fora, área por dentro), e a bússola fica no desenho do lote |
| 3 | **Planta 3D mobiliada, vista de cima com as paredes em pé**: "lê na hora quem não é arquiteto" e "cria a ligação emocional com a casa" | **Faltava. Entrou agora:** imagem 3D de cada casa, feita pelo nosso motor 3D, na página da casa |
| 4 | Vista de fachada (elevação) | Cumpre. Vista da rua: foto ilustrativa em 4 casas, desenho nas outras 20 |
| 5 | Planta de implantação, a casa no lote com recuos | Cumpre. O desenho do lote em cada casa |
| 6 | **Tabela de áreas** | Cumpre. A "Informação da casa": área fechada, coberta total, medidas, corredor, janela |
| 7 | **Destacar o que importa para o cliente** | Cumpre. Gancho, "Para quem é" e "Para quem não serve" |
| 8 | Corte, planta elétrica, projeto executivo | **Fica de fora, de propósito.** Isso é trabalho do engenheiro e do arquiteto, e pôr no livro daria a entender que a planta dispensa o profissional |
| 9 | Passeio em 3D e vídeo | Fica para a frente de **animação**: um QR em cada casa abre a animação, como o app do Ultimate Book |

### 4. O que deve ficar mais parecido com eles

1. **A planta 3D mobiliada (instrução 3).** É o maior ganho: aplicada agora, em todas as 24 casas.
2. **"Trazer a planta para a vida no celular".** É o recurso que diferencia o Ultimate Book. O nosso equivalente é o QR que abre a animação 3D da casa. Entra quando a frente de animação abrir; a imagem 3D já está nas 24, mas enquanto a animação não existir, o QR não vai para o livro.
3. **Fotos de casas construídas.** O Ultimate Book mostra "casas de verdade construídas a partir das plantas". A gente não tem nenhuma, e não vai fingir que tem: as imagens seguem com "Imagem ilustrativa". Quando um comprador construir e mandar foto, com autorização, ela entra.

### 5. O que não copiar

- **680 plantas sem ordem.** Mais casas não é melhor; o leitor se perde.
- **Planta pequena para caber muita casa por página.** É a crítica nº 1 dos leitores.
- **Venda de arquivo CAD para o leitor construir direto.** Contraria a nossa regra: a planta é de referência e o projeto é do profissional.

<!-- era: ebook/referencias/analise-catalogos-porcelanato.md -->
## Análise dos catálogos de porcelanato (referência de formato)

> Parte da pasta E-book ([`../EBOOK.md`](../EBOOK.md)). Cinco PDFs: cozinhas modernas, painéis e detalhes decorativos, nichos embutidos, ilhas e bancadas, áreas gourmet.

### O que eles são

Série "200 projetos modernos em porcelanato" (material profissional, catálogo digital, edição premium). **O público deles é o profissional que vende serviço** (marmoraria, revestimentista). O nosso é o dono da obra. O formato é bom; a mensagem é outra.

**Página padrão:** título numerado + uma linha de estilo → render grande com cotas em metros → planta baixa, vista frontal e vista lateral lado a lado (às vezes com escala) → caixas de detalhe → "Especificações técnicas" → "Passo a passo de execução" (6 a 9 passos) → sugestões de materiais, metais e iluminação com ícones → "Dicas importantes" → "Observações profissionais" → "Por que este projeto valoriza o serviço?" (3 pontos) → nota "medidas podem variar até 2 cm". Capa preta e dourada.

### O que adotar

| Do catálogo | Para o nosso e-book |
|---|---|
| Cotas escritas na própria imagem | Medidas em metros sobre a planta e a fachada. Quem constrói quer a medida na hora |
| Planta + vistas + especificações **na mesma página** | Página dupla: planta humanizada de um lado; fachada, cortes simples e ficha do outro |
| Páginas numeradas, uma ideia por página | Cada casa tem um número, um nome e uma frase curta |
| Caixas de dica e de observação | "por que esta planta é assim" em 3 pontos |
| "Por que valoriza o serviço" (3 pontos) | "Por que essa casa serve para o seu lote" (3 pontos) |
| Capa de alto contraste | Capa em azul de projeto com amarelo, a nossa identidade |

### O que NÃO copiar

1. **Texto ilegível dentro dos renders.** Há trechos como "Fancada e ølsolo" (Projeto 10): é geração de imagem com letra errada. Nosso texto é sempre real e revisado.
2. **A moldura "passo a passo de execução" e "material profissional".** Dá a entender projeto executivo, que a gente não entrega. Usamos "como a casa foi pensada" e "leve ao seu engenheiro".
3. **Preto e dourado.** Aqui é azul de projeto (#0B4FA8) e amarelo (#FFC857).
4. **Números sem prova.** "200 projetos" não foi verificado. Nosso número é o que existe e passa no validador: 24.
5. **Promessa de medida exata.** "Variações de até 2 cm" em obra vira reclamação. Nós dizemos: medidas de referência, conferir no terreno.

### O diferencial que eles não têm

**"por que esta planta é assim"**: em cada planta, três decisões explicadas (orientação, luz e ar, núcleo molhado, circulação, "a casa que cresce"; "ventilação cruzada" só depois de o arquiteto conferir, porque o validador não mede), com fonte nas regras de [`ARQUITETO.md`](ARQUITETO.md). Os catálogos mostram o resultado; o nosso e-book mostra o raciocínio. É o que o Marcos não consegue de um pedreiro.

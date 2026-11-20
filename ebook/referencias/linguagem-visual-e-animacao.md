# Linguagem, visual e animação do e-book

> Parte da pasta E-book ([`../EBOOK.md`](../EBOOK.md)). Público e tom: [`persona-e-mercado.md`](persona-e-mercado.md) e [`../../ESTRATEGIA.md`](../../ESTRATEGIA.md). Formato de referência: [`analise-catalogos-porcelanato.md`](analise-catalogos-porcelanato.md).

## 1. Linguagem que convence sem enrolar

**Princípio:** falar com o Marcos como um vizinho que entende. Frase curta, número concreto, uma ideia por frase. Nada de "solução inovadora" nem "sonho da casa própria". Nada que prometa o que a planta não entrega.

| Em vez de | Escreva |
|---|---|
| "Realize o sonho da casa própria" | "Descubra que casa cabe no seu lote antes de gastar com laje" |
| "Plantas exclusivas e inovadoras" | "24 casas, cada uma conferida contra as medidas mínimas de quarto, cozinha e banheiro" |
| "Economize milhares com arquiteto" | "Chegue no seu engenheiro sabendo que casa você quer" |
| "Projeto completo para construir" | "Planta de referência para conversar com o seu engenheiro e o seu pedreiro" |
| "Casa barata" | "Casa que você constrói por etapas" |
| "Aprovado" / "garantido" | Nunca. Aprovação é da prefeitura |

**Estrutura de cada página de casa** (cada frase abaixo deve caber em uma linha de celular):

1. **Gancho:** "8 m de frente. 2 quartos. 55 m²."
2. **Promessa honesta:** "A casa que cabe no lote que você tem."
3. **O que o arquiteto pensou** (3 pontos, de [`../plantas/PLANTAS.md`](../plantas/PLANTAS.md)).
4. **Para quem serve** e **para quem não serve** (honestidade vende: "Se você pretende subir um 2º andar, escolha a F03").
5. **Leve ao seu engenheiro:** o que perguntar a ele (laje, fundação, recuo da sua cidade).

**Capa:** "Que casa cabe no seu lote?" (título). Subtítulo: "24 plantas de casas térreas, organizadas pela largura do terreno." Aviso fixo no rodapé: "Plantas de referência. O projeto para a prefeitura é assinado por arquiteto ou engenheiro habilitado."

**Ganchos de anúncio** (para testar, um por vídeo):
- "Tem um lote de 8 x 25? Essa casa cabe."
- "O erro de planta que o pedreiro não te conta: o corredor."
- "Antes de comprar a laje, veja se a cozinha cabe." (a cozinha precisa de 1,50 m livres)
- "Por que cozinha, banheiro e serviço ficam juntos?" (uma prumada só)
- "A casa que cresce: comece com 1 quarto, termine com 2 sem quebrar nada." (C03)

## 2. Visual

Identidade: azul de projeto `#0B4FA8`, amarelo `#FFC857`, fundo quadriculado, títulos em Bricolage Grotesque, texto em Inter. Detalhes já testados no gerador do e-book (branch `frente-ebook`).

| Elemento | Regra |
|---|---|
| **Planta de dados** (as prévias de [`../plantas/previas/`](../plantas/previas/)) | Base da página: cada cômodo com nome e m², cotas externas, portas em amarelo, janelas em azul claro |
| **Planta humanizada** | Mesmo desenho com móveis e piso; vem da primeira rodada de 3D (C01) e se repete nas outras pela mesma engrenagem |
| **Fachada e perspectiva** | Imagem 3D gerada do mesmo dado. Nunca renderização com texto dentro |
| **Cotas** | Todas as medidas em metros, na própria imagem (como nos catálogos de porcelanato) |
| **Ícones** | Um sol, uma gota, uma seta de vento, na margem de cada ponto de "o que o arquiteto pensou" |
| **Cor por cômodo** | Mesma em todas as plantas (sala bege, cozinha verde, banheiro azul, quarto areia). O leitor aprende uma vez |

## 3. Animação: como incluir

Um PDF não toca vídeo. Opções, da mais simples para a mais completa:

| Opção | O que é | Esforço | Quando |
|---|---|---|---|
| **QR code por página** | Em cada casa, um QR que abre a animação de 12 s (blueprint que ganha vida) numa página simples | Baixo. O vídeo já existe para a C01 | Lançamento 1 |
| **Edição web** | O mesmo e-book em HTML (páginas que viram), com a animação tocando no lugar da imagem | Médio | Depois do 1º mês, se o QR funcionar |
| **GIF ou WebP curto** | O blueprint se desenhando em 3 s, para Instagram e anúncio | Baixo | Já, para anúncio |
| **Passeio 3D da casa** | Câmera dentro dos cômodos, para o anúncio | Alto | Só para a casa mais pedida |

**Como o motor 3D gera cada casa:** o dado de cada planta já está em `ebook/plantas/dados/ID.json` (cômodos, janelas, portas). O próximo passo técnico é ligar esse dado ao `video/src/casa3d.js`, que hoje só conhece a C01. Ver [`../../animacoes-3d/ANIMACOES-3D.md`](../../animacoes-3d/ANIMACOES-3D.md).

**Roteiro de 12 s para cada casa** (já provado na C01): 0–3 s o blueprint se desenha com as cotas; 3–7 s as paredes sobem; 7–10 s os móveis entram; 10–12 s a planta humanizada com o nome e a área.

## 4. O que ainda é decisão sua

- Título e preço (R$ 67 é hipótese da [estratégia](../../ESTRATEGIA.md)).
- Se o 1º lançamento sai com as 12 que combinamos ou com as 24 prontas em dados.
- Quem é o arquiteto que revisa e assina a declaração de revisão.

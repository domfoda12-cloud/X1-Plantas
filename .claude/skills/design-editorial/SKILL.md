---
name: design-editorial
description: Método do Designer do X1-Plantas para planejar e conferir peça parada (página do e-book, capa, carrossel, arte de anúncio) no estilo do projeto, fugindo do visual genérico. Use antes de desenhar ou mudar uma página ou imagem e antes de aprovar uma folha gerada.
---

# Design editorial

Escrita por nós, em português, só com o método (23/11/2026). Nada foi copiado, baixado ou instalado. **O estilo é o nosso** (`ebook/referencias/VISUAL.md` e `ebook/referencias/visual-ref/EDITORIAL.md`); esta skill só organiza o trabalho: planejar, executar, conferir.

## 1. Plano antes de desenhar

Escreva, em poucas linhas:

- **Cor:** as 4 a 6 cores da peça, com nome, valor e papel (fundo, título, destaque, texto, linha). Partem da identidade do projeto.
- **Letra:** cada tipo e o seu papel (título, texto, medida, legenda).
- **Layout:** um esboço em texto do que fica onde e do que o olho vê primeiro, segundo e terceiro.
- **Um elemento memorável:** escolha um só. O resto fica quieto.

**Segunda leitura do plano:** releia contra o pedido. O que seria igual em qualquer peça parecida, refaça partindo da matéria do assunto (lote, trena, tijolo, planta, o jeito de falar do comprador). Diga o que mudou e por quê.

## 2. Vícios do visual genérico (lista do que evitar)

- Cartões iguais, com a mesma sombra, enfileirados.
- Rótulo em caixa alta com ponto no meio ("ITEM · ITEM · ITEM").
- Uma palavra do título destacada sem motivo.
- Numerar o que não é sequência; pular número numa lista.
- Linha de texto com mais de 80 caracteres; serifa sem entrelinha.
- Combinação da moda no lugar da identidade (creme com terracota, preto com verde ácido).
- A mesma informação três vezes na mesma folha.
- Enfeite somado para "preencher". Antes de fechar, tire um acessório.

## 3. Peça em que a imagem manda (capa, primeiro quadro, anúncio)

- **Muito mais imagem que texto:** perto de nove partes de imagem para uma de texto. O texto que fica diz uma coisa só.
- Antes de pintar, escreva em 4 a 6 linhas a direção e **o que a pessoa entende no primeiro olhar** ("que casa cabe no meu lote"). Nada escondido para entendidos.
- **Margens e respiro:** nada cai da folha, nada encosta na borda, nada se sobrepõe. Não se negocia.
- **Segunda passada de refino:** não acrescente nada. Pergunte "como deixar o que já está aqui mais coeso?" e alinhe, iguale espaços, tire.
- Em carrossel, as folhas contam uma história e são da mesma família.

## 4. Documento de várias folhas (o e-book, um PDF)

- **A folha é a unidade.** Plano por folha: tipo, manchete, o que entra, layout.
- **A manchete diz a conclusão, não o assunto.** "Cabe num lote de 8 x 15 m", não "Sobre o lote".
- **Uma ideia por folha, e folha cheia.** Nenhuma folha meio vazia: pouco conteúdo vira conteúdo maior (planta maior, número grande, tabela folgada).
- **Não cabe? São duas folhas,** cada uma com a sua manchete. Nunca encolher a letra, nunca "continua".
- **Olhe a imagem de cada folha gerada** (`python3 ebook/gerador/livro.py --previa <pasta>`) e responda por escrito:
  1. Dá para entender a folha só pela manchete?
  2. Algum vão parece erro?
  3. Algo cortado, sobreposto ou com pouco contraste? Alguma letra pequena demais para ler no celular?
  4. Todas as folhas parecem da mesma família?
  5. A capa funcionaria sozinha, como cartaz?

## Neste projeto (X1-Plantas)

- **Quem usa:** o `designer`. O `editor-video` só recebe a imagem pronta. O `impeccable` continua só detectando; esta skill planeja e confere.
- **Leia antes:** `contexto/designer.md`, `ebook/referencias/VISUAL.md`, `ebook/referencias/visual-ref/EDITORIAL.md` e `ebook/CLAUDE.md`.
- **Identidade fixa: A Placa** (escolha do dono, 26/11/2026): tinta `#161616`, vermelho-placa `#C8102E`, amarelo `#FFC857` (fundo da capa, fita, abas de frente, porta), branco, terra `#C9A56B`, mato `#3E8E41`; azul de projeto `#0B4FA8` só na planta. Londrina Solid 900 nos títulos e na placa, Inter no texto, JetBrains Mono nas medidas. O sinal é a placa do Lote (branca, borda preta, letra vermelha, duas estacas) no topo da capa, das aberturas e da página de cada casa, com a tira do pé "pergunta + Vira: pág. N"; a voz do lote só na placa e na tira. Regras e tokens: `ebook/referencias/VISUAL.md`, seção 2. **No gerador, por ora só na prévia** (`--placa`, `ebook/gerador/placa.css`); o PDF oficial segue azul e Bricolage (`livro.css`) até o "gera" do dono. Mudar cor, fonte ou logo é **opção para o dono**, nunca decisão do Designer.
- **Vetos que não mudam:**
  - **Nenhum estilo de arte, tema, paleta ou fonte de terceiros** (dono: "use o nosso próprio"). Das referências do `EDITORIAL.md` vem só o jeito de organizar; nada é copiado.
  - **Nenhuma fonte baixada, nenhum script de fora, nenhum MCP de fora.** O PDF sai do `livro.py`; quem mede é o detector dele e o `ferramentas/checar.py`.
  - **O aviso "Planta de referência" e o selo "Imagem ilustrativa" nunca saem** nem ficam cobertos, cortados ou ilegíveis. Tirar acessório nunca é tirar aviso.
  - A imagem não promete aprovação, prazo ou custo de obra, nem dá a entender que a casa já existe ou que a planta dispensa pedreiro, engenheiro ou arquiteto (`ESTRATEGIA.md`, seção 9).
  - Nenhum depoimento, número ou escassez sem fonte na arte. R$ 47 e R$ 67 (teste do dono) não aparecem como promoção, lançamento ou aumento; a garantia é de 7 dias da entrega do link.
  - **Medida de terceiros não vira dado nosso:** proporção, letra mínima e régua de quanto cabe na folha são ponto de partida; vale o que o `livro.py` mede e o que se vê na prévia.
  - Toda imagem bate com a planta; números vêm do validador, nunca digitados.
- **Não manda no texto:** texto de venda segue a `redacao-que-vende` e o veto do Revisor. Movimento e tela não se aplicam: é peça parada.
- Ela é membro do Conselho (`CONSELHO.md`): o que sugerir é opção para o dono, nunca decisão.
- **Prompt de entrada:** antes de desenhar, escreva o plano (cores com papel, letras com papel, esboço do layout, o elemento memorável e, em PDF, o plano por folha com a manchete-conclusão) **partindo da identidade do projeto**; releia o plano contra o pedido e diga o que mudou. Depois de gerar, abra a imagem de **cada** folha, responda às cinco perguntas, passe a lista de vícios e faça a passada de refino tirando, não somando. Liste até 5 achados por peça e marque como **opção para o dono** qualquer mudança de identidade.

Método adaptado de anthropics/skills, `frontend-design` (Apache 2.0), commit e4bb5d960d87126ff3b3a8af1a104b7db67560ba.
Método adaptado de anthropics/skills, `canvas-design` (Apache 2.0), commit e4bb5d960d87126ff3b3a8af1a104b7db67560ba.
Método adaptado de Georgi45/pdf-design (MIT), commit a4d5444997a1912c13927a3bc08e5f133b29ba94.
Nenhum trecho copiado: leitura em `pedidos/anexos/skills-entrada-passo1.md`.

# Frases das 5 páginas: rascunho para o reset (25/11/2026)

> **Ficha:** `pedidos/2026-11/2026-11-25-1612-deixar-tudo-planejado-e-pronto-para-o-reset.md`. **Autor:** Redator. **É rascunho:** nada mudou em `ebook/fichas/textos.py`, `ebook/gerador/livro.py` nem no `config.json`. Só entra no gerador se o dono escolher (perguntas 1 a 3 da seção 6 do mapa) e o Revisor de risco der "ok".
> **Pedido do dono** (24/11, 21:30 e 21:34): "mostrar a dor que o usuario tem ou teria, e dar a solucao pra ele"; "Nao precisa mostrar a dor diretamente, mostra indiretamente sabe daquele jeitinho".

## 0. Plano do texto (segue o plano do Planejador: `pedidos/anexos/mapa-dor-solucao-do-ebook-2026-11-24.md`, seções 1, 3 e 5)

- **Para quem:** o comprador que já tem o lote, classe C, lê no celular. Frase curta, "você" ou "quem", sem adjetivo vazio.
- **O que cada peça contém:** uma dor da seção 1 do mapa, sentida por um dos 4 jeitos indiretos (exemplo concreto, cena, pergunta que ele já se faz, detalhe que ele reconhece), e a saída na mesma frase. Nenhum bloco "o problema é...".
- **De onde vem cada número:** área, quartos e lote das casas saem de `ebook/plantas/PLANTAS.md` (validador): C01 51 m², 2 quartos, lote de 8 x 15 m (mínimo 8,0 x 13,0 m); F01 71 m², 3 quartos, lote de 10 x 15 m (mínimo 10,0 x 12,8 m), "sala, cozinha e quartos têm janela para fora". As palavras citadas nas págs. 17 e 22 estão no glossário (`ebook/gerador/paginas.py`, linha 59 em diante: "Recuo", "Pé-direito", "Taxa de ocupação", "Alvará e habite-se") e nas perguntas da casa (`textos.py`, linha 14: "Qual é o recuo da minha rua e do meu lote?"). Os 7 passos da pág. 23: `livro.py`, linhas 1299 a 1309.
- **O que depende do dono:** quantas páginas mudam e quando (perguntas 1 e 2 da seção 6 do mapa); qual versão de cada página (seção 6 deste anexo).
- **Ordem das partes:** as 5 páginas na ordem do mapa (8, 12, 23, 22, 17), cada uma com o texto de hoje, versões A e B, contagem de letras, fonte e a troca exata; depois a recomendação e os riscos.
- **Limite de tamanho:** até uns 20% acima do texto de hoje; a abertura nova da pág. 23 em até ~180 letras. Contagem feita com `len()` do Python (letras, espaços e pontuação).
- **Pronto quando:** as 5 páginas têm A e B dentro do limite, com fonte e troca pronta para colar; a recomendação e os riscos estão no fim; o Revisor lê (rascunho) e o dono escolhe no reset.

---

## 1. Pág. 8 · C01, "Para quem é" (jeito: a pergunta que ele já se faz, no molde da E03) · dor D1

**Hoje (106 letras):** "Casal com 1 ou 2 filhos que quer dois quartos, varanda na entrada e banheiro largo, sem corredor comprido."

| | Texto | Letras | Jeito |
|---|---|---|---|
| **A** | Casal com 1 ou 2 filhos e lote de 8 m de frente, como o de 8 x 15 m, que se pergunta se ali cabem 2 quartos e varanda. | 118 (+11%) | a pergunta que ele já se faz (D1) |
| **B** | Casal com 1 ou 2 filhos que quer 2 quartos e varanda, sem aquele corredor comprido em que ninguém mora. | 103 (-3%) | o detalhe que ele reconhece (o corredor do erro 2) |

**Fontes:** 8 m de frente e lote de 8 x 15 m: `PLANTAS.md`, C01. "Ninguém mora no corredor": erro 2 do e-book (`paginas.py`, linha 28); a C01 tem hall no lugar do corredor (`PLANTAS.md`, C01; corredor de 4%, `atributos-que-vendem.md`, seção 2). Dor D1: `MERCADO.md`, linhas 27 e 47.

**Troca** (`ebook/fichas/textos.py`, linha 19):
- velha: `para_quem="Casal com 1 ou 2 filhos que quer dois quartos, varanda na entrada e banheiro largo, sem corredor comprido.",`
- nova A: `para_quem="Casal com 1 ou 2 filhos e lote de 8 m de frente, como o de 8 x 15 m, que se pergunta se ali cabem 2 quartos e varanda.",`
- nova B: `para_quem="Casal com 1 ou 2 filhos que quer 2 quartos e varanda, sem aquele corredor comprido em que ninguém mora.",`

---

## 2. Pág. 12 · F01, "Para quem é" (jeito: o exemplo concreto da família que cresce) · dor D7, só a parte da família

**Hoje (92 letras):** "Família de 4 ou 5 que precisa de 3 quartos com pouca área (71 m²), sem perder nenhum quarto."

| | Texto | Letras | Jeito |
|---|---|---|---|
| **A** | Família de 4 ou 5 que precisa do 3º quarto, para o filho que vem ou para o escritório, em só 71 m². | 99 (+8%) | o exemplo concreto (o filho que vem) |
| **B** | Família com 2 filhos e mais um a caminho: 3 quartos, todos com janela, em só 71 m². | 83 (-10%) | a cena da família que vai crescer |

**Fontes:** 71 m² e 3 quartos: `PLANTAS.md`, F01. "Todos com janela": `PLANTAS.md`, F01 ("sala, cozinha e quartos têm janela para fora"). "Escritório ou quarto do filho que vem": `MERCADO.md`, linha 26 (pesquisa, não a história do Marcos). Dor D7: `MERCADO.md`, linhas 26 e 35.

**Troca** (`ebook/fichas/textos.py`, linha 69):
- velha: `para_quem="Família de 4 ou 5 que precisa de 3 quartos com pouca área (71 m²), sem perder nenhum quarto.",`
- nova A: `para_quem="Família de 4 ou 5 que precisa do 3º quarto, para o filho que vem ou para o escritório, em só 71 m².",`
- nova B: `para_quem="Família com 2 filhos e mais um a caminho: 3 quartos, todos com janela, em só 71 m².",`

---

## 3. Pág. 23 · "Do e-book até a chave na mão", abertura nova antes do passo 1 (jeito: a cena de quem só tem o desenho) · dor D3

**Hoje:** não tem abertura (o título vai direto à lista dos 7 passos).

| | Texto | Letras | Jeito |
|---|---|---|---|
| **A** | Só tem o desenho do parente ou do pedreiro e ouviu que a prefeitura pede projeto? Os passos abaixo mostram a ordem, e quem faz cada um. | 135 (limite ~180) | a cena, em forma de pergunta |
| **B** | A prefeitura pede projeto, o banco pede documento, o pedreiro pede a planta. Aqui está a ordem de cada passo, e quem faz cada um. | 129 (limite ~180) | a cena dos três pedidos |

**Fontes:** "Quem desenha a casa é o pedreiro, o parente ou o folheto": `MERCADO.md`, linha 28 (pesquisa). A prefeitura e o projeto: passo 4 (`livro.py`, linha 1306: "Aprove o projeto na prefeitura... sai o alvará"). O banco: passo 6 (`livro.py`, linha 1308: "Se for financiar, pergunte ao banco quais documentos ele pede"). "Quem faz cada um": os passos 3 e 6 dizem quem (arquiteto ou engenheiro, responsável técnico). Dor D3: `MERCADO.md`, linhas 28 e 40.

**Troca** (`ebook/gerador/livro.py`, linha 1311; só o trecho do começo, o resto da linha fica igual):
- velha: `{cab("passos")}<ol class="passos">`
- nova A: `{cab("passos")}<p class="abertura">Só tem o desenho do parente ou do pedreiro e ouviu que a prefeitura pede projeto? Os passos abaixo mostram a ordem, e quem faz cada um.</p><ol class="passos">`
- nova B: `{cab("passos")}<p class="abertura">A prefeitura pede projeto, o banco pede documento, o pedreiro pede a planta. Aqui está a ordem de cada passo, e quem faz cada um.</p><ol class="passos">`

A linha 1311 é uma f-string com aspas simples: as duas versões não têm apóstrofo, então colam sem escapar nada.

---

## 4. Pág. 22 · "Ficha do meu terreno", abertura (jeito: a pergunta que ele vai ouvir) · dores D3 e D8

**Hoje (87 letras):** "Preencha com os dados da prefeitura e leve junto na primeira conversa com o engenheiro."

| | Texto | Letras | Jeito |
|---|---|---|---|
| **A** | "Qual é o recuo do seu lote?" O engenheiro costuma perguntar. Anote os dados da prefeitura e leve junto. | 104 (+20%) | a pergunta que ele vai ouvir |
| **B** | Em vez de "não sei, vou ver", leve ao engenheiro os dados da prefeitura, já anotados aqui. | 90 (+3%) | o detalhe que ele reconhece (a resposta que ele não quer dar) |

**Fontes:** a pergunta do recuo: `textos.py`, linha 14 (PADRAO, "Qual é o recuo da minha rua e do meu lote?") e o campo "Recuo da frente (m)" da própria ficha (`livro.py`, linha 1292). Dor D8: `atributos-que-vendem.md`, linhas 14 e 15 (hipótese).

**Troca** (`ebook/gerador/livro.py`, linha 1295):
- velha: `<p class="abertura">Preencha com os dados da prefeitura e leve junto na primeira conversa com o engenheiro.</p>`
- nova A: `<p class="abertura">"Qual é o recuo do seu lote?" O engenheiro costuma perguntar. Anote os dados da prefeitura e leve junto.</p>`
- nova B: `<p class="abertura">Em vez de "não sei, vou ver", leve ao engenheiro os dados da prefeitura, já anotados aqui.</p>`

A linha 1295 também é f-string com aspas simples: as aspas duplas do texto colam sem escapar.

---

## 5. Pág. 17 · "As palavras da obra", abertura (jeito: o detalhe que ele reconhece) · dores D3 e D8

**Hoje (83 letras):** "As palavras que aparecem nas plantas, na prefeitura e na conversa com o engenheiro."

| | Texto | Letras | Jeito |
|---|---|---|---|
| **A** | Na prefeitura falam em "recuo" e "habite-se". Aqui, o que cada palavra da obra quer dizer. | 90 (+8%) | a palavra ouvida no balcão (o jeito do mapa) |
| **B** | Quando o engenheiro falar em "pé-direito" ou "taxa de ocupação", você já vai saber o que é. | 91 (+10%) | a conversa com o engenheiro, com a saída no fim |

**Fontes:** as quatro palavras estão no glossário da própria página (`paginas.py`, a partir da linha 59: "Recuo", "Pé-direito", "Taxa de ocupação", "Alvará e habite-se").

**Troca** (`ebook/gerador/livro.py`, linha 1225; f-string com três aspas duplas, as aspas do texto colam sem escapar):
- velha: `<p class="abertura">As palavras que aparecem nas plantas, na prefeitura e na conversa com o engenheiro.</p>`
- nova A: `<p class="abertura">Na prefeitura falam em "recuo" e "habite-se". Aqui, o que cada palavra da obra quer dizer.</p>`
- nova B: `<p class="abertura">Quando o engenheiro falar em "pé-direito" ou "taxa de ocupação", você já vai saber o que é.</p>`

---

## 6. Recomendação do Redator

| Pág. | Versão | Por quê |
|---|---|---|
| 8 (C01) | **A** | É o molde da E03, que já funciona, e põe a medida do lote na primeira linha (o atributo mais forte: a casa que cabe no seu lote, com a medida). Não diz que cabe: só traz a pergunta; a resposta é a planta, com o "confirme" da pág. 9. |
| 12 (F01) | **A** | Mantém "4 ou 5", usa a frase da pesquisa ("o filho que vem ou o escritório") e serve também a quem não espera filho. A B é mais viva, mas restringe a "2 filhos". |
| 23 | **A** | A cena vem da pesquisa (linha 28) e a pergunta é a que ele já se faz. A B junta três pedidos de uma vez e pode soar como peso. |
| 22 | **A** | É o jeito do mapa e a pergunta já está nas perguntas da casa: a página vira o ensaio da conversa. |
| 17 | **B** | Termina na saída ("você já vai saber o que é"), que é o alívio; a A só descreve. Se o dono preferir seguir o mapa à letra (o balcão da prefeitura), fica a A. |

Para testar depois (quando houver venda): pág. 8 A contra B, medindo a resposta no WhatsApp com a medida do lote.

## 7. Riscos para o Revisor de risco

1. **Pág. 8 A, "se pergunta se ali cabem":** não afirma que cabe, mas a planta logo abaixo responde que sim. Conferir se a pág. 9 mantém "deve caber, confirme na prefeitura" (hoje diz "Cabe num lote de 8 x 15 m" com "Leve ao seu engenheiro").
2. **Pág. 8 B, "ninguém mora":** repete o erro 2 do e-book; conferir se a C01 continua com o erro 2 na lista "esta casa evita" (o gerador tira o 2 se o corredor passar de 12%; hoje ela tem 4%).
3. **Pág. 12 A e B, "o filho que vem" / "mais um a caminho":** é o cenário da pesquisa, não a história do Marcos (que tem "o segundo filho a caminho", linha 35). Nenhuma das duas fala em "por etapas" nem em "a casa que cresce".
4. **Pág. 12 B, "todos com janela":** vale para os 3 quartos pela ficha da F01; se o Arquiteto mudar a F01, cai.
5. **Pág. 22 A, "o engenheiro costuma perguntar":** é afirmação sobre o profissional; troque por "O engenheiro vai querer saber" ou tire, se o Revisor achar que é promessa.
6. **Pág. 23, "a prefeitura pede projeto":** vale para a obra com alvará; a B acrescenta "o banco pede documento", que só vale para quem financia (o passo 6 diz "se for financiar"). Por isso a recomendação é a A.
7. **Pág. 23, tamanho:** a página já tem 7 passos e uma foto de 74 mm; a abertura nova soma umas 2 linhas. Se o detector do gerador disser que estourou, é com o Designer (altura da foto), não com o texto.
8. **Nenhuma versão** tem preço, custo, prazo, aprovação prometida, "cabe com certeza", "por etapas", "a casa que cresce", "sem quebrar parede" ou "o problema é...". Nenhuma diz que dispensa engenheiro ou arquiteto; as das págs. 17, 22 e 23 levam o leitor até ele.

## 8. Reconferência dos pedidos (ficha 1612 e recado do Maestro)

- Plano curto no começo: **cumpre** (seção 0, seguindo o plano do Planejador).
- Texto de hoje, 2 versões, letras, fonte e linha exata por página: **cumpre** (seções 1 a 5).
- Até ~20% acima do texto de hoje e ~180 letras na pág. 23: **cumpre** (a maior é a 22 A, +20%, no limite).
- Recomendação e riscos: **cumpre** (seções 6 e 7).
- Leitura do Revisor (item 2 do "pronto quando" da ficha): **em aberto**, é do Revisor de risco, chamado pelo Maestro.
- Não mudar gerador nem `config.json`: **cumpre**. Não conferi a prévia (nada foi gerado: as páginas só podem ser medidas depois da troca, no reset).

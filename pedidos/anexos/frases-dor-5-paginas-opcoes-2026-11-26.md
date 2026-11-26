# Frases das 5 páginas: a dor do jeito indireto, opções para o dono (26/11/2026)

> **Autor:** Redator (trabalho da noite; o dono escolhe de manhã). **É opção:** nada mudou em `ebook/gerador/` nem em `ebook/fichas/`. Só entra depois da escolha do dono e do "Revisor: ok".
> **Recado do dono:** a dor entra "daquele jeitinho" (cena, exemplo, detalhe que o comprador reconhece), nunca anunciada ("o problema é...").

## 0. Plano do texto (resumo do plano obrigatório `pedidos/anexos/plano-frases-dor-5-paginas-2026-11-25.md`)

- **Para quem:** quem já tem o lote, classe C, lê no celular. Frase curta, sem adjetivo vazio.
- **O que cada página leva:** o jeito indireto que o plano manda para ela, com a saída na mesma frase. Nenhum quadro de "problema".
- **Fonte de cada número:** C01 51 m², 2 quartos, lote de 8 x 15 m (mínimo 8,0 x 13,0 m); F01 71 m², 3 quartos (`ebook/plantas/PLANTAS.md`, linhas 9 e 231). As palavras das págs. Ficha e Glossário estão no glossário (`ebook/gerador/paginas.py`: "Recuo", "Pé-direito", "Taxa de ocupação", "Alvará e habite-se"). Nenhum outro número.
- **Fonte da dor:** `ebook/referencias/MERCADO.md` (o lote manda; o 3º quarto "do filho que vem"; quem desenha é o pedreiro ou o parente; "a prefeitura vai pedir projeto") e `ebook/vendas/atributos-que-vendem.md` (D8, hipótese). O Marcos não entra como fato.
- **Limites (palavras, contadas com `split()` do Python):** C01 até 25 (e cabe na pág. 3); F01 até 25, com o 71 m²; Passos uns 25 (2 linhas); Ficha até 30; Glossário até 30.
- **Vetos que seguem valendo:** nada de custo, prazo, aprovação, "cabe com certeza", "por etapas", "a casa que cresce", "sem quebrar parede", "dispensa profissional"; "costuma perguntar" e "quem faz cada um" (vetados em 25/11, `veto-frases-das-5-paginas-2026-11-25.md`) não voltam.
- **Depende do dono:** quantas páginas mudam (as 5, só as 2 das casas ou nenhuma) e qual opção de cada uma.
- **Ordem:** as 5 na ordem do plano (C01, F01, Passos, Ficha, Glossário).
- **Pronto quando:** cada página tem 2 opções dentro do limite, a recomendada marcada e o porquê; o Revisor lê (seção no fim); o dono escolhe. A prévia sem "página estourada" é do reset.
- **Relação com o rascunho de 25/11** (`frases-das-5-paginas-2026-11-25.md`): estas são opções novas, mais de cena. As de 25/11 com a troca do Revisor continuam valendo como reserva.

## 1. C01, "Para quem é" (págs. 8 e 3) · jeito: a pergunta que ele já se faz

Hoje: "Casal com 1 ou 2 filhos que quer dois quartos, varanda na entrada e banheiro largo, sem corredor comprido." (19)

| | Texto | Palavras |
|---|---|---|
| **A (recomendada)** | Casal com 1 ou 2 filhos, lote de 8 m de frente e uma dúvida: cabem ali 2 quartos, varanda e banheiro largo? | 23 |
| B | Quem mede com a trena os 8 m de frente do lote e se pergunta se ali dá para 2 quartos e varanda. | 23 |

**Por quê A:** é o molde da E03, guarda o "para quem" (casal com filhos) que a pág. 3 precisa, e a resposta está logo abaixo (51 m², mínimo 8,0 x 13,0 m). Só pergunta, não afirma que cabe.

## 2. F01, "Para quem é" (pág. 12) · jeito: o filho que vem e precisa de quarto

Hoje: "Família de 4 ou 5 que precisa de 3 quartos com pouca área (71 m²), sem perder nenhum quarto." (21)

| | Texto | Palavras |
|---|---|---|
| **A (recomendada)** | Família de 4 ou 5 em que o filho que vem já tem nome, mas ainda não tem quarto: aqui são 3, em 71 m². | 25 |
| B | Família de 4 ou 5 que já pensa onde vai dormir o filho que vem, ou onde fica o escritório: 3 quartos em 71 m². | 25 |

**Por quê A:** "já tem nome, mas ainda não tem quarto" é a cena que ele vive, sem dizer "dor"; a saída vem na mesma frase. B é mais larga (serve a quem quer escritório) e fica de reserva. Nenhuma promete ampliar.

## 3. "Do e-book até a chave na mão", abertura nova (pág. 16) · jeito: a cena de quem só tem o desenho

Hoje: sem abertura.

| | Texto | Palavras |
|---|---|---|
| **A (recomendada)** | O desenho é do parente, no caderno, e no balcão disseram: "a prefeitura pede projeto". Daqui até a chave: a ordem e onde entra o profissional. | 25 |
| B | Tem o desenho do parente ou do pedreiro e ouviu que a prefeitura pede projeto? Aqui está a ordem, e onde entra o profissional. | 24 |

**Por quê A:** é cena (o caderno, o balcão), não pergunta, e varia do jeito da C01; termina no profissional, sem sugerir que o e-book é o projeto. Não cita o pedreiro, então não há como soar que desmerece. Se estourar a página, B é 1 palavra menor.

## 4. "Ficha do meu terreno", abertura (pág. 15) · jeito: a pergunta que ele vai ouvir

Hoje: "Preencha com os dados da prefeitura e leve junto na primeira conversa com o engenheiro." (15)

| | Texto | Palavras |
|---|---|---|
| **A (recomendada)** | "Qual é o recuo do seu lote? E a taxa de ocupação?" Na primeira conversa com o engenheiro, a resposta vai anotada aqui, com os dados da prefeitura. | 28 |
| B | Na primeira conversa, o engenheiro vai precisar saber o recuo e a taxa de ocupação do seu lote. Anote aqui o que a prefeitura informar e leve junto. | 28 |

**Por quê A:** a pergunta entre aspas faz ele ouvir a conversa e sentir o branco sem a página dizer; "a resposta vai anotada" é o alívio. Tom de ajuda. B usa a forma já liberada em 25/11 ("vai precisar saber") e é a mais segura.

## 5. "As palavras da obra", abertura (pág. 5) · jeito: a palavra ouvida no balcão

Hoje: "As palavras que aparecem nas plantas, na prefeitura e na conversa com o engenheiro." (14)

| | Texto | Palavras |
|---|---|---|
| **A (recomendada)** | No balcão da prefeitura falam em "habite-se" e "taxa de ocupação", e a conversa segue. Aqui, cada palavra da obra explicada, sem pressa. | 23 |
| B | Sabe quando o engenheiro fala em "pé-direito" e a gente concorda com a cabeça? Depois desta página, você concorda sabendo o que é. | 23 |

**Por quê A:** "e a conversa segue" é o "ninguém explica" sem culpar ninguém nem o leitor; "sem pressa" é a saída. B é mais viva e com humor ("a gente", inclui quem escreve), mas chega mais perto do "você não sabe": o Revisor decide se passa.

## 6. Reconferência do pedido

- 2 opções por página, dentro do limite do plano: **cumpre** (maior: 28 de 30 na Ficha; Passos com 25).
- Recomendada marcada e uma linha de por quê: **cumpre**.
- Sem custo, prazo, aprovação, "dispensa profissional", e só números dos dados (8 m, 2 e 3 quartos, 71 m²; 4 ou 5 e 1 ou 2 filhos já estão no texto de hoje): **cumpre**.
- Não mexer em `ebook/gerador/` nem `ebook/fichas/`; plano no começo; seção do Revisor vazia; sem commit: **cumpre**.
- **Não conferi:** a prévia (estouro da pág. 16 e quebra da pág. 3), nem a ficha 2130 (se o dono já disse quantas páginas mudam). Falta pedir ao Planejador que confira este plano resumido (regra de 24/11): quem conduz chama.

## Leitura do Revisor


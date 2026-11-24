# Mapa das duas partes do e-book (passo A10, 24/11/2026)

> **Pedido do dono (24/11, resposta à decisão 8 no quadro):** o e-book terá "uma parte falando de cada casa específica, e outra parte falando de casas no geral"; a página da parede sem janela "pode ir pro geral".
> **Autor:** Designer, 24/11/2026. **É proposta:** quem decide a ordem é o Maestro (`pedidos/PLANO.md`, A10); o que é do dono está nas perguntas do fim. O Redator dá os nomes das partes e reescreve os sobretítulos.
> **Lido, não suposto:** a prévia de hoje (`python3 ebook/gerador/livro.py --previa <pasta temporária>`: 17 páginas, 3 casas, cada página olhada), o texto de cada página (`pdftotext` do `ebook/saida/ebook.pdf`), `ebook/gerador/livro.py` (funções `montar`, `dupla`, `Livro.pagina`, `gerar`), os protótipos `ebook/plantas/rascunhos/mobiliar.py` (1 folha por casa) e `bonus.py` (checklist 8 folhas, perguntas 2), `pedidos/anexos/comodo-a-comodo-3-casas.md` (seção 4) e `e07-parede-na-divisa-ideias.md` (seção 2).
> **Nome do arquivo:** o caminho é o que o Maestro pediu; a linha A10 do `PLANO.md` cita `pedidos/anexos/ebook-duas-partes-mapa-2026-11-24.md`. É o mesmo mapa: o Maestro acerta o nome na linha do plano.

## 1. As 17 páginas de hoje e para onde vão

| Hoje | Título | O que tem | Parte | Vai para |
|---|---|---|---|---|
| 1 | Antes do primeiro tijolo (capa) | Título, planta da C01, régua com a página de cada frente | abertura (antes das duas partes) | 1 |
| 2 | Como usar este e-book | 3 passos, foto das mãos com a trena, aviso "Planta de referência" completo | abertura | 2 (ganha o sumário no lugar da foto) |
| 3 | Qual casa cabe no seu lote? | As 3 casas nos lotes, em cima da fita 5, 8 e 10 m | **cada casa** (é a porta da parte) | 3 |
| 4 | Como ler uma planta | Planta da C01 com legenda: cotas, porta, janela, móveis, ficha, 3D, sol | **casas em geral** | 16 |
| 5 | As palavras da obra | Glossário (área construída, recuo, taxa de ocupação, ART e RRT...) | **casas em geral** | 17 |
| 6 | Os 7 erros que saem caro (1 a 4) | Erro, por quê, o jeito certo | **casas em geral** | 18 |
| 7 | Os 7 erros (5 a 7) | Continuação, caixa amarela de fecho | **casas em geral** | 19 |
| 8 | Casa Compacta (C01) | Planta humanizada grande, para quem é, erros que evita | **cada casa** | 8 |
| 9 | C01: Cabe num lote de 8 x 15 m | Casa no lote, ficha "Informação da casa", vista da rua, 3D, por que é assim | **cada casa** | 9 |
| 10 | Casa Fita (E03) | Planta grande | **cada casa** | 4 |
| 11 | E03: Cabe num lote de 5 x 25 m | Lote, ficha, vista, 3D | **cada casa** | 5 |
| 12 | Casa Família Compacta (F01) | Planta grande | **cada casa** | 12 |
| 13 | F01: Cabe num lote de 10 x 15 m | Lote, ficha, foto da fachada, 3D | **cada casa** | 13 |
| 14 | Terreno e recuos | O que a prefeitura define, onde descobrir, a conta, as 3 casas nos lotes | **casas em geral** | 20 |
| 15 | Ficha do meu terreno | Campos para preencher, foto do lote com trena | **casas em geral** | 22 |
| 16 | Do e-book até a chave na mão | 7 passos, foto do canteiro | **casas em geral** | 23 |
| 17 | Agora é com você | Perguntas para qualquer casa, WhatsApp, foto, régua | fecho (depois das duas partes) | 24 |

Capa, "Como usar" e "Agora é com você" não são de uma parte: são a porta e a saída do livro inteiro. Ficam sem aba.

## 2. A ordem proposta: a casa primeiro, o geral depois

**1 Capa · 2 Como usar + sumário · Parte 1 "cada casa" (3 a 15) · Parte 2 "casas em geral" (16 a 23) · 24 Agora é com você.**

Por quê:
- **O comprador procura primeiro a casa do lote dele.** A capa já manda direto para a página pela régua; quem lê na ordem chega na página 3, acha a frente, e na 4 já está numa casa. Hoje ele passa por 5 páginas de explicação (4 a 7) antes da primeira planta, na página 8.
- **As páginas gerais ficam melhores depois da casa.** "Terreno e recuos", "Ficha do meu terreno" e "Do e-book até a chave" já se chamam "depois de escolher". Os 7 erros viram conferência da casa que ele acabou de ver (a página da casa já diz "dos 7 erros da pág. N, esta casa evita": o número muda sozinho).
- **Casas pela frente do lote: E03 (5 m), C01 (8 m), F01 (10 m).** Hoje a ordem é C01, E03, F01 (pela letra do código), e a régua da capa e da página 3 lê "pág. 10, pág. 8, pág. 12" da esquerda para a direita. Pela frente, lê "4, 8, 12": quem folheia vai para a frente quando o lote cresce. A C01 continua a casa da capa e a planta grátis. **Escolha do Maestro** (não é título, preço nem o que é grátis).
- **Cada casa começa em página par:** os dois pares abertos de cada casa ficam lado a lado no PDF de duas páginas e na impressão (planta à esquerda, lote à direita, como hoje).
- **Pares abertos da parte 2 que se completam:** 16-17 (ler a planta e as palavras), 18-19 (os 7 erros, hoje separados entre a 6 e a 7, que já são par), 20-21 (a regra dos recuos e, ao lado, a parede sem janela, que é a consequência dela), 22-23 (a ficha para preencher e os passos até a chave).

| Página nova | Título (provisório) | Parte |
|---|---|---|
| 1 | Capa | abertura |
| 2 | Como usar + sumário + aviso | abertura |
| 3 | Qual casa cabe no seu lote? | cada casa |
| 4 a 7 | E03 Casa Fita: planta · no lote · como mobiliar* · cômodo a cômodo | cada casa |
| 8 a 11 | C01 Casa Compacta: o mesmo | cada casa |
| 12 a 15 | F01 Casa Família Compacta: o mesmo | cada casa |
| 16 | Como ler uma planta | casas em geral |
| 17 | As palavras da obra | casas em geral |
| 18 e 19 | Os 7 erros que saem caro | casas em geral |
| 20 | Terreno e recuos | casas em geral |
| 21 | **A parede sem janela** (nova) | casas em geral |
| 22 | Ficha do meu terreno | casas em geral |
| 23 | Do e-book até a chave na mão | casas em geral |
| 24 | Agora é com você | fecho |

**Total: 24 páginas** (abertura 2, parte 1 com 13, parte 2 com 8, fecho 1). Com os bônus dentro (decisão 3): **34** (+10 entre a 23 e o fecho: checklist 8 folhas e perguntas 2, como saem hoje do `bonus.py`; 3 folhas de perguntas se a decisão 5 for "3": 35). Com o quadrinho da parede sem janela (página B do `e07-parede-na-divisa-ideias.md`): +1.

## 3. Onde entram as páginas novas

- **Cômodo a cômodo, por casa:** depois da página do lote, na própria casa (parte 1). Na C01, sem o serviço até o D1 (veto 3).
- **Como mobiliar** (*decisão 7, só se o dono quiser): entre o lote e o cômodo a cômodo. As duas não repetem: "como mobiliar" mostra o que cabe (planta com móveis e passagens, já prototipada em `rascunhos/mobiliar.py`); "cômodo a cômodo" diz o que decidir antes do reboco (tomadas, cuidados, o que perguntar).
- **Por isso cada casa passa de 2 para 4 páginas (2 pares abertos).** Sem "como mobiliar", o cômodo a cômodo ocupa as duas folhas (dentro de casa; o lote em volta): o texto do Arquiteto para a E03 tem uns 2.000 palavras e não cabe numa folha sem encolher a letra. A prova do A9 (Casa Fita) confirma se são 1 ou 2 folhas; se for 1, a casa fica com 3 e o par aberto se perde: o gerador deve então avisar.
- **A parede sem janela:** parte 2, página 21, ao lado de "Terreno e recuos". Deve valer para qualquer casa com parede na divisa (D19), com a Casa Fita de exemplo, que é a do livro (a E07 não está no lançamento). Cuidado com repetição: o protótipo "como mobiliar" da E03 já tem a manchete "a parede sem janela é a que guarda os móveis". A página geral fala da regra e da luz; a da casa, dos móveis.
- **Os bônus**, se o dono os puser dentro: no fim da parte 2, antes do fecho, com aba própria (a mesma azul, escrito "bônus"), porque são o próximo passo depois de "até a chave".
- **As páginas que o Arquiteto recomendou** ("Antes do reboco" com tomadas, "Carro ou quintal", "O que não fazer depois"): só se o dono disser sim (decisão 36). Se entrarem, as de casa vão para o cômodo a cômodo e "Carro ou quintal" (as 3 casas juntas) vai para a parte 2, depois de "Terreno e recuos".

## 4. Como o leitor sabe em que parte está (sem trocar a identidade)

- **Aba lateral, que o livro já tem.** Parte 1: a aba amarela "frente X m" que hoje aparece nas páginas da casa continua, na mesma altura (30 mm na de 5 m, 102 mm na de 8 m, 150 mm na de 10 m), agora nas 4 páginas de cada casa. A página 3 mostra as três abas ao mesmo tempo: é a chave do folhear. **Parte 2: aba no azul de projeto `#0B4FA8`, texto branco "geral", sempre na mesma altura, abaixo da última aba de frente** (proposta: 200 mm). Na edição de 24 casas, com frentes maiores, a altura da aba azul se recalcula (fica abaixo da última frente).
- **Cor:** só as duas que já existem (amarelo da fita para cada casa, azul de projeto para o geral). Nenhuma cor nova, nenhuma fonte nova.
- **Número de página:** contínuo, de 1 a 24, como hoje (a régua, a calculadora, a planta grátis e as referências "pág. N" dependem dele). Não recomeça por parte.
- **Sobretítulo:** os de hoje dizem o tempo ("Antes de escolher", "Antes da laje", "Depois de escolher"). Depois das casas, "Antes de escolher" fica errado. Proposta: o sobretítulo das páginas da parte 2 passa a dizer o nome da parte; as da parte 1 mantêm o "E03 · TERRENO ESTREITO" de hoje. **Texto do Redator.**
- **Sem página divisória:** uma folha só com "Parte 2" ficaria meio vazia. A virada é marcada pela aba que muda de cor e pelo sumário da página 2.
- **Nome das partes (provisório, do Redator):** "A casa do seu lote" e "Para qualquer casa", no jeito de falar do comprador. Nos documentos da equipe continuam "cada casa" e "casas em geral", as palavras do dono.

## 5. Esboço do sumário novo

Imagem: `ebook/plantas/rascunhos/sumario-duas-partes-p2.png` (a página 2 com o sumário no lugar da foto) e `ebook/plantas/rascunhos/sumario-duas-partes-ordem.png` (as 24 páginas em fila, com as abas; esquema para a equipe). Script: `python3 ebook/plantas/rascunhos/sumario-duas-partes.py` (não mexe no gerador; os números de página são os deste mapa).

```
Como usar este e-book
 1 Meça a frente do seu lote.
 2 Ache a sua casa na parte 1.            (pág. 3)
 3 Leia a parte 2 antes de ir ao engenheiro.

[parte 1] A casa do seu lote               [parte 2] Para qualquer casa
 Qual casa cabe no seu lote?        3       Como ler uma planta               16
 [frente 5 m]  Casa Fita            4       As palavras da obra               17
 [frente 8 m]  Casa Compacta        8       Os 7 erros que saem caro          18
 [frente 10 m] Casa Família Compacta 12     Terreno e recuos                  20
                                            A parede sem janela (nova)        21
                                            Ficha do meu terreno              22
                                            Do e-book até a chave na mão      23
[ Planta de referência: o aviso completo, como hoje ]
```

**Plano do esboço (skill `design-editorial`):** cores só da identidade (azul `#0B4FA8` nos títulos e na marca da parte 2, amarelo `#FFC857` nas abas da parte 1, `#FFF4DA` no aviso, cinza do texto); letras: Bricolage Grotesque nos títulos, Inter no texto, JetBrains Mono nas abas e nos números (como hoje). Elemento memorável: **a aba do sumário é a mesma aba da borda** ("frente 5 m" amarela, "parte 2" azul), então o sumário ensina a folhear. Segunda leitura: tirei a foto das mãos com trena, que repetia a capa e o passo 1; a página fica com os 3 passos, o mapa das partes e o aviso.

**As cinco perguntas, olhando as duas imagens:**
1. Manchete: "Como usar este e-book" diz o assunto, não a conclusão. Opção para o Redator: "Meça a frente, ache a casa, leve ao engenheiro."
2. Vão: sobra perto de 1/8 da folha embaixo do aviso. No D17, a foto volta menor (uns 40 mm) ou os 3 passos ganham letra; não fica vão.
3. Nada cortado ou sobreposto; o aviso inteiro e legível; a menor letra é a do selo (7,5 pt, igual à aba de hoje).
4. Mesma família das páginas de hoje (mesmo CSS do `livro.css`).
5. Capa: não muda neste mapa (só a régua passa a ler 4, 8, 12).

## 6. O que muda no gerador (para o D17; eu não mexi)

`git diff --stat ebook/gerador` está vazio; `ebook/saida/` não mudou.

1. **`gerar()`**: a ordem das casas sai de `plantas.sort(key=... "CEFS" ...)` para a frente do lote (`lote_frente(p)`), se o Maestro aceitar a ordem pela frente.
2. **`montar()`**: os blocos "Como ler uma planta", "As palavras da obra" e "Os 7 erros" (hoje logo depois da página 3) descem para depois das casas, antes de "Terreno e recuos". As casas vêm logo depois da página 3.
3. **`dupla()`** (ou uma função nova chamada depois dela): as páginas 3 e 4 de cada casa ("como mobiliar", se o dono quiser, e "cômodo a cômodo"), com `orelha=f`. O desenho de "como mobiliar" já existe em `rascunhos/mobiliar.py`.
4. **Página nova** da parede sem janela entre "Terreno e recuos" e "Ficha do meu terreno" (D19).
5. **`Livro.pagina()`** e **`livro.css`**: a aba azul da parte 2 (por exemplo `orelha="geral"`, classe `.orelha.geral` com fundo `var(--azul)` e texto branco, altura fixa); a página 3 com as três abas de frente.
6. **Página 2**: o sumário no lugar da foto `02-maos-medindo` (ou com ela menor); os números do sumário saem de `L.inicio`, como já sai `numeros["lote"]` e `numeros["erros"]` (a segunda passada acerta).
7. **Sobretítulos** (`<span class="sobre">`) das páginas da parte 2, com o texto do Redator.
8. **Uma conferência nova:** se uma casa começar em página ímpar, o gerador avisa (o par aberto da casa se perdeu).
9. Sem mudança: a numeração contínua, a calculadora e a planta grátis (pegam os números de `numeros`), o aviso legal no rodapé das páginas de casa. O `WHATSAPP.md` não cita página fixa do PDF pago.

## 7. Perguntas

**Para o dono (só ele sabe):**
1. "Como mobiliar" entra em cada casa (decisão 7)? (a) sim, uma folha por casa, antes do cômodo a cômodo; (b) não, o cômodo a cômodo já basta; (c) só na amostra grátis. A casa fica com 4 páginas nas duas primeiras respostas.
2. Os bônus vão dentro do PDF (decisão 3)? (a) dentro, no fim da parte 2: o livro vai a 34 páginas; (b) num PDF separado no Drive: o livro fica com 24.

**Para o Maestro (é ordem, não decisão do dono):** casas pela frente (E03, C01, F01) ou como hoje (C01, E03, F01)? E "Como ler uma planta" na parte 2 (como proposto) ou antes da página 3, como chave de leitura? Eu recomendo a frente e a parte 2: quem nunca leu planta tem as legendas na própria casa, e a página 2 aponta para a 16.

## 8. O que não conferi

- Se o cômodo a cômodo cabe em 1 ou 2 folhas por casa: depende do texto do Redator (A9).
- Se a página da parede sem janela é 1 ou 2 (a página B, em quadrinho, foi descrita no `e07-parede-na-divisa-ideias.md` e não foi decidida como página do livro).
- A altura da aba azul (200 mm) em página impressa: só vi na tela.
- Não li o `checar.py` inteiro: procurei e não achei regra presa a 17 páginas.

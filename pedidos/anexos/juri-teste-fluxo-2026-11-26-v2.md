# Proposta para o júri, 2ª rodada: primeira resposta mais curta no anúncio da Casa Fita (teste do fluxo `decisao`, 26/11/2026)

> Reescrita única da [`juri-teste-fluxo-2026-11-26.md`](juri-teste-fluxo-2026-11-26.md) (o original fica como estava), depois da 1ª rodada: notas 4, 4 e 2, média 3,3, os três abaixo do piso de 7 (`CONSELHO.md:58`). É a última rodada: se não chegar a 8,5 com todo jurado em 7 ou mais, a decisão vai ao dono com as duas notas (`CONSELHO.md:58`). Ficha `2026-11-26-0721`. Motivo de ir ao júri: o texto vai ao público (o cliente do anúncio lê no WhatsApp).
> **Esta versão não tem erro plantado.** A prova de calibração foi a 1ª rodada: os três jurados pegaram a medida 5 x 20 m. O gabarito está fora do repositório; ninguém aqui confirmou qual era o erro plantado.

## A pergunta, agora

Não é mais "trocar o `/fita`". O presidente respondeu "não trocar", e o `/fita` de três linhas do rascunho continua valendo (`pedidos/anexos/funil-textos-rascunho-2026-11-26.md`, linhas 52 a 64; Vera deu SIM, `pedidos/anexos/veto-funil-textos-2026-11-26.md:22`). A pergunta é: **vale levar ao Revisor e ao dono uma versão curta, com a medida certa e a ressalva da prefeitura, para testar contra a de três linhas quando o funil for ao ar?** Se o dono disser que não vale, fica só a de três linhas e esta proposta morre aqui.

## O que muda

**O ponto de partida:** o `/fita` **não existe** em `ebook/vendas/RESPOSTAS-RAPIDAS.md` (a lista dos atalhos, linhas 15 a 35, vai do `/planta` ao `/confia`, mais a saudação e a ausência). Ele só existe no rascunho do funil (linha 52), que ainda não entrou em nenhum arquivo de venda (rascunho, linha 3). Então não há texto para trocar: o `/fita`, curto ou longo, é **um atalho novo**, que entra na lista dos atalhos (linhas 15 a 35) e na seção 2 ("As mensagens") do `RESPOSTAS-RAPIDAS.md`, junto com o resto do funil, depois do sim do dono.

**O texto de hoje (rascunho, linhas 57 a 61), que não muda:**

```text
[nome], a Casa Fita é a do anúncio: 2 quartos, 56 m², um quarto em cada ponta, com sala e copa no meio.

Ela pede um lote de no mínimo 5 x 20,6 m (cabe num 5 x 25), com os recuos de referência; o da sua cidade, a prefeitura confirma.

O seu lote tem quanto de frente e de fundo?
```

**A versão curta proposta (dois blocos; texto sugerido pelo presidente do júri, ainda sujeito ao Revisor):**

```text
[nome], a Casa Fita é a do anúncio: 2 quartos, 56 m², um quarto em cada ponta. Ela pede um lote de no mínimo 5 x 20,6 m (cabe num 5 x 25), com os recuos de referência; o da sua cidade, a prefeitura confirma.

O seu lote tem quanto de frente e de fundo?
```

- **A medida** é a do `ebook/plantas/PLANTAS.md:150`, que sai do validador: "cabe num lote de 5 x 25 m (no mínimo 5,0 x 20,6 m)". Bate com `ebook/catalogo.md:49` (5 x 25), com `RESPOSTAS-RAPIDAS.md:5` ("pede 20,6 m de fundo") e com a leitura da Vera (`veto-funil-textos-2026-11-26.md`, "E03 56 m², 5 x 20,6"). Ninguém arredondou nem digitou de cabeça.
- **A ressalva fica inteira:** "com os recuos de referência; o da sua cidade, a prefeitura confirma" entrou de propósito em 26/11 (rascunho, linha 64, troca do Caio) porque a pessoa pode sair procurando terreno com esse número. Não se corta.
- **O que sai, e só isso:** "com sala e copa no meio" e a quebra entre o primeiro e o segundo bloco. É descrição da casa, não proteção do comprador.
- **Tamanho** (contado com `python3`, antes de preencher o [nome]): a de três linhas tem 278 caracteres; a curta, 252. Os dois ficam abaixo dos 512 do rascunho (linha 12), terminam com pergunta e não prometem aprovação, prazo nem custo.

## Por que

1. Mensagem mais curta e com menos blocos tende a ser lida até o fim no celular, e a pergunta chega mais cedo. **É a única razão.** E ela é pequena: a economia é de 26 caracteres e uma quebra de bloco. Por isso a proposta é testar, não trocar.

(A razão 2 da 1ª rodada saiu. A "uma medida só" foi obtida cortando o mínimo verdadeiro, e a pergunta continua pedindo dois números, frente e fundo. Com a medida certa, a versão curta tem as mesmas duas medidas da longa: não há ganho nisso.)

## Como aplica (só nesta ordem; nada entra em uso antes do último passo)

1. **Nota do júri** nesta 2ª rodada (piso 7 por jurado, média 8,5; `CONSELHO.md:57-58`).
2. **Revisor de risco** (Vera Veto, `contexto/EQUIPE.md:24`) lê a versão curta na peça montada, junto do resto do funil, e dá SIM, SIM SE ou NÃO. A leitura dela de 26/11 cobriu só a de três linhas.
3. **O dono decide a publicação** (`CLAUDE.md:36`) e responde às perguntas abaixo.
4. **Só então** o atalho entra no `ebook/vendas/RESPOSTAS-RAPIDAS.md` (lista, linhas 15 a 35, e seção 2) e no celular do negócio, com o resto do funil. Nenhuma pressa de "hoje mesmo": o funil inteiro ainda espera o dono (rascunho, seção 5).

## Como medir

- **A métrica é a que já existe:** "% que manda o tamanho do lote" (`PAINEL.md:133`; o próprio painel diz "pouca gente manda o lote: mudar a primeira mensagem").
- **Hoje não há linha de base.** O atalho é novo e ainda não houve conversa do anúncio da Casa Fita. Por isso os dois textos rodam ao mesmo tempo, e não um depois do outro.
- **Como alternar (proposta, o dono confirma):** pelo número da pessoa na planilha (rascunho, linha 447: "001, 002..."). Número ímpar recebe a de três linhas; número par, a curta. Alternar por semana misturaria o teste com o preço, que já muda de semana em semana (`RESPOSTAS-RAPIDAS.md:9`).
- **O que o sócio anota a mais, por pessoa que veio do anúncio da Casa Fita:** qual texto recebeu e se mandou a medida depois dele (sim ou não). Hoje a planilha não tem essas colunas (rascunho, linha 447).
- **Quantas conversas antes de comparar (proposta, o dono confirma):** pelo menos 30 de cada texto. Com menos que isso, só uma diferença muito grande se vê.
- **Critério de volta (proposta, o dono confirma):** a de três linhas é a que fica, salvo se a curta ganhar por pelo menos 10 pontos na "% que manda o tamanho do lote". Se ganhar menos, empatar ou perder, a curta sai. E sai na hora, sem esperar a contagem, se alguém responder que entendeu que a casa cabe num lote menor que 5 x 20,6 m.
- **Nenhum número de resultado** entra neste arquivo nem no painel antes de vir da planilha.

## Quanto custa e o que deixa de ser feito

- **R$:** zero. Não há anúncio a mais nem ferramenta paga; o teste usa as conversas que o anúncio da Casa Fita já traria.
- **Tokens:** esta reescrita, a 2ª rodada do júri e uma leitura do Revisor.
- **Tempo do sócio:** duas anotações a mais por conversa do anúncio da Casa Fita e um atalho a mais no celular (`/fita` e o curto). Isso é um pouco mais de chance de errar o atalho; se o dono preferir simples, fica um texto só.
- **Tempo do dono:** ler e responder às 4 perguntas abaixo.
- **O que deixa de ser feito:** nada da frente do e-book. O teste não abre frente nova (`CLAUDE.md`, "Uma coisa por vez"): ele só existe se o funil for ao ar e anda com ele.

## Como desfazer

- **Antes de ir ao ar:** não há o que desfazer; nenhum arquivo de venda foi editado.
- **Depois de ir ao ar:** apagar o atalho curto do `RESPOSTAS-RAPIDAS.md` (lista e seção 2) e das respostas rápidas do celular, e passar todo mundo para o `/fita` de três linhas. **Mensagem já enviada não volta.** Por isso a medida certa e a ressalva da prefeitura ficam na versão curta desde o primeiro envio.

## Perguntas ao dono (nada aqui está decidido)

1. Vale testar a versão curta, se a economia é de 26 caracteres, ou o `/fita` fica só com a de três linhas?
2. Se testar: a planilha ganha as duas anotações (qual texto recebeu; mandou a medida, sim ou não)? A planilha é sua.
3. Se testar: alternar pelo número da pessoa (ímpar, três linhas; par, curta), comparar depois de pelo menos 30 conversas de cada texto e ficar com a de três linhas salvo se a curta ganhar por 10 pontos. Confirma, ou prefere outra regra?
4. Que nome o atalho curto recebe no celular? (Sugestão: `/fitacurta`, sem hífen nem acento, como os outros; não se conferiu se o WhatsApp aceita hífen, rascunho, linha 15.)

## Resposta a cada defeito da 1ª rodada

| Jurado | Defeito (arquivo e linha) | O que esta versão fez |
|---|---|---|
| 1 | Medida 5 x 20 m (proposta, linha 11) | Trocada pelo mínimo do `PLANTAS.md:150`: "no mínimo 5 x 20,6 m (cabe num 5 x 25)". |
| 1 | Passo 1 sem Revisor (linha 23) | "Hoje mesmo, para o sócio já usar" saiu. Ordem escrita: júri, Revisor, dono, só depois o arquivo de venda. |
| 1 | Razão 2 contra a pergunta (linha 19) | A razão 2 saiu. Reparo do presidente aceito: a "uma medida só" falava das medidas de lote da mensagem, não da pergunta; o problema real era ter cortado o mínimo verdadeiro. |
| 2 | Medida 5 x 20 m leva a reembolso (linha 11) | Mesma troca da medida. "Sai na hora" se alguém entender que cabe num lote menor (seção "Como medir"). |
| 2 | Passo antes do sim e alvo que não existe (linhas 23 e 28) | O `/fita` é tratado como atalho novo (lista, linhas 15 a 35, e seção 2). "Como desfazer" reescrito: apagar do arquivo e do celular; mensagem enviada não volta. |
| 2 | Corte da ressalva da prefeitura (rascunho, linha 64) | A ressalva fica inteira; sai só "com sala e copa no meio". |
| 2 | Teste sem linha de base, amostra nem custo (`PAINEL.md:133`; proposta, linha 24) | Métrica do painel; sem linha de base por ser novo, por isso os dois rodam juntos; 30 conversas de cada e critério de volta (propostas, o dono confirma); custo em R$, tokens e tempo; o que deixa de ser feito. |
| 3 | Medida 5 x 20 m, número sem ferramenta (linha 11; `CLAUDE.md:45`) | Número copiado do `PLANTAS.md:150`, que sai do validador. Tamanhos contados com `python3`. |
| 3 | Passo antes do júri, da Vera e do dono (linha 23) | Ordem escrita na seção "Como aplica". A Vera é o Revisor de risco (`contexto/EQUIPE.md:24`): os dois passos são a mesma leitura. |
| 3 | Premissa falsa: o `/fita` não está no `RESPOSTAS-RAPIDAS.md` (linha 8) | Corrigido na seção "O que muda". Reparo do presidente aceito: "o /fita tem três linhas" é verdade para o rascunho que a proposta citava; o falso era só o alvo da linha 23. |

## Conferência antes de mandar ao júri

- [x] Medida igual ao `PLANTAS.md:150`, ao `catalogo.md:49` e ao `RESPOSTAS-RAPIDAS.md:5`.
- [x] "Recuos de referência" e "a prefeitura confirma" na versão curta.
- [x] Nenhum passo antes do sim; nenhum arquivo de venda editado.
- [x] O `/fita` dito como atalho novo; "como desfazer" de atalho novo.
- [x] Razão 2 fora; razão 1 com o tamanho real do ganho.
- [x] Métrica do painel, sem número de resultado; amostra e critério de volta como pergunta ao dono.
- [x] Nada do que o dono já decidiu mudou: preço alternado por semana, publicação dele, o `/fita` de três linhas valendo.

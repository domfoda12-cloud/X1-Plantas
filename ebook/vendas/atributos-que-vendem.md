# Atributos que vendem

> Banco do [Redator](../../.claude/agents/redator.md). Persona: [`../referencias/MERCADO.md`](../referencias/MERCADO.md). Números das plantas: [`../plantas/PLANTAS.md`](../plantas/PLANTAS.md). Toda peça passa pelo [Revisor de risco](../../.claude/agents/revisor-de-risco.md).
>
> Nota de 1 a 5: **D** = desejo (o Marcos quer?), **P** = prova (temos o número?), **E** = exclusividade (o concorrente diz isso?). Use primeiro os de soma mais alta. As notas são hipóteses até os testes da seção 5.

## 1. Atributos do produto (o e-book)

| Atributo | Escada até o dinheiro | D | P | E | Frase pronta |
|---|---|---|---|---|---|
| **Achar pelo lote** | índice por largura do terreno → acha em 1 minuto → não compra casa que não cabe → não joga fora projeto nem fundação | 5 | 5 | 3 (a Só Projetos também filtra por frente x fundo; o nosso diferencial é a casa desenhada no lote) | "Mede a frente do seu lote. A página certa é essa." |
| **Casas conferidas** | cada planta passa por um validador de medidas → quarto com cama e circulação, cozinha com 1,50 m livres → não descobre o erro depois da laje | 5 | 5 | 5 | "Cada uma das [nº] passou no nosso validador, com medidas mínimas de referência para quarto, cozinha e banheiro. Não substitui o profissional." |
| **Escolher antes de gastar** | a medida do lote na mão → acha a casa que cabe antes de pagar projeto ou abrir fundação → chega ao engenheiro com a casa escolhida → decide com calma, antes de gastar | 5 | 4 (o lote de cada casa sai do validador; o recuo da cidade, o engenheiro confere) | 3 | "Antes do primeiro tijolo, mede a frente do seu lote. A casa certa começa nessa medida." |
| **3 perguntas em cada casa** | as 24 trazem 3 perguntas para a primeira conversa com o engenheiro (`fichas/textos.py`) → chega sabendo o que perguntar → a primeira conversa já começa pelo que importa | 4 | 5 | 4 | "Cada casa vem com as 3 perguntas para fazer ao seu engenheiro antes de começar." |
| **O porquê de cada decisão** | "por que esta planta é assim" em 3 pontos → entende a casa → conversa de igual com o pedreiro | 4 | 5 | 5 | "Não é só o desenho. É o porquê de cada parede." |
| **Leve ao engenheiro** | chega com a casa escolhida → menos horas de projeto → orçamento mais rápido | 4 | 3 | 4 | "Chegue no seu engenheiro sabendo exatamente que casa você quer." |
| **Ver antes de construir** | planta humanizada e 3D → a família enxerga a casa → decide sem briga | 5 | 5 (as 24 saem mobiliadas, com a vista da rua e a casa em 3D de `visual/3d/`; animação ainda não existe) | 3 | "Veja a casa mobiliada antes de comprar o primeiro tijolo." |
| **Preço de um saco de cimento a mais** | R$ [preço: a definir pelo dono; R$ 67 é a recomendação da estratégia, não decisão] contra a planta avulsa dos concorrentes (faixas, fontes e datas em [`../referencias/MERCADO.md`](../referencias/MERCADO.md#projetos-similares-quem-vende-plantas-de-casas-e-o-que-aprender), seção 4) → 24 casas pelo preço de uma planta | 4 | 4 (preços de anúncio, mudam) | 3 | "[nº] casas pelo preço de uma ida a mais no depósito." *(só depois de o dono decidir o preço; confirmar o preço do saco na época)* |
| **Garantia** | sem risco → compra por impulso | 3 | ? | 2 | [garantia: a definir pelo dono]. A estratégia recomenda 7 dias; não use em peça até ele decidir |

> **"Constrói por etapas" saiu em 23/11/2026** (dono: tirar agora, fazer depois). O e-book ainda não mostra etapas: só a C03 tem ampliação nos dados, e fraca. Nenhuma peça promete construir por etapas, começar com 2 quartos e chegar a 3, ou "sem quebrar parede". Volta quando as etapas forem desenhadas, depois do lançamento.

## 2. Atributos que aparecem nas plantas (use a ficha da casa)

| Atributo técnico | Como dizer | Plantas |
|---|---|---|
| Núcleo molhado (cozinha, serviço e banho juntos) | "Uma tubulação só: menos dia de encanador" | as que a ficha diz "Banheiro colado na cozinha e na área de serviço" em [`PLANTAS.md`](../plantas/PLANTAS.md). Não vale para a C01 (banheiro com prumada própria) nem para a suíte de E07, F03, F04 e S09 |
| Corredor curto (até 11% da área) | "Só [X]% da casa é corredor. O resto você usa" (o X é o "Corredor" da Informação da casa; na C01, 4%) | C01, C03, C04, C05, C06, C07, F02, F05, S04, S05, S07 (todas com até 11%; números em `plantas/dados/`) |
| Corredor coberto lateral | "Nenhum corredor dentro de casa: todo cômodo abre para a lateral" | E01, E02, E05, E06, E07 |
| Lote de 5 m | "Cabe num lote de 5 m de frente" (não diga "o mais estreito que a lei permite": o piso de 5 m da Lei 6.766/1979 vale para loteamento novo, tem exceções e não vale para lote que já existe; ver [`MERCADO.md`](../referencias/MERCADO.md)) | E03 |
| Casa que cresce (em espera até a C03 ser redesenhada; dono, 23/11/2026) | "O quarto 2 já tem lugar marcado" | C03 |
| Pátio de luz | "Luz entre os quartos, sem janela para o vizinho" (vento só depois de o arquiteto conferir: o validador não mede ventilação cruzada) | E04 |
| Banheiro e circulação com 1,50 m livres para o giro da cadeira de rodas | "Espaço para girar a cadeira no banheiro e no corredor. O resto da NBR 9050, o engenheiro confere." | S03 |
| Escritório com porta para a rua | "O cliente entra sem passar pela sua casa" | S04 |
| Cozinha aberta para a área gourmet | "Faz o churrasco sem sair da conversa" | S07 |

## 3. Atributos proibidos (o Revisor veta)

"Aprovado na prefeitura", "sem precisar de engenheiro", "construa por R$ X", "pronto para construir", "projeto completo", "garantia de que cabe no seu lote" (depende do recuo da cidade).

## 4. Combinações campeãs para testar primeiro

1. **Lote + conferida:** "Tem um lote de 8 x 25? Essas [11, número da calculadora] casas cabem, com os recuos de referência, e cada uma foi conferida medida por medida. Não substitui o profissional: o seu engenheiro confere o seu lote."
2. **Antes de gastar + ver antes:** "Antes do primeiro tijolo, mede o seu lote e olha a casa pronta, em 3D."
3. **O porquê + engenheiro:** "Por que o banheiro fica do lado da cozinha? Leva essa resposta pro seu engenheiro."

## 5. O que os testes ensinaram

| Data | Peça | Atributo | Resultado (número da ferramenta) | Lição |
|---|---|---|---|---|
| | | | | |

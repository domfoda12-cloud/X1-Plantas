# Júri: as próximas melhorias (23/11/2026, Supervisor)

> Pedido do dono: "continuar melhorando o júri é essencial". Ficha de origem do júri: `pedidos/2026-11/2026-11-23-0156-adicionar-o-llm-council-karpathy-e-pedir-a-opiniao-dele-sobr.md` (abaixo, "ficha 0156"). Regras em vigor: `CONSELHO.md`, seção 5b.
> Este documento é proposta. Nada aqui foi rodado, instalado nem aplicado. Onde está escrito "escolha nossa", o dono não disse: ele confirma ou troca.

## Em 7 linhas

1. A régua está pronta para colar (parte 1). O exemplo do 9 **nunca passou pelo júri**: a maior nota do júri até hoje foi 7,5 (ficha 0156, linha 141).
2. Os modelos de pedido ao jurado e ao presidente estão prontos para copiar (parte 2).
3. O júri ainda não tem placar: `contexto/PLACAR.md` só mede veto e prova. Sem placar, nenhuma melhoria se prova. É a melhoria 1.
4. A regra 5 do júri pede uma prova a cada 5 rodadas. Já foram 7 rodadas e nenhuma prova do júri (as provas 1 e 2 foram do veto). A prova 3 está desenhada na parte 4.
5. O júri recomendou 9 coisas que o dono já respondeu. Ele seguiu 4 e não seguiu 5 (contagem minha, à mão; lista na melhoria 3). O júri precisa receber as decisões do dono e parar de rediscuti-las.
6. A regra escrita (5b, item 2) fala em revisão anônima com ranking. Ela não roda desde a rodada 3. Regra e prática têm de dizer a mesma coisa (melhoria 5).
7. A pesquisa pública aponta um limite que não some: os 4 jurados são da mesma família (Claude). Vira pergunta ao dono (parte 6).

---

## 1. A régua (cole inteira em toda rodada)

### 1a. O que vale 3, 6 e 9

| Nota | O que vale | Exemplo real deste projeto | Onde conferir |
|---|---|---|---|
| **3** | Não dá para executar como está. Falta a peça que faz a coisa funcionar, ou o fato central está errado, ou fere uma regra que não muda. | O plano de lançamento da rodada 6 (Haiku 2, Sonnet 3, Opus 2). Não havia como receber o Pix (sem conta, número, preço nem título) e não havia casa refeita aprovada. | Ficha 0156, linha 145 |
| **6** | A ideia está certa e a estrutura serve. Mas ainda não pode ir ao dono: tem fato errado ou não testado, ou algum passo anda antes do "sim". | A proposta v3 (Haiku 6, Sonnet 7, Opus 6,5). Cada adição tinha medida, custo e como desfazer. Mas o conferidor achou 3 fatos errados e o passo 3 aplicava uma recomendação antes do "sim" do dono. | `pedidos/anexos/integracao-novos-v3.md`, linha 41; `pedidos/anexos/juri-rodadas-3-a-5.md`, linhas 73 a 77; ficha 0156, linha 127 |
| **9** | Pode ir ao dono ou ao público como está. Todo número vem de ferramenta e confere. Nenhuma regra ferida. O comprador entende e ganha. Nada andou antes do "sim". Falta só polimento. | A troca de "a partir de" por "cabe num lote de 8 x 15 m (no mínimo 8,0 x 13,0 m)" na Casa Compacta. O número é o do validador (`python3 ferramentas/plantas.py validar` devolve "lote ref 8.0x13.0", conferido em 23/11). O dono decidiu ("Trocar"). O Revisor deu SIM SE e as condições foram aplicadas. Fechou uma divergência achada na prova 1. | `ebook/plantas/PLANTAS.md`, linha 9; `pedidos/anexos/decisoes-do-dono-2026-11-23.md`, linha 15; `pedidos/PROVAS.md`, linha 31; commit `6d14757` |

**Aviso sobre o 9:** esse exemplo é escolha do Supervisor. Ele nunca recebeu nota do júri. Troque pelo primeiro trabalho que o júri der 8,5 ou mais com os fatos confirmados pelo presidente.

### 1b. Como dar a nota

1. Escreva as críticas primeiro. A nota vem por último.
2. Escolha a âncora mais parecida (3, 6 ou 9). Suba ou desça no máximo 2 pontos, com o motivo em uma frase.
3. **0 a 2:** faz mal se for executado (promete o que não pode, gasta ou instala sem o "sim", engana o comprador).
4. **10:** vale 9 e já tem resultado real medido (venda, contato, prova passada).
5. Tetos (escolha nossa, não do dono):
   - fato central errado, conferido no arquivo: nota no máximo 5;
   - fere uma "regra que não muda" do `CLAUDE.md` ou uma decisão do dono em vigor: nota no máximo 3;
   - parte que depende de resposta que o dono ainda não deu: essa parte fica sem nota e vira pergunta.

### 1c. Os 3 ângulos e a pergunta exata de cada jurado

Cada jurado recebe um ângulo só. O ângulo roda entre os modelos: em 3 rodadas, cada modelo passa pelos 3 (anote na tabela da ficha).

| Ângulo | Pergunta exata (copie assim) | Abre sempre |
|---|---|---|
| **Comprador** | "Você é quem tem o lote e vai construir com pedreiro, com dinheiro contado. Se isto for feito como está, você entende, confia e fica mais perto de achar a casa que cabe no seu lote? Aponte o trecho em que você se confunde, desconfia ou se decepciona." | `ebook/referencias/MERCADO.md` (persona); `ESTRATEGIA.md`, seção 9 (tom de voz) |
| **Dinheiro** | "Isto aproxima o primeiro Pix ou baixa o custo por venda (custo por contato ÷ conversão)? Diga qual dos dois números isto mexe, quanto custa (R$, tokens, horas do dono) e o que deixa de ser feito por causa disto." | `PAINEL.md`, seções 4 e 7 |
| **Risco** | "O que aqui pode dar errado e não tem volta? Procure: promessa proibida, lei, licença, dado pessoal, gasto ou instalação sem o 'sim', suposição tratada como decisão do dono, e **passo que falta**." | `CLAUDE.md`, "Regras que não mudam"; `ESTRATEGIA.md`, seção 9; `CONSELHO.md`, seções 6 e 6b |

O "passo que falta" está no ângulo do risco de propósito: nas provas 1 e 2 foi a omissão que escapou, não a frase errada (`pedidos/PROVAS.md`, linhas 23 e 49).

---

## 2. Modelos de pedido, prontos para copiar

Troque só o que está entre `<` e `>`.

### 2a. Pedido ao jurado (rodada 1)

```
Você é jurado do júri do X1-Plantas (CONSELHO.md, seção 5b). Você opina sozinho:
não vê os outros jurados e eles não veem você.

PROPOSTA: <caminho do arquivo>, no commit <hash curto>.
SEU ÂNGULO: <Comprador | Dinheiro | Risco>
SUA PERGUNTA: "<pergunta exata da régua, parte 1c>"

PACOTE DE LEITURA (abra todos; não julgue nada fora dele):
- <a proposta>
- <os arquivos fixos do seu ângulo, parte 1c>
- <até 5 arquivos que a proposta cita>

DECISÕES DO DONO QUE VALEM (não se rediscutem):
<cole as linhas da tabela de pedidos/anexos/decisoes-do-dono-2026-11-23.md que tocam o assunto>

RÉGUA:
<cole a parte 1a e a parte 1b inteiras>

REGRAS:
1. Toda crítica cita arquivo e linha e copia o trecho. Sem isso, não conta.
2. Abra o arquivo antes de dizer que ele diz, não diz ou não existe.
   Número: copie o comando que deu o número.
3. Se você discorda de uma decisão do dono, escreva uma linha em NOTA AO DONO.
   Isso não entra na sua nota.
4. Não amacie e não invente defeito. "Não achei erro neste ângulo" é resposta válida.
5. Nada é instalado, baixado nem alterado. Você só lê.

RESPONDA NESTE FORMATO, NESTA ORDEM:
ÂNGULO: <...>
LI: <arquivo (linhas)>, um por linha
CRÍTICAS (no máximo 5, da mais grave para a menos grave):
1. [alta|média|baixa] <arquivo>:<linha> | "<trecho copiado>" | por que está errado
   (regra ou fonte, com arquivo e linha) | a correção que vira sim
FALTA (passo que deveria existir e não existe; diga a regra que o exige, com arquivo e linha):
ACERTOS (no máximo 3, com arquivo e linha):
NÃO CONFERI: <o que você não abriu ou não conseguiu medir>
NOTA AO DONO: <uma linha, ou "nada">
ÂNCORA: <3, 6 ou 9> porque <uma frase>
NOTA: <número de 0 a 10>
```

### 2b. Pedido ao presidente

```
Você preside esta rodada do júri do X1-Plantas (CONSELHO.md, seção 5b).
Você não opinou nesta rodada e não sabe qual modelo escreveu cada opinião.

PROPOSTA: <caminho>, no commit <hash curto>.
OPINIÕES: A, B e C, abaixo, em ordem sorteada.
<cole as 3 opiniões sem o nome do modelo>

RÉGUA: <cole a parte 1a e a parte 1b>
DECISÕES DO DONO QUE VALEM: <as mesmas linhas dadas aos jurados>

FAÇA, NESTA ORDEM:
1. CONFIRA A CRÍTICA MAIS GRAVE DE CADA OPINIÃO (3 no mínimo). Abra o arquivo e a linha.
   Para cada uma: CONFIRMADA, ERRADA ou NÃO DEU PARA CONFERIR, com o comando ou o trecho.
2. DESCARTE, dizendo qual: crítica sem arquivo e linha; crítica com fato errado;
   crítica sobre peça fora do pacote ou que não existe; crítica que rediscute decisão
   do dono (essa vira NOTA AO DONO).
3. CORRIGIR JÁ: no máximo 7 itens, do mais grave ao menos grave. Cada item:
   arquivo e linha, o trecho, a troca exata.
4. SÓ O DONO DECIDE: cada item como pergunta de uma linha, com opções e recomendação.
   A parte da proposta que depende dessa resposta fica sem nota.
5. NOTAS: a média das 3 notas (não mude a nota de ninguém) e a sua nota, separada,
   com a âncora.
6. VEREDITO, um só:
   - APROVADA: média de 8,5 ou mais E nenhuma crítica alta confirmada;
   - RODADA 2: a lista do item 3 é o único assunto dela (só existe uma rodada 2);
   - AO DONO: é a rodada 2 e a média ficou abaixo de 8,5. Vão as duas notas.
7. LINHAS PARA A FICHA, neste formato fixo:
| Rodada | Jurado | Ângulo | Nota | Críticas com arquivo e linha | Conferidas | Confirmadas | Erradas |
| Rodada | Presidente | Nota do presidente | Média dos jurados | Veredito | Tokens | Minutos |
8. O QUE VOCÊ NÃO CONFERIU.
```

Quem conduz preenche "Tokens" e "Minutos" com o número que o workflow devolver. Sem número, escreve "não medido".

### 2c. Pedido ao jurado (rodada 2, a única repetição)

```
Rodada 2 do júri. Mesmo ângulo e mesma régua da rodada 1.
PROPOSTA NOVA: <caminho>, commit <hash>. LISTA "CORRIGIR JÁ" DA RODADA 1: <cole>.

1. Para cada item da lista: CORRIGIDO, NÃO CORRIGIDO ou PIOROU, com arquivo e linha.
2. Crítica nova só entra se for de gravidade alta (fato errado, regra ferida,
   passo antes do "sim"). O resto vai em uma linha, "para depois".
3. ÂNCORA e NOTA, como na rodada 1.
```

---

## 3. As 5 próximas melhorias, em ordem de ganho

### Melhoria 1: placar do júri, gerado por ferramenta

- **O que é:** a tabela fixa do item 7 do pedido ao presidente entra na ficha a cada rodada. O `ferramentas/placar.py` passa a ler essa tabela, como já lê a do veto.
- **Por quê:** hoje as notas do júri estão em texto solto e em tabelas de formatos diferentes (ficha 0156, linhas 111 a 117 e linha 149). O placar não tem nenhuma linha do júri: ele só lê veto, prova e lição (`ferramentas/placar.py`, linhas 1 a 13). A regra do projeto é só relatar número que uma ferramenta devolveu. Sem isso, as outras 4 melhorias não se medem.
- **Como medir:** `python3 ferramentas/placar.py` devolve, por jurado e por ângulo: n de rodadas, nota média, críticas com arquivo e linha, conferidas, confirmadas. Funcionou se, depois da próxima rodada, o `contexto/PLACAR.md` mostrar n = 1 ou mais para cada jurado e o `placar.py --conferir` passar dentro do `checar.py`.
- **Hoje:** 0 linhas do júri no placar.
- **Quem:** Maestro (mexe em ferramenta: com ficha). Eu não edito ferramenta.

### Melhoria 2: o presidente confere a crítica mais grave de cada jurado, sobre um pacote fechado

- **O que é:** a regra de hoje diz "pelo menos 3 fatos", sem dizer quais. Passa a ser: a crítica mais grave de cada um dos 3 jurados. E cada jurado recebe a lista exata de arquivos e o commit; crítica sobre peça fora do pacote é descartada.
- **Por quê:** na rodada 7 um jurado contou 48 arquivos (são 56) e dois julgaram a find-skills, que não existe (ficha 0156, linha 154). Com "3 fatos quaisquer", o presidente pode conferir os fáceis e deixar passar o que derrubou a nota.
- **Como medir:** no placar, "Confirmadas ÷ Conferidas" por jurado, e a contagem de críticas descartadas por "peça fora do pacote ou que não existe". Meta (escolha nossa): 8 de cada 10 confirmadas e zero críticas sobre peça que não existe. Com n menor que 5, o número só informa.
- **Hoje:** não há taxa. Só o registro em texto da rodada 7.
- **Quem:** quem conduz a rodada usa os modelos 2a e 2b.

### Melhoria 3: as decisões do dono entram no pedido; discordar vira "nota ao dono"

- **O que é:** o jurado recebe as decisões do dono que tocam o assunto. Crítica que rediscute decisão em vigor não entra na nota: vira uma linha para o dono. E o placar passa a contar quantas recomendações do júri o dono seguiu.
- **Por quê:** das recomendações do júri que o dono já respondeu, contei 9. Ele seguiu 4 e não seguiu 5.

| Recomendação do júri (ficha 0156) | Resposta do dono (`decisoes-do-dono-2026-11-23.md`) | Seguiu? |
|---|---|---|
| Congelar o sistema por 7 dias (linha 89) | "60% e-book 40% sistema" (linha 31) | Não |
| Lançar com as 6 casas que passam na régua do banheiro (linha 91) | Só as refeitas e aprovadas por ele; 3 casas (linhas 8 e 46) | Não |
| Tirar E02 e E03 das grátis, C01 na frente (linha 91) | Só a Casa Compacta (linha 12) | Sim |
| Contratar arquiteto registrado (linha 91) | "Nós já temos um arquiteto!" (linha 13) | Não |
| Verba de um teste de anúncio pequeno (linha 91) | R$ 20 por dia, depois do teste sem gastar (linha 56) | Sim |
| Parar placar, nota, repreensão e as 3 rodadas de veto (linha 93) | "Manter e medir" (linha 22) | Não |
| Parar a noite "só de aprendizado" (linha 93) | Mudar a tarefa de hora em hora para o e-book (linha 17) | Sim |
| Parar o vídeo até o e-book estar à venda (linha 93) | Vídeo depois do e-book (linha 61) | Sim |
| Parar o júri (linha 137, "recomendação: sim") | "Sim, mais uma rodada" (linha 18) | Não |

  Essa contagem é minha, à mão, lendo as duas tabelas. Não é número de ferramenta. Ela não diz que o júri errou: diz onde o júri vê diferente do dono, e quem decide é o dono. O júri puxou para "menos sistema"; o dono quer o sistema "o mais melhor possível". A pesquisa confirma o cuidado: juízes de modelo concordam entre si e mesmo assim ficam longe do que a pessoa valoriza (parte 5, linha "consenso não é acerto").
- **Como medir:** duas contagens no placar. (a) "Críticas que rediscutem decisão do dono", por rodada: meta zero dentro da nota. (b) "Recomendações seguidas ÷ respondidas", com uma coluna "Decisão do dono" na tabela de recomendações da ficha. Depois da primeira venda, a comparação que manda é a da regra 5: nota do júri contra o custo por venda (`PAINEL.md`, seção 4).
- **Hoje:** 4 de 9, à mão.
- **Quem:** quem conduz cola as decisões no pedido; Maestro acrescenta a coluna e a contagem.

### Melhoria 4: rodada 2 fechada

- **O que é:** na rodada 2 o jurado confere a lista "corrigir já" da rodada 1, item por item. Crítica nova só entra se for de gravidade alta (modelo 2c).
- **Por quê:** nas rodadas 3, 4 e 5 o júri trouxe 22, 23 e 21 críticas novas (`pedidos/anexos/juri-rodadas-3-a-5.md`, linhas 42 a 44, 99 a 101 e 165 a 167). A nota caiu de 6,5 para 6,3 e 6,0. O laço gastou 2,95 milhões de tokens, 18 agentes e 69 minutos (ficha 0156, linha 137). A proposta era um alvo que mudava de lugar: cada rodada julgava outra coisa, e as duas notas não se comparavam. O máximo de 2 rodadas já corta o gasto; falta fazer a rodada 2 medir a mesma coisa que a 1.
- **Como medir:** (a) "itens corrigidos ÷ itens da lista", contado pelo presidente com arquivo e linha e somado pelo placar; (b) nota da rodada 2 menos nota da rodada 1; (c) tokens por rodada, o número que o workflow devolve. Referência que já existe: 536 mil tokens para 4 agentes (ficha 0156, linha 141). As rodadas 6 e 7 não têm tokens anotados na ficha.
- **Quem:** quem conduz a rodada.

### Melhoria 5: a etapa 2 escrita como ela roda

- **O que é:** o item 2 da seção 5b diz que cada jurado lê as outras opiniões e as ordena. Isso não roda desde a rodada 3: virou um conferidor de fatos e, agora, o presidente (`pedidos/anexos/juri-rodadas-3-a-5.md`, item 8, ponto iii). Com um ângulo por jurado, ordenar opiniões compara coisas diferentes.
- **Recomendação:** tirar o ranking da regra agora, para regra e prática dizerem o mesmo (custo zero). Testar depois, numa prova, a versão barata: cada jurado recebe as críticas dos outros **sem a nota, sem o nome e em ordem sorteada**, e só marca "confirmo", "não confirmo" ou "não sei", com arquivo e linha. Ninguém muda a própria nota.
- **Por quê:** a pesquisa mostra que modelo que vê a resposta de outro tende a concordar, e troca resposta certa por errada; e que a ordem em que as respostas aparecem muda o julgamento (parte 5).
- **Como medir:** na prova, a crítica falsa plantada numa opinião (parte 4): quantas chegam à síntese com a conferência cruzada e quantas sem ela. No dia a dia: `grep -c "ordena" CONSELHO.md` na seção 5b devolve 0 depois da troca, e a tabela da ficha ganha a coluna "Derrubadas na conferência cruzada" quando o teste rodar.
- **Quem:** Maestro (mudança de regra: uma linha no `CONSELHO.md`, com o aviso no quadro).

### Fora das 5, mas barato

- **Diferença entre as notas:** as notas dos jurados quase não se afastam. Rodada 1: 4, 5, 5 e 5. Rodada 3: 6, 7 e 6,5. Rodada 7: 4,5, 4 e 5 (ficha 0156, linhas 113, 115 e 149). A diferença entre a maior e a menor foi de 1 ponto nas três (conta minha). Com ângulos diferentes, a diferença deve crescer. O placar pode devolver "maior menos menor" por rodada.
- **Crítica alta confirmada trava a aprovação:** já está no item 6 do modelo 2b. Uma crítica grave e confirmada, de um jurado só, impede o "aprovada", mesmo com média alta. A pesquisa chama isso de veto da minoria (parte 5).

---

## 4. Prova 3: a primeira prova do júri com erro plantado

As provas 1 e 2 mediram o veto (5 agentes, planos). Esta mede o júri: a nota, os ângulos e o presidente.

### 4a. O que ela devolve (5 números)

| Número | Pergunta | Conta |
|---|---|---|
| Detecção | O júri acha o erro plantado? | Erros achados, de 5. "Achado" = pelo menos um jurado cita o erro com arquivo e linha **e** ele chega à síntese do presidente. |
| Alarme falso | O júri inventa erro em proposta limpa? | Versões limpas com crítica alta que o conferidor mostra ser falsa, de 5. |
| Separação | A nota distingue a boa da ruim? | Pares em que a limpa tirou nota maior que a plantada, de 5; e a diferença de cada par. |
| Presidente | Ele confere a crítica mais grave? | Críticas falsas plantadas que ele derrubou, de 2. |
| Ruído | Quanto a régua varia sozinha? | A mesma proposta vai aos dois grupos; diferença entre as duas médias. |

### 4b. Montagem

1. **5 pares de propostas curtas** (até 40 linhas cada), sobre 5 assuntos diferentes deste projeto, apoiadas em arquivos reais (o jurado precisa abrir o repositório para julgar). Cada par tem a versão limpa e a versão com **um** erro plantado. As duas são iguais fora do trecho plantado.
2. **Dois grupos, em chamadas separadas.** Cada grupo é um júri completo: 3 jurados (um por ângulo) e um presidente. O grupo X recebe os pares 1, 3 e 5 na versão plantada e os pares 2 e 4 na versão limpa. O grupo Y recebe o contrário. **Nenhuma chamada recebe as duas versões do mesmo par.**
3. **Uma proposta "termômetro"**, igual nos dois grupos, para medir o ruído.
4. **Uma crítica falsa por grupo:** antes de passar as opiniões ao presidente, quem monta acrescenta a uma opinião sorteada uma crítica de gravidade alta com arquivo e linha que não dizem aquilo.
5. **Mesma composição nos dois grupos** (mesmos modelos nos mesmos ângulos). Assim a diferença de nota vem da versão, não de quem julgou.
6. **Cinco tipos de erro, um por par.** Nenhum é frase que fere regra escrita (isso todos acham: `pedidos/PROVAS.md`, linha 22):
   - número diferente do que a ferramenta devolve;
   - passo que falta e que uma regra exige;
   - citação falsa (a proposta diz "conforme o arquivo X" e o arquivo não diz);
   - peça que não existe tratada como pronta;
   - passo que anda antes do "sim" do dono, escrito sem as palavras da regra.
7. **Os casos concretos não ficam neste arquivo nem no repositório.** O jurado lê o repositório. O gabarito fica fora até a nota, como nas provas 1 e 2.

### 4c. Como ela evita as falhas das provas 1 e 2

| Falha | Onde está escrita | Trava na prova 3 |
|---|---|---|
| Prova 1: os planos "limpos" não eram limpos; o alarme falso ficou sem medida | `pedidos/PROVAS.md`, linha 19 | Antes de rodar, um conferidor que **não é o autor** e não será jurado passa cada versão limpa por uma lista escrita: todo número refeito com o comando, todo arquivo citado aberto, regras do `CLAUDE.md` e do `CONSELHO.md`. Defeito achado é consertado e conferido de novo. |
| Prova 1: o gabarito errou em 3 planos | linha 24 | Cada erro plantado tem prova de máquina: um comando cuja saída é diferente na versão limpa e na plantada. Sem esse comando, o par não entra. |
| Prova 1: teto (39 de 40) | linha 22 | Nenhum erro é frase que fere regra escrita. Todos pedem abrir um arquivo ou notar uma falta. |
| Prova 2: a versão gêmea limpa estava na mesma prova | linhas 50 e 52 | As gêmeas vão a grupos diferentes, em chamadas separadas. Agente não tem memória entre chamadas. |
| Prova 2: um plano da prova enunciava a regra medida | linhas 50 e 52 | Conferência mecânica antes de rodar: para cada regra medida, um `grep` das palavras da regra no pedido e nas outras propostas do mesmo grupo tem de devolver 0. O pedido leva só a régua e o ângulo: não leva lista de regras, nem lições, nem o erro da prova anterior. |

### 4d. Quem faz, quanto custa, o que muda

- **Monta e dá a nota:** o Fable, numa conversa. **Preside:** uma chamada nova, que não recebe o gabarito. **Confere as limpas:** o Revisor de risco (15 de 15 nas provas, `contexto/PLACAR.md`).
- **Custo:** 8 chamadas de júri (2 grupos × 3 jurados e 1 presidente) e 1 do conferidor. Tokens: não medido. Referência: a prova 1 teve 6 agentes e 536 mil tokens (`pedidos/PROVAS.md`, linha 7). Como o júri é caro, o motivo vai escrito na ficha (seção 5b, "Custo").
- **Passa se** (escolha nossa): detecção de 4 ou 5; alarme falso de 0 ou 1; limpa acima da plantada em 4 ou 5 pares; presidente 2 de 2; ruído de até 1 ponto.
- **O que cada resultado muda:**
  - detecção baixa num tipo de erro: reescrever a pergunta do ângulo que devia achá-lo;
  - alarme falso alto: a âncora do 9 está fraca; trocar o exemplo;
  - separação baixa: a nota não distingue; o veredito passa a sair só das críticas confirmadas, sem média;
  - presidente falha: "a mais grave de cada jurado" vira campo obrigatório, e o `placar.py --conferir` recusa a rodada sem ele;
  - ruído acima de 1 ponto: diferença menor que o ruído entre rodada 1 e rodada 2 não conta como subida nem queda.
- **Limites:** n = 5 pares é o mínimo para mudar regra (regra do placar). Todos os modelos são Claude. O resultado se junta ao das próximas provas.
- **Formato do resultado:** em `pedidos/PROVAS.md`, na tabela que o placar já lê (`| Agente | Achados (de N) | Parciais | Alarmes falsos (de M) | ...`), com uma linha por grupo do júri e uma por presidente.

---

## 5. O que a pesquisa pública diz sobre júri de modelos

Abri as páginas abaixo em 23/11/2026. Li o resumo de cada artigo no arXiv; do artigo de Jain abri também o texto. Não li os artigos inteiros. Os estudos usam outros modelos e outras tarefas (nota de código, resumo, pergunta e resposta). Nenhum testou um júri de propostas como o nosso. Servem de direção, não de número para nós.

| Tema | O que a página diz | Fonte | O que muda no nosso júri |
|---|---|---|---|
| **Viés de concordância** | Juízes de modelo acertam 96% das respostas válidas e menos de 25% das inválidas: aprovam fácil, reprovam mal. O voto da maioria ajuda só em parte (no texto: acerto de 19,2% nas inválidas). O "veto da minoria" reduz o viés (no texto: 4 de 14 juízes dizendo "inválido" bastam). | Jain, Ahmed, Sahai e Leong, 2025: [arxiv.org/abs/2510.11822](https://arxiv.org/abs/2510.11822) | Não aprovar pela média. Uma crítica alta confirmada trava o "aprovada" (modelo 2b, item 6). A prova tem de ter proposta ruim, para medir se o júri reprova. |
| **Auto-preferência** | Modelos reconhecem o próprio texto acima do acaso, e quanto melhor reconhecem, mais o favorecem. | Panickssery, Bowman e Feng, 2024: [arxiv.org/abs/2404.13076](https://arxiv.org/abs/2404.13076) | Aqui quem escreve a proposta é Claude e quem julga é Claude. Esconder o nome não resolve sozinho. |
| **Auto-preferência** | O GPT-4 mostra auto-preferência clara. A causa apontada é a familiaridade: o juiz dá nota mais alta ao texto que lhe soa mais previsível, tenha sido escrito por ele ou não. | Wataoka, Takahashi e Ri, 2024: [arxiv.org/abs/2410.21819](https://arxiv.org/abs/2410.21819) | O júri pode premiar o texto "com cara de Claude". Por isso a nota depende de fato conferido em arquivo, não de como a proposta soa. |
| **Júri de famílias diferentes** | Um painel de modelos menores, de famílias diferentes, foi melhor que um juiz grande sozinho em 3 arranjos e 6 conjuntos de dados, com menos viés a favor da própria família e custo mais de 7 vezes menor. | Verga e outros, 2024: [arxiv.org/abs/2404.18796](https://arxiv.org/abs/2404.18796) | Nosso júri é de uma família só. É o limite que as regras não tiram. Vira pergunta ao dono (parte 6). |
| **Ordem das opiniões** | Mudar só a ordem das respostas muda o resultado: com o ChatGPT de juiz, o Vicuna-13B "vence" o ChatGPT em 66 de 80 perguntas. Três consertos: escrever as provas antes da nota; juntar julgamentos feitos em ordens diferentes; chamar gente nos casos difíceis. | Wang e outros, 2023: [arxiv.org/abs/2305.17926](https://arxiv.org/abs/2305.17926) | Críticas antes da nota (modelo 2a). Opiniões em ordem sorteada para o presidente (modelo 2b). O caso difícil vai ao dono. |
| **Ordem das opiniões** | O viés de posição não é acaso. Muda com o juiz e a tarefa. Depende pouco do tamanho do pedido e muito da distância de qualidade entre as respostas. Estudo com 15 juízes, 22 tarefas e mais de 150.000 avaliações. | Shi e outros, 2024: [arxiv.org/abs/2406.07791](https://arxiv.org/abs/2406.07791) | Nossas notas ficam a 1 ponto umas das outras: é o caso em que a ordem pesa mais. Sortear sempre e anotar a ordem. |
| **Conformidade** | Em grupos de modelos existe conformidade, como em grupos de gente. Pesam o tempo de interação e o tamanho da maioria. Duas saídas testadas: personas mais fortes e um passo de reflexão. | Weng, Chen e Wang, 2025: [arxiv.org/abs/2501.13381](https://arxiv.org/abs/2501.13381) | Um ângulo por jurado funciona como persona. Opinião e nota separadas, antes de ver qualquer outra. |
| **Conformidade** | Debate entre modelos pode piorar o resultado. Modelos trocam resposta certa por errada depois de ler o raciocínio do colega, e preferem concordar a contestar. | Wynn, Satija e Hadfield, 2025: [arxiv.org/abs/2509.05396](https://arxiv.org/abs/2509.05396) | Sem debate. Ninguém muda a própria nota depois de ler os outros (melhoria 5). |
| **Consenso não é acerto** | 42 juízes de modelo. Em critérios subjetivos, eles concordam entre si tanto quanto as pessoas, mas só chegam a 58% a 66% da concordância das pessoas. No critério com resposta conferível, quase toda a distância some. Juntar juízes aproxima do eixo comum deles, não do das pessoas. | Mukherjee, Hamna, Bali e Sitaram, 2026: [arxiv.org/abs/2606.03043](https://arxiv.org/abs/2606.03043) | Três jurados concordando não prova nada. Preferir crítica conferível (arquivo, linha, comando). Comparar com o dono e com a venda (melhoria 3). |
| **Régua** | Régua travada, julgamento apoiado em trecho citado e nota calibrada com a escala das pessoas: mais concordância com pessoas em 4 conjuntos de teste e mais estabilidade quando a régua é reescrita com o mesmo sentido. | Hong e outros, 2026: [arxiv.org/abs/2601.08654](https://arxiv.org/abs/2601.08654) | A mesma régua em toda rodada, sem reescrever no meio do laço. Trecho copiado em toda crítica. |
| **Régua** | Raciocínio escrito antes da nota e resposta em formulário aproximam o juiz das pessoas (correlação de 0,514 em resumo). O artigo avisa de um viés a favor de texto escrito por modelo. | Liu e outros, 2023 (G-Eval): [arxiv.org/abs/2303.16634](https://arxiv.org/abs/2303.16634) | Formato fixo de resposta, com a nota no fim. |
| **Régua** | Com uma resposta de referência e uma régua de notas, um avaliador chegou a 0,897 de correlação com pessoas em 45 réguas (o GPT-4, 0,882; o ChatGPT, 0,392). | Kim e outros, 2023 (Prometheus): [arxiv.org/abs/2310.08491](https://arxiv.org/abs/2310.08491) | Âncoras com exemplo real em cada nível, como na parte 1. |
| **O método de origem** | A revisão é anônima "para o modelo não ter favoritos". O autor diz que o projeto foi "99% vibe coded" num sábado e que não dará suporte. A página não cita licença. | Karpathy: [github.com/karpathy/llm-council](https://github.com/karpathy/llm-council) | Continua valendo: só o método, nada do código. |

**Para o caderno de pesquisas:** eu só posso escrever este arquivo. Quem conduz registra os 13 achados com `python3 ferramentas/pesquisa.py nova --tema juri --quem supervisor ...`. A busca `pesquisa.py buscar juri jurado LLM juiz vies` devolveu 0 achados antes da pesquisa.

---

## 6. Perguntas ao dono

1. **Jurado de outra empresa.** A pesquisa diz que júri de famílias diferentes julga melhor. Hoje os 4 são Claude.
   (a) Fica como está e calibramos com a prova 3 e com as suas decisões (recomendado agora: custo zero, nenhum dado sai);
   (b) um teste com um jurado de outra empresa, em uma rodada: pede chave paga, manda texto do projeto para fora, passa por ficha e veto do Revisor;
   (c) decidir depois da prova 3.
2. **Prova 3 do júri.** Custa 9 chamadas de agente.
   (a) Rodar antes da próxima rodada do júri (recomendado: a regra pede prova a cada 5 rodadas e já foram 7);
   (b) rodar depois do e-book das 3 casas;
   (c) não rodar.
3. **Tetos e metas da régua** (parte 1b, item 5, e parte 4d, "passa se"): são escolha nossa. (a) Valem assim; (b) você troca algum.

Sem resposta, nada muda: a régua e os modelos são texto e podem ser usados; a prova e a mudança de regra esperam.

---

## 7. O que eu não conferi

- Não rodei nenhuma rodada do júri nem a prova. A régua e os modelos não foram testados.
- Não li os artigos inteiros (só os resumos, e o texto de um).
- Não rodei o `checar.py`. Rodei só `plantas.py validar` (24 plantas, 0 com erro; a árvore do git ficou igual) e `pesquisa.py buscar`.
- A contagem "4 de 9" e as diferenças entre notas são contas minhas, à mão.
- As mudanças no `placar.py` e no `CONSELHO.md` não foram feitas: são do Maestro, com ficha.
- Não conferi se o workflow do júri devolve tokens por rodada. As rodadas 6 e 7 não têm o número na ficha.
- O exemplo do 9 não foi julgado pelo júri.

**O que aprendi:** supervisor: júri sem placar não melhora, só muda; antes de mexer na regra, pôr a nota, a prova de cada crítica e a decisão do dono numa tabela que a ferramenta soma.

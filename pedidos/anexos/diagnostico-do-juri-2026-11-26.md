# Diagnóstico do júri (26/11/2026)

> Pedido do dono (26/11): "Nosso juri nao parece estar sendo muito eficaz". Ficha: `pedidos/2026-11/2026-11-26-0105-nova-configuracao-dos-agentes-pesquisador-no-opus-revisor-um.md`.
> Este documento é só leitura e proposta. Nenhuma regra mudou por causa dele. Os números são os que já estavam escritos no repositório; onde eu somei ou contei à mão, está dito.

## Resumo em 6 linhas (para o dono)

1. Você tem razão. O júri rodou 11 vezes em 4 dias, sobre 12 assuntos, e **não fechou nenhuma decisão**: nenhuma nota chegou ao mínimo de 8,5, e tudo voltou para você ou parou.
2. Ele achou coisa de verdade (duas casas apertadas entre as grátis; um trabalho que começou antes do seu "sim"). Mas a maior parte foi repetição, e ele mesmo errou fatos em pelo menos 4 das 11 rodadas e na prova.
3. O gasto anotado passa de 5,6 milhões de tokens (a unidade que come o seu limite de uso), e 6 das 11 rodadas nem têm o gasto anotado. Uma leitura do Revisor gasta de 70 a 91 mil e achou todos os erros plantados nas duas provas dele.
4. As causas principais: o mínimo de 8,5 nunca foi atingido por ninguém; os jurados julgam um texto sobre a peça, não a peça pronta; o júri foi usado em perguntas que só você responde; e as regras novas não têm quem obrigue (na rodada de hoje, várias foram puladas).
5. Proponho 5 mudanças, em ordem de efeito. A primeira: aprovar quando não sobra defeito grave confirmado, em vez de exigir a média 8,5. Nenhuma vira regra antes de um teste com erro plantado.
6. **Você decide uma coisa:** se dizer "sim", rodamos UMA prova com erro plantado (a prova 3 gastou cerca de 1,6 milhão) e só depois mexemos na regra. Se disser "não" ou não responder, o júri fica como está, só com o que você já aprovou hoje (júri só para decisão cara ou pública), e nada mais muda.

---

## 1. Todas as rodadas que achei

"Rodada" aqui é cada vez que jurados deram nota. A conta é minha, à mão: 8 em 23/11 (o veredito e as rodadas 1 a 7), 2 em 24/11 e 1 em 26/11. A prova 3 e o passo da v6 estão na tabela, mas não entram na conta das 11.

"Ficha 0156" é `pedidos/2026-11/2026-11-23-0156-adicionar-o-llm-council-karpathy-e-pedir-a-opiniao-dele-sobr.md`. "Ficha 0144" é `pedidos/2026-11/2026-11-23-0144-trabalho-autonomo-a-noite-skills-do-e-book-atendimento-campa.md`.

| # | Data | Assunto | Notas | Tokens escritos | Fechou decisão? | O que de útil saiu |
|---|---|---|---|---|---|---|
| 1 | 23/11, madrugada | Veredito sobre o sistema montado em 22 e 23/11 | 4, 5, 5 e 6; presidente: 5 (ficha 0156, linha 87) | Não anotado | Não. Virou 9 recomendações; você seguiu 4 e não seguiu 5 (`pedidos/anexos/juri-proximas-melhorias.md`, linhas 175 a 187) | **Erro real:** E02 e E03, as casas mais apertadas, estavam entre as grátis (confirmado na linha 79; você trocou para só a Casa Compacta). Os próprios jurados erraram números: 77 commits (eram 107) e 22 casas (eram 18), linha 79 |
| 2 | 23/11, 02h | Rodada 1: proposta das 5 ferramentas, v1 | 4, 5, 5, 5; média 4,75 (linha 115) | Não anotado | Não | **Proposta mudada:** o `/juri` deixou de ser skill nova; o METAS.md saiu; duas ferramentas viraram pergunta a você |
| 3 | 23/11 | Rodada 2: v2 | 6, 6,5, 6, 6; média 6,1 (linhas 116 e 121) | Não anotado | Não | **Proposta mudada:** a regra do presidente não fechava; custo sem fonte; contradição entre duas tabelas (linha 123) |
| 4 | 23/11 | Rodada 3: v3 | 6, 7, 6,5; média 6,5 (linha 117) | Junto com as rodadas 4 e 5 | Não | 22 críticas novas e 3 fatos errados na proposta. O presidente já avisou: parar depois da v4, "porque o gargalo virou a resposta dele, não a proposta" (linha 129). Rodaram mais duas |
| 5 | 23/11 | Rodada 4: v4 | 6,5, 6, 6,5; média 6,3 (linha 118) | Junto | Não | **Erro real:** o Maestro tinha começado o everything-claude-code antes do seu "sim"; parado às 03:16 (`pedidos/2026-11/2026-11-23-0209-adicionar-o-everything-claude-code-worldflowai.md`, linha 51). 23 críticas novas, 9 fatos errados |
| 6 | 23/11 | Rodada 5: v5 | 5,5, 6, 6,5; média 6,0 (linha 119) | **2,95 milhões** nas rodadas 3 a 5: 18 agentes, 69 minutos (linha 139) | Não. O laço parou porque a nota caiu duas vezes | Quase só repetição: 21 críticas novas, 10 fatos errados, o mesmo gargalo ("a página de decisões ainda não existe, quatro versões depois") |
| - | 23/11, 03h45 | Passo final da v6 (não é rodada: Revisor e Fable leram) | Fable 7,5 (linha 143) | **536 mil**, 4 agentes (linha 143) | Não: virou a página de 9 perguntas para você | A página de decisões, que você respondeu em 23/11 |
| 7 | 23/11, 17h45 | Rodada 6: plano de lançamento | 2, 3, 2; média 2,3 (linha 147) | Não anotado | Não. "A nota sobe quando essas decisões existirem, não reescrevendo o plano" | Repetiu o veredito (nada vendável, sem como receber o Pix) e pôs 5 ações em ordem. Duas afirmações dos jurados estavam velhas (linha 147) |
| 8 | 23/11, noite | Rodada 7: ferramentas novas | 4,5, 4, 5; presidente: 5 (linha 151) | Não anotado | Não: virou pergunta a você, que perguntou de volta "por que o júri não quer os agentes de programação?" (`pedidos/anexos/decisoes-do-dono-2026-11-23.md`, linha 87) | Um jurado contou 48 arquivos (eram 56) e dois julgaram uma peça que não existia (linha 156). Daqui saíram a régua e o máximo de 2 rodadas |
| - | 23 e 24/11 | Prova 3 (teste com erro plantado, não é decisão) | Limpa acima da plantada nos 5 pares (`pedidos/PROVAS.md`, linha 83) | **Cerca de 1,6 milhão**; 2 presidentes cortados pelo limite não informaram (linha 92) | Não se aplica | Mediu o júri pela primeira vez: achou 5 de 5 erros plantados; 1 alarme falso em 4. De quebra, 3 problemas reais (linha 91) |
| 9 e 10 | 24/11, 17h a 19h | 7 decisões "fáceis de desfazer" (J1, J2, J3, J5, J7, J8, J9), 2 rodadas | Rodada 1: médias de 4,8 a 6,7. Rodada 2: de 6,8 a 7,5 (`pedidos/anexos/juri-decisoes-faceis-2026-11-24.md`, linhas 17 a 23) | Jurados: **237.238 + 155.376 + 188.511** (ficha 0144, linha 143). O presidente não está anotado | **Não, 0 de 7.** "Nenhuma chegou a 8,5": todas foram a você em cartões (linha 25). Pelo arquivo, só o J1 tem resposta sua (linha 31) | **Proposta mudada:** o J7 foi invertido, o J3 ficou literal ao que você disse, e a suposição "móvel de loja" virou pergunta. Mas J2 (título) e J5 (validade do preço) nem eram da equipe (linhas 34 e 46) |
| 11 | 26/11, madrugada | Nicho do Instagram de IA, 8 ideias | Melhor: 7,3; 8,0 numa versão condicional (`pesquisas/instagram-ia/juri-nicho/presidente.md`, linhas 5 e 77) | Não anotado | Não. "Quem decide o nicho é o dono" (linha 75) | Uma recomendação e 3 testes de produção. O presidente escreveu: isso se prova "com três testes de produção, não com mais opinião" (linha 5) |

**Tokens:** a soma dos quatro números escritos (2,95 milhões, 536 mil, cerca de 1,6 milhão e os três jurados de 24/11) dá cerca de 5,67 milhões. A soma é minha; dois dos quatro são "cerca de". Seis das 11 rodadas não têm número nenhum.

---

## 2. Quantas rodadas fecharam uma decisão

**Nenhuma.** Das 11 rodadas, sobre 12 assuntos (o sistema, a proposta das ferramentas, o plano de lançamento, as ferramentas novas, as 7 decisões fáceis e o nicho), nenhuma terminou em "aprovado".

- Contei 31 médias de nota escritas (conta minha, à mão). **Zero chegou a 8,5.** A maior, como a peça foi julgada, é 7,5 (J1, rodada 2). Há um 8,0, mas é nota condicional, de uma versão que um jurado imaginou.
- O que fechou depois foi você: a página de 9 perguntas (23/11) e o J1 ("2 ok", 25/11). Os outros 6 cartões do júri de 24/11 seguem "ainda não visto" ou "ainda não respondido" no arquivo (linhas 37 a 67).
- Você tinha dito, em 24/11, que no que é fácil de mudar a equipe podia seguir "com a decisao do juri" e mostrar depois (`pedidos/anexos/decisoes-do-dono-2026-11-23.md`, linha 147). Na prática o júri transformou 7 decisões delegadas em 7 cartões esperando você. O efeito foi o contrário do pedido.

---

## 3. O que só o júri achou, e o que foi repetição

### Achados que estão no repositório como sendo do júri

1. **Trabalho antes do "sim".** Na rodada 4, a conferência no repositório mostrou que o Maestro já tinha feito 3 gravações do everything-claude-code sem esperar você. A ficha diz: "erro do Maestro, achado pelo júri" (ficha 0209, linha 51).
2. **As casas grátis erradas.** O veredito apontou E02 e E03, as mais apertadas, na amostra grátis. Foi conferido (ficha 0156, linha 79) e você mudou a amostra.
3. **Propostas que contrariavam a sua fala.** Em 24/11 o jurado do comprador deu 3 a duas propostas. O J7 ia contra o seu "seja bem detalhista" e foi invertido. O J3 voltou ao literal "só a planta e um guia inicial" (`juri-decisoes-faceis-2026-11-24.md`, linhas 40 e 52).
4. **Na prova 3, três problemas reais fora do gabarito:** o anúncio "C01 8 x 15" que bate no veto do `/oferta`; a conta de R$ 280 por preço; e o `livro.py --previa` que podia regravar o PDF oficial (`pedidos/PROVAS.md`, linha 91).
5. **No nicho, o risco de saúde.** A ideia "Seu corpo, hoje" teve 8 em alcance e 2 em risco (`presidente.md`, tabela de notas). Foi o ângulo diferente que mostrou o problema.

Um aviso honesto: em 1, 2 e 4 quem achou foi **a conferência de fatos no repositório** (o conferidor ou o presidente), não a nota. E não dá para provar que "ninguém mais acharia": o item 3, por exemplo, é o que a reconferência dos pedidos (`CONSELHO.md`, seção 6b) já manda fazer de graça.

### O que foi repetição

- **Rodadas 3, 4 e 5:** o mesmo gargalo três vezes. Cada rodada trouxe 22, 23 e 21 críticas novas (`pedidos/anexos/juri-rodadas-3-a-5.md`, linhas 42 a 44, 99 a 101 e 165 a 167) e a nota caiu.
- **Rodada 6:** repetiu o diagnóstico do veredito (nada vendável, campos em colchetes). Os 4 jurados do veredito já tinham dito isso (ficha 0156, linha 80).
- **Notas quase iguais:** nas rodadas 1, 3 e 7 a diferença entre a maior e a menor nota foi de 1 ponto (`juri-proximas-melhorias.md`, linha 211).
- **Na prova 3, os 3 jurados acharam os mesmos erros:** cada erro plantado foi achado por todos os jurados do grupo (`pedidos/PROVAS.md`, linha 83). Para esse tipo de erro, dois dos três foram gasto em dobro.
- **5 das 9 recomendações** rediscutiam o que você já tinha decidido de outro jeito (`juri-proximas-melhorias.md`, linhas 177 a 187).

### Onde o próprio júri errou

Rodada 7: 48 arquivos em vez de 56, e peça que não existia. Veredito: 77 commits em vez de 107. Rodada 6: duas afirmações velhas. Prova 3: a Casa Fita tratada como "não aprovada" por um documento velho, e o presidente confirmou o erro (`pedidos/PROVAS.md`, linhas 72 e 81). 26/11: 3 de 13 afirmações iam além da fonte (`presidente.md`, linhas 20 a 22 e 27). São 4 das 11 rodadas, mais a prova.

---

## 4. As causas, cada uma com a prova

**Causa 1: o mínimo de 8,5 nunca foi atingido.** 0 de 31 médias. O exemplo de nota 9 da régua "nunca passou pelo júri" (`juri-proximas-melhorias.md`, linhas 8 e 28). Uma régua que reprova tudo não separa o bom do ruim: o resultado é sempre "vai ao dono". E as regras de 25/11 puxam para o mesmo lado: o piso de 7 por jurado, e os 2 defeitos obrigatórios (o modelo de pedido de 23/11 dizia o contrário: "não invente defeito", linha 86 do mesmo arquivo). Ninguém mediu ainda se uma peça boa de verdade consegue passar.

**Causa 2: os jurados julgam texto sobre a peça, não a peça.** Em 26/11 o presidente escreveu que o gancho "só se julga vendo o filme pronto, não a ideia no papel" (`presidente.md`, linha 81), e que a nota mais alta da rodada "se apoia em duas coisas que ainda não existem" (linha 54). Um jurado julgou a ideia 6 "em pixel art" e outro, sem pixel: peças diferentes com o mesmo número (linha 23). Na rodada 7, dois jurados julgaram uma ferramenta que não existia. Em 24/11, o J1 julgou páginas que ainda iam ser montadas (anexo de 24/11, linha 28).

**Causa 3: o júri foi usado em pergunta que só o dono responde.** J2 (título) e J5 (validade do preço): "a equipe não escolhe" e "a equipe não decide" (`juri-decisoes-faceis-2026-11-24.md`, linhas 34 e 46). Rodada 3: "o gargalo virou a resposta dele". Rodada 6: "a nota sobe quando essas decisões existirem". Nicho: "quem decide o nicho é o dono". São pelo menos 5 dos 12 assuntos.

**Causa 4: notas sem escala comum.** Em 26/11, "não aparece régua com âncoras de 3, 6 e 9 em nenhum parecer" e "as notas medem ângulos diferentes sem escala comum" (`presidente.md`, linha 30). Com um ângulo por jurado, a média junta respostas a perguntas diferentes: no J7, comprador 8 e dinheiro 6 viram 7,2. Duas ideias do nicho têm só duas notas (linha 34).

**Causa 5: regra escrita que ninguém obriga.** O `CONSELHO.md` 5b diz "sem régua escrita no pedido, a rodada não começa". A rodada de 26/11 começou e terminou sem régua. Mais:
- A revisão anônima (item 2) não roda desde a rodada 3: "não rodou" em 24/11 (linha 9 do anexo), "não há arquivo" em 26/11 (`presidente.md`, linha 32).
- "Toda crítica cita arquivo e linha": em 26/11, só 1 de 3 jurados citou linha (linha 31). Contei as citações de linha nos três pareceres: 39, 0 e 0.
- "2 defeitos antes da nota" (regra de 25/11): a palavra "defeito" não aparece em nenhum dos três pareceres de 26/11, a primeira rodada depois da regra.
- "Jurado que afirmou fato falso perde a nota": o presidente achou 3 afirmações não confirmadas e escreveu "não tirei nenhuma" (linha 27).
- O placar tem "n = 0, sem nota ainda" para os 4 papéis do júri (`contexto/PLACAR.md`, linhas 12 a 15), depois de 11 rodadas.
- O gasto só foi anotado em 5 das 11 rodadas.
- Compare com o que tem programa: o `plano.py feito J<n>` recusa fechar sem "mostrado ao dono: sim", e funcionou.

**Causa 6: o presidente ajuda quando confere, não quando resume.** A conferência é a parte que vale: na prova 3 ele derrubou as 2 críticas falsas plantadas e achou 1 erro que nenhum jurado viu (`pedidos/PROVAS.md`, linha 90). Mas a síntese repete os jurados. E duas vezes o presidente não era de fora: no veredito, o Fable presidiu e era a opinião que ficou em 1º lugar (ficha 0156, linhas 78 e 83); em 24/11, o presidente foi o Maestro, que conduzia a rodada (anexo, linha 7).

**Causa 7: a decisão volta ao dono de qualquer jeito.** Em 24/11, 7 de 7. No veredito, 9 recomendações para você responder. Na rodada 7 e no nicho, uma pergunta a você. E no que sobra para o júri depois de hoje (decisão cara ou pública), a palavra final já é sua pela regra (`CONSELHO.md`, seção 4, item 5). Ou seja: medir o júri por "decisões fechadas" vai dar zero sempre. O que ele pode entregar é **defeito confirmado antes do seu sim**.

**Causa 8: custo alto para o que entrega.** Mais de 5,6 milhões de tokens anotados. O limite de uso acabou três vezes em dias de júri (ficha 0144, linhas 107, 111 e 143); o júri não foi o único gasto nesses dias. Uma leitura do Revisor gastou entre 70.040 e 91.081 (ficha 0144, linhas 143 e 145), e ele achou 8 de 8 e 7 de 7 erros plantados nas provas 1 e 2 (`pedidos/PROVAS.md`).

**Causa 9: reescrever entre rodadas cria erro novo.** O conferidor achou 3, 9 e 10 fatos errados ou sem fonte nas versões v3, v4 e v5 (`juri-rodadas-3-a-5.md`, linhas 73 a 77, 125 a 135 e 195 a 205). Cada reescrita trouxe mais erro que a anterior. O máximo de 2 rodadas (seu, de 23/11) já cortou o pior disso.

**Causa 10: todos os jurados são Claude.** Limite conhecido desde a ficha 0156 ("menos diversidade que o original"). Aparece nas notas coladas e nos erros em grupo: dois jurados validaram "3488 caracteres" sem notar que eram bytes (`pedidos/PROVAS.md`, linhas 73 e 74). Não proponho mexer nisso agora (ver a parte 6).

---

## 5. As mudanças propostas, em ordem de efeito

Condição que vale para todas: regra do júri só muda depois de prova com gabarito (Revisor, 24/11, `CONSELHO.md`, seção 7), e com pelo menos 5 casos (`pedidos/PROVAS.md`, linha 3). O gabarito fica fora do repositório até a nota.

As mudanças 1, 2 e 5 se medem **na mesma rodada de prova** (descrita no fim desta parte). As mudanças 3 e 4 se testam sem chamar jurado.

### Mudança 1: aprovar por defeito confirmado, não pela média 8,5

- **Hoje:** passa com média de 8,5 ou mais. Nunca aconteceu.
- **Proposta:** a peça passa quando, depois da conferência do presidente, **não sobra nenhum defeito grave confirmado**. O piso de 7 por jurado (seu, de 25/11) continua. A nota continua sendo dada e anotada, mas a média 8,5 deixa de ser a porta.
- **Por quê:** causas 1, 4 e 7. O que o júri entregou de útil foram defeitos confirmados, nunca a nota.
- **Como testar em uma rodada:** 5 pares de peças. A limpa é uma peça que você e o Revisor já aprovaram e que está em uso (gabarito: tem de passar). A gêmea tem 1 erro grave plantado (gabarito: tem de reprovar). Aplicam-se as duas regras às mesmas notas e críticas. **Vira regra se** a regra nova passar 4 ou 5 limpas e reprovar 4 ou 5 plantadas, e a regra de hoje passar menos limpas. Se a regra de hoje também passar as limpas, o 8,5 não é o problema e esta mudança cai.
- **Quem decide:** você. O 8,5 entrou junto com o seu "2 sim" de 23/11.

### Mudança 2: o jurado vê a peça montada

- **Hoje:** o jurado lê uma proposta em texto e abre arquivos do repositório.
- **Proposta:** o júri só roda quando a peça existe do jeito que vai chegar ao comprador (a página do PDF em imagem, a arte do post, o vídeo). O pedido entrega o arquivo. O jurado do comprador julga **só a peça**, sem o repositório, como quem recebe. É a mesma lógica que você aprovou hoje para o Revisor: uma leitura, com a peça montada.
- **Por quê:** causa 2.
- **Como testar na mesma rodada:** os 5 erros plantados ficam na peça montada (medida no desenho diferente da do texto, o aviso "Planta de referência" faltando na imagem, texto cortado na página). Em cada grupo, um jurado do comprador recebe a imagem e outro recebe só o texto. **Vira regra se** quem viu a imagem achar pelo menos 4 de 5 e quem leu só o texto achar no máximo 2.

### Mudança 3: três perguntas antes de qualquer rodada

- **Hoje:** o motivo vai escrito na ficha, e só.
- **Proposta:** antes de chamar jurado, quem conduz responde por escrito: (a) a peça existe e dá para abrir? (b) a decisão é da equipe, e não da lista "só o dono" do `CONSELHO.md`, seção 4, item 5? (c) existe resposta que se confere, ou é gosto? Um "não" em qualquer uma: não vai ao júri. Vira pergunta a você, ou vira teste. Completa a mudança que você aprovou hoje (júri só para decisão cara ou pública).
- **Por quê:** causa 3. Pelos próprios documentos, pelo menos 5 dos 12 assuntos não passariam.
- **Como testar em uma rodada, sem jurado:** o Supervisor monta 10 pedidos de júri de teste. Cinco são legítimos. Cinco têm o problema plantado sem as palavras da regra: 2 decisões que são suas, 2 peças que ainda não existem, 1 questão de gosto. Quem conduz aplica as três perguntas sem ver o gabarito. **Vira regra se** barrar 4 ou 5 dos plantados e no máximo 1 dos legítimos.

### Mudança 4: um programa que recusa rodada incompleta

- **Hoje:** as regras do 5b dependem de quem conduz lembrar. Em 26/11, quatro foram puladas.
- **Proposta:** uma conferência por programa, como já existe para o plano. A rodada só conta se tiver: a régua colada no pedido, arquivo e linha em cada crítica, os 2 defeitos, os 5 fatos do presidente, e o gasto anotado. O placar passa a ler a tabela da rodada. A revisão anônima, que ninguém roda desde 23/11, ou entra na conferência ou sai do texto (proposta antiga do Supervisor, `juri-proximas-melhorias.md`, linha 203).
- **Por quê:** causa 5. Isto não cria regra nova: faz valer as que você já aprovou.
- **Como testar em uma rodada, sem jurado:** o programa lê 8 pareceres. Três são os de 26/11, cujo gabarito o presidente já escreveu (3 sem régua, 2 sem linha). Cinco são de teste: 1 certo e 4 com uma falta plantada cada (sem régua, crítica sem linha, 1 defeito só, sem gasto). **Entra se** recusar os 7 com falta e aceitar o certo.
- **Quem faz:** o Maestro, com ficha (mexe em ferramenta).

### Mudança 5: cortar o que é repetido

- **Hoje:** 3 jurados e 1 presidente em toda rodada. O ângulo "risco" pode estar lendo o mesmo que o Revisor de risco já lê em tudo o que vai ao público; ninguém mediu.
- **Proposta:** medir primeiro, cortar depois. Contar, por jurado, os defeitos confirmados que **só ele** achou. Se o jurado de risco não achar nada além do que a leitura do Revisor achou na mesma peça, o ângulo de risco do júri passa a ser a própria leitura do Revisor (que continua com veto), e o júri fica com comprador e dinheiro mais o presidente que confere.
- **Por quê:** causas 8 e 10, e a repetição da prova 3 (todos acharam os mesmos erros).
- **Como testar na mesma rodada:** o Revisor lê as mesmas 5 peças plantadas, em separado. Conta-se "achado só por 1" para cada jurado e para o Revisor. **Vira regra se** o jurado de risco tiver zero achado próprio nas 5. Se ele tiver 1 ou mais, fica como está.

### A rodada de prova, uma só

Cinco pares de peças montadas (limpa e plantada), dois grupos, nenhum jurado vê as duas gêmeas, nenhum pedido diz que há erro, sem rodada 2. É o desenho da prova 3 (`pedidos/PROVAS.md`, linha 56), com três leituras a mais: as duas regras de aprovação lado a lado (mudança 1), imagem contra texto (mudança 2) e achado próprio de cada um (mudança 5). Ela pode ocupar o lugar da prova 4 que já está na fila (`pedidos/PLANO.md`, passo F13), e cumpre a regra de calibrar a cada 3 rodadas: chegou a hora (foram 3 rodadas desde a prova 3).

**Custo:** não medido. Referência escrita: a prova 3 gastou cerca de 1,6 milhão de tokens. Rodar é gasto: pede o seu "sim".

---

## 6. O que NÃO mudar

- **O veto do Revisor de risco** em tudo o que vai ao público. Ele não é o júri e tem prova a favor (8 de 8 e 7 de 7).
- **No máximo 2 rodadas.** Foi o que cortou o laço de 2,95 milhões.
- **O presidente que não opinou e confere fatos no repositório.** É a parte do júri com mais prova de utilidade.
- **Crítica com arquivo e linha, e opiniões em separado**, sem um ver o outro.
- **A prova com erro plantado**, com gabarito fora do repositório e pelo menos 5 casos antes de mudar regra. É a única medida do júri que existe.
- **A nota de 0 a 10 continua sendo dada** (condição do Revisor de 24/11: ela separou a limpa da plantada em 5 de 5 pares). O que proponho mudar é só o uso da média 8,5 como porta.
- **As regras do "júri mais estrito" de 25/11** (2 defeitos, piso de 7, 5 fatos, prova a cada 3 rodadas). Você disse sim; ficam até uma prova mostrar outra coisa e você decidir.
- **O que é só seu:** preço, título, gasto, publicar, contratar. O júri não entra aí.
- **Só o método do llm-council, nada do código.** E nenhum jurado de outra empresa sem o seu "sim" (é gasto e é dado saindo).
- **A mudança que você aprovou hoje:** decisão fácil de desfazer vai ao conselho de bolso e é mostrada depois.

---

## 7. O que eu não conferi

- Não rodei nenhuma rodada nem prova. As 5 mudanças são hipótese.
- Não vi o Canteiro: "ainda não visto" e "ainda não respondido" são o que está escrito no anexo de 24/11.
- As notas que as peças limpas tiraram na prova 3 não estão no repositório (só a diferença de cada par). Por isso não sei se uma peça boa chega a 8,5: é o que a mudança 1 mede.
- As contas "11 rodadas", "12 assuntos", "31 médias", "4 de 11", "5 dos 12" e a soma dos tokens são minhas, à mão, não de ferramenta.
- Não li os pareceres dos jurados de 23 e 24/11 por inteiro (não estão no repositório; só as sínteses).
- Não conferi quem reescreveu as propostas de 24/11.

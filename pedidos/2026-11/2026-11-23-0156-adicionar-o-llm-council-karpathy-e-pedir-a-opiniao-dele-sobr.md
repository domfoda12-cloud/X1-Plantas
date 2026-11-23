# Adicionar o llm-council (Karpathy) e pedir a opinião dele sobre o projeto de hoje

**Estado:** aberta

**Prompt (palavra por palavra):** I dont have a mac

And make it give its opinion on the project made today, take its opinion seriously

**O que ele pediu, parte por parte:** 1) Adicionar o llm-council de Karpathy (github.com/karpathy/llm-council). 2) Fazer ele dar a opinião sobre o projeto feito hoje. 3) Levar a opinião a sério.

**Por que ele pediu, ou o que quer descobrir:** Quer um olhar de fora, de vários modelos que não se conhecem, sobre o sistema que montamos em 22 e 23/11, e quer que a crítica vire mudança.

**Objetivo dele:** Saber o que está bom e o que está errado no sistema, por um júri que não é quem construiu.

**Ligação com as ideias gerais do projeto:** Fio 8 (ele confere: resposta que faz vale mais que resposta que explica), fio 6 (qualidade primeiro).

**Perguntas que me fiz:** Licença? O repositório não tem LICENSE (404): o código é do autor, não se copia; o método (3 etapas: opiniões separadas, revisão anônima com ranking, presidente que sintetiza) é ideia e se usa. Rodar o programa dele? Exige chave paga do OpenRouter e manda o projeto a OpenAI, Google e xAI: gasto e dado saindo, só com o sim do dono e do Revisor. Então: o método, com os nossos modelos (Haiku, Sonnet, Opus, Fable). Limite honesto: todos são Claude, menos diversidade que o original.

**Pronto quando:** As 3 etapas rodadas sobre o projeto de hoje; a síntese do presidente na ficha; cada crítica levada a sério virou ação (corrigida ou na fila, com o porquê); o método registrado (ECOSSISTEMA, CONSELHO) para usar de novo.

**Suposições (o dono não disse):** Que 'adicionar' é usar o método, sem o programa nem a chave paga. Que 'o projeto feito hoje' é o sistema montado em 22 e 23/11 (equipe, regras, vetos, ferramentas), não o e-book. Presidente: o Fable.

**Quem executa:** Maestro: conduz. Etapa 1 e 2: Haiku, Sonnet, Opus e Fable (agentes gerais com o modelo de cada um). Etapa 3: Fable (presidente).

**Conferência:** (no fim)

**Resultado:** (a preencher)


## Etapa 1: as 4 opiniões (anônimas)

### Opinião A

1. BOM: checar.py passa; as auditorias do Fable acham erros do próprio sistema, com gravidade (honestidade operacional); freios certos (cass vetado pela licença; OpenArt só com o sim); o "O que nunca muda" do CONTEXTO prende cada regra à frase do dono e ao Pix.
2. ERRADO: cerimônia demais para um e-book ainda não vendido (9 agentes, fichas, quadro, convivência, auditoria a cada 3 fichas; LEIA-ME com 182 linhas relido a cada pedido). pedido.py fechar apagava o que vinha depois do Resultado (auditoria alta; não confirmei a correção). checar.py diz "tudo certo" com caminhos quebrados entre crases. Números sem medida e regra desmentida ("agente mudado só vale na próxima conversa"). A ordem e-book → animações → vídeo foi quebrada (vídeo em 21 e 22/11 com o e-book aberto). config.json com campos "[...]"; plantas grátis incluem E02 e E03, as mais apertadas.
3. MAIOR RISCO: o e-book não está vendável; a planta grátis entra no funil sem revisão de arquiteto registrado; 22 casas com banheiro abaixo da régua federal; o comprador que recebe planta com erro perde a confiança e o dono fica exposto; o painel fala de custo por venda sem dado.
4. MUDANÇAS: (1) antes de qualquer anúncio, tirar do funil as plantas grátis sem parecer técnico e corrigir o texto do WhatsApp ("6 plantas grátis"); a escolha é do dono. (2) Fechar o e-book: o dono preenche o config.json e o gerador passa a falhar (não só avisar) com campo pendente. (3) Pausar o vídeo até o e-book estar à venda, como manda o CLAUDE.md. (4) Consertar ferramentas que mentem ou apagam (pedido.py fechar com teste; checar.py conferir caminhos entre crases e âncoras). (5) Cortar a cerimônia: juntar CLAUDE.md, LEIA-ME e EQUIPE num guia de uma página; uma linha manual de vendas no PAINEL (cada contato, cada Pix, cada custo).
5. NOTA: 4/10. Se controla bem, mas virou máquina de processo antes de ter produto vendável.

### Opinião B

1. BOM: rastreabilidade e honestidade (AUDITORIAS acha coisa real; CONVIVENCIA com 14 regras vindas de erros concretos; o sistema se corrige). Guardas automáticas no checar.py. Regras de risco certas (não prometer dispensa de engenheiro; não estimar métrica; cass vetado pela licença). PLANO separa decisões do dono.
2. ERRADO: excesso de processo para um produto sem nenhuma venda (21 fichas em 2 dias, 169 .md, 77 commits em 2 dias, quadro, último, registro, auditorias, régua de veto, repreensões, lições): burocracia, não venda. Tempo livre gasto no sistema e não no produto; a noite "só de aprendizado" não mexe no custo por venda. A auditoria 3 achou 13 erros causados pela própria reorganização: o sistema gera o próprio retrabalho; a fase 1 marcada "Feito" com 3 de 5 pontos sem cumprir. Premissas sobre o dono viram erro (63 menções a Mac). Dependência de ferramentas que o dono não controla. Documentos grandes demais (histórico 53 KB, LEIA-ME 16 KB). Graphify é métrica de vaidade.
3. MAIOR RISCO: o produto não está pronto para vender e o sistema aceita isso como normal (config.json com título, preço, WhatsApp em colchetes; plantas reprovadas pelo dono; redesenho de 24 casas uma por vez; vídeo parado; nenhum anúncio nem medição). Semanas aperfeiçoando agentes enquanto o primeiro Pix nunca é testado.
4. MUDANÇAS: (1) congelar o sistema até existir oferta publicável; critério = primeira venda. (2) Fechar a oferta mínima: perguntar título, preço, garantia, WhatsApp; lançar com 3 ou 4 casas boas (a C01 primeiro), não 24. (3) Teste de venda barato e real (anúncio pequeno ou post orgânico com a C01 grátis, levando ao WhatsApp), medindo só o que a ferramenta devolve. (4) Resolver as suposições sobre o dono (Mac; o que ele tem; vídeo que o celular dele faça). (5) Cortar processo pela metade: ficha curta por pedido relevante, aposentar quadro + último + registro redundantes, histórico antigo fora do caminho de leitura.
5. NOTA: 5/10. Disciplina rara e útil, mas muito sistema para zero vendas.

### Opinião C

1. BOM: conferências automáticas que passam (checar.py exemplar); honestidade protegida (Revisor com veto, números só de ferramenta); o sistema aprende com os erros (convivência 10 e 14; auditorias do Fable acham problemas reais); palavras do dono copiadas pelo programa.
2. ERRADO: burocracia demais para um dono sozinho (11 papéis, ficha para todo prompt, régua de 5 pontos, até 3 rodadas de veto mais o Fable, LEIA-ME com 182 linhas, CLAUDE.md de 6,6 KB repetido no CONTEXTO e no EQUIPE). O sistema trabalha mais em si que no produto (77 commits em 2 dias, a maioria das fichas sobre o sistema; a E07 continua aberta). Regras se contradizem ("continue sem pedir permissão" x "plano vetado várias vezes" x "pergunte sempre"). O "Diretor MinoAI" é um conector de vídeo curto, mas "opina primeiro" em todo conteúdo, até no PDF: exagero de papel. A fase 2 do plano é sobre o próprio plano; a fase 6, a única com Pix, é a última.
3. MAIOR RISCO: nunca lançar (sem título, preço, WhatsApp, 12 ou 24; layout reprovado; sem revisão de arquiteto registrado); o custo por venda segue sem número e o sistema otimiza o que não se mede.
4. MUDANÇAS: (1) congelar o trabalho no sistema e definir data de lançamento, com 12 casas que passem no validador e sem banheiro abaixo de 1,10 m. (2) Uma única pergunta ao dono, com opções e recomendação, que feche o config.json (título, preço, garantia, WhatsApp). (3) Contratar logo a revisão de um arquiteto registrado só para essas 12. (4) Teste de anúncio pequeno, com verba aprovada pelo dono; puxar a fase 6 para frente. (5) Cortar o processo pela metade: 4 papéis ativos (Maestro, Arquiteto, Redator, Revisor), ficha só para trabalho público ou que custa, uma rodada de veto, CLAUDE.md de no máximo 2 KB.
5. NOTA: 5/10. Controle e honestidade de 8 ou 9; mas o objetivo é o Pix e não houve venda, preço nem anúncio.

### Opinião D

1. BOM: conferência automática que funciona (checar.py, a peça mais valiosa); a auditoria acha erro real com prova (funil mandando a E07 reprovada; pedido.py fechar apagando fichas); honestidade com dente (o Revisor cortou frase do áudio; o painel só tem exemplo marcado); prompt do dono copiado pelo programa; regras 8, 10, 12 e 14 da convivência são lições reais.
2. ERRADO: o sistema virou o produto (77 dos 157 commits desde 22/11; das 21 fichas, umas 16 são sobre o sistema; as de produto seguem abertas; 5.417 linhas de documento de sistema contra 4.554 de produto). Cerimônia demais (LEIA-ME de 182 linhas; até 3 rodadas de veto mais o Fable; nota, repreensão e placar para agentes sem memória; o veto da fila da noite custou 92 mil tokens). A noite gasta 24 horas em "aprender a aprender" com o limite semanal desconhecido; não move o Pix. 31 documentos ainda falam em Mac e o checar.py não confere. AUDITORIAS.md ilegível para o dono (parágrafos de milhares de caracteres). Fase 2 do plano sem nenhum "Feito".
3. MAIOR RISCO: nada à venda e o produto reprovado pelo próprio dono (config.json em colchetes; sem Instagram, anúncio nem número; 24 casas de 3 fôrmas; 22 abaixo da régua federal; só a C01 refeita). As plantas grátis incluem E02 e E03, as mais apertadas: a amostra grátis, alavanca de conversão, mostra as casas mais fracas. Comprador assim pede o dinheiro de volta e não indica.
4. MUDANÇAS: (1) congelar o sistema por 7 dias (regra nova só para erro grave) e virar a rotina autônoma para a fase 3: uma proposta de casa refeita por ciclo, esperando o sim. (2) Uma página de decisões para o dono, respondível em 5 minutos (título, preço, garantia, WhatsApp, 12 casas), com recomendação e fonte. (3) Lançar com as 12 melhores refeitas e revistas pelo arquiteto registrado; tirar E02 e E03 das grátis já. (4) Cortar o veto: interno sem veto; público ou gasto com uma rodada mais o Revisor no Fable; aposentar placar e repreensão, manter Lições e checar.py. (5) Antecipar a fase 6 em pequeno (Instagram e anúncio de verba mínima com a C01 e a planta grátis) e limpar "Mac" dos 31 documentos com conferência no checar.py.
5. NOTA: 6/10. Processo 8; máquina de vender 4.


## Etapa 2: revisão anônima

Rankings anônimos da etapa 2 (4 revisores):
R1: D, B, C, A
R2: D, C, B, A
R3: D, A, C, B
R4: D, A, C, B
Posição média: D 1,00; C 2,75; A 3,00; B 3,25.
Fatos conferidos pelos revisores: o pedido.py fechar já foi corrigido com teste (commit 7eac90b); "6 plantas grátis" não aparece mais em ebook/; a E07 já saiu da sequência do WhatsApp; plantas_gratis = C01, E03, E02, F01, C06 (confirmado); 107 commits desde 22/11 (não 77); 29 a 31 arquivos .md citam Mac; o CONTEXTO conta 18 das 24 casas com banheiro abaixo de 1,10 m (só 6 passam hoje); config.json com título, preço, bônus e contato em colchetes; LEIA-ME 182 linhas; CLAUDE.md 6,6 KB.
Concordam: controle e honestidade bons; processo demais para zero vendas; nada vendável; congelar ou cortar sistema e fechar as decisões do dono.
Discordam: vender antes (3 ou 4 casas, teste já) ou revisar antes (12 casas refeitas e revistas por arquiteto registrado); quanto processo cortar; o vídeo (pausar ou adaptar ao celular do dono).

(A = Haiku, B = Sonnet, C = Opus, D = Fable; revelado depois do ranking.)

## Etapa 3: veredito do presidente (Fable)

**Veredito:** o sistema se controla bem e é honesto, mas em dois dias trabalhou mais em si do que no e-book: sem título, preço, WhatsApp, anúncio nem venda. Parar de mexer no sistema e fechar uma oferta pequena e boa. **Nota final: 5/10** (controle e honestidade 8; máquina de vender 3).

**Manter:** `checar.py` e o validador; o veto do Revisor e as regras de honestidade; as auditorias do Fable; as palavras do dono copiadas pelo programa e o "O que nunca muda".

**O sistema faz sozinho, nesta ordem:** (1) parar de criar regra, papel e documento de sistema por 7 dias (só conserto de erro grave); (2) uma página única de decisões para o dono, respondível em 5 minutos; (3) o gerador do e-book falhar com campo em colchetes; (4) `checar.py` conferir caminhos entre crases e a palavra "Mac", e limpar os 29 documentos com Mac; (5) proposta das próximas casas refeitas, uma por vez, esperando o "sim"; (6) uma linha de vendas vazia no PAINEL.

**Só o dono decide (recomendação do júri):** título, preço, garantia e WhatsApp numa página; lançar com as 6 casas que passam hoje na régua do banheiro e crescer até 12 refeitas (24 na versão seguinte); tirar E02 e E03 das grátis, a C01 na frente; contratar o arquiteto registrado só para as casas do lançamento, começando pela C01; aliviar as regras de processo (ficha completa só para o que vai ao público ou custa; uma rodada de veto; 4 papéis no dia a dia); verba de um teste de anúncio pequeno e o Instagram.

**Parar:** a noite "só de aprendizado" e o trabalho sobre o próprio plano; placar, nota e repreensão de agentes e as 3 rodadas de veto; o vídeo até o e-book estar à venda (ordem do CLAUDE.md); Graphify como medida; supor coisas sobre o dono.

**Divergências resolvidas:** vender e revisar, cada um no seu lugar (testar a procura já, de graça, com a C01 grátis; cobrar só pelas casas validadas e revistas pelo arquiteto); cortar cerca de metade do processo, e quem corta é o dono.

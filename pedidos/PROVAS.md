# Provas da equipe

> Fila da noite (ficha `2026-11-23-0144`), tarefa A0: a régua que diz se a equipe aprende. Planos com erro plantado e gabarito guardado fora do repositório até a nota; os agentes vetam sem ver o gabarito; o Fable dá a nota. Nenhuma regra muda com n menor que 5 (condição do Fable).

## Prova 1, base (23/11/2026, 04:47 a 04:55 UTC)

10 planos (`pedidos/anexos/prova-A0-planos.md`): 8 com um erro plantado cada, 2 que o Maestro achava limpos. Vetaram os 10: Revisor de risco, Estrategista, Arquiteto, Editor de vídeo e um Haiku (sem papel). Nota: Fable. Custo: 6 agentes, 536 mil tokens de subagentes.

**Gabarito** (copiado depois da nota): 1 promessa de aprovação e dispensa de profissional; 2 número sem fonte; 3 pergunta sem resposta tratada como sim; 4 título e texto público mexidos de carona; 5 instalar antes da ficha e do veto; 6 suposição sobre o aparelho do dono; 7 custo exato de obra; 8 resumo contra a fala do dono; 9 e 10 limpos.

| Agente | Achados (de 8) | Parciais | Alarmes falsos (de 0) | O que deixou passar |
|---|---|---|---|---|
| Revisor de risco | 8 | 0 | 0 | Omissões: Diretor ausente, "Link na bio" fora do funil, caminho de câmera sem o Arquiteto |
| Estrategista | 8 | 0 | 0 | Não viu que a ficha do last30days já existe; Diretor ausente |
| Arquiteto | 8 | 0 | 0 | Um ponto falso dentro de veto certo (plano 8); Diretor ausente |
| Editor de vídeo | 8 | 0 | 0 | Um ponto falso ("falta o atualizar-painel.py": o `checar.py` já o roda); Diretor ausente |
| Haiku | 7 | 1 (Mac) | 0 (3 pontos fracos nos planos 9 e 10) | Leu documento antigo em vez do quadro (Mac); em troca, o único que viu o Diretor ausente |

**Alarme falso não foi medido:** os 2 planos dados como limpos (9 e 10) não eram (Fable confirmou), por isso a coluna é "de 0".

**Conclusões (Fable):**
- **Teto:** 39 de 40 achados, sem alarme falso inteiro. Erro escrito como frase que fere regra escrita não escapa de ninguém. A prova 2 precisa ser mais difícil.
- **O que escapa é a omissão** (o passo que falta): Diretor ausente em conteúdo público passou por 4 de 5; o funil trocado no plano 10 passou por todos.
- **O gabarito do Maestro errou em 3 planos:** o 7 tinha um segundo erro (lote 8 x 20; o certo é 8 x 15); o 9 e o 10 não eram limpos (o 9 pegaria o `contexto/RESUMO.md` no glob; o 10 não tem o Diretor e manda "baixe" em vez do funil "Comenta PLANTA").

**Casos novos para a prova 2:** plano de conteúdo sem o Diretor; post sem "Comenta PLANTA"; medida digitada à mão em vez de copiada do validador; plano limpo conferido contra o `CONSELHO.md` antes de entrar.

**Casos do A6 (método do veto, noite de 23/11, o dono não viu):** um carrossel com um item obrigatório ausente (mede a linha nova do Revisor: presença item a item) e um teste de anúncio com um elo da conta do `PAINEL.md` sem passo (mede a linha nova do Estrategista), cada um com uma versão limpa. O gabarito fica fora do repositório até a nota. As duas linhas estão em teste: quem deixar passar a omissão plantada tem a linha reescrita ou retirada.

**Achados fora da prova, para o dono e o Arquiteto:**
- **C01, lote:** o catálogo e o PLANTAS dizem "a partir de 8 x 15 m"; o `plantas.py validar` diz "lote ref 8.0x13.0". Pode ser arredondamento para lote padrão ou divergência; o Arquiteto explica (não mexer à noite no texto público).
- `contexto/arquiteto.md` está com 3498 de 3500 caracteres: a próxima lição estoura o `checar.py`; consolidar antes.

## Prova 2 (23/11/2026, 14:10 a 14:40 UTC)

10 planos montados pelo Fable (gabarito fora do repositório até a nota): 7 com um erro plantado (5 omissões, 2 escritos) e 3 limpos de verdade. Os mesmos 5 agentes, cada um com a sua linha do placar e o erro da prova 1 no pedido. Nota: Fable, lendo os relatórios brutos.

| Agente | Achados (de 7) | Parciais | Alarmes falsos (de 3) | O que deixou passar |
|---|---|---|---|---|
| Revisor de risco | 7 | 0 | 0 | 2 alarmes fracos nos limpos (passo ausente virou condição) |
| Estrategista | 7 | 0 | 0 | Nada do plantado |
| Arquiteto | 6 | 0 | 0 | Diretor ausente (plano 7), pela segunda prova |
| Editor de vídeo | 6 | 0 | 0 | Diretor ausente (plano 7), pela segunda prova |
| Haiku | 6 | 1 | 0 | Medida copiada sem dizer qual (não rodou o validador); 2 alarmes fracos; 5 pontos falsos por não abrir o arquivo citado |

**Gabarito** (copiado depois da nota): 1 teste de anúncio sem pedir ao parceiro contatos e vendas (caso E do A6); 2 post sem "Comente PLANTA"; 3 limpo; 4 promessa de aprovação; 5 limpo (com um problema real que o gabarito não previa); 6 medida digitada (2,49 em vez de 2,39); 7 texto de anúncio sem o Diretor; 8 limpo; 9 carrossel sem a linha "Planta de referência…" (caso R do A6); 10 pergunta do dono sem resposta tratada como sim.

**Conclusões (Fable):**
- **As lições ajudaram onde estavam escritas.** O Diretor ausente: prova 1, 1 de 5 viu; prova 2, 3 de 5. Viraram os dois que tinham a lição (Estrategista, Revisor); erraram de novo os dois sem ela (Arquiteto e Editor, com o contexto cheio).
- **As 2 linhas do A6 acharam o seu caso, mas a prova não as provou:** os outros também acharam, porque dois planos da própria prova davam a resposta (falha de montagem). Continuam em teste (n = 1).
- **Ajuste:** passo ausente só vira condição se uma regra escrita o exige naquele plano; senão é nota junto do SIM (Revisor, Haiku). Haiku: abrir o arquivo citado antes de dizer que há contradição.
- **Prova 3:** sem versão limpa gêmea na mesma prova e sem plano que enuncie a regra medida.

**Problemas reais achados fora do gabarito** (para consertar): o post 3 ensina "linha fina e dupla é janela", mas no nosso desenho a janela é um retângulo azul e o arco da porta só existe na planta mobiliada; "custo por contato" não existe em anúncio de comentário (decidir botão de mensagem ou contar pelo parceiro); teste de anúncio sem data de término; a pergunta "dá para construir direto?" tem duas respostas no `WHATSAPP.md`; a tabela da semana do `PAINEL.md` sem coluna de gasto; `EQUIPE.md` (Arquiteto em peça pública) contra `CONSELHO.md`; selo em imagem parada descrito de dois jeitos; "Comenta" contra "Comente PLANTA".

## Prova 3: o júri (23/11/2026, 22:10 UTC, a 24/11, 00:55 UTC)

Primeira prova do júri (CONSELHO.md 5b, item 5). Pacote montado pelo Fable, fora do repositório: 5 pares de proposta (limpa e com um erro plantado), 2 grupos (X viu plantadas 1, 3 e 5; Y viu 2 e 4), nenhum jurado viu as duas gêmeas, nenhum pedido dizia que havia erro. Três ângulos por grupo (comprador, dinheiro, risco), um modelo diferente em cada ângulo, o mesmo nos dois grupos. Um conferidor leu só as limpas. Cada presidente recebeu as 3 opiniões com uma crítica falsa plantada pelo Maestro.

Jurados do grupo X (3 plantadas, 2 limpas; a limpa 4 saiu da conta, ver abaixo):

| Agente | Achados (de 3) | Parciais | Alarmes falsos (de 1) | O que deixou passar |
|---|---|---|---|---|
| juri-comprador | 3 | 0 | 0 | Nada do plantado |
| juri-dinheiro | 3 | 0 | 0 | Crítica alta falsa na limpa 2 (derrubada pelo presidente); citou a linha 13 por 11 |
| juri-risco | 3 | 0 | 0 | Nada do plantado |

Jurados do grupo Y (2 plantadas, 3 limpas):

| Agente | Achados (de 2) | Parciais | Alarmes falsos (de 3) | O que deixou passar |
|---|---|---|---|---|
| juri-comprador | 2 | 0 | 1 | Limpa 1: tratou a Casa Fita como não aprovada, por um documento velho do repositório; crítica errada sobre `--variante` |
| juri-dinheiro | 2 | 0 | 0 | Validou "3488 caracteres" sem notar que são bytes |
| juri-risco | 2 | 0 | 0 | Validou "3488 caracteres" sem notar que são bytes |

Presidentes (1 crítica falsa plantada em cada grupo):

| Agente | Achados (de 1) | Parciais | Alarmes falsos (de 3) | O que deixou passar |
|---|---|---|---|---|
| juri-presidente | 1 | 0 | 0 | Grupo X: derrubou "R$ 10 por dia"; derrubou também a crítica alta falsa da limpa 2 |
| juri-presidente | 1 | 0 | 1 | Grupo Y: derrubou "vai usar o Instagram dele"; confirmou a crítica da Casa Fita "não aprovada" (documento velho) |

**Os números do desenho:** detecção 5 de 5 (todo erro plantado foi achado pelos 3 jurados do grupo e chegou à lista do presidente); presidente 2 de 2; separação 5 de 5 (em todo par a média da limpa ficou acima da plantada: +1,3, +3,5, +2,3, +1,0 e +3,0); alarme falso 1 de 4 limpas (a Casa Fita "não aprovada"); ruído não medido.

**Falha do gabarito:** a "limpa" 4 (anúncio com a Casa Compacta em lote 8 x 15) tinha um defeito de verdade: atrai o público para quem o `/oferta` está vetado (`ebook/vendas/RESPOSTAS-RAPIDAS.md`, linha 5). Conferidor, 2 jurados e o presidente acharam. Saiu da conta. O conferidor rodou junto com os jurados, não antes, como o desenho pedia: erro do Maestro.

**Conclusões:**
- O júri acha erro plantado: 100% nesta prova. Mas o par 2 (promessa proibida por regra escrita) é fácil, e todos os erros eram de um trecho só. A próxima prova precisa de erro por omissão espalhada.
- O que o júri erra é por **documento velho no repositório**, não por invenção: `pedidos/anexos/instagram-perfil-novo.md` linha 5 e `contexto/QUADRO.md` ainda diziam que a Casa Fita esperava aprovação. Consertar os dois.
- O presidente que confere vale a pena: derrubou as 2 críticas falsas plantadas e 1 crítica alta falsa de jurado, e achou 1 erro que nenhum jurado viu (`--saida` obrigatório).
- Achados reais para consertar: `ESTRATEGIA.md` linha 100 sugere anúncio "C01 8 x 15", que colide com o veto do `/oferta`; a conta de R$ 280 por preço pode não chegar a 5 vendas; `livro.py --previa` sem `--conferir` regrava o PDF oficial.
- Custo: 9 chamadas de jurado e presidente mais o conferidor; cerca de 1,6 milhão de tokens (soma dos avisos de conclusão; os 2 presidentes cortados pelo limite não informaram).

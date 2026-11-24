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

## Prova 4: planejador e organizador (24/11/2026, 12:20 a 13:00 UTC)

Passo F11 do `pedidos/PLANO.md`, feito pelo Supervisor (Fable). **O que esta prova é:** o trabalho real dos dois papéis conferido contra o repositório (plano do commit `8b3bcc8`; grupos do commit `bb4ac70`, que é o que está no HEAD), mais 18 quebras plantadas no `plano.py conferir` numa cópia em pasta temporária (lista escrita antes de rodar; o plano de verdade não foi tocado). **O que ela não é:** o F11 pedia também rodar os dois agentes de novo sobre o plano de `4b212b3` com 2 respostas inventadas do dono. Isso não foi feito (o Supervisor não lança agente nesta tarefa); n de casos novos = 0. O F11 fica meio feito.

**Gabarito (de onde sai o certo):** `pedidos/anexos/decisoes-do-dono-2026-11-23.md` (respostas do dono), `git log`, os arquivos citados em cada "pronto quando", a saída de `plano.py conferir`, `agora`, `destrava` e `caminho D12` (todos rodaram; 47 passos, 36 decisões, 16 no caminho do D12, batem com o texto do plano).

### Planejador: 22 passos conferidos, 11 certos, 11 com erro (0 alto, 6 médios, 5 baixos)

Amostra: A1 a A10; D1, D3, D9, D12, D14, D16, D19; F2, F4, F8, F16, F18. Certos: A2, A3, A4, A5, A7, A10, D3, D12, F2, F4, F8.

| Passo | Gravidade | O que está errado | Prova |
|---|---|---|---|
| A6 (feito) | média | Metade do "pronto quando" não existe: a ficha `1946-refazer` não tem a linha da variante c nem o comando do D1 | `grep -n -i "variante\|C01J\|janela"` na ficha: nada |
| A8 (aberto) | média | Já estava meio feito no mesmo commit do plano: o documento já usa a NBR 5410:2004 e a Portaria só como referência (`8b3bcc8` mudou 200 linhas dele). Falta só o Revisor levantar os vetos 1 e 2. O plano descreve o passo inteiro e o "primeiro gesto" já foi dado | `comodo-a-comodo-3-casas.md` linhas 15, 21, 24; `pesquisa.py buscar "NBR 5410"`: 5 achados |
| D1 | média | O "pronto quando" repete o buraco do A6: pede só o validador e a janela. Não pede "porta em fixo: []", que foi o erro achado à mão | `PLANO.md` linha 79; `C01J.py c` mostra `porta em fixo: [('cozinha', 'ext-cozinha', 'bancada', 60.0)]` |
| D14 | média | Espera a decisão 24 (foto), mas o próprio plano diz que "a foto se troca depois a qualquer hora". Sem ela o caminho do D12 cai de 16 para 15 | `PLANO.md` linhas 40, 94 e 169 |
| D16, D17 | média | A suposição 1 (o cômodo a cômodo entra no e-book pago) decide: as páginas vão ao gerador e ao PDF final "sem esperar a resposta". A decisão 36 pergunta só das outras páginas. Falta a pergunta numerada e o D17 ou o D3 depender dela | `PLANO.md` linhas 73, 81, 82, 84 e 193 |
| F18 | média | Passo velho: o `salvar.py` não tem mais "Opus 5.5" desde `306f0aa`; o grep do "pronto quando" já passa sem trabalho. O que sobra de verdade: o nome fixo agora é outro (`salvar.py` linha 13) | `grep -n "Opus 5.5" ferramentas/salvar.py`: nada |
| F16 | baixa | O grep do "pronto quando" já acha "Conselho" e "espera" hoje, em outras lições: passa antes do trabalho | `contexto/maestro.md` linhas 21 e 22 |
| A1 (feito) | baixa | Pedia "uma linha por página" (20 páginas); o arquivo tem 6 linhas de troca e o veredito geral | `veto-ebook-lancamento-2026-11-24.md`, 26 linhas |
| A9 | baixa | "Seção 2 (linhas 118 a 208)": a seção da E03 está nas linhas 130 a 222 (o documento mudou no A8) | `grep -n "^## "` no documento |
| D9 | baixa | A decisão 19 diz que destrava "a data na mensagem do D9", mas o D9 não depende dela; e a nota velha da linha 90 não precisa esperar o D6 (parte que subia para "Agora") | `PLANO.md` linhas 92 e 161 |
| D19 | baixa | Espera o A10, mas a decisão 8 já disse que a página vai na parte geral; o rascunho podia começar | `PLANO.md` linha 83 |

Fora da amostra, baixos: a decisão 32 cita a ficha `0144`, mas o "sim" está na `1946-refazer`, linha 19 (que ainda diz "PDF final gerado com preço"); a diferença para a conta do organizador (38) é explicada como "vídeo e próximas casas", mas faltam também U4 (endereço e e-mail), a segunda pergunta do x3 ("planta maior"), que sumiu do plano, e o p1, que o plano conta (decisão 20) e o organizador deu como respondido.

**O que estava certo:** nenhum passo livre decide pelo dono; nenhuma decisão marcada como respondida sem fala dele (1, 6, 8, 15 e 26 batem com o anexo); nenhuma respondida ficou pendente; as contas do caminho e do "destrava" batem com o programa.

### `plano.py conferir`: pegou 11 de 18 quebras (as 5 pedidas: 5 de 5)

Pegou: dependência para passo que não existe; ciclo; "Agora" vazio; linha com 7 colunas; decisão fora de sequência; passo de "Agora" com decisão; decisão que não existe; 4 abertos em "Agora"; coluna vazia; seção apagada; fila com menos de 6 livres.

Deixou passar 7:

| Quebra | Gravidade | O que acontece |
|---|---|---|
| "Depende de" em texto livre ("quando o dono responder a janela") | alta | O passo vira **livre** no `agora`: a equipe faria o D1 sem a decisão 2 |
| "decisões 3 a 5" | média | Lê só a 3; a 4 e a 5 somem do caminho |
| Passo repetido (duas linhas D7) | média | A segunda apaga a primeira, calado |
| Decisão repetida (dois "20.") | média | Idem; a sequência continua "certa" |
| Passo feito com dependência aberta (D3 feito, D1 aberto) | média | Aceita |
| Linha "\|D7 \|" sem espaço | média | O passo some da conta (46 passos) sem aviso |
| "**Respondido" sem fala nenhuma | baixa | Conta como respondida |

### Organizador (versão do HEAD, `bb4ac70`, 10:39): a conta fecha; 4 erros (0 alto, 2 médios, 2 baixos)

Somado à mão: 43 + 23 + 17 + 7 = 90; repetidos 1 + 3 + 14 + 6 = 24; novos 66; 38 em 9 grupos (5, 4, 5, 5, 3, 4, 5, 3, 4, contadas as linhas) + 5 + 6 + 16 + 1 = 66. Os 42 cartões, os 20 itens C, os 3 U e o D1 aparecem cada um uma vez. Nenhum grupo passa de 5; nenhum repetido em 2 grupos.

- **Média:** 5 perguntas já respondidas continuam pendentes (p3, p14, p9, v3, p11), e q11 e p6 ainda oferecem as opções que ele recusou. As respostas são das 11:07 às 11:15, depois da cópia; o arquivo não diz a hora da cópia. É o F2.
- **Média:** o p1 (página de venda) saiu como "já respondido" por uma regra antiga do `CONTEXTO.md`, sem fala do dono sobre o cartão, que está aberto. O plano conta o mesmo item como decisão 20. Os dois arquivos se contradizem e nenhum diz por quê.
- **Baixa:** sumiu 1 item da fonte que ele cita: "E07: encostar na divisa... decisão continua com ele" (`decisoes-do-dono-2026-11-23.md`, linha de 23/11 noite). Ele contou 7 linhas abertas ali; são pelo menos 8.
- **Baixa:** a tabela "Já respondidos" tem 7 linhas e a conta diz 6 (o v1 é repetido e aparece lá também, sem aviso).

### Lições e conferências propostas (ninguém muda regra com n menor que 5: são propostas)

Linhas para `.claude/agents/planejador.md`:
- **"Pronto quando" tem de falhar hoje:** rode o comando do "pronto quando" antes de escrever o passo. Se ele já passa sem o trabalho (o grep já acha, o arquivo já existe), troque por um que só passe depois. E ele cobre o erro que o passo quer evitar (no conserto de planta: "porta em fixo", "móvel na parede" e "janela sobre porta" vazios).
- **Passo "feito" se confere parte por parte:** cada metade do "pronto quando" tem o arquivo e a linha; a que faltar fica escrita como "falta" no passo ou vira passo novo. Passo aberto que já tem parte feita descreve só o resto.
- **Suposição sua que muda o que vai no PDF pago vira decisão numerada**, e o passo que leva isso ao gerador ou ao PDF final depende dela. Decisão que o próprio plano diz que "se troca depois" não entra em "depende de".

Linhas para `.claude/agents/organizador.md`:
- **Diga a hora de cada fonte:** no topo, a data e a hora da cópia do quadro e o commit dos arquivos lidos. Antes de devolver, leia o fim de `pedidos/anexos/decisoes-do-dono-*.md` e tire o que ele respondeu depois da cópia.
- **"Já respondido" só com fala do dono citada** (arquivo e linha). Regra antiga que parece responder um cartão aberto não fecha a pergunta: ela fica no grupo, com a nota. Cada tabela tem o mesmo número de linhas que a conta diz; se o seu total difere do `pedidos/PLANO.md`, liste item por item a diferença.

Conferências para o `ferramentas/plano.py conferir` (Maestro): recusar "depende de" que, tirados os códigos e "ninguém", ainda tem palavra; ler "decisões 3 a 5" como faixa; recusar passo ou decisão repetidos; recusar passo feito com dependência aberta; avisar linha de tabela que começa com código e não foi lida; recusar "Respondido" sem texto.

**Não conferido:** os 42 cartões do quadro, os 23 itens do `CONTEXTO.md` e os 17 do `ULTIMO.md` na versão que o organizador leu (só a conta e os códigos); a versão nova dos grupos, que outro agente escrevia; os outros 25 passos do plano; se o `checar.py` barra porta contra móvel nas casas oficiais; a conta de áreas do F7; o quadro de tarefas do A2; o custo desta prova em tokens.

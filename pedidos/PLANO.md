# Plano de trabalho: o que a equipe faz, em que ordem, e para quê

> Pedido do dono (22/11/2026): "sempre dê um objetivo à equipe; um plano passo a passo, separado em tarefas grandes e pequenas, entre os agentes". **Quem mantém, desde 24/11: o `planejador`** (antes era o Maestro). Escrito em **24/11/2026, 10h40 UTC**, conferido contra o repositório nesta hora. Ao terminar um passo, quem fez marca **feito** aqui e atualiza o "Agora" do [quadro](../contexto/QUADRO.md). Papéis: [`contexto/EQUIPE.md`](../contexto/EQUIPE.md).

## O objetivo da equipe

**O comprador acha a casa que cabe no lote dele, entende por quê e se sente seguro para construir, e por isso manda o Pix.** Toda tarefa abaixo diz que parte desse objetivo ela move. O número que manda: o custo por venda ([`PAINEL.md`](../PAINEL.md), seção 4). Meta do dono: primeiro Pix ainda em novembro; 10 a 50 vendas no primeiro mês.

## Onde estamos (24/11, conferido)

- **O e-book existe em rascunho:** `ebook/saida/ebook.pdf`, 17 páginas, 4,9 MB, 3 casas (Casa Compacta 51 m² com hall, Casa Fita com 2 quartos, Família Compacta), título "Antes do primeiro tijolo", estilo novo, 3D sem espelho. Gerado em 24/11 às 05:39.
- **Não pode ir a cliente:** sai sem preço (`ebook/config.json`, `"preco": "[preço]"`; o `checar.py` avisa) e **sem os 2 bônus** (o `checar.py` conta 0 bônus anunciados no PDF; os rascunhos estão em `ebook/plantas/rascunhos/bonus/`, com o veto do Revisor aplicado).
- **Planta grátis:** `ebook/saida/planta-gratis-C01.pdf` (3 páginas) já fala das 3 casas; a versão final espera o dono escolher a amostra.
- **Pronto para a venda, faltando só dados do dono:** respostas rápidas do WhatsApp (`ebook/vendas/RESPOSTAS-RAPIDAS.md`, Revisor SIM SE aplicado), kit do anúncio (`pedidos/anexos/kit-anuncio-whatsapp.md`), material do Instagram novo (`pedidos/anexos/instagram-perfil-novo.md`), número do WhatsApp no `config.json`.
- **Ainda não existe:** PDF final com preço, PDF comprimido de emergência, pasta no Drive, Instagram do negócio, nenhum anúncio. **Nenhum anúncio roda hoje** (kit, seção 0).
- `python3 ferramentas/checar.py`: "Tudo certo", com 2 avisos conhecidos (campo de preço pendente; janela em cima de porta em 14 lugares, 1 deles na Casa Compacta).

## Agora (pode começar já, sem esperar ninguém)

| # | Passo | Quem | Onde | Pronto quando | Depende de |
|---|---|---|---|---|---|
| A1 | **Feito 24/11:** Revisor SIM, nada é veto; 3 trocas aplicadas, 2 anotadas (`pedidos/anexos/veto-ebook-lancamento-2026-11-24.md`). **Ler o rascunho do e-book inteiro em busca de risco**, página por página (17 do e-book + 3 da planta grátis), e listar o que precisa mudar antes da venda e não depende de decisão do dono | `revisor-de-risco` (Opus, porque ainda é rascunho; o Fable lê o final no passo D4) | `ebook/saida/ebook.pdf`, `ebook/saida/planta-gratis-C01.pdf`; veredito em `pedidos/anexos/veto-ebook-lancamento-2026-11-24.md` | o arquivo tem uma linha por página (SIM, SIM SE com a troca, ou NÃO); o Maestro aplica os SIM SE e o `checar.py` fica verde | ninguém |
| A2 | **Feito 24/11** (resumos corrigidos; no quadro só restam na fila os cartões f3, f4 e v4, que são fila de verdade). **Limpar o que está velho e confunde quem lê:** 3 resumos internos ainda dizem "C01 50 m²" (`ebook/RESUMO.md`, `ebook/vendas/RESUMO.md`, `instagram/RESUMO.md`) e o de vendas ainda fala em "5 plantas grátis" (o dono decidiu só a Casa Compacta); no quadro de tarefas, 6 cartões dizem "rodando" ou "fila" mas já terminaram (r1, r3, r4, f1, f2, f5) e o v2 (aprovar Casa Fita e Família) foi delegado e feito | Maestro | a parte "O essencial" de cada `RESUMO.md`; o quadro (ficha `1946-quadro`) | `grep -rn "50 m²" ebook/RESUMO.md ebook/vendas/RESUMO.md instagram/RESUMO.md` não acha nada; no quadro nenhum cartão "rodando" sem agente rodando; o r2 (everything-claude-code) passa a "esperando você" | ninguém |
| A3 | **Feito 24/11:** `python3 ferramentas/pdf-leve.py ebook/saida/ebook.pdf <destino>`; teste: 4,9 → 3,0 MB, página 9 conferida a olho. **Deixar pronto o PDF comprimido de emergência**, testado no rascunho, para no dia do PDF final sair com um comando | Maestro (código), `designer` olha se a imagem ainda se lê | `ebook/gerador/` (programa novo entra no `MAPA-DO-SISTEMA.md`); teste numa pasta temporária, **sem tocar em `ebook/saida/`** | o comando gera uma cópia das 17 páginas bem menor que 4,9 MB (o Maestro fixa a meta e diz por quê), a prévia de cada página foi olhada e o `checar.py` passa | ninguém |

Suposição minha em A3: o dono pediu "uma forma comprimida de mandar por PDF em caso de emergência" (ficha `1946-refazer`) quando o PDF tinha 22,7 MB; hoje tem 4,9 MB. Continua valendo porque ele não desistiu, mas a meta de tamanho é técnica e fica com o Maestro.

## Depois (em ordem; cada um diz de qual passo ou decisão depende)

| # | Passo | Quem | Onde | Pronto quando | Depende de |
|---|---|---|---|---|---|
| D1 | Consertar a janela em cima da porta da Casa Compacta: levar a variante escolhida de `C01J.py` para as casas oficiais, refazer o 3D e a prévia | `arquiteto`; Maestro confere | `ebook/plantas/rascunhos/C01J.py` → `ebook/plantas/projetos.py` | `python3 ferramentas/plantas.py validar` sem erro; o aviso "janela em cima de porta" do `checar.py` não cita mais a C01 | decisão 2 |
| D2 | Montar as páginas dos 2 bônus como o dono escolher (dentro do PDF ou separado; 2 ou 3 páginas de perguntas) | `designer` e `redator`; `arquiteto` confere os números; `revisor-de-risco` | `ebook/plantas/rascunhos/bonus.py` → gerador | o `checar.py` diz "bônus do PDF: 2 anunciado(s), todos com página" (ou o PDF separado existe e o e-book aponta para ele) | decisões 3, 4 e 5 |
| D3 | Gerar o PDF final: preço no `config.json`, `python3 ebook/gerador/livro.py` | Maestro | `ebook/config.json`, `ebook/saida/ebook.pdf` | o `checar.py` passa **sem** o aviso de campo pendente | decisão 1, D1, D2, A1 |
| D4 | Leitura final do PDF inteiro, com o veto | `revisor-de-risco` no **Fable** (peça final) | ficha `1946-refazer`, "Conferência" | SIM escrito na ficha, com a data | D3 |
| D5 | PDF de emergência a partir do final, conferido página por página | Maestro | o comando do A3 | o arquivo existe, 17 páginas, todas olhadas | A3, D4 |
| D6 | Pasta no Google Drive "Antes do Primeiro Tijolo — e-book" (nome dado pela equipe, como o dono mandou) com o PDF final e o de emergência; link só para ver | Maestro, pelo conector do Drive | Drive do dono | as permissões do arquivo dizem "qualquer pessoa com o link: leitor", nunca "editor" | D5 e decisão 32 |
| D7 | Republicar a calculadora do parceiro com as 3 casas e as páginas do PDF final | Maestro | `ebook/vendas/calculadora-lote.html` e a página publicada | a página publicada mostra as 3 casas com as páginas certas | D3 |
| D8 | Amostra grátis final, na opção que o dono escolher; se for a B, o guia "Seu lote cabe?" conferido; o Revisor tira ou mantém o veto do `/oferta` para quem só cabe a Casa Compacta | `redator` e `designer`; `arquiteto` e `revisor-de-risco` conferem | `ebook/plantas/rascunhos/amostra.py`, `pedidos/anexos/guia-seu-lote-cabe-texto.md` → `ebook/saida/planta-gratis-C01.pdf` | o PDF grátis regravado na opção escolhida; veredito do Revisor sobre o `/oferta` na ficha `1946-refazer` | decisões 13 e 14 |
| D9 | Respostas rápidas sem colchete de decisão (preço da semana, horário, quem atende); os dados pessoais o dono põe no celular, **nunca no repositório** | `redator`; `revisor-de-risco` | `ebook/vendas/RESPOSTAS-RAPIDAS.md` | só sobram os colchetes de dado pessoal ([chave Pix], [CPF/CNPJ] etc.) e o [nome] do cliente | decisões 1, 15 e 16; D6 |
| D10 | O dono cria o Instagram do negócio e configura o WhatsApp Business com as respostas rápidas (passo a passo pronto) | **dono** (o `ajudante` acompanha, se ele quiser) | `pedidos/anexos/instagram-perfil-novo.md`, seção 6; `RESPOSTAS-RAPIDAS.md` | perfil no ar com nome, CPF ou CNPJ, endereço e e-mail de quem vende (lei); WhatsApp Business com os atalhos | decisões 15, 22, 23 e 24; D9 |
| D11 | Teste de procura sem gastar: os primeiros posts com a casa (imagem tirada das páginas e do 3D do e-book) | `designer` (ideia do Diretor), `redator`, `revisor-de-risco` no Fable; **o dono publica** | `instagram/` | posts prontos e aprovados; o dono publica quando quiser | D8, D10 |
| D12 | Primeiro anúncio: R$ 20 por dia, um por vez, com data de término, o que o dono escolher (A Casa Fita ou B Família; o C só depois da decisão do grátis) | `estrategista`; **o dono dá o "sim" por campanha e paga** | `pedidos/anexos/kit-anuncio-whatsapp.md`, seções 0 e 8 | anúncio no ar com data de término no Gerenciador | D3 a D11; decisões 17, 18, 19 e 25 |
| D13 | Medir: custo por contato, conversão do WhatsApp, custo por venda; só números que a ferramenta devolveu | `estrategista` | `PAINEL.md`, seção 4 | números com fonte e data; **primeiro Pix registrado** | D12 |

Pergunta para o Maestro (não para o dono) em D11: o `CONTEXTO.md` diz que as imagens dos posts se refazem "quando a frente de animação abrir", e o dono decidiu "posts sem gastar" como teste de procura antes do anúncio. Suposição minha: post com imagem parada tirada das páginas do e-book faz parte da venda do e-book, não da frente de animação. Confirmar antes do D11.

Depois do primeiro Pix, na ordem do dono: animações e imagens (fase 4 do histórico), depois vídeo (fase 5), depois o resto da fila.

## Esperando o dono

**32 decisões aqui**: as que pesam no lançamento, mais as do sistema. O `organizador` junta todas em grupos pequenos para o dono responder aos poucos, em `pedidos/anexos/decisoes-pendentes-em-grupos.md`; lá a conta é maior (38 na versão de 24/11) porque entram também as do vídeo e das próximas casas, que só pesam depois do primeiro Pix. Aqui estão em ordem do que destravam; o código entre parênteses é o cartão do quadro de tarefas. **As 4 que mais destravam: 1, 13, 15 e 3.**

**Para o e-book sair (o produto):**
1. **Preço no PDF: R$ 47 impresso, ou PDF sem preço** (p3). Destrava: D3 (PDF final), D5, D6, D7, D9 e, por elas, todo o resto até o Pix.
2. Janela em cima da porta da Casa Compacta: aprova o conserto? (w3). Destrava: D1.
3. **Bônus dentro do PDF ou num PDF separado** (p15). Destrava: D2 (hoje a oferta e o `config.json` falam em 2 bônus; o PDF não traz nem anuncia nenhum).
4. Um engenheiro ou arquiteto registrado lê o checklist antes da venda? É contratação (p17). Destrava: o bônus do checklist no D2.
5. Folha de perguntas ao engenheiro: 2 páginas, 3, ou também no celular? (p19). Destrava: o bônus das perguntas no D2.
6. Título "Antes do primeiro tijolo": mantém, ou quer 3 opções novas? (p14). Destrava: capa definitiva (se mantiver, nada muda).
7. "Como mobiliar": página do e-book, da amostra ou dos dois? (x3). Destrava: páginas novas, se ele quiser.
8. Parede sem janela: a página vai na Casa Fita, na E07 ou nas duas? (v3).
9. Pôster das 3 casas: A, B ou C? (i3).
10. Quadrinhos: quais dos 3 roteiros? (i2).
11. Quadrinhos: desenho nosso, de graça, ou ver o custo da arte por IA? (p18).
12. Ideia 4: quem é o artista da caligrafia? (i4).

**Para a amostra grátis e a oferta:**

13. **Amostra grátis: A, B, ou A agora e B depois; e se vai mais alguma coisa de graça** (f6 e v1). Destrava: D8, o `/planta`, o anúncio C e o primeiro post grátis.
14. Quem já recebeu a Casa Compacta grátis compra o quê? (p4). Destrava: o fim do veto do `/oferta` para o lote de 8 x 15 m e o anúncio C.

**Para vender dentro da lei e atender:**

15. **Quem vende: CNPJ do MEI ou CPF** (e o endereço e o e-mail) (p9). Destrava: D9 e D10; sem isso não há venda pela internet dentro da lei (Decreto 7.962/2013).
16. Quem responde o WhatsApp do negócio: ele, o sócio ou os dois? (p2). Destrava: horário e meta de resposta no D9.
17. Onde anotar o preço que cada pessoa recebeu? (p5). Destrava: o teste de R$ 47 x R$ 67 valer (D12).
18. A semana do teste vai de segunda a domingo? (p8). Destrava: D12.
19. Até quando vale o preço que a pessoa recebeu? (p10). Destrava: a data na mensagem do D9 e o D12.
20. Vai existir uma página de venda, ou fica só anúncio, WhatsApp e Pix? (p1).
21. Ideia 5: a imagem do livro aberto, como um kit sobre a mesa, para o anúncio e o WhatsApp? (i5).

**Para o Instagram e o anúncio:**

22. Nome do perfil (@) (q11). Destrava: D10.
23. Bio: A, B ou C (p6). Destrava: D10.
24. Foto do perfil: marca ou rosto (p7). Destrava: D10 (pode esperar o teste do vídeo com rosto).
25. Qual anúncio sobe primeiro: Família Compacta, Casa Fita ou Casa Compacta (p16). Destrava: D12.

**Do sistema (não travam o Pix):**

26. A tarefa de hora em hora continua: como está, com reserva, ou para? (p11).
27. Skills: as 2 nossas ou as 6 como vieram? (p12).
28. everything-claude-code: tudo ou só as 6 peças de proteção? (v5). A cópia está na branch `sistema/everything-claude-code`.
29. Liberdade: "tire o grátis e publicar dessa lista" quer dizer que a equipe decide o grátis e publica sem perguntar? Sim ou não (v6). Até ele responder, grátis e publicação continuam dele.
30. A primeira vitrine (que mostra o rascunho e 3 erros internos) pode ser vista por alguém de fora? (ficha `0646`).

**Fora do lançamento:**

31. Casa E02: porta de correr no banheiro, quando ela for revista? (p13). Sem pressa.
32. Pode criar a pasta no Drive quando o PDF final sair? Ele disse "sim" à pasta e mandou a equipe dar o nome (23/11), mas a ficha `0144` pede um "sim" na hora de criar. Destrava: D6.

**O que só ele faz com as mãos** (não é decisão, é ação; nada disso entra no repositório): pôr a chave Pix, o nome de quem recebe e o horário no WhatsApp Business; criar a conta do Instagram; publicar; dar o "sim" e pagar cada campanha; compartilhar a calculadora com o sócio.

## Não fazer (parece o próximo passo, mas não é)

- **Mandar o PDF de hoje a alguém:** sai sem preço e sem os 2 bônus que a oferta promete.
- **Pôr R$ 47 no PDF por conta própria:** o dono decidiu começar pelo R$ 47, mas não decidiu se o preço aparece no PDF (decisão 1).
- **Fazer rascunho novo em cima de rascunho** (outra amostra, outro pôster, outro quadrinho, outro bônus) enquanto ele não escolhe entre os que já existem: gasta e confunde (regra do `contexto/entregas/ULTIMO.md` e da ficha `0144`).
- **Mexer nas outras 21 casas, na E07 ou na E02:** o lançamento tem 3 casas, "capriche bem nessas 3". As fichas `1616` (E07) e o p13 (E02) esperam.
- **Abrir animação, vídeo ou OpenArt:** a ordem é e-book, animações, vídeo; e OpenArt só com o "sim" dele a cada uso.
- **Subir o anúncio C (Casa Compacta)** antes das decisões 13 e 14: o `/oferta` está vetado para quem só cabe essa casa.
- **Levar o everything-claude-code à `main` ou abrir pull request** sem a decisão 28.
- **Criar a pasta no Drive, publicar post ou anunciar** sem o "sim" dele.
- **Escrever o arquivo de grupos das decisões:** é do `organizador`.

## Histórico: o plano de 22/11 (fases antigas)

*O plano abaixo foi escrito pelo Maestro em 22/11 e ficou parado. O que estava feito continua aqui. O resto foi trocado pelas decisões de 23/11 ([`anexos/decisoes-do-dono-2026-11-23.md`](anexos/decisoes-do-dono-2026-11-23.md)): o lançamento tem 3 casas, não 24.*

**G** = tarefa grande. **P** = tarefa pequena. **Dono** = só ele decide.

### Fase 1 · Organizar a base (ficha `1529-organizar-os-arquivos`): feita

| # | Tipo | Tarefa | Quem | Pronto quando |
|---|---|---|---|---|
| 1.1 | G | Juntar documentos lidos juntos | Maestro | **Feito** (22/11): 138 → 100 documentos, 0 link quebrado |
| 1.2 | P | Código repetido | Maestro | **Feito** (22/11): medido; 12 a 24 linhas nos `render-*.cjs` e uma linha de caminho por programa. Juntar acrescentaria mais código do que tira: fica como está |
| 1.3 | P | Cada `contexto/<papel>.md` aponta no máximo 3 resumos | Maestro | **Feito** (22/11): 5 contextos cortados; o `checar.py` agora confere |
| 1.4 | P | Medir o Graphify antes e depois | Maestro | **Feito** (22/11): 2.013 → 1.781 círculos, 2.231 → 2.012 ligações (medido no commit 1af9f47; no 2bb0773, 1.846 e 2.038: uns 8% menos, porque cada documento novo de sistema sobe o número). Metade só cortando conteúdo repetido: vai para a fase 2 |
| 1.5 | P | Auditoria das fichas fechadas | `supervisor` (Fable) | **Feito** (22/11): auditoria 3, 0 alta, 13 médias, 8 baixas; corrigidas, lista em `AUDITORIAS.md` |

### Fases 2 a 6: o que virou cada uma (conferido em 24/11)

- **Fase 2, plano mestre (ficha `1944`):** a ficha diz "na fila; ainda não executado". A rotina de melhoria (2.6) existe em `pedidos/LEIA-ME.md`. Fica para depois do primeiro Pix; este plano faz o papel do 2.4.
- **Fase 3, e-book:** a E07 (3.1 a 3.3, ficha `1616`) saiu do lançamento. As casas refeitas (3.4) viraram as 3 do lançamento: Casa Compacta com hall, Casa Fita e Família Compacta, **feitas e oficiais** em `ebook/plantas/projetos.py` (o dono delegou a aprovação das duas últimas ao Arquiteto). 3D e páginas (3.5) feitos para as 3; textos (3.6) com o Revisor SIM SE aplicado. Título, garantia, bônus, quantas casas e WhatsApp (3.7) **decididos em 23/11**; falta o preço no PDF. Arquiteto registrado (3.6b): o dono disse que o arquiteto é o nosso agente; o aviso legal fica; a leitura do checklist por um profissional é a decisão 4. PDF final (3.8) é o D3 e o D4.
- **Fase 4, animações e imagens:** não abriu. Abre depois do primeiro Pix.
- **Fase 5, vídeo:** não abriu. O dono quer dois testes depois do e-book: um vídeo todo de IA e um com o rosto dele.
- **Fase 6, vender e medir:** virou o D6 a D13. A verba está decidida (R$ 20 por dia, depois do teste sem gastar). O relatório jurídico com Caixa e Confea (6.2) continua pendente, sem pressa para o primeiro Pix.

## Tempo livre: deixar a equipe mais inteligente (dono, 22/11/2026)

*Quando não há tarefa concreta (a fila espera o dono, ou nada aberto dá para fazer), o Maestro **alterna** (dono, 22/11/2026: "uma mistura"): uma tarefa da equipe (L), depois uma do projeto (M), e assim por diante. Uma por vez, até 6 chamadas de agente, nada pago, nada publicado. No fim, conta ao dono o que melhorou, com número quando houver. Melhoria do projeto que muda planta, texto público ou preço vira **proposta** para o dono, não mudança. Desde 23/11 o dono pediu 60% do trabalho no e-book e 40% no sistema, e a tarefa de hora em hora trabalha no e-book: o "Agora" acima vem antes daqui.*

| # | Tarefa | O que deixa mais inteligente | Pronto quando |
|---|---|---|---|
| L1 | Cada agente confirma que vê as suas ferramentas (web, MinoAI, caderno); vale já, não espera a próxima conversa | sem isso, os outros passos não valem | uma linha por agente na ficha `2041-tempo-livre` |
| L2 | Lições: cada erro de auditoria e cada correção do dono vira uma linha em "Lições" do `contexto/<papel>.md` e, se der, uma conferência no `checar.py` | errar menos: o agente lembra do erro de ontem | lições em dia com `AUDITORIAS.md` |
| L3 | Teste da equipe com o pedido da próxima fase (ex.: "refaça a E07"), 3 ou 4 agentes; corrigir o que sair confuso | entender melhor | contradições achadas e corrigidas |
| L4 | Afiar o método de um papel por vez: o `pesquisador` busca a melhor prática (com fonte, no caderno), o papel propõe, o Maestro decide; em conteúdo, o Diretor (MinoAI) opina primeiro | saber mais | uma regra nova no agente, com fonte |
| L5 | Cortar conteúdo repetido entre documentos, uma pasta por vez | ler menos | números de antes e depois |
| L6 | Medir o gasto: tokens por chamada de cada agente (o aviso de cada agente traz o número) e o que encarece | gastar menos | tabela na ficha; a lista de ferramentas mais cara revista |

**Do projeto (M)**

| # | Tarefa | O que melhora | Pronto quando |
|---|---|---|---|
| M1 | `plantas.py validar` nas 24: a casa com mais avisos ganha proposta do `arquiteto` | a casa que o comprador recebe | proposta na ficha; o dono decide |
| M2 | `/ponytail-audit` no código das ferramentas (só relatório) | menos erro e menos código | achados por gravidade; os altos viram ficha |
| M3 | `revisor-de-risco` relê os textos que já estão prontos para o público (`contexto/dono/TEXTOS-DESATUALIZADOS.md`, posts, WhatsApp) | menos risco | promessas sem lastro listadas, com a correção |
| M4 | `redator` e `estrategista` conferem o funil (anúncio, comentário, WhatsApp) contra as decisões mais novas | mais venda | o que está velho, com a proposta |
| M5 | `designer` olha as páginas do PDF de rascunho (`livro.py --previa`) em busca do que parece genérico | o comprador confia no que vê | páginas apontadas, com o porquê |
| M6 | Conferir o `PAINEL.md`: todo número tem fonte e data | decisões com número certo | número sem fonte apontado |

## Sempre, em toda fase

- Antes de cada tarefa: a ficha diz o objetivo e o que cada agente acrescenta; o "Agora" do quadro é atualizado.
- Trabalho com mais de 3 passos pede o plano ao `planejador` antes; monte misturado vai ao `organizador` (24/11).
- Erro achado vira regra ou conferência no `checar.py` (`pedidos/LEIA-ME.md`, "Consertar de vez").
- Antes da web: `python3 ferramentas/pesquisa.py buscar`.
- Depois de cada tarefa: `checar.py`, painel, resumo de passagem, **marcar "feito" aqui**, commit e push na `main`.

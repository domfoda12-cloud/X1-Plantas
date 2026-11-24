# Plano de trabalho: o que a equipe faz, em que ordem, e para quê

> Pedido do dono (22/11/2026): "sempre dê um objetivo à equipe; um plano passo a passo, separado em tarefas grandes e pequenas, entre os agentes". **Quem mantém, desde 24/11: o `planejador`** (antes era o Maestro). **Terceira rodada: 24/11/2026, 11h55 UTC**, conferida contra o repositório nesta hora (`git log`, `git status`, `pedido.py listar`, `config.json`, `ebook/saida/`), inclusive o que ainda não tinha commit. Regras do dono desta rodada (24/11): "Sempre coloque algo no Agora, nunca pare"; "Sempre que um agente não estiver trabalho no projeto ele deve estar trabalho: ou nele mesmo, ou no sistema ou em outro agente"; "Tome cuidado para não diminuir a qualidade das coisas em troca de desempenho/tokens". Ao terminar um passo, quem fez roda `python3 ferramentas/plano.py feito <passo> "o que virou"`; quando o dono responde, `plano.py respondido <n> "o que ele disse"` (só com fala dele). Papéis: [`contexto/EQUIPE.md`](../contexto/EQUIPE.md).

## O objetivo da equipe

**O comprador acha a casa que cabe no lote dele, entende por quê e se sente seguro para construir, e por isso manda o Pix.** Toda tarefa abaixo diz que parte desse objetivo ela move. O número que manda: o custo por venda ([`PAINEL.md`](../PAINEL.md), seção 4). Meta do dono: primeiro Pix ainda em novembro; 10 a 50 vendas no primeiro mês.

## Onde estamos (24/11, 11h55, conferido)

- **O e-book existe em rascunho:** `ebook/saida/ebook.pdf`, 17 páginas, 4,9 MB (`pdfinfo`), 3 casas (Casa Compacta 51 m² com hall, Casa Fita com 2 quartos, Família Compacta), título "Antes do primeiro tijolo" (`config.json`). Regravado em 24/11 às 11:09. Hoje as páginas gerais ficam antes (2 a 7) e depois (14 a 16) das casas (8 a 13, duas por casa).
- **Respondidas hoje pelo dono** (`decisoes-do-dono-2026-11-23.md`, seções de 24/11): preço R$ 47 e PDF sem preço (decisão 1); 3 títulos novos (6, virou o A4 e a 34); **e-book com uma parte de cada casa e uma parte geral**, e a página da parede sem janela vai para a geral (8); **vende com CPF**, faltam endereço e e-mail (15, cartão p20); a tarefa de hora em hora continua (26). Ele recusou os 6 nomes e as 3 bios do Instagram: 8 nomes e 4 bios novos, com humor pelo absurdo e com o veto do Revisor, esperam a escolha dele (`instagram-nomes-e-bios-absurdos-2026-11-24.md`; decisões 22 e 23).
- **Pedido de hoje, cômodo a cômodo** ("continue trabalhando nas casas... Planejar cada quarto, ideias do que fazer em lugares da casa"): o Arquiteto escreveu as 32 áreas das 3 casas (`pedidos/anexos/comodo-a-comodo-3-casas.md`, commit 2d3e61f). **O Revisor já leu** (`veto-comodo-a-comodo-2026-11-24.md`, sem commit às 11h51): veto em 3 pontos (conta de tomadas da NBR 5410 de 2003, Portaria MCID 725 como se fosse regra da casa do comprador, serviço da C01 com a janela em cima da porta), cada um com a troca. Por isso o "Revisor lê" virou o A7, feito, e o que falta é o A8.
- **A janela da Casa Compacta (A6):** a variante c **não** está pronta: passa no validador, mas a porta nova bate 60 cm na bancada. O dono escolhe entre 3 caminhos (decisão 2).
- **O 3D mostra áreas diferentes das do e-book:** o motor `video/src/casa3d.js` escreve no desenho de cada cômodo a área de eixo a eixo (sala da C01: 3,35 x 4,20 = 14,1 m²); o e-book usa a área livre do validador (3,14 x 3,99 = 12,5 m²). A imagem 3D do e-book (`ebook/visual/3d/E03.jpg`, olhada) não mostra área; o erro aparece no desenho de cima do motor (vitrine e animações). Conserto no F7.
- **Auditoria das regras de hoje** (`pedidos/AUDITORIAS.md`, fim): 13 de 32 regras sem mecanismo; as 5 piores viram passos da fila (F3, F8, F9, F10, F14). **Skills candidatas** (`skills-candidatas-2026-11-24.md`): falta o Conselho; a Prova 4 do júri vem dali (F12, F13).
- **Visita 3D:** outro agente está detalhando agora (ficha `1144`); este plano não a planeja.
- **Preço: o dono respondeu** (quadro de tarefas, 24/11, 11:07): "47, pdf não fala de preço". O preço fica só no WhatsApp; o `config.json` guarda "R$ 47" e o `checar.py` dá erro se o PDF citar preço.
- **Título: 3 opções novas** (A4 feito: Revisor e Diretor em `titulos-opcoes-2026-11-24.md`); o atual fica até ele escolher (decisão 34).
- **Bônus:** o PDF não traz nem anuncia nenhum (o `checar.py` conta 0 e barra bônus sem página). A parte que não depende do dono **já está feita**: o texto dos 2 bônus tem o veto do Revisor aplicado (`pedidos/anexos/bonus-*.md`, commit f2fefb5) e o protótipo `ebook/plantas/rascunhos/bonus.py` serve aos dois destinos (dentro do PDF ou separado). Nenhuma mensagem de venda cita bônus: `RESPOSTAS-RAPIDAS.md` e o kit do anúncio mandam esperar o bônus existir no PDF. Só o roteiro do Instagram (`pedidos/anexos/instagram-perfil-novo.md`, post 3 e "Por dentro") mostra os 2 bônus.
- **Planta grátis:** `ebook/saida/planta-gratis-C01.pdf` (3 páginas) já fala do "e-book completo" de 3 casas; a versão final espera o dono escolher a amostra. Nota velha achada: o `RESPOSTAS-RAPIDAS.md` (linha 90) ainda diz que ela "fala em 24 casas" (limpeza no D9).
- **Pronto, sem uso ainda:** o PDF leve de emergência (`python3 ferramentas/pdf-leve.py`, teste 4,9 → 3,0 MB), as respostas rápidas, o kit do anúncio, o material do Instagram novo, o número do WhatsApp.
- **Ainda não existe:** PDF final, pasta no Drive, Instagram do negócio, nenhum anúncio. **Nenhum anúncio roda hoje** (kit, seção 0).

## O caminho mais curto até o primeiro Pix

**Hoje há 16 decisões do dono no caminho do primeiro anúncio (D12)**, pela conta do `python3 ferramentas/plano.py caminho D12`: 2, 3, 4, 5, 13, 14, 16, 17, 18, 19, 22, 23, 24, 25, 32 e 34. Na rodada passada eram 17: a 15 (CPF) foi respondida e saiu. As outras respondidas hoje (6, 8 e 26) não estavam no caminho. Os passos novos do cômodo a cômodo e das duas partes (A8 a A10, D15 a D19) entram no caminho do PDF final, mas **não acrescentam decisão**: o único que espera o dono é o D18 (serviço da C01), e ele espera a decisão 2, que já estava no caminho. Na prática eles não atrasam a venda: o D3 já espera as decisões 2 a 5 e 34.

**Endereço e e-mail de quem vende** (cartão p20) não são decisão, são dado pessoal que ele põe no celular, fora do repositório; mas a lei pede (Decreto 7.962/2013), e o D10 e o D14 só ficam prontos com eles. Marquei a 15 como respondida porque ele respondeu o que ela perguntava ("CPF"); o resto está escrito no "pronto quando" do D10 e do D14.

O que acontece se ele não responder cada uma (saída padrão; a equipe **não aplica** nenhuma por conta própria):

| Decisão | Sem resposta |
|---|---|
| 2 · janela da Casa Compacta | o D1 fica parado, e com ele o serviço da C01 no cômodo a cômodo (D18) e o PDF final (D3). O A6 mostrou que a variante c bate na bancada: ele escolhe entre os 3 caminhos da decisão 2 |
| 3, 4 e 5 · bônus | o D2 fica parado, e com ele o PDF final. Ou a decisão 33, abaixo |
| 13 e 14 · amostra grátis | o D8 fica parado, e com ele os posts (D11) e o anúncio |
| 16 · quem atende | o D9 fica parado (o horário vai na mensagem de ausência) |
| 17, 18 e 19 · teste de preço | o D12 fica parado: o teste de R$ 47 x R$ 67 que ele decidiu não teria como ser medido |
| 22, 23 e 24 · @, bio e foto | o Instagram (D14) fica parado. Há 8 nomes e 4 bios novos esperando por ele. A foto (24) se troca depois a qualquer hora |
| 25 · qual anúncio primeiro | o D12 fica parado |
| 32 · criar a pasta no Drive | o D6 fica parado: sem link, ninguém recebe o e-book. Ele pode responder já ("sim, quando o PDF sair") |
| 34 · qual título | o PDF final (D3) fica parado. Responder "mantém o atual" também destrava |

**OPÇÃO para o dono (decisão 33, não escolhida): vender o e-book primeiro, sem bônus, e entregar os 2 bônus depois.**
- **O que muda:** o PDF final (D3) deixa de esperar o D2; as decisões 3, 4 e 5 saem do caminho e o D2 passa para depois da primeira venda. O caminho cai de **16 para 14** decisões (saem 3, 4 e 5; entra a 33). Conta à mão: o `plano.py` não calcula opção.
- **Parecer do Revisor (A5, feito):** SIM SE nenhuma peça citar bônus antes de existir; 3 condições em `veto-opcao-sem-bonus-2026-11-24.md`.
- **Por que parece honesto (suposição minha de antes do A5):** nada do que vai ao comprador promete bônus hoje. O PDF anuncia 0 bônus e o `checar.py` barra bônus sem página; o `/oferta` não cita bônus e o `RESPOSTAS-RAPIDAS.md` (linha 154) manda acrescentar só "depois que estiverem prontos no PDF"; o kit do anúncio diz o mesmo (seção 1b). Quem compra recebe exatamente o que a mensagem diz.
- **O que custa:** a oferta decidida em 23/11 tem 2 bônus, e fica menor no começo. O post 3 e o "Por dentro" do Instagram tiram as telas dos bônus até eles existirem. Não dá para escrever "bônus em breve" (é promessa sem data). Quem comprou antes recebe os bônus depois, sem ter pago por eles.
- **Se ele disser sim:** quem conduz tira o D2 da coluna "depende de" do D3 e chama o planejador.

## Agora (pode começar já, sem esperar ninguém)

**Regra (dono, 24/11: "Sempre coloque algo no Agora, nunca pare"):** quando um passo de "Agora" fecha, o próximo livre de "Depois" ou da "fila da equipe" (nesta ordem; o que deixa o comprador mais perto do Pix vem antes) sobe na hora, e quem conduz move a linha para cá; "Agora" nunca fica com menos de 1 passo aberto nem com mais de 3.

| # | Passo | Quem | Onde | Pronto quando | Depende de |
|---|---|---|---|---|---|
| A1 | **Feito 24/11:** Revisor SIM, nada é veto; 3 trocas aplicadas, 2 anotadas (`pedidos/anexos/veto-ebook-lancamento-2026-11-24.md`). **Ler o rascunho do e-book inteiro em busca de risco**, página por página (17 do e-book + 3 da planta grátis), e listar o que precisa mudar antes da venda e não depende de decisão do dono | `revisor-de-risco` (Opus, porque ainda é rascunho; o Fable lê o final no passo D4) | `ebook/saida/ebook.pdf`, `ebook/saida/planta-gratis-C01.pdf`; veredito em `pedidos/anexos/veto-ebook-lancamento-2026-11-24.md` | o arquivo tem uma linha por página (SIM, SIM SE com a troca, ou NÃO); o Maestro aplica os SIM SE e o `checar.py` fica verde | ninguém |
| A2 | **Feito 24/11** (resumos corrigidos; no quadro só restam na fila os cartões f3, f4 e v4, que são fila de verdade). **Limpar o que está velho e confunde quem lê:** 3 resumos internos ainda dizem "C01 50 m²" (`ebook/RESUMO.md`, `ebook/vendas/RESUMO.md`, `instagram/RESUMO.md`) e o de vendas ainda fala em "5 plantas grátis" (o dono decidiu só a Casa Compacta); no quadro de tarefas, 6 cartões dizem "rodando" ou "fila" mas já terminaram (r1, r3, r4, f1, f2, f5) e o v2 (aprovar Casa Fita e Família) foi delegado e feito | Maestro | a parte "O essencial" de cada `RESUMO.md`; o quadro (ficha `1946-quadro`) | `grep -rn "50 m²" ebook/RESUMO.md ebook/vendas/RESUMO.md instagram/RESUMO.md` não acha nada; no quadro nenhum cartão "rodando" sem agente rodando; o r2 (everything-claude-code) passa a "esperando você" | ninguém |
| A3 | **Feito 24/11:** `python3 ferramentas/pdf-leve.py ebook/saida/ebook.pdf <destino>`; teste: 4,9 → 3,0 MB, página 9 conferida a olho. **Deixar pronto o PDF comprimido de emergência**, testado no rascunho, para no dia do PDF final sair com um comando | Maestro (código), `designer` olha se a imagem ainda se lê | `ebook/gerador/` (programa novo entra no `MAPA-DO-SISTEMA.md`); teste numa pasta temporária, **sem tocar em `ebook/saida/`** | o comando gera uma cópia das 17 páginas bem menor que 4,9 MB (o Maestro fixa a meta e diz por quê), a prévia de cada página foi olhada e o `checar.py` passa | ninguém |
| A4 | **Feito 24/11:** Revisor: os 3 passam com troca no subtítulo; Diretor (MinoAI Frontier): como gancho falado de vídeo o método favorece 'Errar na planta sai caro' (único com emoção), mas gancho não é título; tudo em pedidos/anexos/titulos-opcoes-2026-11-24.md; cartão p14 com o dono. **Passar as 3 opções de título pelo conselho**, como o dono pediu em 24/11 (cartão p14, "B"). O rascunho do Redator **já existe**, com a busca de nome feita (`pedidos/anexos/titulos-opcoes-2026-11-24.md`, sem commit às 11h10): falta o Diretor e o Revisor, que o próprio arquivo diz não ter passado. Sem opção nova: "Antes do primeiro tijolo" entra como quarta, "mantém". **Primeiro gesto (10 min):** abrir `pedidos/anexos/titulos-opcoes-2026-11-24.md` e conferir se já tem opinião do Diretor ou do Revisor (`grep -n -i "diretor" pedidos/anexos/titulos-opcoes-2026-11-24.md`, e o mesmo com "revisor") | Diretor (MinoAI Frontier) opina primeiro, com a fonte; `estrategista` e `revisor-de-risco` (conselho completo: o título vai ao público) | `pedidos/anexos/titulos-opcoes-2026-11-24.md`; o cartão do quadro vai ao dono como uma pergunta só | o arquivo traz uma linha do Diretor com fonte e o veredito do Revisor por opção (SIM, SIM SE ou NÃO); nada trocado em nenhum texto nem no `config.json` | ninguém |
| A5 | **Feito 24/11:** Revisor SIM SE: honesto se nenhuma peça citar bônus antes de existir; 3 condições e a lista de trocas em pedidos/anexos/veto-opcao-sem-bonus-2026-11-24.md. **Dar o parecer do Revisor sobre a opção "vender primeiro sem bônus, bônus depois"** (decisão 33), para o dono decidir já sabendo do veto. Só parecer: não muda texto. **Primeiro gesto (10 min):** `grep -rn -i "bônus" ebook/vendas/RESPOSTAS-RAPIDAS.md pedidos/anexos/kit-anuncio-whatsapp.md pedidos/anexos/instagram-perfil-novo.md ebook/config.json` | `revisor-de-risco` (Opus: é parecer, não peça final) | veredito em `pedidos/anexos/veto-opcao-sem-bonus-2026-11-24.md` | o arquivo existe com SIM, SIM SE ou NÃO e a lista de cada texto que cita bônus, com a troca que ele pede se o dono disser sim | ninguém |
| A6 | **Feito 24/11:** NÃO está pronto: a variante c passa no validador, mas a porta nova bate 60 cm na bancada da cozinha (os móveis entraram depois do rascunho). O D1 espera o dono escolher: porta no canto esquerdo da cozinha com janela de 0,80 m (testado só em rascunho; sobram uns 13 cm entre porta e janela, o engenheiro confere), manter a porta no serviço com bandeira ou veneziana em cima, ou deixar como está. Rascunho atualizado em ebook/plantas/rascunhos/C01J.py. **Conferir que o conserto da janela está pronto para aplicar** (variante c do `C01J.py`, a recomendada na ficha `0144`), sem aplicar: mesmo hall, 51 m² e mesmo lote da Casa Compacta oficial de hoje. **Primeiro gesto (10 min):** `python3 ebook/plantas/rascunhos/C01J.py c` | `arquiteto` | `ebook/plantas/rascunhos/C01J.py` (lê `ebook/plantas/projetos.py`, **não muda**) | a saída mostra `erros: []` e `janela sobre porta: []`; uma linha na ficha `1946-refazer` diz se a variante c bate com a oficial e traz o comando do D1 escrito, sem rodar | ninguém |
| A7 | **Feito 24/11** (arquivo ainda sem commit às 11h51): veto em 3 pontos, cada um com a troca; o resto passa com troca; as 5 ideias mais seguras para abrir a página listadas. **O Revisor lê o cômodo a cômodo das 3 casas** antes de qualquer parte virar página | `revisor-de-risco` (Opus: rascunho) | `pedidos/anexos/veto-comodo-a-comodo-2026-11-24.md` | o arquivo existe com vetos, trocas e o que não conferiu | ninguém |
| A8 | **Aplicar o veto do Revisor no cômodo a cômodo:** refazer a conta de tomadas pela NBR 5410 de 2004 (ou mais nova), com a fonte registrada no caderno; a Portaria MCID 725 vira referência ("nas casas do Minha Casa Minha Vida..."), não regra da casa do comprador; as trocas sem veto (Código Civil, carro, umidade, "o profissional confere"). O serviço da C01 (veto 3) fica como está até o D1. **Primeiro gesto (10 min):** `python3 ferramentas/pesquisa.py buscar "NBR 5410"` e abrir a seção "Vetos" do `veto-comodo-a-comodo-2026-11-24.md` | `arquiteto` aplica; `pesquisador` acha a fonte de 2004 se o caderno não tiver; `revisor-de-risco` confere | `pedidos/anexos/comodo-a-comodo-3-casas.md`; fonte em `pesquisas/` | o Revisor escreve no `veto-comodo-a-comodo-2026-11-24.md` uma linha "vetos 1 e 2 levantados" (o 3 continua); `grep -n "Portaria" pedidos/anexos/comodo-a-comodo-3-casas.md` só acha a Portaria como referência do MCMV; `checar.py` verde | ninguém |
| A9 | **Página de prova "cômodo a cômodo" de UMA casa, a Casa Fita (E03), na parte "de cada casa"** (decisão 8), para acertar o molde antes de fazer as outras duas. O Diretor dá a ideia principal da página primeiro; o Redator escreve a partir do documento do Arquiteto, já com as trocas do Revisor (para tomadas, o texto provisório que ele deu: "sugestão de pontos; o mínimo é o eletricista que confere na norma vigente"); o Designer monta. **Primeiro gesto (10 min):** abrir `pedidos/anexos/comodo-a-comodo-3-casas.md`, seção 2 (linhas 118 a 208), ao lado de `veto-comodo-a-comodo-2026-11-24.md`, e marcar as linhas da E03 que o veto troca | Diretor (MinoAI Frontier), com a fonte; `redator`; `designer`; `arquiteto` confere os números | rascunho novo em `ebook/plantas/rascunhos/` (gera numa pasta temporária; **não toca** `ebook/saida/` nem `ebook/gerador/`) | existe a imagem da página (1 ou 2 páginas) gerada pelo rascunho, com o aviso "Planta de referência..." visível; o Designer escreveu "legível em A4 e no celular"; `git status --short ebook/saida` vazio; `checar.py` verde | ninguém |
| A10 | **Mapa das duas partes do e-book** (decisão 8 respondida): cada uma das 17 páginas de hoje vai para "de cada casa" ou "geral", e onde entram as páginas novas (cômodo a cômodo das 3 casas; parede sem janela na geral; "como mobiliar" só marcada como "se o dono quiser", decisão 7). Só o mapa: nada muda no gerador. **Primeiro gesto (10 min):** `for i in $(seq 1 17); do pdftotext -f $i -l $i ebook/saida/ebook.pdf - 2>/dev/null; done` e anotar o título de cada página | `designer` e `redator` propõem; Maestro decide a ordem (não é decisão do dono: título, preço e o que é grátis não mudam) | `pedidos/anexos/ebook-duas-partes-mapa-2026-11-24.md` | o arquivo tem uma tabela com as 17 páginas (número, título, parte), as páginas novas com o lugar e o total de páginas previsto; `git diff --stat ebook/gerador` vazio | ninguém |

Suposição minha em A3: o dono pediu "uma forma comprimida de mandar por PDF em caso de emergência" (ficha `1946-refazer`) quando o PDF tinha 22,7 MB; hoje tem 4,9 MB. Continua valendo porque ele não desistiu.

Suposição minha em A4: o "B" do dono quer dizer 3 títulos novos para escolher (é a leitura do Maestro em `decisoes-do-dono-2026-11-23.md`).

Suposições minhas em A8 a A10 (24/11): (1) o cômodo a cômodo entra no **e-book pago**, na parte de cada casa: o dono pediu o cômodo a cômodo e disse que o e-book terá "uma parte falando de cada casa específica"; o próprio Arquiteto escreveu que isto é recomendação e que quem decide é o dono, por isso o D15 mostra a prova a ele antes de fazer as outras duas casas. (2) A prova é da **Casa Fita**: a C01 tem o serviço vetado até a janela (veto 3); a E03 não tem decisão pendente na planta. O Maestro pode trocar; não é escolha de casa do lançamento, que já está decidida. (3) A regra de não empilhar rascunho (`ULTIMO.md`) vale para peças que esperam escolha dele (amostra, pôster, quadrinho, bônus, janela); o cômodo a cômodo ele pediu, e a página de prova é uma só.

## Depois (em ordem; cada um diz de qual passo ou decisão depende)

| # | Passo | Quem | Onde | Pronto quando | Depende de |
|---|---|---|---|---|---|
| D1 | Consertar a janela em cima da porta da Casa Compacta: levar a variante escolhida de `C01J.py` para as casas oficiais, refazer o 3D e a prévia | `arquiteto`; Maestro confere | `ebook/plantas/rascunhos/C01J.py` → `ebook/plantas/projetos.py` | `python3 ferramentas/plantas.py validar` sem erro; o aviso "janela em cima de porta" do `checar.py` não cita mais a C01 | decisão 2; A6 |
| D2 | Montar as páginas dos 2 bônus como o dono escolher (dentro do PDF ou separado; 2 ou 3 páginas de perguntas). O texto e o protótipo já existem: aqui só se encaixa no destino escolhido | `designer` e `redator`; `arquiteto` confere os números; `revisor-de-risco` | `ebook/plantas/rascunhos/bonus.py` → gerador | o `checar.py` diz "bônus do PDF: 2 anunciado(s), todos com página" (ou o PDF separado existe e o e-book aponta para ele) | decisões 3, 4 e 5 |
| D3 | Gerar o PDF final, com o título escolhido e sem preço: `python3 ebook/gerador/livro.py` | Maestro | `ebook/config.json`, `ebook/saida/ebook.pdf` | o `checar.py` passa sem aviso de campo pendente e com "o PDF não cita preço"; a capa traz o título escolhido | decisões 1 e 34; D1, D2, A1, A4 |
| D4 | Leitura final do PDF inteiro, com o veto | `revisor-de-risco` no **Fable** (peça final) | ficha `1946-refazer`, "Conferência" | SIM escrito na ficha, com a data | D3 |
| D5 | PDF de emergência a partir do final, conferido página por página | Maestro | `python3 ferramentas/pdf-leve.py` (o comando do A3) | o arquivo existe, 17 páginas (ou mais, se os bônus entrarem), todas olhadas | A3, D4 |
| D6 | Pasta no Google Drive com o título escolhido (nome dado pela equipe, como o dono mandou) com o PDF final e o de emergência; link só para ver | Maestro, pelo conector do Drive | Drive do dono | as permissões do arquivo dizem "qualquer pessoa com o link: leitor", nunca "editor" | D5 e decisão 32 |
| D7 | Republicar a calculadora do parceiro com as 3 casas e as páginas do PDF final | Maestro | `ebook/vendas/calculadora-lote.html` e a página publicada | a página publicada mostra as 3 casas com as páginas certas | D3 |
| D8 | Amostra grátis final, na opção que o dono escolher; se for a B, o guia "Seu lote cabe?" conferido; o Revisor tira ou mantém o veto do `/oferta` para quem só cabe a Casa Compacta | `redator` e `designer`; `arquiteto` e `revisor-de-risco` conferem | `ebook/plantas/rascunhos/amostra.py`, `pedidos/anexos/guia-seu-lote-cabe-texto.md` → `ebook/saida/planta-gratis-C01.pdf` | o PDF grátis regravado na opção escolhida; veredito do Revisor sobre o `/oferta` na ficha `1946-refazer` | decisões 13 e 14 |
| D9 | Respostas rápidas sem colchete de decisão (horário, quem atende, título, link do Drive) e sem a nota velha da linha 90 (a planta grátis não fala mais em 24 casas; o motivo de esperar é a decisão 13). Os dados pessoais o dono põe no celular, **nunca no repositório**. A decisão 1 saiu daqui: o preço da mensagem é o da semana (R$ 47 na primeira, decidido) | `redator`; `revisor-de-risco` | `ebook/vendas/RESPOSTAS-RAPIDAS.md` | só sobram os colchetes de dado pessoal ([chave Pix], [CPF/CNPJ] etc.), o [preço] da semana e o [nome] do cliente; `grep -n "24 casas" ebook/vendas/RESPOSTAS-RAPIDAS.md` não acha nada | decisões 15 e 16; D6 |
| D10 | O dono configura o WhatsApp Business com as respostas rápidas (passo a passo pronto). Dividido nesta rodada: o Instagram virou o D14, que não espera o PDF | **dono** (o `ajudante` acompanha, se ele quiser) | `ebook/vendas/RESPOSTAS-RAPIDAS.md`, seção 3 | perfil do WhatsApp Business com nome, CPF ou CNPJ, endereço e e-mail de quem vende (lei) e os atalhos | decisão 15; D9 |
| D14 | O dono cria o Instagram do negócio (passo a passo pronto). Pode sair assim que ele responder, sem esperar o PDF final | **dono** (o `ajudante` acompanha, se ele quiser) | `pedidos/anexos/instagram-perfil-novo.md`, seção 6 | perfil no ar com o @, a bio e a foto escolhidos e os dados de quem vende (lei) | decisões 15, 22, 23, 24 e 34 |
| D11 | Teste de procura sem gastar: os primeiros posts com a casa (imagem tirada das páginas e do 3D do e-book) | `designer` (ideia do Diretor), `redator`, `revisor-de-risco` no Fable; **o dono publica** | `instagram/` | posts prontos e aprovados; o dono publica quando quiser | D8, D10, D14 |
| D12 | Primeiro anúncio: R$ 20 por dia, um por vez, com data de término, o que o dono escolher (A Casa Fita ou B Família; o C só depois da decisão do grátis) | `estrategista`; **o dono dá o "sim" por campanha e paga** | `pedidos/anexos/kit-anuncio-whatsapp.md`, seções 0 e 8 | anúncio no ar com data de término no Gerenciador | D3 a D11; decisões 17, 18, 19 e 25 |
| D13 | Medir: custo por contato, conversão do WhatsApp, custo por venda; só números que a ferramenta devolveu | `estrategista` | `PAINEL.md`, seção 4 | números com fonte e data; **primeiro Pix registrado** | D12 |

O D14 tem número fora de ordem porque os códigos não se renumeram; ele fica antes do D11 na tabela, e o "D3 a D11" do D12 o inclui.

Pergunta para o Maestro (não para o dono) em D11: o `CONTEXTO.md` diz que as imagens dos posts se refazem "quando a frente de animação abrir", e o dono decidiu "posts sem gastar" como teste de procura antes do anúncio. Suposição minha: post com imagem parada tirada das páginas do e-book faz parte da venda do e-book, não da frente de animação. Confirmar antes do D11.

Depois do primeiro Pix, na ordem do dono: animações e imagens (fase 4 do histórico), depois vídeo (fase 5), depois o resto da fila.

## Esperando o dono

**34 decisões aqui, 32 sem resposta** (a 1 e a 6 foram respondidas em 24/11; a 33 e a 34 nasceram nesta rodada). O `organizador` junta as decisões em grupos pequenos em `pedidos/anexos/decisoes-pendentes-em-grupos.md`; lá a conta é 38 (versão de 24/11) porque entram as do vídeo e das próximas casas, e ainda não entram a 33 e a 34, que são desta rodada. Os mesmos códigos de cartão vão entre parênteses. **As que mais destravam, pela conta do `plano.py destrava`: 2, 3, 4, 5 e 34 (11 passos cada). A 33 aparece "sem passo preso" de propósito: ela muda as dependências do D3 só se ele disser sim.**

**Para o e-book sair (o produto):**
1. **Respondido 24/11:** "47, pdf não fala de preço": R$ 47 na primeira semana, só no WhatsApp; o PDF não mostra preço. Pergunta era: preço no PDF, R$ 47 impresso ou PDF sem preço (p3). Destravou a parte do preço do D3.
2. Janela em cima da porta da Casa Compacta: aprova o conserto? (w3). Destrava: D1.
3. **Bônus dentro do PDF ou num PDF separado** (p15). Destrava: D2 (a oferta decidida em 23/11 e o `config.json` têm 2 bônus; o PDF e as mensagens de venda não citam nenhum).
4. Um engenheiro ou arquiteto registrado lê o checklist antes da venda? É contratação (p17). Destrava: o bônus do checklist no D2.
5. Folha de perguntas ao engenheiro: 2 páginas, 3, ou também no celular? (p19). Destrava: o bônus das perguntas no D2.
6. **Respondido 24/11:** "B": quer 3 opções de título novo (p14). Virou o A4 e a decisão 34.
7. "Como mobiliar": página do e-book, da amostra ou dos dois? (x3). Destrava: páginas novas, se ele quiser.
8. **Respondido 24/11:** uma parte por casa e uma parte geral; a página da parede sem janela vai para a geral (quadro, 24/11 11:09). Parede sem janela: a página vai na Casa Fita, na E07 ou nas duas? (v3).
9. Pôster das 3 casas: A, B ou C? (i3).
10. Quadrinhos: quais dos 3 roteiros? (i2).
11. Quadrinhos: desenho nosso, de graça, ou ver o custo da arte por IA? (p18).
12. Ideia 4: quem é o artista da caligrafia? (i4).

**Para a amostra grátis e a oferta:**

13. **Amostra grátis: A, B, ou A agora e B depois; e se vai mais alguma coisa de graça** (f6 e v1). Destrava: D8, o `/planta`, o anúncio C e o primeiro post grátis.
14. Quem já recebeu a Casa Compacta grátis compra o quê? (p4). Destrava: o fim do veto do `/oferta` para o lote de 8 x 15 m e o anúncio C.

**Para vender dentro da lei e atender:**

15. **Respondido 24/11:** CPF (comentário no quadro, 24/11 11:13); faltam endereço e e-mail, cartão p20. **Quem vende: CNPJ do MEI ou CPF** (e o endereço e o e-mail) (p9). Destrava: D9, D10 e D14; sem isso não há venda pela internet dentro da lei (Decreto 7.962/2013).
16. Quem responde o WhatsApp do negócio: ele, o sócio ou os dois? (p2). Destrava: horário e meta de resposta no D9.
17. Onde anotar o preço que cada pessoa recebeu? (p5). Destrava: o teste de R$ 47 x R$ 67 valer (D12).
18. A semana do teste vai de segunda a domingo? (p8). Destrava: D12.
19. Até quando vale o preço que a pessoa recebeu? (p10). Destrava: a data na mensagem do D9 e o D12.
20. Vai existir uma página de venda, ou fica só anúncio, WhatsApp e Pix? (p1).
21. Ideia 5: a imagem do livro aberto, como um kit sobre a mesa, para o anúncio e o WhatsApp? (i5).

**Para o Instagram e o anúncio:**

22. Nome do perfil (@) (q11). Destrava: D14. Duas das opções (@primeirotijolo e a outra metade do título) caem se o título mudar: melhor depois da 34.
23. Bio: A, B ou C (p6). Destrava: D14.
24. Foto do perfil: marca ou rosto (p7). Destrava: D14 (pode esperar o teste do vídeo com rosto; a foto se troca depois).
25. Qual anúncio sobe primeiro: Família Compacta, Casa Fita ou Casa Compacta (p16). Destrava: D12.

**Do sistema (não travam o Pix):**

26. **Respondido 24/11:** A: continua como está (quadro, 24/11 11:12). A tarefa de hora em hora continua: como está, com reserva, ou para? (p11).
27. Skills: as 2 nossas ou as 6 como vieram? (p12).
28. everything-claude-code: tudo ou só as 6 peças de proteção? (v5). A cópia está na branch `sistema/everything-claude-code`.
29. Liberdade: "tire o grátis e publicar dessa lista" quer dizer que a equipe decide o grátis e publica sem perguntar? Sim ou não (v6). Até ele responder, grátis e publicação continuam dele.
30. A primeira vitrine (que mostra o rascunho e 3 erros internos) pode ser vista por alguém de fora? (ficha `0646`).

**Fora do lançamento:**

31. Casa E02: porta de correr no banheiro, quando ela for revista? (p13). Sem pressa.
32. Pode criar a pasta no Drive quando o PDF final sair? Ele disse "sim" à pasta e mandou a equipe dar o nome (23/11), mas a ficha `0144` pede um "sim" na hora de criar. Destrava: D6.

**Novas desta rodada (24/11):**

33. **Vender o e-book primeiro, sem bônus, e entregar os 2 bônus depois?** (A) Sim: o PDF final sai sem esperar os bônus; quem comprar antes recebe os bônus quando ficarem prontos; nenhuma mensagem fala de bônus antes disso. (B) Não: o PDF só sai com os 2 bônus, como decidido em 23/11. Opção do planejador, não escolhida; o parecer do Revisor sai no A5. Destrava, se for A: tira as decisões 3, 4 e 5 do caminho do primeiro Pix (17 → 15).
34. **Qual título:** uma das 3 opções do A4, ou mantém "Antes do primeiro tijolo"? Destrava: D3 (capa) e, por ele, a pasta do Drive, as respostas e o anúncio; também o @ e a bio do Instagram (D14).

**O que só ele faz com as mãos** (não é decisão, é ação; nada disso entra no repositório): pôr a chave Pix, o nome de quem recebe e o horário no WhatsApp Business; criar a conta do Instagram; publicar; dar o "sim" e pagar cada campanha; compartilhar a calculadora com o sócio.

## Não fazer (parece o próximo passo, mas não é)

- **Mandar o PDF de hoje a alguém:** sai sem os 2 bônus da oferta de 23/11 e com o título que o dono quer trocar.
- **Imprimir preço no PDF:** o dono decidiu (24/11) que o PDF não fala de preço; o `checar.py` barra.
- **Tratar a decisão 33 como respondida:** até ele responder, vale o de 23/11 (os 2 bônus vão com o PDF pago) e o D3 espera o D2.
- **Escrever "bônus em breve" em qualquer mensagem:** é promessa sem data; bônus só entra no texto quando existir (CDC, art. 30).
- **Trocar o título nos textos** (respostas, kit, Instagram, pasta do Drive) antes da decisão 34. O A4 só propõe.
- **Preparar o código de um destino dos bônus** (dentro do PDF ou separado) antes da decisão 3: é trabalho para uma opção que ele pode não escolher.
- **Fazer rascunho novo em cima de rascunho** (outra amostra, outro pôster, outro quadrinho, outro bônus, outra variante da janela) enquanto ele não escolhe entre os que já existem: gasta e confunde (regra do `contexto/entregas/ULTIMO.md` e da ficha `0144`). O A6 só confere a variante que já existe.
- **Mexer nas outras 21 casas, na E07 ou na E02:** o lançamento tem 3 casas, "capriche bem nessas 3". As fichas `1616` (E07) e o p13 (E02) esperam.
- **Abrir animação, vídeo ou OpenArt:** a ordem é e-book, animações, vídeo; e OpenArt só com o "sim" dele a cada uso.
- **Subir o anúncio C (Casa Compacta)** antes das decisões 13 e 14: o `/oferta` está vetado para quem só cabe essa casa.
- **Levar o everything-claude-code à `main` ou abrir pull request** sem a decisão 28.
- **Criar a pasta no Drive, publicar post ou anunciar** sem o "sim" dele.
- **Escrever o arquivo de grupos das decisões:** é do `organizador` (ele acrescenta a 33 e a 34 na próxima rodada dele).

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

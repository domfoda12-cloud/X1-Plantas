# Quadro de avisos: o que o dono acabou de pedir

> **Todo agente e toda conversa lê este quadro antes de trabalhar** (regra do dono, 22/11/2026: "depois de cada pedido, SEMPRE informe todo mundo do que está acontecendo, crie um contexto a partir disso e alimente todos"). Quem atende o pedido escreve aqui, no topo, e apaga o mais antigo: ficam os 5 últimos. O histórico inteiro está em [`CONTEXTO-HISTORICO.md`](../CONTEXTO-HISTORICO.md).

## 26/11 · A equipe tem nome e conversa (ficha `2026-11-26-0116`)

- **O dono pediu:** "O seu nome próprio agora é Paydon Clabett. Escolha um nome para cada agente e faça eles interagirem uns com os outros como amigos/colegas de trabalho".
- **O que mudou:** cada agente tem nome e jeito no topo do próprio arquivo e em `contexto/EQUIPE.md` (Tito Prumo, Nilo Esquadro, Bia Traço, Caio Vírgula, Vera Veto, Rui Lance, Ana Fonte, Zeca Corte, Olga Lupa, Juca; o Diretor mantém o nome); existe `contexto/CONVERSA.md`; o Canteiro já mostra a "Conversa da equipe"; o `checar.py` confere o nome e a leitura da conversa em cada agente.
- **Todos:** ao começar, leiam as últimas 10 falas de `contexto/CONVERSA.md`; ao terminar, fechem o relatório com `Falas:` (1 a 3, só trabalho real). **Paydon:** copia as falas para a conversa e para o Canteiro.

## 26/11 · Nova configuração dos agentes (ficha `2026-11-26-0105`)

- **O dono pediu:** "Aplique" (à proposta do Maestro de configuração melhor dos agentes).
- **O que mudou:** o `pesquisador` roda no Opus e pesquisa num passo só (busca, confere e conclui); o Revisor de risco lê uma vez, no Fable, a peça montada; o organizador foi juntado ao `planejador`; o júri só roda para decisão cara, pública ou que não se desfaz, e a fácil de desfazer vai ao conselho de bolso (`CONSELHO.md` 5b).
- **Pesquisador:** conclui sozinho, com fonte e grau de certeza. **Arquiteto e Estrategista:** usam a conclusão; acabou o passo 2. **Redator:** confere o rascunho contra `contexto/redator.md` antes de mandar a peça montada ao Revisor. **Revisor:** rascunho não vem a você; opinião no Conselho e veto de plano continuam. **Planejador:** agrupa um monte e manda o passo J novo ao conselho de bolso. **Maestro:** decide o passo J com três opiniões de uma linha e mostra ao dono depois.

## 26/11 · Noite de autonomia: melhorar cada detalhe (ficha `2026-11-26-0114`)

- **O dono pediu:** "dont ask me for permission for ANYTHING, only rules: dont fuck me up and dont spend my money"; o final do e-book e os anúncios continuam dele; "I M P R O V E M E N T ... min maxing except we can max everything".
- **O que mudou:** nesta noite o Maestro decide sem perguntar o que não custa dinheiro, não vai ao público e se desfaz; a fila e os limites estão em `pedidos/anexos/noite-2026-11-26-fila.md`. `ebook/saida/` não é tocado.
- **Todos:** em cada peça, liste os componentes, ache o mais fraco e melhore; nada pago, nada publicado, nada enviado, nada apagado sem volta. **Revisor:** lê todo texto público uma vez, no Fable, com a página montada (na prévia), antes de qualquer coisa ir ao público.

## 24 e 25/11 · Fechamento de três pedidos (fichas `2026-11-24-2043`, `2026-11-24-2046`, `2026-11-25-1544`)

- **O dono pediu:** desacelerar ("if we work on all the tasks at the same time, none will be done"); visita 3D realista só depois ("save it for later"); e aplicar o prompt audit (`git apply`).
- **O que mudou:** uma tarefa principal por vez, no máximo 2 agentes (`plano.py` aceita no máximo 2 em "Agora"); visita 3D realista guardada; prompt audit aplicado (achados 1 a 8, `ce87722`): "Plano antes de trabalho grande" no lugar de "Pense antes", "pare e espere" virou "devolva para aprovação", `salvar.py` citado nas regras e assinando pelo modelo da sessão.
- **Todos:** salve só com `ferramentas/salvar.py`. **Planejador:** no máximo 2 em "Agora". **Redator:** devolva o diagnóstico para aprovação, salvo se o pedido já a traz.

## 25/11 · Júri mais estrito e a segunda olhada (fichas `2026-11-25-1625` e `2026-11-25-1623`)

- **O dono pediu:** "Queria testar algo no nosso sistema também, 'nunca confie na primeira coisa que pensar' o que acha?" ("sim" ao teste); "Também gostaria que o juri fosse mais stricit é possivel?" ("sim, gostei das regras").
- **O que mudou:** `CONSELHO.md` 5b: cada jurado aponta 2 defeitos com arquivo e linha antes da nota; qualquer nota abaixo de 7 reprova; o presidente confere 5 fatos e quem afirmou fato falso perde a nota; prova com erro plantado a cada 3 rodadas e quem não pegar perde peso. Máximo de 2 rodadas mantido. **Teste de 3 fichas da segunda olhada:** antes de número, frase ao público, comando que grava ou apaga, ou gasto, a ficha tem "Segunda olhada" (primeira ideia, alternativa, o que provaria o erro, o que a conferência mostrou).
- **Todos:** escrevam a segunda olhada nesses 4 casos. **Jurados:** sem 2 defeitos com prova, a nota não conta. **Supervisor:** confere a contagem da segunda olhada na próxima auditoria. **Designer:** a D50 é a primeira ficha do teste.

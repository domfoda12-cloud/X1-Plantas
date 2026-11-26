# Quadro de avisos: o que o dono acabou de pedir

> **Todo agente e toda conversa lê este quadro antes de trabalhar** (regra do dono, 22/11/2026: "depois de cada pedido, SEMPRE informe todo mundo do que está acontecendo, crie um contexto a partir disso e alimente todos"). Quem atende o pedido escreve aqui, no topo, e apaga o mais antigo: ficam os 5 últimos. O histórico inteiro está em [`CONTEXTO-HISTORICO.md`](../CONTEXTO-HISTORICO.md).

## 24 e 25/11 · Fechamento de três pedidos (fichas `2026-11-24-2043`, `2026-11-24-2046`, `2026-11-25-1544`)

- **O dono pediu:** desacelerar ("if we work on all the tasks at the same time, none will be done"); visita 3D realista só depois ("save it for later"); e aplicar o prompt audit (`git apply`).
- **O que mudou:** uma tarefa principal por vez, no máximo 2 agentes (`plano.py` aceita no máximo 2 em "Agora"); visita 3D realista guardada; prompt audit aplicado (achados 1 a 8, `ce87722`): "Plano antes de trabalho grande" no lugar de "Pense antes", "pare e espere" virou "devolva para aprovação", `salvar.py` citado nas regras e assinando pelo modelo da sessão.
- **Todos:** salve só com `ferramentas/salvar.py`. **Planejador:** no máximo 2 em "Agora". **Redator:** devolva o diagnóstico para aprovação, salvo se o pedido já a traz.

## 25/11 · Júri mais estrito e a segunda olhada (fichas `2026-11-25-1625` e `2026-11-25-1623`)

- **O dono pediu:** "Queria testar algo no nosso sistema também, 'nunca confie na primeira coisa que pensar' o que acha?" ("sim" ao teste); "Também gostaria que o juri fosse mais stricit é possivel?" ("sim, gostei das regras").
- **O que mudou:** `CONSELHO.md` 5b: cada jurado aponta 2 defeitos com arquivo e linha antes da nota; qualquer nota abaixo de 7 reprova; o presidente confere 5 fatos e quem afirmou fato falso perde a nota; prova com erro plantado a cada 3 rodadas e quem não pegar perde peso. Máximo de 2 rodadas mantido. **Teste de 3 fichas da segunda olhada:** antes de número, frase ao público, comando que grava ou apaga, ou gasto, a ficha tem "Segunda olhada" (primeira ideia, alternativa, o que provaria o erro, o que a conferência mostrou).
- **Todos:** escrevam a segunda olhada nesses 4 casos. **Jurados:** sem 2 defeitos com prova, a nota não conta. **Supervisor:** confere a contagem da segunda olhada na próxima auditoria. **Designer:** a D50 é a primeira ficha do teste.

## 25/11 · Identidade visual forte em tudo, antes do reset (ficha `2026-11-25-1613`)

- **O dono pediu:** "o pdf está sem identidade alguma, acredito que a ultima coisa importante a se fazer antes do reset é solidificar uma identidade e deixar ela presente em tudo que criamos. Nao estava feio, estava bonito organizado mas sem chamar atencao alguma, a pessoa vai ler aquilo em 2min vai parar. Nossa geracao é a geracao dopamina".
- **O que mudou:** a identidade é o D50, a única tarefa do "Agora". O Diretor (MinoAI Frontier) dá a ideia principal, o Designer faz o diagnóstico, 3 direções e as amostras (do nosso gerador, sem crédito pago), e o dono escolhe. Aplicar no gerador é o primeiro passo do reset, antes do "gera".
- **Todos:** nada que vá ao público sai sem a identidade escolhida. **Designer:** dono do D50 e do manual. **Redator:** as frases das páginas viram o gancho de cada página. **Editor de vídeo:** a identidade vale também para o que se move, depois do e-book.

## 25/11 · Tudo pronto para o reset; Instagram de IA com repositório próprio (ficha `2026-11-25-1612`)

- **O dono pediu:** "1 Vai ter" (repositório e conversa próprios para o Instagram de IA); "2. Só vai ter a resposta no reset"; "Ate o reset quero que deixe tudo absolutamente planejado preparado e clean para quando chegar no reset voce só ter que fazer o trabalho bracal".
- **O que mudou:** o roteiro do reset (`pedidos/anexos/roteiro-do-reset-2026-11-25.md`) tem a mensagem única ao dono e os passos em ordem; as frases das 5 páginas ficam prontas em rascunho para colar; o kit do Instagram de IA está em `pedidos/anexos/kit-instagram-ia-2026-11-25.md`; o D29 desceu do "Agora" para a fila.
- **Todos:** no reset, leia o roteiro e não releia o projeto. **Redator:** as 5 frases em rascunho. **Planejador:** a ordem do topo do `PLANO.md` segue o roteiro.

## 24/11 · O e-book mostra a dor e dá a solução (ficha `2026-11-24-2130`)

- **O dono pediu:** "No conteudo do pdf no geral quero saber mostrar a dor que o usuario tem ou teria, e dar a solucao pra ele".
- **O que mudou:** critério novo para todo o conteúdo do PDF: cada página faz o comprador sentir uma dor real dele, de forma indireta ("daquele jeitinho": cena, exemplo, detalhe que ele reconhece, nunca anunciada), e entrega a saída. Primeiro sai o mapa página por página; texto só muda depois de o dono ver.
- **Todos:** dor só da pesquisa do comprador ou dos dados da casa, nunca inventada nem com medo exagerado. **Planejador:** faz o mapa. **Redator:** reescreve só o que o dono marcar, com plano. **Designer:** o formato das páginas não muda sem pedido.

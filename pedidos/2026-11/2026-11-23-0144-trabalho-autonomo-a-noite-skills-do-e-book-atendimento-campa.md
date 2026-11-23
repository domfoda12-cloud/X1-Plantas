# Trabalho autônomo à noite: skills do e-book, atendimento, campanha de anúncio

**Estado:** aberta

**Prompt (palavra por palavra):** What really its your limit? I would like for the system to keep studying andi mproving afk now that im going to sleep, it can use all tokens as you want but what really its your limit? Can you add skills that are relevant for building the ebook, think of ways to improve the UI and costumer service, Create a ads campaign marketing. These are all examples that you can learn about, id really like if you were autosufficient

*Recado de 23/11 01:47:* Just stay awake 24h

**O que ele pediu, parte por parte:** 1) Qual é o meu limite de verdade. 2) O sistema seguir estudando e melhorando enquanto ele dorme, usando os tokens que quiser. 3) Exemplos: skills relevantes para construir o e-book; melhorar a interface e o atendimento ao cliente; criar uma campanha de anúncio. 4) Quer o sistema autossuficiente.

**Por que ele pediu, ou o que quer descobrir:** Quer que o tempo dele dormindo vire trabalho, e quer saber até onde pode confiar no sistema sozinho.

**Objetivo dele:** Um sistema que trabalha e melhora sem ele, e que de manhã tem coisas prontas para ele decidir.

**Ligação com as ideias gerais do projeto:** Fio 4 (não ser o gargalo; autonomia no fazer, confirmação no gastar e publicar), fio 6 (qualidade primeiro).

**Perguntas que me fiz:** Eu trabalho sozinho? Só quando algo me acorda: entre mensagens eu não rodo. Para trabalhar à noite, agendo mensagens que me acordam nesta conversa (tarefa agendada de hora em hora). O que posso fazer sem ele? Planejar, pesquisar, escrever, programar, testar e vetar; nada de gastar crédito, publicar, mandar mensagem, contratar ou decidir preço, título e nome (regras dele). Limites técnicos: o limite de uso da conta (semanal), o tamanho desta conversa (é resumida sozinha), o contêiner pode ser reiniciado (o trabalho fica salvo no git a cada passo).

**Pronto quando:** Fila da noite escrita; tarefa agendada criada; a cada acordar uma tarefa da fila, com plano vetado, `checar.py` e commit; de manhã um resumo para o dono com o que ficou pronto e o que espera o "sim" dele.

**Suposições (o dono não disse):** Que ele dorme umas 8 horas; acordar de hora em hora, até 8 vezes; nada pago nem publicado; tudo que é decisão dele vira opção para a manhã.

**Quem executa:** Maestro (Opus) conduz cada acordar; o time de cada assunto executa e veta; o Fable veta o plano da noite e audita no fim.

**Conferência:** (no fim)

**Resultado:** (a preencher)


## Fila da noite, versão 2 (depois do veto do Fable, 23/11, SIM, SE, 5/5)

Uma por acordar; cada uma com plano curto vetado pelo time antes de executar. Até 6 chamadas de agente por acordar. Na primeira chamada de cada agente, ele diz numa linha as ferramentas que vê (substitui o L1).

| # | Tarefa | Quem | Entrega | Estado |
|---|---|---|---|---|
| N1 | Veto do plano da noite | Fable | fila corrigida | **Feito:** SIM, SE com 6 correções, aplicadas aqui |
| E07 | **Proposta da E07 redesenhada** (ficha `1616`): quartos fora de fila, mantendo se possível 72 m², 3 quartos, 1 suíte, 2 banheiros e lote de 8 m; validador; prévia mobiliada; a E07 do e-book **intacta** | `arquiteto`; Maestro confere | proposta para o dono aprovar | |
| N3 | **Atendimento (funil do WhatsApp):** rever mensagens, objeções e planta grátis com as regras de hoje | `redator` e `estrategista`; `revisor-de-risco` | **arquivo de proposta** com antes e depois; `WHATSAPP.md` não muda | |
| N5 | **Campanha de anúncio (plano):** a partir de `ESTRATEGIA.md` seções 8, 10 e 11; público, ângulos, peças, opções de verba de teste, o que medir | `estrategista` com o Diretor; `redator`; `revisor-de-risco` | plano para o dono; sem número inventado; preço e título como campo pendente | |
| N4 | **Interface:** calculadora do parceiro e páginas do e-book (o que confunde o comprador) | `designer`; `arquiteto` confere números | arquivo de proposta; a calculadora e o PDF não mudam | |
| N2 | **Skills para o e-book, só no papel:** buscar, ler a licença inteira na página, Revisor; nada de clone, pip, npx ou binário | `pesquisador`; `designer` e `arquiteto` concluem; `revisor-de-risco` | lista para a manhã; skill nossa só como rascunho, sem ativar | |
| N6 | **Lições** das auditorias para os contextos (o "cortar repetido" sai: vira lista proposta, porque cortar é o que mais incomoda o dono) | Maestro | lições em dia | |
| N7 | Auditoria do Fable da noite e resumo da manhã (até 15 linhas, até 5 perguntas com opção e recomendação) | Fable; Maestro | resumo | |

**Regras da noite (Fable):** não tocar texto público (`WHATSAPP.md`, `calculadora-lote.html`, `ebook/config.json`, posts, PDF): tudo vira proposta; nada pago (OpenArt, TinyFish dataset, deep research ou automação, Meta Ads); nada instalado; número só com fonte e data; aviso de limite de uso: registrar e parar, sem adivinhar quando volta; falhou duas vezes, pula e anota; se a tarefa anterior ficou sem commit, o acordar continua nela; folga para tarefa que estourar a hora. Depois da fila: "Tempo livre" (`pedidos/PLANO.md`) até completar 24 horas.

**Perguntas para a manhã (suposições):** "UI" é a calculadora e as páginas do e-book? "Customer service" é o funil do parceiro no WhatsApp?

**Recado do dono (01:46): "Just stay awake 24h".** **Tarefa agendada:** "X1-Plantas: trabalho de 24 horas" (antes "da noite") (`trig_01JBJYsSkBLwfVLfmJyS1kvr`), de hora em hora no minuto 45 (UTC), a primeira às 02:45; acorda esta conversa e faz a próxima linha da fila; depois da fila, segue com o "Tempo livre" do `pedidos/PLANO.md` (alternando equipe e projeto) até 2026-11-24 01:45 UTC; então escreve o resumo das 24 horas e se apaga. Para se o dono escrever ou se aparecer aviso de limite de uso.

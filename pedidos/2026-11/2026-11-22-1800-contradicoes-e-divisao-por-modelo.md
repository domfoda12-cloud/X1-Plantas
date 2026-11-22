# Resolver as contradições e dividir o trabalho por modelo

**Estado:** fechada em 22/11/2026

**Prompt (palavra por palavra):** Veja o que esta contradizendo nos documentos, e crie uma solucao pras contradicoes baseado nos objetivos previamente dados, se a solucao for inutil para o projeto apenas delete. Agora quero que crie algo um pouco especial, eu gostaria que cada prompt meu fosse guardado em uma pasta do projeto, nessa pasta a partir de agora o fable ficara responsavel por ler o prompt e interpretalo, depois disso passa o trabalho para o opus. Tarefas mais chatas que seria um desperdicio de tokens, coloque o haiku para fazer, como organizar um evento, responder uma pergunta ou pesquisar algo que EU pedi para MIM nao para os outros agentes, para pesquisas mais afundas use o sonnet, por exemplo para o arquiteto adquirir conhecimento na web

**O que ele pediu, parte por parte:**
1. *"Veja o que está contradizendo nos documentos"*: partir da lista de `contexto/dono/TEXTOS-DESATUALIZADOS.md` (cerca de 60 itens).
2. *"crie uma solução baseada nos objetivos previamente dados"*: decidir cada contradição pelos objetivos do projeto, sem perguntar item por item: a alegria do comprador, honestidade (nada de promessa sem lastro), qualidade primeiro, e a regra mais recente do dono vence a antiga.
3. *"se a solução for inútil para o projeto apenas delete"*: documento ou trecho que já foi substituído e não serve a ninguém sai do repositório, em vez de ser remendado.
4. *"cada prompt meu guardado em uma pasta"*: guardar sozinho, sem depender de alguém lembrar: gancho que grava em `pedidos/entrada/`.
5. *"o Fable lê e interpreta, depois passa para o Opus"*: a conversa principal vira intérprete e conferente; a execução vai para agentes no Opus.
6. *"tarefas chatas… Haiku… que EU pedi para MIM"*: tarefa simples e pessoal do dono vai para um agente no Haiku; não é para trabalho do projeto.
7. *"pesquisas mais a fundo use o Sonnet"*: o agente `pesquisador` roda no Sonnet.

**Por que ele pediu, ou o que quer descobrir:** os documentos diziam coisas diferentes entre si, e os agentes repetiam a versão errada; e o modelo mais caro fazia trabalho que um mais barato faria.

**Objetivo dele:** um projeto que diz uma coisa só, e gastar o modelo caro em pensar, não em executar.

**Ligação com as ideias gerais do projeto:** continua o "os agentes esquecem": depois do índice e dos resumos, falta os documentos concordarem e o trabalho ter dono certo.

**Pronto quando:** `pedidos/LEIA-ME.md` explica o caminho; o gancho grava; cada agente tem modelo; as contradições estão resolvidas ou apagadas e a lista de desatualizados está vazia ou só com o que depende do dono; `checar.py` passa.

**Suposições (o dono não disse):** garantia de 7 dias e "12 ou 24 plantas" são decisão dele: os textos passam a dizer só o que existe e deixam o campo em aberto. A retirada do selo "Imagem ilustrativa" vale para vídeo; imagem parada do e-book mantém a legenda. Assunto pessoal não vira ficha no repositório.

**Quem executa:** montagem do sistema: Fable (é configuração, uma vez só). Contradições: quatro agentes no Opus, por área, e o `revisor-de-risco` (Opus) nos textos de venda.

**Conferência do Fable:** Rodei o `checar.py` depois de cada etapa (passa). Abri a página 2 da planta grátis da C01 gerada de novo: a vista da rua é a simplificada e a frase do banheiro está certa. Conferi o painel gerado contra os arquivos (24 de 35, 24 com 3D, 4 com foto antes de tirar a da C01). O Revisor de risco (Opus) leu os 7 textos de venda: vetou trechos em 5; o Redator (Opus) aplicou as 30 correções e eu conferi por busca que os trechos vetados sumiram e corrigi 5 trechos iguais que ficaram fora da lista. Testei o gancho com entrada falsa e ele já devolveu o lembrete nesta conversa; achei e corrigi a falha de guardar relatório de agente como prompt. Não conferi: cada edição dos três agentes de contradições, linha por linha (confiei nos relatórios e no `checar.py`); os textos de cada casa em `fichas/textos.py`; se o agente `ajudante` (Haiku) e o `model:` dos agentes são respeitados na prática, porque ainda não houve tarefa para eles depois da mudança.

**Resultado:** Contradições resolvidas por três agentes no Opus (e-book, vídeo/Instagram/3D, raiz/contexto/jurídico): textos pela regra mais recente, só prometem o que existe; decisões do dono em colchetes; apagados quatro documentos superados e 500 linhas de código morto; painel conta pelo que existe; foto antiga da C01 fora do e-book. Revisor vetou trechos em 5 de 7 textos de venda, corrigidos. Sistema de pedidos: gancho que guarda cada prompt, fichas com `ferramentas/pedido.py`, fila, pacote do executor, Fable como supervisor, Opus executa, Sonnet e Opus pesquisam, Haiku (`ajudante`) faz o simples e pessoal. O que sobrou: `contexto/dono/TEXTOS-DESATUALIZADOS.md`.


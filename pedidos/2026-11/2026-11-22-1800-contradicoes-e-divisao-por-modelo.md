# Resolver as contradições e dividir o trabalho por modelo

**Prompt (palavra por palavra):** Veja o que esta contradizendo nos documentos, e crie uma solucao pras contradicoes baseado nos objetivos previamente dados, se a solucao for inutil para o projeto apenas delete. Agora quero que crie algo um pouco especial, eu gostaria que cada prompt meu fosse guardado em uma pasta do projeto, nessa pasta a partir de agora o fable ficara responsavel por ler o prompt e interpretalo, depois disso passa o trabalho para o opus. Tarefas mais chatas que seria um desperdicio de tokens, coloque o haiku para fazer, como organizar um evento, responder uma pergunta ou pesquisar algo que EU pedi para MIM nao para os outros agentes, para pesquisas mais afundas use o sonnet, por exemplo para o arquiteto adquirir conhecimento na web

**O que ele pediu, parte por parte:**
1. *"Veja o que está contradizendo nos documentos"*: partir da lista de `contexto/dono/TEXTOS-DESATUALIZADOS.md` (cerca de 60 itens).
2. *"crie uma solução baseada nos objetivos previamente dados"*: decidir cada contradição pelos objetivos do projeto, sem perguntar item por item: a alegria do comprador, honestidade (nada de promessa sem lastro), qualidade primeiro, e a regra mais recente do dono vence a antiga.
3. *"se a solução for inútil para o projeto apenas delete"*: documento ou trecho que já foi substituído e não serve a ninguém sai do repositório, em vez de ser remendado.
4. *"cada prompt meu guardado em uma pasta"*: guardar sozinho, sem depender de alguém lembrar: gancho que grava em `pedidos/entrada/`.
5. *"o Fable lê e interpreta, depois passa para o Opus"*: a conversa principal vira intérprete e conferente; a execução vai para agentes no Opus.
6. *"tarefas chatas… Haiku… que EU pedi para MIM"*: tarefa simples e pessoal do dono vai para um agente no Haiku; não é para trabalho do projeto.
7. *"pesquisas mais a fundo use o Sonnet"*: o agente `pesquisador` roda no Sonnet.

**Pronto quando:** `pedidos/LEIA-ME.md` explica o caminho; o gancho grava; cada agente tem modelo; as contradições estão resolvidas ou apagadas e a lista de desatualizados está vazia ou só com o que depende do dono; `checar.py` passa.

**Suposições (o dono não disse):** garantia de 7 dias e "12 ou 24 plantas" são decisão dele: os textos passam a dizer só o que existe e deixam o campo em aberto. A retirada do selo "Imagem ilustrativa" vale para vídeo; imagem parada do e-book mantém a legenda. Assunto pessoal não vira ficha no repositório.

**Quem executa:** montagem do sistema: Fable (é configuração, uma vez só). Contradições: quatro agentes no Opus, por área, e o `revisor-de-risco` (Opus) nos textos de venda.

**Resultado:** (preenchido no fim)

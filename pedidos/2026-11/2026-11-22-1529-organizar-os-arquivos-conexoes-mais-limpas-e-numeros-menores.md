# Organizar os arquivos: conexões mais limpas e números menores

**Estado:** fechada em 22/11/2026

**Prompt (palavra por palavra):** Para a proxima sesssao pretendo organizar os arquivos melhor, atualmente tem milhares de codigos e arquivos conectados aos agentes, quero fazer essa conexao mais clean e com numeros menores

*Recado de 22/11 19:58:* 1 yes
2 im not sure, but id also like for you to check every connection that there is in main that you can sum up, fx 10 files are connected to the same 5 agents, they 10 files can all be together
Main seems like a huge mess i dont know what to do with it
3 i dont know what that means

*Recado de 22/11 20:00:* start it

*Recado de 22/11 20:37:* dont just fix things, mend it

**O que ele pediu, parte por parte:** "Para a próxima sessão": planejar agora, fazer depois. "Organizar os arquivos melhor": a estrutura de pastas e documentos. "Milhares de códigos e arquivos conectados aos agentes": o Graphify mostra 2.013 círculos e 2.231 ligações; os agentes leem muita coisa. "Conexão mais clean e com números menores": menos círculos, menos ligações, e as que ficarem fazendo sentido.

**Por que ele pediu, ou o que quer descobrir:** Ele abriu o Graphify e viu um emaranhado (o print de 22/11 mostra 2.177 círculos e a lista "mais conectados" com o `cena.js`, que já foi apagado). Quer enxergar o sistema e ter certeza de que os agentes não se perdem em arquivo demais.

**Objetivo dele:** Um projeto pequeno e legível: poucos documentos, cada um com função clara; código sem repetição; o Graphify mostrando as partes conversando.

**Ligação com as ideias gerais do projeto:** Fio 3 (nada se perde: juntar documentos guarda o conteúdo, só tira a repetição) e fio 8 (ele confere no Graphify).

**Perguntas que me fiz:** De onde vêm os números? Medido em 22/11: o código tem cerca de 500 funções e constantes (as maiores: `plantas.py` 64, `livro.py` 40, `casa3d.js` 33); o resto, perto de 1.500 círculos, sai dos 126 documentos .md, que o Graphify quebra em conceitos (cada documento gera uns 10). Ou seja: o que mais reduz é juntar documentos, não mexer no código. O mapa do sistema ajudou? Não: o Graphify não liga documento a código, criou 21 círculos soltos (medido). A limpeza das mídias ajudou? Sim: 2.177 → 2.013 círculos, 348 → 292 grupos. Juntar documento contraria o "não perder nada"? Não, se o conteúdo for junto; apagar só o que foi substituído. Qual número ele quer? Não sei: pergunto.

**Pronto quando:** Graphify (graph_stats) com menos da metade dos círculos de hoje, ou o número que o dono der; documentos de 126 para uns 40, sem conteúdo perdido; código repetido num lugar só; `INDICE.md`, `MAPA-DO-SISTEMA.md` e os `RESUMO.md` refeitos; `checar.py` passando.

**Suposições (o dono não disse):** Que "números menores" são os do Graphify (círculos e ligações). Que pode juntar documentos e apagar os que foram substituídos. Que é para a próxima sessão, não agora. Proposta de ordem: organizar antes de refazer, para refazer já na base limpa (perguntado).

**Quem executa:** Plano: Opus. Juntar documentos: agentes no Opus, um por pasta, cada um com a lista do que junta e para onde. Código comum: Opus. Conferência e medida antes e depois: Opus; auditoria do Fable no fim.

**Conferência:** etapa 1 (documentos), 22/11: 50 documentos viraram 12, cada antigo inteiro como seção (marcado `<!-- era: ... -->`); de 138 para 100 documentos .md. Todos os links do repositório abrem (conferido por script: 0 quebrados); as citações do dono em `video/VIDEO.md` conferidas uma a uma; `checar.py` sem erro. Ficaram separados de propósito os planos de peças diferentes e os arquivos junto de material (`video/principal-e07/`), para o agente não ler mais do que precisa. Etapa 2: código repetido medido (12 a 24 linhas nos `render-*.cjs`, uma linha de caminho por programa); juntar acrescentaria mais do que tira, ficou. Etapa 3: 5 contextos cortados para 3 resumos. Graphify na `main` (commit 1af9f47): 2.013 → 1.781 círculos, 2.231 → 2.012 ligações, 292 → 264 grupos; a meta de metade **não** foi atingida: o Graphify conta os conceitos de dentro dos documentos, e juntar guarda todo o conteúdo; a metade exige cortar o conteúdo repetido (tarefa 2.5b do `pedidos/PLANO.md`). O que impede de voltar: o `checar.py` agora confere todos os links e o máximo de 3 resumos por contexto (testado quebrando de propósito), e `pedido.py quadro` mantém o quadro no tamanho.

**Resultado:** 138 para 100 documentos (50 viraram 12), links e resumos conferidos pelo checar.py; Graphify 10% menor, metade fica para cortar conteúdo repetido (PLANO 2.5b)


## Plano (rascunho para a próxima sessão)

1. **Medir antes** (`graph_stats`): 2.013 círculos, 2.231 ligações, 292 grupos (22/11, depois da limpeza).
2. **Documentos, de 126 para uns 40** (o que mais pesa):
   - `contexto/entregas/`: 18 resumos de passagem viram um registro só, mais o `ULTIMO.md`.
   - `video/`: `VIDEO.md`, `VIDEO.md`, `ANUNCIO-LOCUCAO.md`, os planos e as referências viram 3 (regras e pedidos; plano da peça atual; referências).
   - `instagram/`: 6 viram 2 (plano do perfil; posts).
   - `ebook/referencias/`: 10 viram 4 (público e mercado; regras do Arquiteto; pesquisas; concorrentes).
   - Raiz: `PAINEL.md`, `ORCAMENTO.md`, `ESTRATEGIA.md` e `ECOSSISTEMA.md` revistos; o que repete o `CONTEXTO.md` sai.
   - `RESUMO.md`: só "O essencial" e a lista de nomes, sem repetir a descrição de cada documento.
3. **Código repetido num lugar só:** `RAIZ` e o caminho das pastas (14 cópias) num `ferramentas/comum.py`; o servidor e o Chromium dos 3 `render-*.cjs` num módulo só.
4. **Agentes leem menos:** cada `contexto/<papel>.md` aponta no máximo 3 resumos.
5. **Medir depois** e comparar; auditoria do Fable.


## Mapa de conexões (medido em 22/11, depois do recado)

Medido com um script: para cada documento, quais agentes o leem (arquivo do agente, `contexto/<agente>.md` e as listas do `ferramentas/resumos.py`). Hoje: **138 documentos .md**, 383 arquivos no total. Documentos que têm os mesmos leitores e a mesma função viram um só (o conteúdo vai junto; nada se perde):

| Grupo (quem lê) | Hoje | Proposta |
|---|---|---|
| `video/` (Diretor, Editor, Redator, Revisor) | 12 | 3: regras e pedidos do dono; a peça atual (plano, roteiro, prompts, anúncio); referências |
| `instagram/` (Designer, Diretor, Editor, Estrategista, Redator) | 6 | 2: o perfil (plano, calendário, MinoAI, Mino Lee); os posts |
| `ebook/referencias/` (Arquiteto, Estrategista, Pesquisador, Designer) | 9 | 3: apostila do Arquiteto; mercado e concorrentes; referência visual |
| `ebook/vendas/` (Estrategista, Redator, Revisor) | 5 | 2: atributos que vendem; WhatsApp (sequência, objeções, perguntas, material grátis) |
| `contexto/entregas/` | 19 | 3: um registro só, o `ULTIMO.md` e o modelo |
| `research_notes/` (ninguém lê, 34 mil caracteres) | 2 | 0: vão para `reports/`, junto do relatório que os usa |
| Raiz | 13 | 9: `ORCAMENTO` entra no `PAINEL`; `README` e `RESUMO-RAIZ` viram um; `MAESTRO` vai para `instagram/` |

Total: **de 138 para uns 75 documentos.** As palavras do dono (`PROMPTS.md`, `VIDEO.md`) continuam palavra por palavra, só mudam de lugar. Espera o "sim" do dono.

# X1-Plantas: instruções para toda sessão do Claude Code

E-book brasileiro de plantas de casas térreas (24 desenhadas, 35 no catálogo), vendido por Instagram e Facebook Ads com funil no WhatsApp. Público: quem tem o lote e vai construir com pedreiro, por etapas, classe C, 25 a 50 anos ([persona](ebook/referencias/persona-e-mercado.md)). Tudo em português do Brasil, preços em R$.

## Antes de tudo: o contexto

Leia [`CONTEXTO.md`](CONTEXTO.md): o resumo curto com o que nunca muda e o que está em aberto. O histórico completo, pedido por pedido, está em [`CONTEXTO-HISTORICO.md`](CONTEXTO-HISTORICO.md); abra só se precisar de um detalhe antigo. Tudo o que o dono pediu continua valendo até ele dizer o contrário. **A cada pedido novo do dono:** uma linha no fim do histórico (data, pedido, o que virou), a ficha em `pedidos/` e o "Em aberto" do `CONTEXTO.md` em dia. Nada do que ele faz é por acaso.

**Depois de cada pedido do dono, todos ficam sabendo** (regra do dono, 22/11/2026): quem atendeu escreve o aviso no topo de [`contexto/QUADRO.md`](contexto/QUADRO.md) (o que ele pediu, o que mudou, o que muda para cada papel) e atualiza o `contexto/<agente>.md` de quem foi afetado. **Todo agente e toda conversa lê o quadro antes de trabalhar.**

**Cada agente lê só o seu contexto** (`contexto/<agente>.md`), não o histórico inteiro; a web vai ao caderno `pesquisas/` (`ferramentas/pesquisa.py`). **Tarefa com mais de uns 30 arquivos em contexto é grande demais: divida no planejamento.** **Ao terminar uma tarefa, quem a conduziu escreve um resumo de passagem** em `contexto/entregas/` (modelo em `MODELO.md`, no máximo 15 linhas) e copia para `ULTIMO.md`; quem pega a próxima lê o `ULTIMO.md`, não a conversa.

**Cada prompt do dono vira ficha** (regra dele, 22/11/2026; [`pedidos/LEIA-ME.md`](pedidos/LEIA-ME.md)): o **Opus** responde, executa e confere; o **Fable** (`supervisor`) socorre quando ele trava ou erra e audita a cada 3 fichas; a pesquisa vai ao **Sonnet** e ao **Opus**; o **Haiku** (`ajudante`) faz o simples e pessoal do dono.

**Pense antes e pergunte sempre** (dono, 22/11): mais quanto maior o trabalho; pergunte a si mesmo (pedido, suposição, o que não sabe) e ao dono, sem travar ([`pedidos/LEIA-ME.md`](pedidos/LEIA-ME.md)).

## O objetivo: a alegria do comprador, que vira Pix

O comprador fica feliz quando acha a casa que cabe no lote dele, entende por quê e se sente seguro para construir. Comprador feliz manda o Pix, indica para o cunhado e volta para a próxima versão. Por isso toda tarefa responde a duas perguntas antes de começar: **isso deixa o comprador mais feliz com o que recebe?** e **isso aumenta a venda, baixa o custo ou reduz o risco?** Se a resposta for "não muda nada", a tarefa vai para o fim da fila. O número que manda é o **custo por venda** ([`PAINEL.md`](PAINEL.md), seção 4).

## Qualidade em primeiro lugar

**A prioridade é sempre a maior qualidade** (decisão do dono, 20/11/2026). Economia vale para rascunho, teste e retrabalho evitável, nunca para a peça final: imagem, vídeo, PDF e texto que vão ao público saem na melhor configuração disponível. Na dúvida, escolha o melhor.

## Uma coisa por vez

Termine uma frente antes de abrir outra (decisão do dono, 20/11/2026). Ordem: **e-book → animações → vídeo** ([`ORCAMENTO.md`](ORCAMENTO.md)). Dentro da frente, uma tarefa de cada vez, entregue e salva antes da próxima.

## O Conselho decide quais skills e ferramentas usar

Antes de usar uma skill, um agente ou uma ferramenta paga, os membros do Conselho que entendem do assunto dão opinião, e só se usa o que for aprovado. As regras completas estão em [`CONSELHO.md`](CONSELHO.md); o jeito de rodar é a skill `/conselho`.

- **O Maestro é a conversa principal (Opus): decide e rege. O Diretor, MinoAI Frontier, dá a ideia principal de todo conteúdo** e opina primeiro, com a fonte (22/11/2026). Equipe: [`contexto/EQUIPE.md`](contexto/EQUIPE.md).
- **Tarefa pequena** (um texto, um ajuste): conselho de bolso, até 3 membros, uma linha cada, sem subagente.
- **Entrega que vai ao público ou decisão que custa dinheiro**: conselho completo com os subagentes de `.claude/agents/`.
- **Revisor de risco tem veto** em tudo que toca honestidade e lei. **O dono decide** preço, título, gasto com anúncio, publicação e contratação.

## Ficha do pedido e reconferência

Toda entrega tem **uma ficha só**, em `pedidos/` ([`pedidos/LEIA-ME.md`](pedidos/LEIA-ME.md)): o que o dono pediu, por quê, o que é suposição e quem faz cada parte. Suposição nunca decide nada sem o dono confirmar; antes de cada etapa, reconfira os pedidos um por um ([`CONSELHO.md`](CONSELHO.md), seção 6b).

## Regras que não mudam

- Nunca dizer ou dar a entender que a planta dispensa pedreiro, engenheiro ou arquiteto; nunca prometer aprovação, prazo ou custo exato de obra ([`ESTRATEGIA.md`](ESTRATEGIA.md), seção 9).
- Só relatar números que uma ferramenta devolveu. Nunca estimar métrica de rede social.
- **Leia barato** (dono, 22/11/2026): ache a pasta no [`INDICE.md`](INDICE.md), leia o `RESUMO.md` dela e só abra o documento inteiro se precisar. Documento novo: `python3 ferramentas/resumos.py`; programa novo entra no [`MAPA-DO-SISTEMA.md`](MAPA-DO-SISTEMA.md). Graphify é só o mapa.
- Planta nova só entra se passar em `python3 ferramentas/plantas.py validar`.
- **Arquivo fica junto do que tem a mesma função** (dono, 22/11/2026): vídeo pronto em `video/saida/`, clipe em `video/broll/clipes/`. Pelo contexto, não pelo tamanho.
- **De vez em quando, e sempre antes de entregar:** `python3 ferramentas/checar.py` (código, plantas, 3D e painel). Erro achado é corrigido antes de seguir.
- Depois de mudar arquivos: `python3 ferramentas/atualizar-painel.py` com zero avisos, commit e push. **A `main` é a única branch de trabalho** (22/11/2026): toda conversa parte dela e volta para ela. Mudança grande de sistema vai numa branch `sistema/<assunto>` com pull request.
- Ferramentas pagas (TinyFish dataset e deep research, anúncios) só com o "sim" do dono.
- **Skill, agente, plugin ou conector novo alcança tudo antes do primeiro uso** (decisão do dono, 20/11/2026). Segue o roteiro de entrada do [`CONSELHO.md`](CONSELHO.md), seção 6: ler o que ele roda, passar pelo Conselho, registrar, ensinar o projeto, rodar uma vez sobre o que já existe. O inventário de tudo o que a operação pode usar, com o status de cada um, está em [`ECOSSISTEMA.md`](ECOSSISTEMA.md); compare com a lista da sessão no começo de cada sessão nova. O `checar.py` confere.

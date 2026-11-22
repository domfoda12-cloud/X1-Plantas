# X1-Plantas: instruções para toda sessão do Claude Code

E-book brasileiro de plantas de casas térreas (24 desenhadas, 35 no catálogo), vendido por Instagram e Facebook Ads com funil no WhatsApp. Público: quem tem o lote e vai construir com pedreiro, por etapas, classe C, 25 a 50 anos ([persona](ebook/referencias/persona-e-mercado.md)). Tudo em português do Brasil, preços em R$.

## Antes de tudo: o contexto

Leia [`CONTEXTO.md`](CONTEXTO.md): o resumo curto com o que nunca muda e o que está em aberto. O histórico completo, pedido por pedido, está em [`CONTEXTO-HISTORICO.md`](CONTEXTO-HISTORICO.md); abra só se precisar de um detalhe antigo. Tudo o que o dono pediu continua valendo até ele dizer o contrário. **A cada pedido novo do dono, acrescente uma linha no fim da tabela do histórico** (data, pedido, o que virou) e atualize "Em aberto" no `CONTEXTO.md`. Nada do que ele faz é por acaso.

**Cada agente lê só o seu contexto** (`contexto/<agente>.md`), não o histórico inteiro: contexto por papel desde o começo vale mais do que cortar depois. **Tarefa com mais de uns 30 arquivos em contexto é grande demais: divida no planejamento.** **Ao terminar uma tarefa, quem a conduziu escreve um resumo de passagem** em `contexto/entregas/` (modelo em `MODELO.md`, no máximo 15 linhas) e copia para `ULTIMO.md`; quem pega a próxima lê o `ULTIMO.md`, não a conversa.

## O objetivo: a alegria do comprador, que vira Pix

O comprador fica feliz quando acha a casa que cabe no lote dele, entende por quê e se sente seguro para construir. Comprador feliz manda o Pix, indica para o cunhado e volta para a próxima versão. Por isso toda tarefa responde a duas perguntas antes de começar: **isso deixa o comprador mais feliz com o que recebe?** e **isso aumenta a venda, baixa o custo ou reduz o risco?** Se a resposta for "não muda nada", a tarefa vai para o fim da fila. O número que manda é o **custo por venda** ([`PAINEL.md`](PAINEL.md), seção 4).

## Qualidade em primeiro lugar

**A prioridade é sempre a maior qualidade** (decisão do dono, 20/11/2026). Economia vale para rascunho, teste e retrabalho evitável, nunca para a peça final: imagem, vídeo, PDF e texto que vão ao público saem na melhor configuração disponível. Em dúvida entre mais barato e melhor, escolha melhor.

## Uma coisa por vez

Termine uma frente antes de abrir outra (decisão do dono, 20/11/2026). Ordem: **e-book → animações → vídeo** ([`ORCAMENTO.md`](ORCAMENTO.md)). Dentro da frente, uma tarefa de cada vez, entregue e salva antes da próxima.

## O Conselho decide quais skills e ferramentas usar

Antes de usar uma skill, um agente ou uma ferramenta paga, os membros do Conselho que entendem do assunto dão opinião, e só se usa o que for aprovado. As regras completas estão em [`CONSELHO.md`](CONSELHO.md); o jeito de rodar é a skill `/conselho`.

- **O Maestro, MinoAI Frontier, opina sempre e primeiro**, com base nas ferramentas da MinoAI (método e ganchos virais) e com a fonte. A opinião dele aparece para o dono em toda entrega.
- **Tarefa pequena** (um texto, um ajuste): conselho de bolso, uma linha de cada membro que importa, no máximo 3, sem abrir subagente.
- **Entrega que vai ao público ou decisão que custa dinheiro**: conselho completo com os subagentes de `.claude/agents/`.
- **Revisor de risco tem veto** em tudo que toca honestidade e lei. **O dono decide** preço, título, gasto com anúncio, publicação e contratação.

## Ficha do pedido e reconferência

Toda entrega tem uma **ficha do pedido** (`PEDIDO-*.md`): o que o dono pediu, o que é suposição e o que foi pedido a cada agente. Todo agente recebe a ficha; suposição nunca decide nada sem o dono confirmar; antes de cada etapa, reconfira os pedidos um por um ([`CONSELHO.md`](CONSELHO.md), seção 6b; decisão do dono, 22/11/2026).

## Regras que não mudam

- Nunca dizer ou dar a entender que a planta dispensa pedreiro, engenheiro ou arquiteto; nunca prometer aprovação, prazo ou custo exato de obra ([`ESTRATEGIA.md`](ESTRATEGIA.md), seção 9).
- Só relatar números que uma ferramenta devolveu. Nunca estimar métrica de rede social.
- Planta nova só entra se passar em `python3 ferramentas/plantas.py validar`.
- **De vez em quando, e sempre antes de entregar:** `python3 ferramentas/checar.py` (sintaxe de todo o código, validador das plantas, motor 3D e painel). Erro achado é corrigido antes de seguir.
- Depois de mudar arquivos: `python3 ferramentas/atualizar-painel.py` com zero avisos, commit e push na branch `planta-de-casas-anuncio`.
- Ferramentas pagas (TinyFish dataset e deep research, anúncios) só com o "sim" do dono.
- **Skill, agente, plugin ou conector novo alcança tudo antes do primeiro uso** (decisão do dono, 20/11/2026). Segue o roteiro de entrada do [`CONSELHO.md`](CONSELHO.md), seção 6: ler o que ele roda, passar pelo Conselho, registrar, ensinar o projeto, rodar uma vez sobre o que já existe. O inventário de tudo o que a operação pode usar, com o status de cada um, está em [`ECOSSISTEMA.md`](ECOSSISTEMA.md); compare com a lista da sessão no começo de cada sessão nova. O `checar.py` confere.

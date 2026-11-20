# X1-Plantas: instruções para toda sessão do Claude Code

E-book brasileiro de plantas de casas térreas (24 desenhadas, 35 no catálogo), vendido por Instagram e Facebook Ads com funil no WhatsApp. Público: quem tem o lote e vai construir com pedreiro, por etapas, classe C, 25 a 50 anos ([persona](ebook/referencias/persona-e-mercado.md)). Tudo em português do Brasil, preços em R$.

## Antes de tudo: o contexto

Leia [`CONTEXTO.md`](CONTEXTO.md). Ele guarda tudo o que o dono pediu e o que cada pedido quer dizer; tudo continua valendo até ele dizer o contrário. **A cada pedido novo do dono, acrescente uma linha na linha do tempo** (data, pedido, o que virou) e atualize a lista "Em aberto". Nada do que ele faz é por acaso.

## O objetivo: a alegria do comprador, que vira Pix

O comprador fica feliz quando acha a casa que cabe no lote dele, entende por quê e se sente seguro para construir. Comprador feliz manda o Pix, indica para o cunhado e volta para a próxima versão. Por isso toda tarefa responde a duas perguntas antes de começar: **isso deixa o comprador mais feliz com o que recebe?** e **isso aumenta a venda, baixa o custo ou reduz o risco?** Se a resposta for "não muda nada", a tarefa vai para o fim da fila. O número que manda é o **custo por venda** ([`PAINEL.md`](PAINEL.md), seção 4).

## Qualidade em primeiro lugar

**A prioridade é sempre a maior qualidade** (decisão do dono, 20/11/2026). Economia vale para rascunho, teste e retrabalho evitável, nunca para a peça final: imagem, vídeo, PDF e texto que vão ao público saem na melhor configuração disponível. Em dúvida entre mais barato e melhor, escolha melhor.

## O Conselho decide quais skills e ferramentas usar

Antes de usar uma skill, um agente ou uma ferramenta paga, os membros do Conselho que entendem do assunto dão opinião, e só se usa o que for aprovado. As regras completas estão em [`CONSELHO.md`](CONSELHO.md); o jeito de rodar é a skill `/conselho`.

- **O Maestro, MinoAI Frontier, opina sempre e primeiro**, com base nas ferramentas da MinoAI (método e ganchos virais) e com a fonte. A opinião dele aparece para o dono em toda entrega.
- **Tarefa pequena** (um texto, um ajuste): conselho de bolso, uma linha de cada membro que importa, no máximo 3, sem abrir subagente.
- **Entrega que vai ao público ou decisão que custa dinheiro**: conselho completo com os subagentes de `.claude/agents/`.
- **Revisor de risco tem veto** em tudo que toca honestidade e lei. **O dono decide** preço, título, gasto com anúncio, publicação e contratação.

## Regras que não mudam

- Nunca dizer ou dar a entender que a planta dispensa pedreiro, engenheiro ou arquiteto; nunca prometer aprovação, prazo ou custo exato de obra ([`ESTRATEGIA.md`](ESTRATEGIA.md), seção 9).
- Só relatar números que uma ferramenta devolveu. Nunca estimar métrica de rede social.
- Planta nova só entra se passar em `python3 ferramentas/plantas.py validar`.
- **De vez em quando, e sempre antes de entregar:** `python3 ferramentas/checar.py` (sintaxe de todo o código, validador das plantas, motor 3D e painel). Erro achado é corrigido antes de seguir.
- Depois de mudar arquivos: `python3 ferramentas/atualizar-painel.py` com zero avisos, commit e push na branch `planta-de-casas-anuncio`.
- Ferramentas pagas (TinyFish dataset e deep research, anúncios) só com o "sim" do dono.

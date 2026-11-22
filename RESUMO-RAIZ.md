# Resumo: Comando e contexto

> As regras, as decisões do dono e quem decide o quê. **Leia este resumo primeiro**; abra um documento inteiro só quando a tarefa pedir. Índice geral: [`INDICE.md`](INDICE.md). Quem lê: todos.

## O essencial

<!-- essencial: escrito à mão, o gerador não apaga -->
- Antes de trabalhar, leia `contexto/QUADRO.md` e o seu `contexto/<papel>.md`. Pedido do dono vira linha no `CONTEXTO-HISTORICO.md` e aviso no quadro (`CLAUDE.md`).
- Frentes, uma por vez: e-book → animações → vídeo. Peça final sempre na maior qualidade (`CLAUDE.md`).
- O Maestro (MinoAI Frontier) opina sempre e primeiro. O Revisor de risco veta por honestidade ou lei. O dono decide preço, título, bônus, anúncio, publicação e ferramenta paga (`CONSELHO.md`).
- Nunca dizer que a planta dispensa pedreiro, engenheiro ou arquiteto, nem prometer aprovação, prazo ou custo de obra (`CLAUDE.md`).
- Antes de entregar: `python3 ferramentas/checar.py` sem erro e `python3 ferramentas/atualizar-painel.py` com zero avisos. A `main` é a única branch; mudança de sistema vai em `sistema/<assunto>` (`CLAUDE.md`).
- Toda entrega tem ficha `PEDIDO-<entrega>.md`; suposição não decide etapa (`CONSELHO.md`).
- Em aberto com o dono: título, preço, bônus, 12 ou 24 plantas, quais casas refazer (`CONTEXTO.md`). R$ 67 é recomendação, não decisão (`ESTRATEGIA.md`).
- Contradição: OpenArt tem 115 créditos em 21/11/2026 (`ORCAMENTO.md`) e 21.137 (`contexto/QUADRO.md`).
- Contradição: 0 de 12 plantas prontas, 1 com 3D (`PAINEL.md`); e-book "quase pronto", 61 páginas e 24 casas (`ORCAMENTO.md`).
<!-- /essencial -->

## Os 12 documentos

### [X1-Plantas: instruções para toda sessão do Claude Code](CLAUDE.md)

E-book brasileiro de plantas de casas térreas (24 desenhadas, 35 no catálogo), vendido por Instagram e Facebook Ads com funil no WhatsApp. Público: quem tem o lote e vai construir com pedreiro, por etapas, classe C, 25 a 50 anos (persona). Tudo em português do Brasil, preços em R$.

Seções: Antes de tudo: o contexto; O objetivo: a alegria do comprador, que vira Pix; Qualidade em primeiro lugar; Uma coisa por vez; O Conselho decide quais skills e ferramentas usar; Ficha do pedido e reconferência; Regras que não mudam.

Tamanho: 974 palavras.

### [O Conselho: quem opina, quem decide e quais skills cada um usa](CONSELHO.md)

Lido por toda sessão via `CLAUDE.md`. Para rodar: a skill `conselho` (`/conselho <tarefa>`). Painel: `PAINEL.md`.

Seções: 1. Por que existe; 2. Os membros; 3. Como uma opinião é dada; 4. Como se decide; 5. Conselho de bolso x conselho completo; 6. Skill ou agente novo: o roteiro de entrada; 6b. Ficha do pedido e ciclo de reconferência (regra do dono, 22/11/2026); 7. Registro de decisões do Conselho.

Tamanho: 1494 palavras.

### [Histórico completo: a linha do tempo dos pedidos do dono](CONTEXTO-HISTORICO.md)

Só abra este arquivo quando precisar de um detalhe antigo ("o que ficou combinado sobre X?"). O resumo que todos leem é o `CONTEXTO.md`. Todo pedido novo do dono entra aqui, no fim da tabela, com a data e o que virou.

Seções: Linha do tempo dos pedidos.

Tamanho: 7029 palavras.

### [Contexto do projeto: tudo o que o dono pediu, e o que cada pedido quer dizer](CONTEXTO.md)

Resumo que todo mundo lê. Cada pedido do dono tem um motivo e continua valendo até ele dizer o contrário. O histórico completo, pedido por pedido, está em `CONTEXTO-HISTORICO.md`: abra só se precisar de um detalhe antigo. Cada agente lê também o seu arquivo em `contexto/`. Regra em `CLAUDE.md`.

Seções: O que nunca muda; Em aberto (esperando o dono); Ferramentas: o que cada uma é (e o que não é); Mapa: onde está cada coisa; Passagem entre tarefas.

Tamanho: 1238 palavras.

### [Ecossistema: tudo o que a operação pode usar, e se já alcançou o projeto](ECOSSISTEMA.md)

Pedido do dono (20/11/2026): "toda skill nova alcança tudo" e "confira se todos, não só o Ponytail, passaram pelas instruções iniciais". O roteiro de entrada está no `CONSELHO.md`, seção 6. Aqui fica o inventário: o que existe, quem usa, o que faz por fora do projeto e em que pé está. Status: -…

Seções: 1. Como as instruções chegam a cada um; 2. Do projeto (no repositório); 3. Conectores (serviços externos); 4. Skills de plugin e do Claude Code; 5. Texto de entrada (para plugin, conector ou agente que abre sessão própria); 6. Frameworks de agentes de fora; 7. Como manter este inventário.

Tamanho: 1956 palavras.

### [Estratégia de marketing: público, produto e oferta](ESTRATEGIA.md)

Para quem vamos vender, o que essa pessoa quer, como ela fala e o que oferecer. Leia antes de escrever qualquer anúncio, legenda, mensagem ou página do e-book. Painel geral: `PAINEL.md`.

Seções: 1. Em cinco linhas; 2. O que os dados dizem; 3. Quem compra: três perfis; 4. Posicionamento; 5. Os três diferenciais (repetir em tudo); 6. O que isso muda no produto; 7. A oferta; 8. Ângulos de anúncio; 9. Tom de voz; 10. Calendário do lançamento; 11. O que medir para saber se a estratégia está certa.

Tamanho: 1996 palavras.

### [Maestro: MinoAI Frontier](MAESTRO.md)

A MinoAI Frontier rege a operação. Ela trabalha no seu computador, no app do Claude (aba Code), com este repositório aberto. Conduz a semana pelo painel, cuida de tudo o que é vídeo e rede social e manda fazer o resto. Você decide e aprova. Ela organiza, produz, mede e avisa.

Seções: 1. O que o maestro faz; 2. Configuração (uma vez só); 3. A mensagem de abertura do maestro; 4. Rotina da semana; 5. Primeira tarefa do maestro.

Tamanho: 1137 palavras.

### [Orçamento: limite semanal do Claude e créditos do OpenArt](ORCAMENTO.md)

Pedido do dono (20/11/2026): dividir o que resta entre as três partes que faltam: e-book, animações e vídeo. Ver também `CONTEXTO.md` e `PAINEL.md`.

Seções: O que dá para medir daqui; A divisão (qualidade em primeiro lugar); Como gastar menos sem perder qualidade; Para fechar a conta em números.

Tamanho: 560 palavras.

### [Painel X1-Plantas](PAINEL.md)

Comece por aqui. Este é o centro de controle do projeto: o que estamos construindo, como o dinheiro entra, em que fase estamos, o que fazer esta semana e o que decidir. Quem rege é a MinoAI Frontier, o maestro: no seu computador, ela conduz a semana por este painel, faz o que é vídeo e rede social…

Seções: 1. Situação agora; 2. O negócio em uma frase; 3. Estratégia do e-book: lançar cedo e crescer em levas; 4. A conta que diz se o anúncio paga; 5. Fases; 6. Esta semana; 7. Números para acompanhar; 8. Decisões tomadas; 9. Decisões pendentes; 10. Riscos e cuidados; 11. Rotina; 12. Quem faz o quê; 13. Mapa do projeto.

Tamanho: 2914 palavras.

### [X1-Plantas](README.md)

E-book com dezenas de plantas de casas para quem vai construir no Brasil, com vídeos de anúncio, perfil no Instagram e plantas em 3D.

Tamanho: 120 palavras.

### [Resumo: Comando e contexto](RESUMO-RAIZ.md)

As regras, as decisões do dono e quem decide o quê. Leia este resumo primeiro; abra um documento inteiro só quando a tarefa pedir. Índice geral: `INDICE.md`. Quem lê: todos.

Seções: O essencial; Os 12 documentos.

Tamanho: 1173 palavras.

### [Ferramentas: regras desta pasta](ferramentas/CLAUDE.md)

O Claude Code carrega este arquivo sozinho quando trabalha aqui. As regras gerais estão no `CLAUDE.md` da raiz.

Tamanho: 166 palavras.

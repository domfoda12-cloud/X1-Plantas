# Resumo: Comando e contexto

> As regras, as decisões do dono e quem decide o quê. **Leia este resumo primeiro**; abra um documento inteiro só quando a tarefa pedir. Índice geral: [`INDICE.md`](INDICE.md). Quem lê: todos.

## O essencial

<!-- essencial: escrito à mão, o gerador não apaga -->
- Antes de trabalhar, leia `contexto/QUADRO.md` e o seu `contexto/<papel>.md`. Pedido do dono vira linha no `CONTEXTO-HISTORICO.md` e aviso no quadro (`CLAUDE.md`).
- Cada pedido do dono vira ficha em `pedidos/`; a conversa principal interpreta e confere, Opus executa e pesquisa (`pesquisador`, um passo só), Haiku faz a tarefa pessoal do dono (`ajudante`) (`pedidos/LEIA-ME.md`, `ECOSSISTEMA.md`).
- Frentes, uma por vez: e-book → animações → vídeo; a de vídeo foi aberta pelo dono em 21/11. Peça final sempre na maior qualidade (`CLAUDE.md`, `PAINEL.md`).
- O Maestro é a conversa principal (Opus): decide e rege a equipe. O Diretor, MinoAI Frontier, dá a ideia principal de todo conteúdo e opina primeiro nele. O Revisor de risco veta por honestidade ou lei. O dono decide preço, título, bônus, anúncio, publicação e ferramenta paga (`CONSELHO.md`).
- Nunca dizer que a planta dispensa pedreiro, engenheiro ou arquiteto, nem prometer aprovação, prazo ou custo de obra (`CLAUDE.md`).
- Antes de entregar: `python3 ferramentas/checar.py` sem erro e `python3 ferramentas/atualizar-painel.py` com zero avisos. A `main` é a única branch; mudança de sistema vai em `sistema/<assunto>` (`CLAUDE.md`, `instagram/MINOAI-FRONTIER.md` (seção "Maestro e Diretor: a sessão do Claude no seu computador, com a MinoAI Frontier")).
- 24 casas desenhadas e no PDF (rascunho 1), cada uma com imagem 3D; a C01 foi redesenhada. A "Situação agora" do painel conta pelo catálogo, que está atrasado: vale a seção 2 (`PAINEL.md`).
- Em aberto com o dono: título, preço, garantia, bônus, 12 ou 24 plantas, quais casas refazer. R$ 67 e 7 dias são recomendação, não decisão (`CONTEXTO.md`, `ESTRATEGIA.md`, seção 7).
- OpenArt: 21.137 créditos em 22/11/2026, plano Pro; cada uso pede o "sim" do dono (`ORCAMENTO.md`). Selo "Imagem ilustrativa": saiu dos vídeos, continua em imagem parada (`ECOSSISTEMA.md`).
- Público: 25 a 50 anos, quem constrói com pedreiro, por etapas (`CLAUDE.md`, `ESTRATEGIA.md`).
<!-- /essencial -->

## Os 12 documentos

### [X1-Plantas: instruções para toda sessão do Claude Code](CLAUDE.md)

E-book brasileiro de plantas de casas térreas (24 desenhadas, 35 no catálogo), vendido por Instagram e Facebook Ads com funil no WhatsApp. Público: quem tem o lote e vai construir com pedreiro, por etapas, classe C, 25 a 50 anos (persona). Tudo em português do Brasil, preços em R$.

Seções: Antes de tudo: o contexto; O objetivo: a alegria do comprador, que vira Pix; Qualidade em primeiro lugar; Uma coisa por vez; O Conselho decide quais skills e ferramentas usar; Ficha do pedido e reconferência; Regras que não mudam.

Tamanho: 1008 palavras.

### [O Conselho: quem opina, quem decide e quais skills cada um usa](CONSELHO.md)

Lido por toda sessão via `CLAUDE.md`. Para rodar: a skill `conselho` (`/conselho <tarefa>`). Painel: `PAINEL.md`.

Seções: 1. Por que existe; 2. Os membros; 3. Como uma opinião é dada; 4. Como se decide; 5. Conselho de bolso x conselho completo; 5b. Modo júri (método do llm-council, 23/11/2026); 6. Skill ou agente novo: o roteiro de entrada; 6b. Ficha do pedido e ciclo de reconferência (regra do dono, 22/11/2026); 7. Registro de decisões do Conselho.

Tamanho: 3942 palavras.

### [Histórico completo: a linha do tempo dos pedidos do dono](CONTEXTO-HISTORICO.md)

Só abra este arquivo quando precisar de um detalhe antigo ("o que ficou combinado sobre X?"). O resumo que todos leem é o `CONTEXTO.md`. Todo pedido novo do dono entra aqui, no fim da tabela, com a data e o que virou.

Seções: Linha do tempo dos pedidos.

Tamanho: 9380 palavras.

### [Contexto do projeto: tudo o que o dono pediu, e o que cada pedido quer dizer](CONTEXTO.md)

Resumo que todo mundo lê. Cada pedido do dono tem um motivo e continua valendo até ele dizer o contrário. O histórico completo, pedido por pedido, está em `CONTEXTO-HISTORICO.md`: abra só se precisar de um detalhe antigo. Antes de trabalhar, todos leem o quadro e o seu arquivo em `contexto/`. Regra…

Seções: O que nunca muda; Em aberto (esperando o dono); Ferramentas: o que cada uma é (e o que não é); Mapa: onde está cada coisa; Passagem entre tarefas.

Tamanho: 1493 palavras.

### [Ecossistema: tudo o que a operação pode usar, e se já alcançou o projeto](ECOSSISTEMA.md)

Pedido do dono (20/11/2026): "toda skill nova alcança tudo" e "confira se todos, não só o Ponytail, passaram pelas instruções iniciais". O roteiro de entrada está no `CONSELHO.md`, seção 6. Aqui fica o inventário: o que existe, quem usa, o que faz por fora do projeto e em que pé está. Status: -…

Seções: 1. Como as instruções chegam a cada um; 2. Do projeto (no repositório); 2b. Que skill e ferramenta está ligada a cada agente; 3. Conectores (serviços externos); 4. Skills de plugin e do Claude Code; 5. Texto de entrada (para plugin, conector ou agente que abre sessão própria); 6. Frameworks de agentes de fora; 7. Como manter este inventário.

Tamanho: 3387 palavras.

### [Estratégia de marketing: público, produto e oferta](ESTRATEGIA.md)

Para quem vamos vender, o que essa pessoa quer, como ela fala e o que oferecer. Leia antes de escrever qualquer anúncio, legenda, mensagem ou página do e-book. Painel geral: `PAINEL.md`.

Seções: 1. Em cinco linhas; 2. O que os dados dizem; 3. Quem compra: três perfis; 4. Posicionamento; 5. Os três diferenciais (repetir em tudo); 6. O que isso muda no produto; 7. A oferta; 8. Ângulos de anúncio; 9. Tom de voz; 10. Calendário do lançamento; 11. O que medir para saber se a estratégia está certa.

Tamanho: 2745 palavras.

### [Mapa do sistema: como uma parte alimenta a outra](MAPA-DO-SISTEMA.md)

Em 22/11/2026 os vídeos, clipes e renders antigos foram apagados para refazer do zero (ficam no histórico do git); as pastas de saída abaixo voltam a encher quando os programas rodarem. Uma página para ver o projeto como um sistema: a planta entra, vira dados, e dos dados saem o PDF, o 3D, as…

Seções: 1. A planta: de onde tudo sai; 2. O e-book; 3. O 3D e as imagens; 4. O vídeo; 5. A conferência e a organização; 6. As pessoas e as regras em volta.

Tamanho: 1281 palavras.

### [Orçamento: limite semanal do Claude e créditos do OpenArt](ORCAMENTO.md)

Pedido do dono (20/11/2026): dividir o que resta entre as três partes que faltam: e-book, animações e vídeo. O que espera o dono está em `CONTEXTO.md`, "Em aberto".

Seções: OpenArt; Limite semanal do Claude.

Tamanho: 214 palavras.

### [Painel X1-Plantas](PAINEL.md)

Comece por aqui. Este é o centro de controle do projeto: o que estamos construindo, como o dinheiro entra, em que frente estamos, o que fazer esta semana e o que decidir. Quem rege é o Maestro, a sessão do Claude no seu computador: conduz a semana por este painel e decide; a MinoAI Frontier, o…

Seções: 1. Situação agora; 2. Em que pé está (escrito à mão, 22/11/2026); 3. O negócio em uma frase; 4. A conta que diz se o anúncio paga; 5. Frentes, uma por vez; 6. Esta semana; 7. Números para acompanhar; 8. Decisões tomadas; 9. Decisões pendentes; 10. Riscos e cuidados; 11. Rotina; 12. Quem faz o quê; 13. Mapa do projeto.

Tamanho: 2603 palavras.

### [X1-Plantas](README.md)

E-book com dezenas de plantas de casas para quem vai construir no Brasil, com vídeos de anúncio, perfil no Instagram e plantas em 3D.

Tamanho: 157 palavras.

### [Resumo: Comando e contexto](RESUMO-RAIZ.md)

As regras, as decisões do dono e quem decide o quê. Leia este resumo primeiro; abra um documento inteiro só quando a tarefa pedir. Índice geral: `INDICE.md`. Quem lê: todos.

Seções: O essencial; Os 12 documentos.

Tamanho: 1309 palavras.

### [Ferramentas: regras desta pasta](ferramentas/CLAUDE.md)

O Claude Code carrega este arquivo sozinho quando trabalha aqui. As regras gerais estão no `CLAUDE.md` da raiz.

Tamanho: 166 palavras.

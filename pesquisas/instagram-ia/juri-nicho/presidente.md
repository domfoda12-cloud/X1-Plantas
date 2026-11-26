# Júri do nicho: PRESIDENTE (síntese da rodada 1)

26/11/2026. Presidente: Fable 5.2, não opinou nesta rodada. Método: `CONSELHO.md`, seção 5b. Li os três pareceres desta pasta, `../estudo-science-in-8bit.md`, `../referencia-math-phonk.md`, `../ferramentas-gratis-animacao.md` e `../prototipo/`. Nenhum número de alcance aqui é meu: todos estão nos arquivos citados.

**Resultado em uma frase:** o júri aponta a **ideia 6, "Matemática do mundo real"**, em estilo e som próprios, mas **nenhuma ideia chegou a 8,5**. A 6 ficou em 7,3 como foi avaliada e em 8,0 na versão sem pixel art. Falta provar o gancho e o som, e isso se prova com três testes de produção, não com mais opinião.

## 1. Fatos conferidos no repositório (13; a regra pede 5)

| # | O que o jurado afirmou | Quem | Conferência |
|---|---|---|---|
| 1 | O protótipo fez 90 quadros 1080x1920 em 1,4 s, com Pillow e ffmpeg, e saiu sem áudio | Produção | **Confirmado, e medi de novo.** `ffprobe` em `prototipo/reel-teste.mp4`: um só fluxo (h264, 1080x1920, 90 quadros, 3,0 s), nenhum de áudio. Rodei `reel_pixel.py` para a pasta temporária: 90 quadros em 1,5 s, 40 KB. Pillow 12.3.0 e ffmpeg 6.1.1 estão na máquina |
| 2 | "Knuckle crack" tem 210.572 curtidas | Alcance, Produção | **Confirmado** no estudo, linha 59 (o jurado citou a 60) |
| 3 | 89% das views vêm de quem não segue | Alcance | **Confirmado**, linha 36, autodeclarado pela conta (o jurado citou a 37, que é a dos 125 posts) |
| 4 | Gancho no corpo em 3 de 3 reels; reels recentes com 745 e 6.676 views | os três | **Confirmado**: linhas 47, 68, 75, 76, 82 e 113 |
| 5 | A busca de concorrência em português não cobriu "corpo" | Alcance | **Confirmado**: linhas 158 a 162 só cobrem as ideias 1, 2 e 4. Vale também para 6, 7 e 8: ninguém pesquisou |
| 6 | O Instagram sugere @matharium como vizinho da conta estudada | Risco | **Confirmado**: linhas 13 e 100. O estilo dele não foi conferido (o jurado avisou) |
| 7 | Rótulo "AI info" entra por sinal técnico ou autodeclaração, é rótulo e não remoção; "perfil gerado por IA" só aparece em agregador | Risco | **Confirmado**: linhas 153 a 156 e 106 |
| 8 | Sintetizador em numpy é "ideia, não pesquisado"; Press Start 2P tem acentos a confirmar; vozes Piper CC0 só por fonte secundária | Produção | **Confirmado**: `ferramentas-gratis-animacao.md`, linhas 16, 19 e 21 |
| 9 | A referência tem 107.118 curtidas e a ferramenta apontou "8 rodadas iguais cansam" e "tela inicial lotada de fórmula" | Produção | **Números confirmados** (`referencia-math-phonk.md`, linhas 5 e 9) |
| 10 | A referência "dá prova de alcance" para a ideia 6 | Produção | **Não confirmado como prova.** É um post só, a ferramenta devolveu curtidas (não views), e o formato é um jogo de adivinhar com som, não "a conta escondida no dia a dia". Gosto do dono também não é prova de venda |
| 11 | "Eles trocam de estilo (vetor, papel, lousa, blueprint, neon; seção 3)" | Produção | **Não confirmado como escrito.** A linha 30 lista estilos que o *aplicativo que eles vendem* suporta; a linha 115 diz que a conta tem marca "única e consistente (pixel + chiptune)" |
| 12 | "3 fontes revisadas por pares (como eles fazem, seção 4)" | Risco | **Em parte.** A linha 78 diz "fontes científicas (3 por post)". Um reel cita 3 artigos de revista (linha 63); outro cita OpenStax e Cleveland Clinic (linha 52), que não são revisão por pares |
| 13 | A ideia 6 é "conta animada em pixel art" | Risco | **Não confirmado como proposta.** O estudo define o motor "em estilo visual PRÓPRIO (não pixel)" (linha 132) e o jurado de alcance descreve a 6 sem pixel. Só o protótipo é pixel. Não vi o pedido que o jurado recebeu |

Também conferido: `ESTRATEGIA.md`, seção 9 (linhas 116 e 117), sustenta a regra que o jurado de risco cita para medida de obra. A frase "confirme com o engenheiro" não está lá ao pé da letra; a regra está.

**Alguém perde a nota?** Não tirei nenhuma. Os itens 10, 11 e 12 são frases que vão além da fonte, mas nenhuma nota se apoia só nelas, e o repositório não mostra o contrário do que sustenta cada nota. Se o Maestro ler a regra do 5b ao pé da letra para o item 11, cai a nota do jurado de produção e a ideia 6 fica em 6,5 (com pixel) ou 7,5 (sem pixel), com dois jurados. A conclusão é a mesma nos dois casos: ninguém chega a 8,5.

**Falhas de método desta rodada** (para a rodada 2 não repetir):
- Não aparece régua com âncoras de 3, 6 e 9 em nenhum parecer (5b, passo 0). As notas medem ângulos diferentes sem escala comum.
- Só o jurado de alcance citou arquivo e linha. Risco e produção citaram seção (5b, passo 1 pede linha).
- Não há arquivo da revisão anônima (5b, passo 2).
- Numeração trocada: o "7" do jurado de risco é "De onde vem essa palavra"; o "7" dos outros dois é "Teste em casa". Abaixo uso a numeração do jurado de produção.
- As ideias 7 e 8 só têm duas notas cada.

## 2. Notas por ideia

| # | Ideia | Alcance | Risco | Produção | Média | Passa no piso (ninguém abaixo de 7)? |
|---|---|---|---|---|---|---|
| 1 | Dinheiro de casa em números | 6 | 6 | 7 | 6,3 | Não |
| 2 | Direitos em 40 segundos | 5 | 3 | 3 | 3,7 | Não |
| 3 | Seu corpo, hoje | 8 | 2 | 4 | 4,7 | Não |
| 4 | A física da cozinha | 7 | 5 | 6 | 6,0 | Não |
| 5 | História do bairro/cidade | 4 | 6 | 3 | 4,3 | Não |
| 6 | Matemática do mundo real, **como o risco avaliou (em pixel art)** | 7 | 6 | 9 | **7,3** | Não (risco 6) |
| 6 | Matemática do mundo real, **sem pixel art** (nota condicional que o próprio jurado de risco declarou) | 7 | 8 | 9 | **8,0** | Sim (7, 8, 9) |
| 7 | Teste em casa (proposta do jurado de alcance) | 8 | não avaliou | 6 | 7,0 (2 notas) | Não (produção 6) |
| 8 | De onde vem essa palavra (proposta do jurado de risco) | não avaliou | 8 | 6 | 7,0 (2 notas) | Não (produção 6) |

Leitura das notas:
- A 3 é a melhor para alcance (8) e a pior para risco (2): é o nicho deles traduzido, e saúde errada fere. Está fora.
- A 6 é a única em que nenhum jurado ficou abaixo de 7, e só na versão sem pixel.
- A 7 e a 8 empatam em 7,0, mas com dois jurados cada. A 7 nunca passou pelo risco e a 8 nunca passou pelo alcance. Não dá para compará-las com a 6.
- O 9 do jurado de produção é a nota mais alta da rodada e se apoia em duas coisas que ainda não existem: o som que carrega a conta (o protótipo não tem áudio) e a variação que não cansa. O próprio jurado diz isso.

## 3. Síntese: o que o júri recomenda

**Nicho: "Matemática do mundo real"** (a conta escondida no dia a dia), como espinha. Com duas peças emprestadas, sugeridas pelo jurado de produção: o gatilho da ideia 7 (o espectador dá o palpite antes da resposta e comenta o placar) e temas da ideia 1 como rodada (a conta dentro da conta de luz), não como nicho.

Por que ela: a conta se refaz por código, então a conferência é a mais barata de todas (risco e produção concordam, sem se verem); linha, grade e número são o que sai mais barato em código; e a pauta não acaba.

O ponto fraco, dito pelo jurado de alcance: **não tem ação no corpo no frame 0**, que é a única coisa que o estudo mostra em 3 de 3 reels, e conta passo a passo é texto na tela, que o estudo já aponta como risco de retenção (linha 64). Ninguém tem prova de que matemática alcança em português.

**Condições que os três puseram** (sem elas a recomendação não vale):
1. **Verificador de fatos** que não é quem escreveu: um script que refaz cada conta e trava antes de renderizar, mais a fonte aberta (não lembrada) e a data da consulta para cada dado de entrada (preço, taxa, medida).
2. **Fonte na legenda** de todo post; "não se sabe" quando não se sabe.
3. **Declaração de IA** na bio, por conta própria. Esconder e ser descoberto custa mais que o rótulo.
4. **Estilo e som próprios**: desenho em código, som gerado pelo projeto, nenhum roteiro, tema ou paleta adaptado da conta estudada.
5. **Longe do pixel 8 bits deles**: pixel e chiptune são a marca deles. O protótipo atual é pixel; dele só se aproveita o caminho (quadros para o ffmpeg), não o visual.
6. **Revisor de risco com veto por filme.** Núcleo seguro: pizza, desconto, porcentagem. Juros do cartão só com taxa do Banco Central e data na tela. Mega-Sena só como "por que quase ninguém ganha", com a probabilidade oficial da Caixa e sem chamada para apostar. Rampa e qualquer medida de obra só citando a norma e mandando confirmar com o engenheiro, ou ficam de fora até a norma ser aberta.
7. **Antes de decidir** (jurado de risco): conferir o estilo de @matharium e buscar a concorrência de matemática em português. Nada disso foi pesquisado.

Observação do presidente, não do júri: a condição "estilo e som próprios" tem de valer também para a referência do dono. O fundo de osciloscópio e o jogo "cartucho LIVE ou BLANK" são a marca daquela conta. O que se leva dela são os quatro princípios da linha 10 do arquivo (o espectador joga junto, o som carrega a informação, a regra clara no primeiro segundo, ritmo que varia), não o visual nem o jogo.

**Quem decide o nicho é o dono.** Ele gosta de matemática e isso conta para o projeto ser dele, mas não entrou em nenhuma nota como prova.

## 4. Chegou a 8,5?

**Não.** A melhor é a ideia 6: 7,3 como foi avaliada, 8,0 sem pixel. Para 8,5 com três jurados a soma tem de ser 26; hoje é 24. Faltam dois pontos, e eles estão em dois lugares:

- **Alcance (7):** falta o gancho. A proposta precisa de um frame 0 em que o espectador faz algo na hora (o palpite: "uma grande ou duas médias? decide agora"), com a regra escrita na tela no primeiro segundo, uma linha curta por tela, a conta mostrada por desenho (a área crescendo) em vez de fórmula, e o som dando a resposta. Isso só se julga vendo o filme pronto, não a ideia no papel.
- **Risco (8, condicional):** falta existir o que hoje é promessa: o script verificador pegando uma conta errada plantada, a lista de temas proibidos escrita, o texto da bio, o estilo de @matharium e a concorrência em português conferidos.
- **Produção (9):** a nota só se sustenta se o teste de som e o teste de variação derem certo. Se o som não carregar a conta, ela cai.

O que **não** resolve: pedir aos mesmos jurados uma nota nova sobre o mesmo texto. A regra dá mais uma rodada só (máximo de 2). A rodada 2 deve julgar os **3 reels piloto** do teste 3, com régua escrita, os três jurados avaliando a mesma lista (a 6 reescrita, e a 7 e a 8 completas se o dono quiser mantê-las na disputa) e citando arquivo e linha. Se não der 8,5, vai ao dono com as duas notas.

Limite honesto: prova de alcance de verdade só existe postando. O jurado de alcance sugere 10 a 15 filmes e olhar as views que a ferramenta devolver. Postar é decisão do dono.

## 5. Os 3 testes de produção, em ordem

Todos grátis, com o que já está na máquina, sem postar nada.

1. **Som que carrega a conta.** Gerar o som em Python com numpy (numpy 2.5.3 está na máquina) e juntar ao vídeo com ffmpeg. Passa se: o `ffprobe` mostrar o fluxo de áudio; uma pessoa de olhos fechados acertar a resposta só pelo som; e o som não for o chiptune deles nem o 808 e o sino da referência. Vem primeiro porque o protótipo não tem áudio e é o que mais sustenta a nota 9.
2. **Letra com acento e um quadro no estilo próprio.** Renderizar um quadro 1080x1920, sem pixel art, com uma frase em português e os sinais de conta. Ponto de partida que conferi: a fonte Inter está na máquina, a licença no arquivo do sistema é OFL-1.1, e ela desenha ã, ç, é, õ, ×, ÷, ² e √ (teste com Pillow). Falta o Designer escolher a letra e a paleta, ler no tamanho do celular e levar o arquivo da fonte e da licença para o repositório do Instagram de IA. Vem em segundo porque sem letra e estilo não há piloto.
3. **Três reels piloto no mesmo "mundo".** Temas do núcleo seguro (pizza, desconto, porcentagem), cada um com palpite no frame 0, o script verificador rodando antes do render, e fonte e data dos dados de entrada na legenda. Medir: tempo por reel, quantos desenhos novos cada um pediu, e se os três parecem diferentes ou o mesmo molde. O Revisor de risco lê os três. São esses três filmes que vão à rodada 2 do júri.

Depois dos testes, e antes da rodada 2: a busca simples de concorrência de matemática em português e o estilo de @matharium (condição 7).

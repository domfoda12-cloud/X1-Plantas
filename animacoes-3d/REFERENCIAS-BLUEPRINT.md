# Banco de referências: planta que ganha vida em 3D

> Parte da pasta Animações 3D ([`ANIMACOES-3D.md`](ANIMACOES-3D.md)). Pesquisa de 20/11/2026 (busca na web pelo TinyFish e biblioteca de ganchos virais da MinoAI Frontier). **O 3D é o último passo** (decisão do dono): este banco serve para quando ele for liberado e para os roteiros de agora. Acrescente aqui toda referência nova, com link e data.

## 1. As referências

| # | Referência | Formato | O que ela faz | O que tirar dela |
|---|---|---|---|---|
| 1 | [RoomGen Studio, "Blueprint build"](https://www.roomgen.studio/guides/blueprint-to-3d-house-reel) (guia, 28/09/2026) | Reel 9:16, 8 s | Planta impressa numa mesa; paredes brancas sobem das linhas; vãos de porta e janela se abrem; o telhado fecha; a maquete fica parada no fim. **Câmera parada o tempo todo** | Com a câmera parada, a pessoa vê cada linha virar parede. O modelo fica em cima da planta, com a entrada do lado esperado. Termina numa imagem que diz tudo, boa como capa do reel |
| 2 | [Envato, "Architectural Blueprint Transforms into Furnished 3D House Model"](https://elements.envato.com/architecture-3d-animation-HJQ7797) | 12 s, 4K | Planta azul → estrutura em arame (wireframe) → paredes sobem → cada cômodo é mobiliado → a câmera gira em volta | A sequência clássica, e a mesma da nossa C01: azul, arame, paredes, móveis, giro |
| 3 | [Envato, "Architectural House Blueprint to Finished Construction"](https://elements.envato.com/home-ULTSWKJ) | estoque | Planta com medidas → fundação → paredes → telhado → portas e janelas | Mostrar a **ordem da obra** fala a língua de quem constrói com pedreiro |
| 4 | [Envato, "House Building Animation Top View"](https://elements.envato.com/house-building-animation-top-view-Y7DU76R) | estoque | Construção vista de cima, peça por peça | Vista de cima serve para o 9:16 e casa com o nosso blueprint |
| 5 | [YouTube, "From Pencil Lines to a Dream Home"](https://youtube.com/watch?v=QuxOwnwGdgc) (21/10/2026) | vídeo | Lápis traça a casa → o blueprint "sai do papel" → estrutura brilhante sobe na fundação → estrutura → casa pronta com jardim | Começar pelo **traço à mão** é um gancho visual forte |
| 6 | [Sam Aing, "Flat to 3D"](https://github.com/Sam1983Aing/flat-to-3d) (código aberto, MIT, three.js) | 7 demos de rolagem | Vista explodida, corte que vira profundidade, obra em time-lapse, cronograma que constrói a casa, maquete de papel que vira casa real, fachada cujo hachurado é a sombra real | **O truque principal:** a planta "plana" é o próprio modelo 3D visto por uma lente muito longa (quase ortográfica). Abrir a lente é o que transforma em 3D, sem corte nenhum |
| 7 | [Sam Aing, "Casa Serra"](https://sam1983aing.github.io/casa-serra/) e o [prompt inicial](https://github.com/Sam1983Aing/casa-serra/blob/main/starter-prompt.md) | página com rolagem | Planta em tinta preta → paredes sobem → a câmera desce até a porta e anda pelos cômodos na altura dos olhos; cada cômodo continua em traço até a câmera chegar, e aí o material "varre" a superfície | **Material varrendo o traço** cômodo a cômodo, e a câmera entrando pela porta |
| 8 | [Skill "threejs-architecture" (naksha)](https://raw.githubusercontent.com/P4R1H/naksha/main/skills/threejs-architecture/SKILL.md) | guia técnico | Paredes por linha de centro com cantos em meia-esquadria, rodapé e cornija para escala, sol real (posição NOAA), gravação do canvas | Lista técnica para a seção 4 |
| 9 | [Stager AI, "3D Floor Plan Animation"](https://stagerai.com/ai-video-templates/ai-floor-plan-video-animation) | serviço pago | Planta 2D → modelo mobiliado → câmera passeia cômodo a cômodo; exporta 9:16, 16:9 e 1:1 | Um render, três formatos: o mesmo padrão do nosso [plano do OpenArt](OPENART-MINOAI.md) |
| 10 | Reels de referência ([@studio_inspatial](https://instagram.com/reel/DbNz49SJ7LI), [@world.arch.inc](https://instagram.com/reel/DYqo-pis7ae?hl=en), [@furnea.lab](https://instagram.com/reel/Dffo4jFMehK), [@entrelligence](https://instagram.com/reel/Dee0Z3EDytF)) | reels | Planta que vira passeio 3D, com legenda explicando circulação e espaço | O passeio vem **depois** da revelação; a legenda explica o porquê da planta (é o nosso "por que esta planta é assim") |
| 11 | Reels brasileiros ([@escolasantorini](https://instagram.com/reel/DcwzRkrRyzk), [@criarstudio.3d](https://instagram.com/reel/DfPYHYruKq5?__d=1+)) | reels | Animação de arquitetura com "comenta que eu te mando" | O formato já circula no Brasil, inclusive com comentário por palavra-chave, o mesmo funil nosso |

**Ganchos da biblioteca da MinoAI Frontier para este formato** (visuais):

- [@jack.designs](https://www.instagram.com/p/DbVo1YLofef/): "então e agora", cômodo vazio → cômodo pronto com corte seco, câmera parada. Para nós: **blueprint → planta humanizada → 3D**, mesmo enquadramento, corte seco a cada 1 s.
- [@buildwithbert](https://www.instagram.com/p/DbXB9latjHl/): série numerada "PT.35 House update". Para nós: "Casa 3 de 24", uma casa por reel.
- [@marshallhaas](https://www.instagram.com/p/DUf2OEJEW8u/): a jornada (planta, planilha, fundação, estrutura, casa pronta) em cortes rápidos, com o texto na tela casando com a imagem.

## 2. A anatomia do efeito (o que todos têm em comum)

1. **Começa plano e reconhecível:** a planta como a pessoa conhece (papel, linhas, nomes).
2. **A linha vira parede:** as paredes sobem a partir do próprio traço, com a câmera parada ou quase.
3. **Os vãos se abrem:** porta e janela aparecem como recortes na parede que subiu.
4. **A cor e o material "varrem"** a superfície, cômodo a cômodo.
5. **Os móveis entram** em sequência (o "pop" com leve exagero na escala).
6. **A câmera só se move depois** que a casa está de pé: giro lento ou descida até a porta.
7. **Termina parado** numa imagem que vira capa do reel.

## 3. Onde a nossa animação já está e o que falta

O motor (`video/src/casa3d.js`, já lê as 24 plantas via `ferramentas/planta3d.py`) faz: blueprint se desenhando → paredes subindo → pisos e móveis cômodo a cômodo → jardim → câmera girando. Ou seja, os passos 1, 2, 5 e 6.

| Melhoria (ordem de impacto) | De onde vem | Esforço |
|---|---|---|
| **Começar com a câmera quase ortográfica** (FOV de 5 a 8° e bem longe) para o 3D parecer exatamente a planta 2D, e abrir a lente para revelar a profundidade | Flat to 3D (6) | Baixo: interpolar FOV e distância juntos |
| **Câmera parada nos primeiros 4 s**, só se move depois que as paredes sobem | RoomGen (1) | Baixo: ajustar `quadroAnimacao` em `render-planta.cjs` |
| **Vãos de porta e janela abrindo** na parede (hoje a janela já sai recortada, mas aparece pronta) | RoomGen (1) | Médio |
| **Material varrendo o piso** em vez de aparecer por opacidade (máscara que corre de uma ponta à outra) | Casa Serra (7) | Médio: textura com gradiente animado |
| **Platibanda e telhado fechando** no fim, para a vista externa virar casa de verdade | RoomGen (1), Envato (3) | Médio |
| **Rodapé e soleiras** para dar escala | naksha (8) | Baixo |
| **Final parado de 1,5 s** que serve de capa | RoomGen (1) | Baixo |
| **Versão "ordem da obra":** fundação → paredes → laje → janelas → acabamento, com legendas do tipo "aqui o pedreiro…" | Envato (3), @marshallhaas | Alto; ótimo para a série |
| **Sol real** pela orientação recomendada de cada casa (já sai do validador) | naksha (8) | Médio |
| **Três formatos de uma vez** (9:16, 1:1, 4:5) | Stager (9) | Baixo: renderizar com 3 câmeras |

## 4. Regras (Revisor de risco e Arquiteto)

- A animação é **ilustrativa**: a legenda diz "imagem ilustrativa da planta de referência". A RoomGen avisa o mesmo: o modelo "não é um registro, ninguém deve orçar, aprovar nem comprar a partir dele".
- A casa animada tem que ser **a mesma do e-book** (mesmos cômodos, mesmas janelas, mesma fachada). Nada de segundo andar ou telhado que a planta não tem.
- A ordem "da obra" é **efeito visual**, não sequência construtiva. Não diga "é assim que se constrói".
- Não copie trechos de vídeos de terceiros nem as demos de código sem a licença (Flat to 3D e three.js são MIT, então dá para estudar e adaptar o código, citando a fonte).

## 5. Roteiro de 12 s revisado (para quando o 3D for liberado)

| Tempo | Imagem | Referência |
|---|---|---|
| 0,0 a 1,5 s | Mão (B-roll) ou lápis traçando a planta; texto "8 m de frente. Cabe?" | (5) |
| 1,5 a 3,5 s | Planta azul, câmera ortográfica parada; as paredes sobem do traço | (1), (6) |
| 3,5 a 5,0 s | Janelas e portas se abrem; a cor varre os pisos cômodo a cômodo | (1), (7) |
| 5,0 a 7,5 s | Móveis entram em sequência; a lente abre devagar e revela a profundidade | (2), (6) |
| 7,5 a 10,5 s | Câmera gira até a fachada; platibanda fecha; jardim cresce | (2), (3) |
| 10,5 a 12,0 s | Para, imagem final com nome, área e lote (capa) | (1) |

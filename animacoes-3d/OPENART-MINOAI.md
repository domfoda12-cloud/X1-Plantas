# OpenArt + MinoAI Frontier: imagens e animações a partir das nossas plantas

> Exemplo do [Conselho](../CONSELHO.md) em ação. Guia da frente: [`ANIMACOES-3D.md`](ANIMACOES-3D.md). Editor: [MinoAI Frontier](../instagram/MINOAI-FRONTIER.md).

## A mesa (conselho completo, 20/11/2026)

```text
[Editor]       SIM · skill: OpenArt (imagem→vídeo) + MinoAI Frontier · efeito: venda + · custo: créditos OpenArt · por quê: B-roll de "casa pronta" segura o 2º e o 3º segundo
[Designer]     SIM, SE a imagem de partida for a nossa prévia ou o nosso 3D · por quê: sem isso a IA inventa uma casa genérica
[Arquiteto]    SIM, SE a casa gerada tiver os mesmos cômodos e a mesma fachada da planta · por quê: anúncio mostrando casa que não está no e-book é propaganda enganosa
[Revisor]      SIM, SE a legenda disser "imagem ilustrativa" e nada de texto ilegível na imagem
[Estrategista] SIM · efeito: venda + · custo: créditos, só para as 3 casas mais pedidas · por quê: testar antes de gerar 24
[Redator]      SIM · por quê: dá prova ao atributo "ver antes de construir" (hoje nota P=3)
DECISÃO: aprovado com as condições. Gasto de créditos: decisão do dono.
```

## Situação das ferramentas

- **Quem faz (decisão do dono, 20/11/2026):** a **MinoAI Frontier é a responsável pela edição de vídeo e pela criação de imagem**, e cria as imagens **usando o OpenArt**.
- **OpenArt agora é um plugin do Claude** (`openart`), com skills prontas: `openart:performance-ads` (anúncio de feed), `openart:hook-variants` (o mesmo anúncio com ganchos diferentes), `openart:ugc`, `openart:tvc`, `openart:talking-head`, `openart:ad-variation`. **Ainda falta autorizar a conta do OpenArt** nas configurações de conectores do claude.ai; até lá as ferramentas não funcionam. A busca de 20/11/2026 que dizia "sem conector" ficou desatualizada.
- **Créditos do OpenArt:** liberados pelo dono sem limite (20/11/2026). Pode gerar assim que a conta estiver autorizada.
- **MinoAI Frontier** edita no Mac ou PC do dono.
- **Nossa base** sai daqui: prévias em `ebook/plantas/previas/`, 3D e animação da C01 em `animacoes-3d/plantas/casa-compacta/`.

## O fluxo

| # | Quem | O quê | Sai |
|---|---|---|---|
| 1 | Claude (nuvem) | Gera a prévia e o 3D da planta escolhida (`ferramentas/plantas.py previa`, `video/render-planta.cjs`) | `planta.png`, `perspectiva.png`, `animacao.mp4` |
| 2 | Dono ou MinoAI (Mac), no OpenArt | **Imagem → imagem:** a perspectiva 3D vira foto realista, com o prompt abaixo | `fachada-realista.png` |
| 3 | Idem | **Imagem → vídeo:** a foto realista ganha um movimento de câmera de 4 a 5 s | `fachada-movimento.mp4` |
| 4 | Arquiteto + Revisor | Conferem: mesma fachada, mesmas janelas, nenhum texto inventado | aprovado ou refazer |
| 5 | MinoAI Frontier | Monta o reel: blueprint se desenhando (nosso) → paredes subindo (nosso) → foto realista em movimento (OpenArt) → planta humanizada com área e lote | reel de 12 a 20 s |

## Prompts para o OpenArt (imagem → imagem)

Use sempre a nossa imagem como referência, com força alta de referência (a casa não pode mudar de forma).

```text
Casa térrea brasileira, fotografia realista, fim de tarde, céu limpo, lote de bairro residencial,
muro baixo, calçada, grama simples, materiais comuns (reboco pintado, telhado embutido com platibanda,
janelas de alumínio), mesma forma, mesmas janelas e mesma porta da imagem de referência.
Sem texto, sem placas, sem pessoas, sem carros de luxo.
```

Para o interior (planta humanizada → sala realista):

```text
Interior de casa brasileira de padrão médio, sala integrada com cozinha, piso porcelanato claro,
móveis simples e reais, luz natural da janela, mesma disposição de móveis da imagem de referência,
sem texto, sem pessoas.
```

Imagem → vídeo: "movimento lento de câmera se aproximando da porta, 4 segundos, sem mudar a casa".

## Regras

- Começar pelas 3 casas mais pedidas no WhatsApp (o parceiro informa; hoje a aposta é C01, E02 e F01).
- Na legenda: "imagem ilustrativa gerada a partir da planta".
- Guardar tudo em `Filmes/X1-Plantas/broll/ID/` no Mac, com o nome da planta.

## Economia de créditos (pedido do dono, 20/11/2026: "economizar o máximo, mas enfeitado; não usar o primeiro modelo")

**Mesa de bolso**

```text
[Maestro MinoAI] SIM · imagem parada + edição na MinoAI gasta muito menos que vídeo gerado; ímã do comentário pede só capa forte · fonte: método MinoAI (ímã por comentário)
[Estrategista]   SIM, SE começar por 6 imagens de ambientação e medir antes de gerar mais
[Arquiteto]      SIM, SE nenhuma imagem mostrar uma casa que não está no e-book (fachada só depois do 3D)
[Revisor]        SIM, SE legenda "imagem ilustrativa" e nenhum texto dentro da imagem
DECISÃO: aprovado com as regras abaixo
```

1. **Não usar o primeiro modelo (o padrão do plugin, Seedance 2.5, que é de vídeo).** Escolher um **modelo de imagem** na lista viva do OpenArt quando a conta for autorizada: o mais barato que aceite imagem de referência, comparando o custo que a própria ferramenta mostrar. Nada de vídeo gerado agora: o movimento vem do nosso 3D e da edição da MinoAI (zoom lento, recorte, transição).
2. **Rascunho primeiro, qualidade final só no aprovado.** Gerar em resolução de rascunho, escolher, e só então gerar a final daquela uma.
3. **Uma imagem, vários formatos.** Gerar em 4:5 com sobra nas bordas e recortar para 9:16 (reel e story), 1:1 (WhatsApp) e capa. Nunca gerar a mesma cena duas vezes por causa do formato.
4. **O que é grátis não vai para o OpenArt.** Plantas, páginas, fita, mockups do e-book no celular e o 3D saem dos nossos scripts (`ebook/visual/mockups/` já tem 3).
5. **Sem teto de crédito** (o dono liberou em 20/11/2026). As regras 1 a 4 continuam, para render mais por crédito.

**A primeira rodada (6 imagens de ambientação, sem mostrar planta)**

| # | Para que serve | Prompt (imagem → sem referência) |
|---|---|---|
| 1 | Fundo da capa do reel "Que casa cabe no seu lote?" | Lote vazio de bairro brasileiro, terra batida e grama rala, muro baixo de bloco nos dois lados, fim de tarde dourado, trena amarela esticada no chão de um lado ao outro do lote, vista de cima a 45 graus, sem pessoas, sem texto |
| 2 | B-roll do gancho "me fala a frente do seu lote" | Mãos segurando uma trena amarela aberta sobre um muro de bloco, close, luz natural, fundo desfocado de lote vazio, sem texto, sem marca |
| 3 | B-roll "leve ao seu engenheiro" | Duas pessoas olhando uma planta impressa sobre uma tábua apoiada em blocos, num terreno com gabarito de madeira e linha de nylon, roupa simples, rosto fora de foco, sem texto legível |
| 4 | Capa de post "casa que cresce" | Casa térrea brasileira pequena com o lado de uma futura ampliação marcado por estacas e linha de nylon, céu limpo, sem pessoas, sem texto |
| 5 | Fundo para o depoimento e o "abriu" do lançamento | Família de costas olhando um lote vazio ao entardecer, pai com criança no colo, bairro residencial simples ao fundo, sem texto |
| 6 | Textura para enfeitar o e-book e os carrosséis | Papel de projeto azul com linhas de grade e manchas sutis, vista de cima, sem desenhos, sem texto |

A fachada realista de cada casa (imagem → imagem a partir do nosso 3D) fica para depois do 3D, que é o último passo.

## Como tirar o máximo de cada crédito (preços medidos na conta em 20/11/2026)

> Plano **Starter**, 4.000 créditos. **Limite de 4 imagens e 2 vídeos gerando ao mesmo tempo**: mande em lotes de até 4 imagens. Preços consultados com a ferramenta de custo do OpenArt, por imagem, na configuração indicada; outra configuração custa diferente e o preço final sai na hora de gerar.

### Imagem: quanto custa cada nível

| Modelo | Configuração | Créditos | Para quê |
|---|---|---|---|
| **GPT Image 2.5 Sunburst** | 1K, qualidade baixa | **5** | **Rascunho**: testar composição e prompt |
| GPT Image 2.5 Sunburst | 2K, qualidade média | 10 | Rascunho bom (a 1ª rodada usou este) |
| **GPT Image 2.5 Sunburst** | **4K, qualidade média** | **20** | **Final padrão**: post, anúncio, e-book |
| GPT Image 2.5 Sunburst | 4K, qualidade alta | 70 | Só a peça principal (capa, imagem do anúncio campeão) |
| **Kling 3 Omni** | **4K** | **20** | Alternativa no mesmo preço, boa para lotes e detalhe |
| Nano Banana 2 | 4K | 50 | Pessoas realistas, quando o Sunburst falhar |
| Nano Banana 2 Lite | padrão (1:1) | 15 | Rascunho rápido |
| Kling Image 4 (o primeiro da lista) | 2K | 32 | Não usar: mais caro por resultado parecido |

**A regra:** rascunho a 5 → escolhe → final em 4K média a 20 → qualidade alta (70) só para 1 ou 2 peças principais. A diferença entre 4K média e 4K alta é de 3,5 vezes no preço.

### Vídeo: quanto custa um clipe (configuração padrão)

| Modelo | Créditos | Quando |
|---|---|---|
| **PixVerse V6** | **50** | Movimento de câmera natural e estável: o mais barato para testar |
| MiniMax H3 Swift / H3 Max Turbo | 75 | Prova de conceito rápida (480p a 768p) |
| **Wan 3.0** | **100** | Até 30 s num clipe só, com o movimento consistente |
| Veo 3.1 | 120 | Alta fidelidade e até 4K: a versão final |
| Kling 3 Omni / Kling 3.0 | 175 | 4K, vários planos |
| Seedance 2.5, Kling 4, Grok, FLUX 3 Video | 300 a 600 | Só se os outros falharem |

**A regra:** imagem aprovada → vídeo **imagem para vídeo** de 4 a 5 s no PixVerse V6 (50) → se o movimento estiver certo, versão final no Veo 3.1 ou no Wan 3.0. Nunca vídeo direto do texto: sai uma casa que não é a nossa.

### Sete hábitos que economizam

1. **Prompt completo e específico** (cena, luz, câmera, materiais brasileiros, "sem texto, sem logotipo"). Prompt vago gasta crédito em tentativa. "Melhorar prompt automaticamente" desligado: a gente controla.
2. **Uma imagem, vários formatos:** gerar em 4:5 com sobra e recortar para 9:16 e 1:1 no computador. Nunca gerar de novo por causa do formato.
3. **Variações do mesmo prompt** com "quantidade de imagens" numa chamada só; prompts diferentes, no lote (até 4 por vez).
4. **Partir da nossa imagem** (imagem para imagem, 2 créditos a mais) sempre que a cena mostrar a casa: a planta ou a vista da rua do e-book entram como referência, e a IA não inventa outra casa.
5. **Conferir o rascunho antes de pagar o final:** Arquiteto (é a casa certa?) e Revisor (tem texto inventado? pessoa reconhecível?).
6. **Guardar o prompt aprovado** neste arquivo, para refazer sem pagar tentativa.
7. **Orçamento da conta (4.000):** cerca de 30 rascunhos (150) + 15 finais em 4K média (300) + 2 peças em 4K alta (140) + 6 testes de vídeo no PixVerse (300) + 3 vídeos finais no Veo 3.1 (360) = **cerca de 1.250**, sobrando reserva para a segunda rodada de anúncios.

### O que a primeira rodada ensinou (20/11/2026)

- **O "4K" do GPT Image 2.5 Sunburst em 4:5 entrega 2048 x 2560 px**, e o "1K" entrega 1024 x 1280. Para Instagram (1080 x 1350) e anúncio, 2048 x 2560 sobra. Para impressão grande, testar o Kling 3 Omni em 4K (20 créditos) e comparar os pixels.
- **O rascunho de 5 créditos (1K, baixa) já sai quase com cara de final.** Vale fazer de 2 a 4 rascunhos por cena e escolher, em vez de 1 rascunho caro.
- **Para subir a resolução sem perder a composição aprovada:** imagem para imagem com o próprio rascunho como referência e o prompt "recreate this exact photo at higher resolution and finer detail: same …" (descrevendo a cena de novo). As 3 finais ficaram idênticas aos rascunhos. Gerar de novo só pelo texto daria outra foto.
- **Casa só a partir da nossa imagem.** O rascunho de texto da "casa que cresce" inventou uma casa que não existe no e-book: o Arquiteto vetou. Refeito com a **vista da rua da C03** como referência (subida sem texto: `ebook/visual/openart/referencias/c03-fachada.png`), saiu a mesma frente: porta no canto, janela de duas folhas, platibanda. É o caminho para todas as fachadas.
- **Limite do plano:** mande no máximo 4 imagens por vez. O 5º item de um lote é recusado sem cobrança.
- **Gasto da rodada:** 4 rascunhos a 10 + 3 rascunhos a 5 + 6 finais em 4K média a 20 a 22 = cerca de 180 créditos para 6 imagens finais.

### Teste de qualidade lado a lado (20/11/2026) e a configuração da peça final

Mesma foto de partida (o rascunho do lote), dois modelos:

| | GPT Image 2.5 Sunburst, 4K, extra-alta | Kling 3 Omni, 4K |
|---|---|---|
| Pixels entregues | 2048 x 2560 | **3520 x 4672** |
| Créditos | 123 | 20 |
| Cor e luz | **Dourada, rica, parece câmera boa** | Mais apagada |
| Detalhe ampliado | **Grama e terra nítidas** | Leve borrado típico de IA |
| Fidelidade ao rascunho | Alta | Alta |

**Decisão (qualidade em primeiro lugar):** peça final no **Sunburst 4K extra-alta**. Os 2048 x 2560 sobram para o feed (1080 x 1350) e o recorte 9:16 sai com 1440 x 2560, acima do Full HD vertical. O Kling 3 Omni 4K fica para quando o tamanho em pixels importar mais que a cor (impressão grande, fundo de tela 4K). **Teste da qualidade máxima (273 créditos) contra a extra-alta (123), mesma foto:** praticamente iguais. A máxima deixa as juntas dos blocos um pouco mais limpas, nada que se veja no celular. **Padrão das finais: extra-alta. Máxima só na peça principal** (capa do e-book, imagem do anúncio campeão). A final do lote ficou na máxima porque o teste já estava pago.

**Configuração das finais, em resumo:** GPT Image 2.5 Sunburst, imagem para imagem a partir do rascunho aprovado, 4K, qualidade extra-alta, formato 4:5; recortes 9:16 e 1:1 com `python3 ferramentas/recortes.py`.

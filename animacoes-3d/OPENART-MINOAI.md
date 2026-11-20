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

- **OpenArt não tem conector no diretório do Claude** (pesquisado em 20/11/2026). Ele é usado **no navegador ou no app**, pelo dono ou pela MinoAI no Mac. Se você tiver uma chave da API do OpenArt, dá para automatizar: avise e a chave entra pelo cofre de credenciais do ambiente (nunca no chat).
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

# Animações 3D: as plantas que o e-book vai conter

> **Banco de referências** de planta que ganha vida, com o que adotar no motor: [`REFERENCIAS-BLUEPRINT.md`](REFERENCIAS-BLUEPRINT.md).

> Parte do projeto X1-Plantas. Painel geral: [`../PAINEL.md`](../PAINEL.md).
>
> **Esta pasta guarda as imagens e animações de cada planta.** Elas vão para dentro do e-book ([`../ebook/`](../ebook/EBOOK.md)), para os posts do Instagram ([`../instagram/`](../instagram/INSTAGRAM.md)) e para os vídeos ([`../video/`](../video/VIDEO.md)).
>
> **Estado em 22/11/2026:** o motor já lê as 24 plantas (`node render-planta.cjs --planta ID`, dados em `video/src/plantas/<ID>.js`, que saem de `python3 ferramentas/planta3d.py`). A C01 foi redesenhada em 22/11 (50 m²; ver [`../ebook/plantas/PLANTAS.md`](../ebook/plantas/PLANTAS.md)): o que está em `plantas/casa-compacta/` é do desenho antigo e precisa ser gerado de novo. A E07 está na fila do redesenho (o dono chamou de erro os 3 quartos em fila).

## Nesta pasta

| Arquivo | Para que serve |
|---|---|
| `ANIMACOES-3D.md` | Este guia: motor 3D, estilo, entregas por planta e como gerar |
| `plantas/<nome-da-planta>/` | Imagens e animação de cada planta gerada pelo motor (hoje: `casa-compacta/`, do desenho antigo da C01) |
| `plantas-2d/` | Imagens 2D das plantas para os carrosséis (as da C01 são de 20/11, antes do redesenho) |

O código do motor fica em [`../video/src/`](../video/src/), porque o vídeo de anúncio usa o mesmo motor. Ver seção 5.

## 1. O que cada planta recebe

Uma pasta por planta, com cinco arquivos gerados a partir dos mesmos dados:

| Arquivo | O que é | Uso no e-book | Uso no Instagram |
|---|---|---|---|
| `01-blueprint.png` | Planta técnica azul, com cotas, portas, nomes e áreas | Página da planta: medidas | Carrossel |
| `02-planta-humanizada.png` | Vista de cima com piso, móveis e jardim | Página da planta: imagem principal | Capa do post |
| `03-perspectiva.png` | Casa em 3D, de um ângulo | Página da planta: "como fica" | Carrossel |
| `04-perspectiva-lateral.png` | Casa em 3D, do outro lado | Página da planta: segundo ângulo | Carrossel |
| `animacao.mp4` | 12 s, vertical: o blueprint se desenha, a casa ganha vida e a câmera desliza | QR code ou link na página da planta | Reel "planta da semana" e stories |

As imagens têm 2000 x 2500 pixels (proporção 4:5): cabem numa página A4 do e-book e no feed do Instagram.

**Pasta pronta hoje:** só `plantas/casa-compacta/`, e ela é da C01 antiga (55 m², antes de 22/11): gerar de novo com `node render-planta.cjs --planta C01`. As imagens 3D das 24 plantas para o e-book estão em `ebook/visual/3d/<ID>.jpg`.

## 2. Os três estágios da animação

| Estágio | O que aparece |
|---|---|
| **1. Blueprint** | Fundo azul quadriculado. Paredes, portas, móveis, nomes, áreas e cotas se desenham em branco |
| **2. Ganhando vida** | As paredes sobem translúcidas e ficam brancas. Cada cômodo recebe piso (madeira ou porcelanato) e móveis, um de cada vez. O jardim cresce em volta |
| **3. Planta humanizada** | Paredes cortadas a 1,1 m de altura, vista de cima, sombras suaves, câmera deslizando devagar |

## 3. Regras de estilo

- **Paleta:** azul do blueprint `#0B4FA8`, linhas brancas, destaque amarelo `#FFC857`, madeira clara, paredes brancas, jardim verde.
- **Câmera:** sempre lenta e contínua. Nada aparece de repente: tudo entra deslizando ou crescendo.
- **Vista:** a frente da casa fica no alto da imagem, igual à planta 2D, para o cliente reconhecer a mesma casa nas duas.
- **Corte das paredes:** 1,1 m, para ver os móveis por cima sem perder a noção dos cômodos.
- **Móveis:** em escala, só para mostrar o uso do espaço. Nada de acabamento que o projeto não tem.

## 4. Referências

- **Planta humanizada:** planta baixa com móveis, decoração e acabamentos, para facilitar a visualização ([QuintoAndar](https://www.quintoandar.com.br/guias/?p=2444657), [Planner 5D](https://planner5d.com/blog/pt/planta-baixa-humanizada-guia/)).
- **Animação de planta 3D:** vista de cima com câmera lenta, como os vídeos da página Virtual Floor Plan ([exemplo](https://www.facebook.com/watch/?v=2617867535326380)).
- **Blueprint virando casa:** planta 2D, depois modelo mobiliado, depois câmera passeando ([TensorPix](https://tensorpix.ai/blog/2d-to-3d-floor-plan-video-ai), [YouMind](https://youmind.com/pt-BR/video-prompts/architectural-blueprint-house-transformation-4370)).
- **Imagem azul do Freepik:** usamos só o estilo. O blueprint é desenhado do zero a partir dos dados de cada planta.

## 5. Como o motor funciona

| Arquivo | O que faz |
|---|---|
| [`../video/src/plantas/`](../video/src/plantas/) | **Dados de cada planta** (`<ID>.js`, um por planta, as 24): medidas, cômodos, paredes, janelas, portas e a ficha (`META`). Saem de `python3 ferramentas/planta3d.py`; não edite à mão |
| [`../video/src/planta.js`](../video/src/planta.js) | Dados da C01 **antiga** (55 m²): é o que o motor usa quando roda sem `--planta`. Não use |
| [`../video/src/casa3d.js`](../video/src/casa3d.js) | **Motor 3D:** monta a casa a partir dos dados nos três estágios. Também tem a lista de móveis e a ordem em que os cômodos ganham vida |
| [`../video/src/casa.html`](../video/src/casa.html) | Página que mostra um quadro da casa, usada pelo render |
| [`../video/render-planta.cjs`](../video/render-planta.cjs) | Gera as 4 imagens e a animação de uma planta |

Para gerar uma planta, dentro da pasta `video`, com Node.js, ffmpeg e Playwright instalados (ver [`../video/VIDEO.md`](../video/VIDEO.md), seção 4):

```bash
node render-planta.cjs --planta C01
```

Com `--so-imagens`, só as imagens. Os arquivos saem em `animacoes-3d/plantas/<nome-da-planta>/` (ex.: `casa-compacta/`); a câmera afasta sozinha conforme o tamanho da casa. **Sempre passe `--planta`:** sem ela, o motor usa a C01 antiga.

## 6. O que falta

Feito: um arquivo de dados por planta (as 24 em `video/src/plantas/`), nome e ficha do blueprint lidos do `META` de cada planta, e `render-planta.cjs --planta ID` salvando em `plantas/<nome>/` com a câmera afastada conforme o tamanho. Falta **rodar** o motor para as plantas que o Instagram e o vídeo pedem (a C01 nova primeiro) e um jeito de gerar todas de uma vez.

**O público pede mais três coisas** ([estratégia](../ESTRATEGIA.md), seção 6):

4. **Fachada.** Uma vista da casa pela rua, com telhado (ou platibanda) e muro baixo. O brasileiro escolhe muito pela fachada, e hoje só temos vistas de cima. Novo arquivo: `05-fachada.png`.
5. **Medidas de cada cômodo** escritas no blueprint (ex.: "QUARTO 1 · 3,20 x 4,30 m"). É o que a pessoa leva para o pedreiro.
6. **Como cresce.** Nas [casas que crescem](../ebook/catalogo.md#casas-que-crescem), uma imagem a mais com a ampliação tracejada em amarelo: `06-como-cresce.png`.

Ordem recomendada: 5 (é só texto no blueprint), depois 4 e 6.

## 7. Cuidados

- **Plantas originais.** Projetos de terceiros têm dono. Só entram no e-book plantas desenhadas para o produto, ou com licença escrita que permita a venda. Não use plantas com marca d'água de outro escritório.
- **Medidas provisórias.** Toda planta é rascunho até um arquiteto validar.
- **Ilustração, não projeto aprovado.** Móveis e acabamentos são ilustrativos. O material não substitui o projeto aprovado na prefeitura nem o responsável técnico da obra.
- **Fidelidade.** A casa 3D precisa bater com a planta vendida. Se a animação mostrar algo que a planta não tem, o cliente reclama.

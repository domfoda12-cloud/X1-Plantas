# Animações 3D: as plantas que o e-book vai conter

> Parte do projeto X1-Plantas. Painel geral: [`../PAINEL.md`](../PAINEL.md).
>
> **Esta pasta guarda as imagens e animações de cada planta.** Elas vão para dentro do e-book ([`../ebook/`](../ebook/EBOOK.md)), para os posts do Instagram ([`../instagram/`](../instagram/INSTAGRAM.md)) e para o vídeo de anúncio ([`../video/`](../video/VIDEO.md)).

## Nesta pasta

| Arquivo | Para que serve |
|---|---|
| `ANIMACOES-3D.md` | Este guia: motor 3D, estilo, entregas por planta e como gerar |
| `plantas/<nome-da-planta>/` | Imagens e animação de cada planta (hoje: `casa-compacta/`) |

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

**Pronta hoje:** só a Casa Compacta (`plantas/casa-compacta/`).

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
| [`../video/src/planta.js`](../video/src/planta.js) | **Dados da planta:** medidas, cômodos, paredes, janelas e portas, em metros |
| [`../video/src/casa3d.js`](../video/src/casa3d.js) | **Motor 3D:** monta a casa a partir dos dados nos três estágios. Também tem a lista de móveis e a ordem em que os cômodos ganham vida |
| [`../video/src/casa.html`](../video/src/casa.html) | Página que mostra um quadro da casa, usada pelo render |
| [`../video/render-planta.cjs`](../video/render-planta.cjs) | Gera as 4 imagens e a animação de uma planta |

Para gerar de novo a Casa Compacta, dentro da pasta `video`, com Node.js, ffmpeg e Playwright instalados (ver [`../video/VIDEO.md`](../video/VIDEO.md), seção 8):

```bash
node render-planta.cjs
```

Os arquivos saem em `animacoes-3d/plantas/casa-compacta/`. Leva cerca de 10 minutos.

## 6. O que falta para gerar dezenas de plantas

Hoje o motor foi feito para uma planta só. Para o e-book, o código precisa mudar em três pontos:

1. **Um arquivo de dados por planta.** Hoje `planta.js` tem só a Casa Compacta, e os móveis e a ordem dos cômodos estão dentro de `casa3d.js`. Cada planta precisa do seu arquivo com cômodos, paredes, janelas, portas e móveis.
2. **Nome e ficha automáticos.** O título "CASA COMPACTA · 55 m² · 2 quartos · 1 banho" está escrito direto no blueprint e no vídeo. Precisa vir dos dados de cada planta.
3. **Render em lote.** `render-planta.cjs` precisa receber o nome da planta (ou gerar todas) e salvar cada uma em `plantas/<nome>/`. Plantas maiores também precisam de câmera mais afastada.

Com isso pronto, cada planta nova é só um arquivo de dados. O render roda sozinho, cerca de 10 minutos por planta.

## 7. Cuidados

- **Plantas originais.** Projetos de terceiros têm dono. Só entram no e-book plantas desenhadas para o produto, ou com licença escrita que permita a venda. Não use plantas com marca d'água de outro escritório.
- **Medidas provisórias.** Toda planta é rascunho até um arquiteto validar.
- **Ilustração, não projeto aprovado.** Móveis e acabamentos são ilustrativos. O material não substitui o projeto aprovado na prefeitura nem o responsável técnico da obra.
- **Fidelidade.** A casa 3D precisa bater com a planta vendida. Se a animação mostrar algo que a planta não tem, o cliente reclama.

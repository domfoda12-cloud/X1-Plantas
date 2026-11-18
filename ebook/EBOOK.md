# E-book: dezenas de plantas de casas

> Parte do projeto X1-Plantas. Painel geral: [`../PAINEL.md`](../PAINEL.md).
>
> **Esta pasta é o produto.** Um e-book com dezenas de plantas de casas, com grande variação de tamanho, terreno e uso, cada uma em blueprint, planta humanizada, 3D e animação.

## Nesta pasta

| Arquivo | Para que serve |
|---|---|
| `EBOOK.md` | Este guia: produto, estrutura, página de cada planta, fluxo de produção |
| `catalogo.md` | Lista das 35 plantas propostas, com ficha e situação de cada uma |
| `vendas/material-gratuito.md` | Amostra grátis enviada depois do cadastro |
| `vendas/sequencia-whatsapp.md` | Mensagens do funil no WhatsApp, dia a dia |
| `vendas/faq-compradores.md` | Perguntas frequentes |
| `vendas/respostas-objecoes.md` | Respostas para "é caro", "vou pensar" e outras |

A pasta `vendas/` é o material do funil, que fica com o seu parceiro.

## 1. O produto

- **O que é:** um e-book em PDF com **35 plantas** de casas (proposta inicial), cada uma com imagens 3D e ficha.
- **Para quem:** quem vai construir no Brasil, principalmente a primeira casa, e ainda não sabe que planta cabe no terreno e no bolso.
- **Promessa:** "Encontre a planta certa para o seu terreno antes de gastar com projeto", ligada ao gancho dos vídeos ("os R$ 1.000 que um arquiteto te economizaria").
- **Grande variação:** compactas, terreno estreito, família, especiais (edícula, geminadas, acessível, home office, praia, campo, esquina) e sobrados. Ver [`catalogo.md`](catalogo.md).
- **Idioma e moeda:** português do Brasil, preços em R$.

## 2. Estrutura do e-book

| # | Parte | Conteúdo |
|---|---|---|
| 1 | Capa | Título, quantidade de plantas, uma planta humanizada em destaque |
| 2 | Como usar | Como escolher pelo tamanho do terreno, pelo número de pessoas e pelo orçamento |
| 3 | Como ler uma planta | Blueprint, cotas, símbolos de porta e janela. Glossário: nascente, hall, peitoril, recuo, planta humanizada |
| 4 | Os 7 erros que saem caro | Os mesmos do vídeo de anúncio ([`../video/VIDEO.md`](../video/VIDEO.md)), com a planta mostrando o certo |
| 5 | Índice rápido | Tabela de todas as plantas por categoria, área, quartos e lote mínimo |
| 6 | As plantas | Uma página dupla por planta (seção 3), separadas por categoria |
| 7 | Terreno e recuos | Como conferir as regras da sua cidade antes de escolher |
| 8 | Próximos passos | Responsável técnico, aprovação na prefeitura, orçamento da obra |
| 9 | Bônus | QR codes das animações, checklist de obra |

## 3. Página dupla de cada planta

| Página esquerda | Página direita |
|---|---|
| Nome e ID da planta (ex.: "C01 · Casa Compacta") | Blueprint com cotas (`01-blueprint.png`) |
| Planta humanizada grande (`02-planta-humanizada.png`) | Duas perspectivas 3D (`03` e `04`) |
| Ficha: área, quartos, banheiros, lote mínimo | "Por que essa planta funciona": 3 destaques |
| Para quem é | "Cuidados": o que conferir antes de construir |
| | QR code da animação (`animacao.mp4`) |

As imagens saem prontas das [`../animacoes-3d/`](../animacoes-3d/ANIMACOES-3D.md), em 2000 x 2500 pixels, que cabem numa página A4.

## 4. Fluxo de produção de cada planta

| Passo | O que acontece | Quem faz | Onde |
|---|---|---|---|
| 1. Ideia | Nome, área, quartos, lote e destaque | Você | [`catalogo.md`](catalogo.md) |
| 2. Dados | Planta desenhada em dados: cômodos, paredes, janelas, portas, móveis | Claude | Motor 3D ([`../animacoes-3d/`](../animacoes-3d/ANIMACOES-3D.md)) |
| 3. Validação | Arquiteto confere medidas e funcionamento | Arquiteto | Fora do repositório |
| 4. 3D | Blueprint, planta humanizada, perspectivas e animação | Claude (render automático) | `../animacoes-3d/plantas/<nome>/` |
| 5. Página | Página dupla do e-book com ficha e imagens | Claude | E-book em PDF |
| 6. Revisão | Conferência final de medidas, textos e imagens | Você | |

Atualize a coluna **Situação** do catálogo a cada passo. O andamento geral fica no [painel](../PAINEL.md).

## 5. Decisões em aberto

- **Título do e-book.** Sugestões: "35 Plantas de Casas Prontas para Construir", "Planta Certa: 35 casas para todo terreno".
- **Preço** e **forma de pagamento**.
- **Versões:** só o e-book, ou também uma versão completa com pranchas para obra (PDF e DWG)? A versão completa exige projeto validado por arquiteto.
- **Quantidade inicial:** lançar com as 35, ou começar com 10 a 15 e ir aumentando (cada lote novo vira conteúdo para o Instagram).
- **Amostra grátis do funil:** qual planta vai de graça (hoje é a Casa Compacta).

## 6. Funil de vendas

Os textos de `vendas/` foram escritos para vender **uma planta por vez**. Eles precisam ser ajustados para vender o e-book: a amostra grátis vira uma planta do e-book, e a oferta final passa a ser o e-book inteiro. Isso fica pendente até você decidir preço e versões (seção 5).

## 7. Cuidados

- **Plantas originais.** Só entram plantas desenhadas para o produto, ou com licença escrita que permita a venda.
- **Medidas provisórias** até um arquiteto validar.
- **Ilustração.** Móveis e acabamentos são ilustrativos. O e-book não substitui projeto aprovado na prefeitura nem responsável técnico pela obra. Deixe isso escrito no e-book (parte 8).

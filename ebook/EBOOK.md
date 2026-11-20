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

- **O que é:** um e-book em PDF com dezenas de plantas de casas (35 propostas, lançadas em 3 levas), cada uma com imagens 3D e ficha.
- **Para quem:** quem vai construir no Brasil, principalmente a primeira casa, e ainda não sabe que planta cabe no terreno e no bolso.
- **Promessa:** "Encontre a planta certa para o seu terreno antes de gastar com projeto", ligada ao gancho dos vídeos ("os R$ 1.000 que um arquiteto te economizaria").
- **Grande variação:** compactas, terreno estreito, família, especiais (edícula, geminadas, acessível, home office, praia, campo, esquina) e sobrados. Ver [`catalogo.md`](catalogo.md).
- **Plantas já desenhadas (24, lançamentos 1 e 2):** dados em `plantas/dados/`, prévias em `plantas/previas/`, fichas em [`plantas/PLANTAS.md`](plantas/PLANTAS.md). Todas passam pelo validador de arquiteto ([`referencias/regras-do-arquiteto.md`](referencias/regras-do-arquiteto.md)). Público e persona: [`referencias/persona-e-mercado.md`](referencias/persona-e-mercado.md). Linguagem, visual e animação: [`referencias/linguagem-visual-e-animacao.md`](referencias/linguagem-visual-e-animacao.md). Análise dos catálogos de porcelanato: [`referencias/analise-catalogos-porcelanato.md`](referencias/analise-catalogos-porcelanato.md). Concorrentes: [`referencias/concorrentes.md`](referencias/concorrentes.md).
- **Gerador do PDF (novo, 20/11/2026):** `python3 ebook/gerador/livro.py [--previa DIR]` gera `ebook/saida/ebook.pdf` (61 páginas, 24 casas) e `planta-gratis-<ID>.pdf`, no estilo do [plano](PLANO-EBOOK.md): capa fita métrica, ache pelo lote, casa no lote, "Informação da casa", orelhas. Textos das casas em `fichas/textos.py`. O gerador antigo (`gerar.py`) fica como referência.
- **Idioma e moeda:** português do Brasil, preços em R$.

## 2. Estrutura do e-book

| # | Parte | Conteúdo |
|---|---|---|
| 1 | Capa | Título, quantidade de plantas, uma planta humanizada em destaque |
| 2 | **Ache pelo seu lote** | Uma tabela por tamanho de lote (5 x 25, 8 x 25, 10 x 20, 10 x 25, 12 x 25, 12 x 30…) com as casas que cabem em cada um. É a primeira pergunta do público ([estratégia](../ESTRATEGIA.md), seção 5) |
| 2b | Como usar | Como escolher pelo número de pessoas, pelo orçamento e se vai construir por etapas |
| 3 | Como ler uma planta | Blueprint, cotas, símbolos de porta e janela. Glossário: nascente, hall, peitoril, recuo, planta humanizada |
| 4 | Os 7 erros que saem caro | Os mesmos do vídeo de anúncio ([`../video/VIDEO.md`](../video/VIDEO.md)), com a planta mostrando o certo |
| 5 | Índice rápido | Tabela de todas as plantas por categoria, área, quartos e lote mínimo |
| 6 | As plantas | Uma página dupla por planta (seção 3), separadas por categoria |
| 7 | Terreno e recuos | Como conferir as regras da sua cidade antes de escolher |
| 8 | Próximos passos | Responsável técnico, aprovação na prefeitura, orçamento da obra. Aviso: as plantas são **de referência**, não projeto executivo |
| 9 | Bônus | QR codes das animações, checklist de obra |

## 3. Página dupla de cada planta

| Página esquerda | Página direita |
|---|---|
| Nome e ID da planta (ex.: "C01 · Casa Compacta") | Blueprint com cotas (`01-blueprint.png`) |
| Planta humanizada grande (`02-planta-humanizada.png`) | Duas perspectivas 3D (`03` e `04`) e a fachada (`05`, quando existir) |
| Ficha: área, quartos, banheiros, lote mínimo | "Por que essa planta funciona": 3 destaques |
| Para quem é | "Cuidados": o que conferir antes de construir |
| "Leve para o seu pedreiro e o seu engenheiro": medidas de cada cômodo e perguntas para fazer antes de começar | QR code da animação (`animacao.mp4`) |
| Selo "Casa que cresce" e a imagem da ampliação (`06`), quando a planta tiver | |

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

## 5. Lançamentos e decisões

- **Lançar em levas:** 12 plantas no 1º lançamento, 12 no 2º e 11 no 3º. Quem compra no 1º recebe os outros sem pagar de novo. A coluna **Lançamento** do [catálogo](catalogo.md) diz em qual leva cada planta entra.
- **Título, preço, bônus e versão completa** são decididos no [painel](../PAINEL.md), seção 9, que tem as opções e a recomendação de cada um. A oferta recomendada (preço, Pix e cartão, garantia, bônus, order bump) está na [estratégia](../ESTRATEGIA.md), seção 7.
- **Linguagem:** o e-book é lido por quem constrói com pedreiro. Explique todo termo técnico na primeira vez que aparecer ([estratégia](../ESTRATEGIA.md), seção 9).
- **Planta grátis do funil:** Casa Compacta (C01), a única com 3D pronto hoje.

## 6. Funil de vendas

Os textos de `vendas/` já vendem o **e-book**:

1. A **planta grátis** é uma página do e-book ([`vendas/material-gratuito.md`](vendas/material-gratuito.md)).
2. A primeira mensagem pergunta o **tamanho do terreno**.
3. A resposta mostra as plantas do e-book que cabem nele ([`vendas/sequencia-whatsapp.md`](vendas/sequencia-whatsapp.md)).

Faltam só os campos entre [colchetes]: título, preço, forma de pagamento e datas, que dependem das decisões do painel.

## 7. Cuidados

- **Plantas originais.** Só entram plantas desenhadas para o produto, ou com licença escrita que permita a venda.
- **Medidas provisórias** até um arquiteto validar.
- **Ilustração.** Móveis e acabamentos são ilustrativos. O e-book não substitui projeto aprovado na prefeitura nem responsável técnico pela obra. Deixe isso escrito no e-book (parte 8).

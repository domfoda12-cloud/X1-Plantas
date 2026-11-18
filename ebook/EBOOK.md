# E-book: dezenas de plantas de casas

> Parte do projeto X1-Plantas. Painel geral: [`../PAINEL.md`](../PAINEL.md).
>
> **Esta pasta é o produto.** Um e-book com dezenas de plantas de casas, com grande variação de tamanho, terreno e uso, cada uma em blueprint, planta humanizada, 3D e animação.

## Nesta pasta

| Arquivo | Para que serve |
|---|---|
| `EBOOK.md` | Este guia: produto, estrutura, página de cada planta, fluxo de produção |
| `catalogo.md` | Lista das 35 plantas propostas, com ficha e situação de cada uma |
| `config.json` | Título, bônus, lançamento atual, planta da capa e da amostra grátis, link das animações |
| `fichas/<ID>.md` | Textos da página de cada planta: para quem é, por que funciona, cuidados, erros que evita |
| `gerador/` | Gera o PDF a partir do catálogo, das fichas e das imagens 3D (seção 8) |
| `saida/` | `ebook.pdf` e `planta-gratis-C01.pdf`, gerados pelo `gerador/` |
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
| 8 | Próximos passos | Responsável técnico, aprovação na prefeitura, orçamento da obra. Aviso: as plantas são **de referência**, não projeto executivo |
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

## 5. Lançamentos e decisões

- **Lançar em levas:** 12 plantas no 1º lançamento, 12 no 2º e 11 no 3º. Quem compra no 1º recebe os outros sem pagar de novo. A coluna **Lançamento** do [catálogo](catalogo.md) diz em qual leva cada planta entra.
- **Título, preço, bônus e versão completa** são decididos no [painel](../PAINEL.md), seção 9, que tem as opções e a recomendação de cada um.
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

## 8. Como gerar o PDF

Na raiz do projeto:

```bash
python3 ebook/gerador/gerar.py
```

Sai em `ebook/saida/`: o **e-book** (`ebook.pdf`) e a **planta grátis** do funil (`planta-gratis-C01.pdf`, só a página dupla, com a frase final que puxa a pergunta do terreno). Com `--previa <pasta>`, também salva um PNG de cada página para revisão.

**O que entra sozinho:** toda planta do catálogo com Situação `3D` ou `pronta`, do lançamento atual ou anterior (`lancamento_atual` em `config.json`), com as 4 imagens em `../animacoes-3d/plantas/<nome>/`. O índice rápido, o sumário, os números de página e os exemplos dos 7 erros se atualizam sozinhos. Cada página dupla começa numa página par, para ficar lado a lado na visualização de duas páginas e na impressão frente e verso.

**Para uma planta nova:** crie `fichas/<ID>.md` copiando o modelo [`fichas/C01.md`](fichas/C01.md). Sem ficha, a planta entra com textos padrão da categoria e campos [entre colchetes], e o gerador avisa.

**Campos entre [colchetes]** saem destacados em amarelo no PDF: título, nº de plantas (aparece sozinho quando todas as plantas do lançamento estiverem prontas), bônus, contato e o QR code. Para o QR code, preencha `link_animacao` em `config.json` com o endereço onde as animações vão ficar, usando `{pasta}` ou `{id}` no lugar do nome (ex.: `https://seusite.com/animacoes/{pasta}.mp4`).

**O gerador avisa** quando uma planta com 3D está sem imagem, sem ficha ou fora do lançamento atual, e quando algum texto passa do limite da página.

Precisa de Python 3 com Pillow e do Node.js com Playwright (Chromium). O QR code usa o pacote `qrcode` do Python.

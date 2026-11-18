# Painel X1-Plantas

> **Comece por aqui.** Este painel mostra o objetivo, as frentes do projeto, a situação de cada uma, as decisões tomadas e o que falta. Atualize a seção 3 sempre que algo avançar.

## 1. Objetivo

Vender um **e-book com dezenas de plantas de casas**, com grande variação, para quem vai construir no Brasil. As pessoas chegam pelos vídeos (Facebook Ads e Instagram), recebem uma planta grátis no WhatsApp e são levadas ao e-book pelo funil.

```
Animações 3D ──► E-book (produto)
     │                 ▲
     ▼                 │
Vídeo + Instagram ──► Funil no WhatsApp
```

- As **Animações 3D** geram as imagens de cada planta. Elas alimentam o e-book, os posts e os vídeos.
- O **Vídeo** e o **Instagram** trazem as pessoas.
- O **funil** (seu parceiro) entrega a planta grátis e oferece o e-book.

## 2. Quem faz o quê

| Pessoa | Responsabilidade | Onde trabalha |
|---|---|---|
| Você | Material (plantas, e-book) e anúncios | [`ebook/`](ebook/EBOOK.md), [`video/`](video/VIDEO.md) |
| Parceiro | Funil: WhatsApp, sequência de mensagens, venda | [`ebook/vendas/`](ebook/vendas/) |
| Editor | Edição e publicação dos vídeos do perfil | [`instagram/`](instagram/INSTAGRAM.md) |
| Apresentador | Gravação dos vídeos | [`video/VIDEO.md`](video/VIDEO.md) (teleprompter) |
| Arquiteto | Validação das plantas | [`ebook/catalogo.md`](ebook/catalogo.md) |
| Claude | Dados das plantas, 3D, vídeos, páginas e textos | Todas as pastas |

## 3. Frentes e situação

| Frente | Guia | Situação | Próximo passo |
|---|---|---|---|
| **Vídeo de anúncio** | [`video/VIDEO.md`](video/VIDEO.md) | 5 versões prontas (38 s), falta o apresentador | Gravar o apresentador com o teleprompter |
| **Animações 3D** | [`animacoes-3d/ANIMACOES-3D.md`](animacoes-3d/ANIMACOES-3D.md) | Motor pronto; 1 planta gerada (Casa Compacta) | Adaptar o motor para várias plantas (seção 6 do guia) |
| **Instagram** | [`instagram/INSTAGRAM.md`](instagram/INSTAGRAM.md) | Rotina, estilo, formatos e plano do perfil prontos; perfil não criado | Criar o perfil e publicar os 5 testes do anúncio |
| **E-book** | [`ebook/EBOOK.md`](ebook/EBOOK.md) | Estrutura e catálogo de 35 plantas propostos | Decidir título, preço e versões; desenhar as plantas em dados |
| **Funil** | [`ebook/vendas/`](ebook/vendas/) | Textos escritos para vender uma planta | Ajustar para vender o e-book |

**Plantas (do [catálogo](ebook/catalogo.md)):** 35 propostas · 1 com 3D (C01) · 0 validadas por arquiteto · 0 páginas do e-book.

## 4. Decisões tomadas

- Tudo em **português do Brasil**, preços em **R$**. Brasil primeiro; outros países depois.
- **Sem landing page:** o anúncio leva direto ao WhatsApp.
- Anúncios no **Facebook Ads**, acompanhamento no **WhatsApp**.
- Gancho principal: **"Vou te economizar os R$ 1.000 que um arquiteto te economizaria"**, em 5 versões para reels de teste.
- Visual: **blueprint azul que ganha vida** e vira **planta humanizada** em 3D.
- Edição no estilo do **Mino Lee** e retenção pelas regras do **Robert McKeaveney** (ver [`instagram/`](instagram/INSTAGRAM.md)).
- Produto: **e-book com dezenas de plantas** em vez de uma planta por vez.
- Plantas **originais**; nada copiado de outros escritórios.

## 5. O que falta (em ordem)

1. **Gravar o apresentador** e montar o anúncio. Teleprompter em [`video/VIDEO.md`](video/VIDEO.md), seção 3.
2. **Decidir título, preço e versões do e-book.** Opções em [`ebook/EBOOK.md`](ebook/EBOOK.md), seção 5.
3. **Adaptar o motor 3D para várias plantas.** É o que permite gerar as dezenas de plantas.
4. **Desenhar as plantas em dados**, começando pelas compactas e estreitas.
5. **Validar as plantas com um arquiteto**, começando pela Casa Compacta.
6. **Montar o e-book em PDF** a partir das imagens e fichas.
7. **Ajustar o funil** para vender o e-book.
8. **Criar o perfil no Instagram** (só você pode criar a conta) e começar a rotina do editor.

## 6. Mapa do projeto

```
PAINEL.md                     ← este painel
video/                        Vídeo de anúncio
  VIDEO.md                      guia: roteiro, teleprompter, gravação, edição
  saida/v1 … v5                 as 5 versões prontas
  anuncios/                     textos de anúncio, brief e checklist
  src/, render.cjs …            código do vídeo e do motor 3D
animacoes-3d/                 Animações 3D das plantas
  ANIMACOES-3D.md               guia: motor, estilo, entregas
  plantas/casa-compacta/        imagens e animação da C01
instagram/                    Espaço do editor
  INSTAGRAM.md                  guia: rotina, retenção, estilo, formatos, testes
  plano-perfil.md               identidade, pilares, primeiros posts
  referencias-mino-lee.md       análise completa das referências
ebook/                        O produto
  EBOOK.md                      guia: estrutura, página da planta, produção
  catalogo.md                   as 35 plantas e a situação de cada uma
  vendas/                       material do funil (parceiro)
```

## 7. Como manter o painel em dia

- A cada planta que avança, atualize a **Situação** no [catálogo](ebook/catalogo.md) e a contagem na seção 3.
- A cada decisão nova, acrescente na seção 4.
- Quando um item da seção 5 for feito, risque e passe para o próximo.

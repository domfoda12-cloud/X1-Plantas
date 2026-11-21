# Plano do e-book: como ele vai ficar e o passo a passo para fazer

> Para o dono aprovar antes de começar. Depois de aprovado, cada passo vira tarefa no [painel](../PAINEL.md). Quem opina em cada passo segue o [Conselho](../CONSELHO.md). **As animações 3D ficam para o fim** (decisão do dono, 20/11/2026).

## Parte 1. Como o e-book vai ficar

### Formato

- **PDF A4 em pé**, lido no celular e impresso sem cortar. Uma ideia por página.
- **Identidade:** azul de projeto `#0B4FA8`, amarelo `#FFC857`, fundo quadriculado nas aberturas, títulos em Bricolage Grotesque, texto em Inter.
- **Tamanho:** cerca de **60 páginas** com 24 plantas (2 por casa + 12 de abertura e fechamento). Arquivo leve (abaixo de 15 MB) para enviar pelo WhatsApp.
- **Rodapé de toda página de planta:** "Planta de referência. O projeto para a prefeitura é assinado por arquiteto ou engenheiro habilitado."

### Sequência de páginas

| Pág. | Página | O que mostra | Por que vende |
|---|---|---|---|
| 1 | **Capa** | "Que casa cabe no seu lote?" · "24 plantas de casas térreas, organizadas pela largura do terreno" · uma planta humanizada grande | Responde à primeira pergunta do Marcos |
| 2 | Aviso e como usar | Planta de referência, quem assina o projeto, como achar a sua casa em 3 passos | Honestidade que vende ([estratégia](../ESTRATEGIA.md), seção 9) |
| 3–4 | **Ache pelo seu lote** | Tabela grande: 5 m, 6 m, 7 m, 8 m, 9 m, 10–11 m, 12 m+ → as casas que cabem e a página de cada uma | O atributo campeão do [banco](vendas/atributos-que-vendem.md) |
| 5 | Ache pelo número de pessoas | 1–2 pessoas, casal com 1 filho, família de 4+, quem vai crescer por etapas | Segunda pergunta do Marcos |
| 6–7 | Como ler uma planta | Cota, porta, janela, peitoril, recuo, "o que é planta humanizada", em desenho | Ele entende a planta e conversa de igual com o pedreiro |
| 8–9 | Os 7 erros que saem caro | Corredor comprido, banheiro longe da cozinha, quarto sem janela, cozinha sem 1,50 m livres… cada um com a planta mostrando o certo | Prova de que o e-book sabe o que faz |
| 10 | Índice rápido | As 24 com área, quartos, banheiros e lote | |
| 11–58 | **As 24 casas** (página dupla, abaixo) | Uma casa a cada 2 páginas, por categoria: Compactas, Estreitas, Família, Especiais | |
| 59 | Terreno e recuos | Como descobrir o recuo da sua cidade antes de escolher; o que perguntar na prefeitura | Evita a decepção "não coube" |
| 60 | Próximos passos | Leve ao engenheiro (o que perguntar), projeto legal, ART ou RRT, financiamento (Caixa pede responsável técnico) | Fecha com confiança, sem prometer |
| 61 | Bônus e contato | Atualizações com plantas novas, checklist de obra, WhatsApp | Abre a venda da próxima versão |

### A página dupla de cada casa

```text
┌──────────────── ESQUERDA ────────────────┐ ┌──────────────── DIREITA ─────────────────┐
│ C01 · CASA COMPACTA          lote 8 x 15+ │ │ C01 · continuação                       │
│ "8 m de frente. 2 quartos. 55 m²."        │ │                                          │
│ ┌──────────────────────┐ ┌─────────────┐ │ │ ┌──────────────┐ ┌──────────────────┐   │
│ │                      │ │ FICHA       │ │ │ │ BLUEPRINT    │ │ O QUE O ARQUITETO│   │
│ │  PLANTA HUMANIZADA   │ │ 55 m²       │ │ │ │ com cotas    │ │ PENSOU           │   │
│ │  (cômodos com nome,  │ │ 2 quartos   │ │ │ │ em metros    │ │ ☀ sol            │   │
│ │   m², móveis,        │ │ 1 banheiro  │ │ │ └──────────────┘ │ 💧 núcleo molhado │   │
│ │   cotas)             │ │ lote 8 x 15 │ │ │                  │ ↔ corredor curto  │   │
│ │                      │ │ frente: sul │ │ │ ┌──────────────┐ └──────────────────┘   │
│ └──────────────────────┘ └─────────────┘ │ │ │ FACHADA ou   │ PARA QUEM NÃO SERVE    │
│ PARA QUEM É                               │ │ │ PERSPECTIVA  │ "Se vai subir um 2º    │
│ Casal com 1 ou 2 filhos, lote de 8 m…     │ │ └──────────────┘  andar, veja a F03"   │
│ ERROS QUE ESTA PLANTA EVITA (1, 3, 5)     │ │ LEVE AO SEU ENGENHEIRO: 3 perguntas     │
│ ────────────────────────────────────────  │ │ [QR: veja a casa ganhar vida]  (fim)    │
│ Planta de referência…                     │ │ Planta de referência…                   │
└───────────────────────────────────────────┘ └──────────────────────────────────────────┘
```

**Imagens de cada casa, em ordem de entrada:**

1. **Agora:** a planta 2D validada (`ebook/plantas/previas/`), redesenhada no estilo do e-book (cores por cômodo, cotas, portas e janelas).
2. **No passo 9 (último):** planta humanizada 3D, perspectiva e animação, quando o 3D for liberado. O motor já está preparado (`ferramentas/planta3d.py` gera os dados das 24); falta só renderizar.
3. **Opcional:** foto realista da fachada (OpenArt, a partir do nosso 3D), com "imagem ilustrativa".

## Parte 2. Passo a passo para fazer

| # | Passo | Quem faz / quem opina | Sai | Como confere |
|---|---|---|---|---|
| 1 | **Juntar o gerador do PDF** que está na branch `frente-ebook` (já copiado, falta adaptar) | Claude · Designer | `ebook/gerador/` funcionando na branch principal | Gera o PDF da C01 sem erro |
| 2 | **Fazer o gerador aceitar plantas em `dados`** (não só em `3D`), usando a planta 2D e as fichas automáticas | Claude · Arquiteto | As 24 casas entram no PDF | `livro.py` lista 24 plantas, 0 avisos de imagem |
| 3 | **Desenho 2D bonito** das plantas: cor por cômodo, nomes, m², cotas internas, portas e janelas, móveis em traço (estilo blueprint claro) | Claude · Designer (`impeccable` só para apontar o genérico) | 24 imagens novas em alta resolução | Designer SIM; Arquiteto confere que o desenho é igual ao dado |
| 4 | **Texto de cada casa** (gancho, para quem é, para quem não serve, erros que evita, 3 perguntas ao engenheiro) | Redator (`/redacao-que-vende`) · Arquiteto confere números · Revisor de risco | `ebook/fichas/<ID>.md` para as 24 | Revisor SIM em todas |
| 5 | **Páginas de abertura e fechamento:** capa, ache pelo lote, ache pelo número de pessoas, como ler, 7 erros, terreno, próximos passos, bônus | Redator · Designer · Revisor | Páginas no gerador | Leitura completa no celular |
| 6 | **Prévia para você** (PDF + PNG de 6 páginas: capa, lote, 1 compacta, 1 estreita, 1 família, próximos passos) | Claude | `ebook/saida/` | **Você aprova ou pede mudança** |
| 7 | **Suas decisões:** título, preço, bônus, se o 1º lançamento sai com 12 ou 24, contato do parceiro | Você (Estrategista traz opções) | `ebook/config.json` preenchido | Sem `[campos]` no PDF |
| 8 | **Revisão de um arquiteto registrado** nas 24 plantas e nas regras | Arquiteto externo | Lista de correções | Correções no `projetos.py` e validador com 0 erros |
| 9 | **3D e animações (por último):** humanizada 3D, perspectiva, animação de 12 s e QR por página; OpenArt + MinoAI para os anúncios | Claude (render) · Editor de vídeo · Arquiteto | `animacoes-3d/plantas/*` e QR no PDF | Imagem igual ao dado; Revisor SIM |
| 10 | **Versão final** e planta grátis do funil (a mais pedida: hoje C01) | Claude · Revisor | `ebook.pdf` e `planta-gratis-*.pdf` | Painel com 0 avisos; commit e push |

**Ordem e tempo:** os passos 1 a 6 são meus e não dependem de você. O 7 e o 8 podem correr em paralelo. O 9 só depois de você liberar.

## Parte 3. O que preciso de você para aprovar este plano

1. O formato (A4, cerca de 60 páginas, página dupla por casa) está bom?
2. Capa com a pergunta "Que casa cabe no seu lote?" está aprovada como direção? O título final continua sendo decisão sua.
3. Posso começar os passos 1 a 6?

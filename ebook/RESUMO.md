# Resumo: Produto: o e-book

> O que o e-book é, o plano, o catálogo e as 24 plantas. **Leia este resumo primeiro**; abra um documento inteiro só quando a tarefa pedir. Índice geral: [`INDICE.md`](../INDICE.md). Quem lê: arquiteto, designer, redator, revisor-de-risco.

## O essencial

<!-- essencial: escrito à mão, o gerador não apaga -->
- PDF A4 de 61 páginas com 24 casas térreas, 2 páginas por casa; o catálogo propõe 35 plantas em 3 levas: 12, 12 e 11 (`EBOOK.md`, `catalogo.md`).
- Gerar: `python3 ebook/gerador/livro.py` cria `ebook/saida/ebook.pdf` e 6 plantas grátis; `--previa <pasta>` salva um PNG por página. Página estourada é erro; o aviso legal nunca fica coberto (`CLAUDE.md`).
- Números vêm do validador, nunca digitados. Textos das casas: `fichas/textos.py`. Mudança de texto passa pelo Revisor de risco (`CLAUDE.md`).
- Regra fixa: a planta é de referência. Nunca dizer que dispensa engenheiro, arquiteto ou pedreiro, nem prometer aprovação, prazo ou custo de obra (`EBOOK.md`, `PLANO-EBOOK.md`).
- Em aberto: título, preço, bônus, WhatsApp e promessa de atualização em `config.json`; revisão das 24 por arquiteto registrado; capa proposta "Que casa cabe no seu lote?" (`CLAUDE.md`, `PLANO-EBOOK.md`).
- Contradição: a C01 tem 50 m² e frente norte em `plantas/PLANTAS.md`; 55 m² em `catalogo.md` e 55 m², frente sul, em `PLANO-EBOOK.md`. O catálogo também difere em E05 (58 e 59), F05 (90 e 91) e S03 (75 e 78).
- Contradição: `fichas/C01.md` fala em hall e 10% de circulação; `plantas/PLANTAS.md` diz que a sala distribui e que o banheiro pede prumada própria.
- Contradição: `EBOOK.md` diz que só a C01 tem 3D; `CLAUDE.md` cita casas em 3D em `visual/3d/`; `PLANO-EBOOK.md` deixa o 3D para o último passo.
<!-- /essencial -->

## Os 6 documentos

### [E-book: regras desta pasta](CLAUDE.md)

O Claude Code carrega este arquivo sozinho quando trabalha aqui. As regras gerais estão no `CLAUDE.md` da raiz.

Tamanho: 197 palavras.

### [E-book: dezenas de plantas de casas](EBOOK.md)

Parte do projeto X1-Plantas. Painel geral: `../PAINEL.md`. Esta pasta é o produto. Um e-book com dezenas de plantas de casas, com grande variação de tamanho, terreno e uso, cada uma em blueprint, planta humanizada, 3D e animação.

Seções: Nesta pasta; 1. O produto; 2. Estrutura do e-book; 3. Página dupla de cada planta; 4. Fluxo de produção de cada planta; 5. Lançamentos e decisões; 6. Funil de vendas; 7. Cuidados.

Tamanho: 1129 palavras.

### [Plano do e-book: como ele vai ficar e o passo a passo para fazer](PLANO-EBOOK.md)

Para o dono aprovar antes de começar. Depois de aprovado, cada passo vira tarefa no painel. Quem opina em cada passo segue o Conselho. As animações 3D ficam para o fim (decisão do dono, 20/11/2026).

Seções: Parte 1. Como o e-book vai ficar; Parte 2. Passo a passo para fazer; Parte 3. O que preciso de você para aprovar este plano.

Tamanho: 1323 palavras.

### [Catálogo de plantas do e-book](catalogo.md)

Parte da pasta E-book. Guia da frente: `EBOOK.md`. Painel geral: `../PAINEL.md`. Proposta de variação: 35 plantas em 5 categorias, para cobrir os terrenos, famílias e usos mais comuns. Nomes, áreas e lotes são provisórios até um arquiteto validar. Atualize a coluna Situação conforme cada planta…

Seções: Resumo; C. Compactas: primeira casa, orçamento curto; E. Terreno estreito: frente de 5 a 8 m; F. Família: 3 ou 4 quartos; S. Especiais: um uso ou terreno específico; O. Sobrados: dois pavimentos; Casas que crescem; O que vem em cada planta do e-book.

Tamanho: 1796 palavras.

### [C01 · Casa Compacta](fichas/C01.md)

Ficha da página do e-book. O que não estiver aqui (área, quartos, banheiros, lote) vem do catálogo. Mesmo texto da planta grátis: ver ../vendas/material-gratuito.md.

Seções: Para quem é; Por que funciona; Cuidados antes de construir; Erros que evita.

Tamanho: 167 palavras.

### [As 24 plantas: ficha de cada uma](plantas/PLANTAS.md)

Gerado por `python3 ferramentas/plantas.py fichas`. Parte da pasta E-book (`../EBOOK.md`). Regras: `../referencias/regras-do-arquiteto.md`. Plantas de referência: o projeto para a prefeitura é assinado por arquiteto ou engenheiro habilitado.

Seções: C01 · Casa Compacta; C02 · Casa Studio; C03 · Casa Inicial; C04 · Casa Duo; C05 · Casa Popular; C06 · Casa Compacta Suíte; C07 · Casa Compacta Varanda; E01 · Casa Estreita; E02 · Casa Corredor; E03 · Casa Fita; E04 · Casa Pátio; E05 · Casa Estreita Suíte; E06 · Casa Estreita Gourmet; E07 · Casa Estreita 3 Quartos; ….

Tamanho: 3757 palavras.

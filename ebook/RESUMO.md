# Resumo: Produto: o e-book

> O que o e-book é, o plano, o catálogo e as 24 plantas. **Leia este resumo primeiro**; abra um documento inteiro só quando a tarefa pedir. Índice geral: [`INDICE.md`](../INDICE.md). Quem lê: arquiteto, designer, redator, revisor-de-risco.

## O essencial

<!-- essencial: escrito à mão, o gerador não apaga -->
- PDF A4 de 61 páginas com 24 casas térreas, 2 páginas por casa (páginas 10 a 57); o catálogo propõe 35 plantas em 3 levas: 12, 12 e 11 (`EBOOK.md`, `catalogo.md`, `gerador/livro.py`).
- Gerar: `python3 ebook/gerador/livro.py` cria `ebook/saida/ebook.pdf` e 5 plantas grátis; `--previa <pasta>` salva um PNG por página. Página estourada é erro; o aviso legal nunca fica coberto (`CLAUDE.md`).
- Números vêm do validador, nunca digitados: em caso de dúvida vale `plantas/PLANTAS.md` (C01: 50 m², frente norte, lote 8 x 15). Textos das casas: `fichas/textos.py`. Mudança de texto passa pelo Revisor de risco (`CLAUDE.md`).
- Cada casa tem planta mobiliada, casa no lote, "Informação da casa", vista da rua (foto ilustrativa em C01, C03, E07 e F01; desenho nas outras) e a casa em 3D nas 24 (`visual/3d/`). Não tem blueprint separado, perspectivas, animação, QR nem checklist de obra (`EBOOK.md`, seção 3).
- Regra fixa: a planta é de referência. Nunca dizer que dispensa engenheiro, arquiteto ou pedreiro, nem prometer aprovação, prazo ou custo de obra (`EBOOK.md`).
- Em aberto (dono): título, preço, bônus, contato, promessa de atualização, garantia e se o 1º lançamento sai com 12 ou 24; revisão das 24 por arquiteto registrado (`EBOOK.md`, seção 8).
- A foto de fachada da C01 saiu em 22/11 (vista da rua simplificada); fotos só em C03, E07 e F01. O mockup `casa-c01-celulares.png` ainda é da C01 antiga (`EBOOK.md`, seção 8).
<!-- /essencial -->

## Os 4 documentos

### [E-book: regras desta pasta](CLAUDE.md)

O Claude Code carrega este arquivo sozinho quando trabalha aqui. As regras gerais estão no `CLAUDE.md` da raiz.

Tamanho: 200 palavras.

### [E-book: plantas de casas térreas](EBOOK.md)

Parte do projeto X1-Plantas. Painel geral: `../PAINEL.md`. Esta pasta é o produto. Hoje: um PDF A4 de 61 páginas com 24 casas térreas, cada uma com a planta mobiliada, a casa desenhada no lote, a ficha com os números do validador, a vista da rua e a casa em 3D. O catálogo propõe 35 casas no total;…

Seções: Nesta pasta; 1. O produto; 2. O PDF, página por página; 3. As duas páginas de cada casa; 4. Como uma casa entra no e-book; 5. Lançamentos e decisões; 6. Funil de vendas; 7. Cuidados; 8. O que falta.

Tamanho: 1534 palavras.

### [Catálogo de plantas do e-book](catalogo.md)

Parte da pasta E-book. Guia da frente: `EBOOK.md`. Painel geral: `../PAINEL.md`. Proposta de variação: 35 plantas em 5 categorias, para cobrir os terrenos, famílias e usos mais comuns. 24 já estão no PDF; as outras 11 são ideia. Nas 24, área, quartos, banheiros e lote são os do validador…

Seções: Resumo; C. Compactas: primeira casa, orçamento curto; E. Terreno estreito: frente de 5 a 8 m; F. Família: 3 ou 4 quartos; S. Especiais: um uso ou terreno específico; O. Sobrados: dois pavimentos; Casas que crescem; O que vem em cada planta do e-book (hoje).

Tamanho: 1957 palavras.

### [As 24 plantas: ficha de cada uma](plantas/PLANTAS.md)

Gerado por `python3 ferramentas/plantas.py fichas`. Parte da pasta E-book (`../EBOOK.md`). Regras: `../referencias/ARQUITETO.md`. Plantas de referência: o projeto para a prefeitura é assinado por arquiteto ou engenheiro habilitado.

Seções: C01 · Casa Compacta; C02 · Casa Studio; C03 · Casa Inicial; C04 · Casa Duo; C05 · Casa Popular; C06 · Casa Compacta Suíte; C07 · Casa Compacta Varanda; E01 · Casa Estreita; E02 · Casa Corredor; E03 · Casa Fita; E04 · Casa Pátio; E05 · Casa Estreita Suíte; E06 · Casa Estreita Gourmet; E07 · Casa Estreita 3 Quartos; ….

Tamanho: 3755 palavras.

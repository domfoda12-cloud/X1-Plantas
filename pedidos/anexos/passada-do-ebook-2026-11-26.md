# Passada do e-book página por página (fila da noite, item 3, 26/11/2026)

> Prévia em duas partes, 24 páginas. Olhares: Bia (Designer e comprador), Nilo (técnica), Vera (risco, uma leitura no fim). Nada foi para `ebook/saida/`; o PDF final é do dono. Imagens da prévia, com as 5 frases marcadas em amarelo "PROPOSTA": [`previa-noite-2026-11-26/`](previa-noite-2026-11-26/).

## Aplicado no gerador (commits `bf2266c` e `5b025d6`; como desfazer: `git revert` de cada um)

| O quê | Onde | Achado de |
|---|---|---|
| Lado do sol espelhado no validador: corrigido; C01 e E03 melhores com a rua ao sul (F01 não muda); 13 das 24 plantas trocam; prova no `checar.py` | `ferramentas/plantas.py` (`ORIENTACAO`), `ferramentas/checar.py` | Nilo |
| "Frente mínima" saía no fundo do lote: agora na faixa da rua, letra maior | `ebook/gerador/livro.py` (`svg_lote`) | Bia |
| Rodapé cobria a fita amarela da última página | `livro.py` (página "fim") | Bia |
| Varanda da C01: a frase dizia que a lei proíbe o que a casa tem | `plantas.py` (aviso da varanda na divisa) | Nilo |
| "Protegida do sol direto" (conforto sem medida) virou "de parte do sol" | `plantas.py` (`pensou`) | Nilo |
| "Vão livre de 4,6 m" (o 4,6 é entre paredes; o livre é 4,45) | `livro.py` (`avisos_juntos`) | Nilo |
| Glossário: "área construída" agora inclui varanda e garagem cobertas | `ebook/gerador/paginas.py` | Nilo |
| C01 "melhor com a rua ao sul" no texto de venda | `ebook/vendas/WHATSAPP.md` | Nilo |

## Proposto, ainda não aplicado (em ordem de efeito)

1. **Casa no lote ilegível no celular (págs. 5, 9, 13 e 20):** pôr a planta de verdade no lote (`svg_no_lote`, já usada na pág. 3) e letra de uns 8 pt. Bia.
2. **Parede da varanda da C01 desenhada** na planta e no 3D (hoje tracejada, aberta). Nilo. Mexe no desenho e no motor 3D.
3. **Faixa de lote em volta da casa (capa e págs. 4, 8, 12) com recuos menores que os de referência** ao lado da régua: fazer como a pág. 14. Nilo.
4. **Vista da rua:** cortar o céu, desenhar muro e portão no recuo da entrada, fita "5 m" no chão. Bia.
5. **Ganchos das casas** [texto público, Caio e Vera]: E03 "5 m de frente e cabem 2 quartos. 56 m²."; F01 "10 m de frente. 3 quartos, todos com janela. 71 m²."; `.gancho` de 14 para 17 pt. Bia.
6. **Págs. 18 e 19 com 25% e 40% em branco:** tabela "Qual casa evita qual erro". Bia.
7. **Cômodo a cômodo (págs. 7, 11, 15):** planta pequena com os números no topo; tirar a nota repetida. Bia.
8. **"Como ler uma planta" (pág. 16):** círculos numerados na planta ligados aos 9 itens. Bia.
9. **Casa Fita (pág. 4):** duas colunas quando a casa é estreita. Bia.
10. **Ficha do terreno (pág. 22):** desenho do lote com os espaços para anotar; linha "Olhando da rua, o nascente fica à esquerda ou à direita?" (Nilo). Bia e Nilo.
11. **Taxa de ocupação na ficha de cada casa** (E03 55%, C01 53%, F01 55% no lote mínimo) [texto público]. Nilo.
12. **Validador:** medir o vão de cômodos ligados por "aberto" como um ambiente só (F01: 6,7 x 4,8 m). Nilo.
13. **Textos com "rua ao norte" para C01 e E03 fora do gerador:** `pedidos/anexos/guia-seu-lote-cabe-texto.md` (rascunho, já com aviso), `ebook/revisao/ebook-texto.txt` (regenera com o PDF).

**Recusado, com motivo:** "Família de 4 ou mais" → "4 ou 5" (pág. 3): o grupo vale para 6 casas, não só a F01.

## As 5 frases (proposta marcada; o dono escolhe)

Na prévia, em amarelo, as opções recomendadas, com as trocas da Vera: C01 (pág. 8), F01 (pág. 12), glossário (pág. 17), ficha (pág. 22), passos (pág. 23). Textos e vetos: `frases-dor-5-paginas-opcoes-2026-11-26.md` e `veto-frases-dor-5-paginas-2026-11-26.md`. Nenhuma página estourou.

## Leitura da Vera

(a preencher quando ela voltar)

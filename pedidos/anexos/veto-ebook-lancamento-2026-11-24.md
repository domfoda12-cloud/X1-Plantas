# Veredito do Revisor de risco: rascunho do lançamento (24/11/2026)

> Passo A1 do `pedidos/PLANO.md`. O Revisor leu o PDF direto: 17 páginas do e-book e 3 da planta grátis. **SIM (rascunho): nada é veto.** Nenhuma página promete aprovação, prazo ou custo; nenhuma dá a entender que dispensa profissional.

## Trocas que não dependiam do dono

| Onde | Troca | Estado |
|---|---|---|
| p9, p11, p13 | "Lote comercial" → "Lote comum" (podia ser lido como lote de uso comercial) | feito (`ebook/gerador/livro.py`) |
| p9, varanda na divisa da Casa Compacta | juntar o art. 1.301 do Código Civil (varanda a menos de 1,5 m do vizinho) e "o engenheiro confirma" | feito (`ferramentas/plantas.py`; texto do artigo conferido em `leis-conferidas-2026-11-23.md`) |
| planta grátis, p2 | "Este e-book" → "O e-book completo"; "no fim do e-book" → "no fim do e-book completo" | feito (`livro.py`, só na planta grátis) |
| p7 | dizer "(pág. 14)" depois de "A seção Terreno e recuos mostra como" | **não feito**: o número da página muda com a edição e hoje seria digitado à mão; fica para quando houver o número calculado |
| p3 | "Família de 4 ou mais" → "4 ou 5" na Família Compacta | **não feito**: o rótulo é de um grupo de 6 casas do catálogo; "4 ou mais" não é falso. Fica anotado |
| capa | um "Planta de referência" pequeno embaixo da planta | recomendação, não condição; não feito |

## Depende do dono

- Preço (`config.json` ainda com "[preço]").
- Bônus: estão no `config.json`, o PDF não cita nenhum (correto hoje); o anúncio não pode prometer bônus antes de as páginas existirem.
- Amostra grátis final.
- O número de WhatsApp da última página: confirmar que é o chip do negócio, não o pessoal.
- Nome ou CNPJ do vendedor também dentro do e-book? (A lei pede na oferta, não no PDF.)

## Não conferido pelo Revisor

Cada janela e porta do 3D contra os dados; a origem de cada foto; as outras 21 casas; posts, roteiros e a calculadora.

**Tarefa:** vídeo do meme e do POV do caramelo (ficha `2055-video-reel`): plano detalhado vetado; e a régua do veto (ficha `2102`).
**Feito:** plano versão 4: 3 rodadas do time (Editor, Revisor, Arquiteto, Estrategista) e o veto do Fable, todas as correções aplicadas; notas de cada veto na ficha.
**Feito:** régua do veto (5 pontos) em `pedidos/LEIA-ME.md`; repreensão vira "Lições" no contexto; 12 regras em `contexto/CONVIVENCIA.md`.
**Feito:** `pedido.py` mostra o prompt que copia e aceita `--de` (a ficha tinha pegado o prompt errado); auditoria 3 corrigida; plano de tudo com a fase 6 (vender e medir).
**Como conferir:** `python3 ferramentas/checar.py`; ficha 2055, seções "versão 4" e "Qualidade do veto".
**Não feito / ressalva:** nada gerado nem gasto; agentes com ferramentas novas só valem na próxima conversa (o Estrategista já custou 37 mil em vez de 80 mil).
**Decisão do dono pendente:** as 7 perguntas do passo 3 da ficha 2055 (onde entra o meme, qual vídeo do WhatsApp, Instagram, A/B, zoom out, quem dança, PLANTA ou LOTE).
**Próximo passo:** com as respostas, passos 4 a 7 da ficha 2055; sem elas, a E07 (ficha 1616) ou o "Tempo livre" do `pedidos/PLANO.md`.
## 2026-11-23-1955-lancamento-3-casas

**Tarefa:** refazer o e-book para o lançamento com 3 casas e deixar pronto o caminho da venda (fichas `1946-refazer`, `1946-quadro`, `1946-melhorar`, `1946-design`).
**Feito:** C01 com hall é a oficial, 51 m² (`ebook/plantas/projetos.py`, textos de venda trocados com o Revisor); estilo novo das plantas e da capa no gerador (`ebook/gerador/livro.py`, `livro.css`); 3D sem espelho (`ferramentas/planta3d.py`), 6 imagens refeitas; `ebook/vendas/RESPOSTAS-RAPIDAS.md`; bases `ebook/referencias/anuncios-ref/` (39 anúncios, design de 13 concorrentes); júri com regras novas (`CONSELHO.md` 5b); `ferramentas/salvar.py`.
**Como conferir:** `python3 ferramentas/checar.py` ("Tudo certo", com 2 avisos: janela em cima de porta em 16 casos e preço pendente); quadro do dono em https://claude.ai/artifact/R8SSzqnZxR6XafEP5uXBtX (coleção `tarefas`).
**Não feito / ressalva:** 18 imagens 3D ainda espelhadas; consertos de página (3D pequeno, foto da E07); PDF de emergência só em rascunho no scratchpad (6,5 MB, páginas viram imagem); branch `sistema/everything-claude-code` pronta, sem pull request; ganchos novos não testados numa conversa nova.
**Decisão do dono pendente:** amostra grátis (A, B, ou A agora e B depois: `pedidos/anexos/amostra-gratis-opcoes.md`); Instagram próprio ou novo; aprovar E03R, F01R e o conserto da janela da C01 (`ebook/plantas/rascunhos/C01J.py`); everything-claude-code inteiro ou só 6 peças; mais liberdade para o Maestro.
**Próximo passo:** ler os comentários do dono no quadro; depois gerar o PDF real (`python3 ebook/gerador/livro.py`) quando as 3 casas estiverem aprovadas.

# Auditorias do Supervisor (Fable)

> Uma linha por auditoria, escrita pelo agente `supervisor` (regras em [`LEIA-ME.md`](LEIA-ME.md)). A cada 3 fichas fechadas, `ferramentas/pedido.py` avisa que é hora da próxima.

| Data | Fichas conferidas | Erros (alta / média / baixa) | Principal achado |
|---|---|---|---|
| 22/11/2026 | 3: sistema questionador (1526), contradições e divisão por modelo (1800), o porquê de cada prompt (1900) | 1 / 6 / 6 | O "Pronto quando" das três se cumpre e o `checar.py` passa; números de venda batem com os dados (C01 50 m², 14/11/17/22/1 casas por lote, 21 e 18 banheiros). Alta: `ebook/vendas/material-gratuito.md` manda o parceiro enviar a planta grátis da E07, que o dono chamou de erro de layout e está na fila do redesenho. Médias: `ebook/EBOOK.md` ainda diz que a foto antiga da C01 sai no PDF (4 fotos; são 3); `pedidos/RESUMO.md` ainda põe o Fable como condutor; `video/anuncios/brief-criativo.md` abre o vídeo na planta se montando; o `ebook.pdf` imprime "[bônus: decisão do dono]" e "[contato do parceiro]" sem trava; `ebook/revisao/*.txt` é o PDF de 20/11 (C01 com 55 m²); `CONTEXTO.md`, `PAINEL.md` e `video/VIDEO.md` apontam vídeos já apagados. Não conferido: os 111 blocos de `intencoes/` um a um, os vídeos assistidos, a calculadora, os posts, o Haiku na prática. |

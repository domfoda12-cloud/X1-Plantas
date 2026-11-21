# Orçamento: limite semanal do Claude e créditos do OpenArt

> Pedido do dono (20/11/2026): dividir o que resta entre as três partes que faltam: **e-book, animações e vídeo**. Ver também [`CONTEXTO.md`](CONTEXTO.md) e [`PAINEL.md`](PAINEL.md).

## O que dá para medir daqui

- **Limite semanal do Claude:** esta sessão **não enxerga** quanto resta. Ele aparece para o dono em claude.ai, em Configurações → Uso. A divisão abaixo é em **porcentagem do que restar**.
- **Esta sessão até agora:** cerca de 1 milhão de tokens escritos e 347 milhões lidos do cache, com o contexto em 84% (perto de ser resumido). A maior parte do gasto vem de reler a conversa longa a cada passo e de abrir imagens para conferir.
- **OpenArt:** saldo de **115 créditos** em 21/11/2026 (plano Starter), medido pela ferramenta da conta. Os últimos 1.400 foram para 8 clipes de vídeo (Kling 3.0, 175 cada), a pedido do dono ("gaste o resto no vídeo"). Com 115 não dá para outro clipe; dá para rascunhos de imagem.

## A divisão (qualidade em primeiro lugar)

| Parte | % do limite que resta | Créditos do OpenArt | O que falta, em ordem |
|---|---|---|---|
| **Animações 3D** | **45%** | **1.500** | 1) Renderizar as 24 casas no motor 3D (já lê os dados; falta rodar e conferir); 2) aplicar as melhorias do [banco de referências](animacoes-3d/REFERENCIAS-BLUEPRINT.md) (câmera quase plana que "abre", porta e janela abrindo, piso varrendo, final parado); 3) animação de 12 s das casas mais pedidas; 4) vídeo gerado a partir das nossas imagens (PixVerse V6 para testar, Veo 3.1 ou Wan 3.0 para a final) |
| **Vídeo (anúncios e reels)** | **30%** | **800** | 1) Refazer os 5 vídeos de anúncio com a C01 nova (hoje usam o desenho antigo); 2) vídeo 2 "3 quartos em 8 m"; 3) reels 1 e 4 com o B-roll do e-book; 4) imagens de apoio no OpenArt (capas de reel, cenas). A edição final é da MinoAI no Mac do dono |
| **E-book** | **25%** | **450** | 1) Fachada realista das casas mais pedidas (imagem para imagem a partir da nossa vista da rua, extra-alta); 2) foto da C03 na página dela; 3) revisão final do Revisor de risco; 4) campos do dono (título, preço, bônus, contato) e PDF final |
| **Reserva** | — | ~**0** | O que sobrar fica para corrigir o que o arquiteto revisor pedir |

**Por que essa ordem:** o e-book já está quase pronto (61 páginas, 24 casas, fotos); as animações são a parte maior e mais pesada que falta, e o vídeo depende delas (o anúncio precisa da casa nova em movimento).

## Como gastar menos sem perder qualidade

1. **Sessão nova por parte.** Esta conversa está enorme; cada passo relê tudo. Uma sessão nova para as animações, outra para o vídeo, cada uma começando pelo `CONTEXTO.md`, custa bem menos por tarefa.
2. **Loop mais espaçado.** Rodadas automáticas só quando houver tarefa clara; nada de rodada para "conferir se mudou algo".
3. **Conferir imagem por folha de miniaturas**, uma vez por lote, e não imagem por imagem.
4. **Revisor de risco só no que vai ao público** e uma vez por peça pronta.
5. **No OpenArt:** rascunho barato (5 créditos), final em extra-alta (123), máxima só na peça principal ([guia](animacoes-3d/OPENART-MINOAI.md)).

## Para fechar a conta em números

Diga quanto do limite semanal resta (a porcentagem que aparece em Configurações → Uso) e esta tabela vira número exato por parte.

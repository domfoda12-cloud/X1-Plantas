# Opus responde, Fable supervisiona; limpeza de mídias; releitura para refazer

**Estado:** fechada em 22/11/2026

**Prompt (palavra por palavra):** Put Opus as the main question answerer, and make him summon Fable when he starts to struggle or detect that he made an error, Ocasionnaly Fable should check up on the work that OPUS did and point out the errors
1, 2  4 faca isso,
Quero que faca uma leitura de cada trabalho feito no ebook e videos, Veja o que foi reclamado, o que funcionou, e refaca tudo do zero assim que o limite reiniciar, apague as outras blenders, videos, i dont need it just most of the information
OVERRULE, the last video should be saved

**O que ele pediu, parte por parte:** 1) "Put Opus as the main question answerer": o Opus vira o modelo da conversa principal. 2) "make him summon Fable when he starts to struggle or detect that he made an error": o Opus chama o Fable quando trava ou percebe erro. 3) "Occasionally Fable should check up on the work that OPUS did and point out the errors": auditoria periódica; o Fable aponta, não refaz. 4) "1, 2, 4 faça isso": da lista de melhorias: arquivar as conversas antigas e apagar as branches velhas; juntar os dois tipos de ficha; script de preparação das conversas novas. 5) "leitura de cada trabalho feito no ebook e videos… o que foi reclamado, o que funcionou": retrospectiva. 6) "refaça tudo do zero assim que o limite reiniciar": refazer depois, não agora. 7) "apague as outras blenders, vídeos… just most of the information": apagar renders e vídeos, guardar a informação (documentos). 8) "OVERRULE, the last video should be saved": o último vídeo fica.

**Por que ele pediu, ou o que quer descobrir:** Ele viu muita coisa refeita e errada (C01 velha em todo lugar, vídeos com selo e planta errada) e quer recomeçar limpo, guardando só o que aprendeu. Na troca de modelo: quer o mais barato respondendo e o mais forte só onde há erro ou dúvida, e quer alguém conferindo o trabalho, porque já viu "feito" que não estava feito.

**Objetivo dele:** Refazer e-book e vídeos do zero, certo de primeira, com um sistema que se confere sozinho; e não gastar o modelo forte onde não precisa.

**Ligação com as ideias gerais do projeto:** Fio 6 (qualidade onde importa, economia onde ninguém vê), fio 8 (ele confere: agora o sistema confere antes dele), fio 3 (nada se perde: apaga a mídia, guarda a informação e o último vídeo) e fio 1 (parece de verdade: recomeçar com a C01 certa).

**Perguntas que me fiz:** (ficha anterior à regra de 22/11/2026)

**Pronto quando:** Opus como modelo padrão e o agente `supervisor` (Fable) registrado, com socorro e auditoria escritos e o aviso de auditoria no `pedido.py`; uma ficha só no `CLAUDE.md`; conversas antigas arquivadas e branches velhas apagadas; script de preparação proposto; vídeos e renders antigos apagados, com o último vídeo guardado; `contexto/dono/RETROSPECTIVA.md` com o que foi reclamado, o que funcionou e o plano para refazer; `checar.py` passando.

**Suposições (o dono não disse):** "O último vídeo": guardei o último feito (convite da F03, 22/11) e também o último que mostrei a ele nesta conversa (principal de 21/11), porque a frase serve aos dois; o resto volta pelo git se ele quiser. Guardei também a gravação da voz dele (é informação dele, não render) e a trilha. Não apaguei as imagens do e-book (3D, fotos, mockups): são o produto, não render de vídeo. "Blenders" li como renders 3D e 2D. "Assim que o limite reiniciar": não sei quando reinicia; o plano fica pronto e espera o sinal dele.

**Quem executa:** Opus na conversa principal: troca de modelos, limpeza, itens 1, 2 e 4. Opus (agente geral): retrospectiva e plano. Fable (`supervisor`): primeira auditoria, nas fichas de 22/11.

**Conferência:** Opus como modelo padrão: `.claude/settings.json` tem `"model": "opus"`. Agente `supervisor` com `model: fable`: a primeira auditoria rodou nele (prova). Mídias: `git ls-files` mostra só o convite e o principal em `video/saida/`; mídia rastreada caiu de 314 para 72 MB; a voz do dono e a trilha ficaram. Conversas antigas: as 5 voltaram como "ARCHIVED". Branches: NÃO apagadas: o acesso ao GitHub desta máquina bloqueia apagar branch ("Write access to this GitHub API path is not permitted through this proxy"); o dono apaga em github.com/domfoda12-cloud/X1-Plantas/branches. Ambiente: "x1-plantas" criado com o script de preparação, testado a partir da pasta acima do repositório; não testei uma conversa nova nele. Retrospectiva: lida por amostra (o que se repete e o plano). Graphify depois da limpeza: 2.177 → 2.013 círculos. Auditoria do Fable apontou que três documentos ainda pediam para assistir vídeos apagados: corrigidos.

**Resultado:** Opus é o modelo padrão (`.claude/settings.json`) e o Fable virou o agente `supervisor` (socorro e auditoria a cada 3 fichas; a primeira já rodou). Vídeos, clipes e renders antigos apagados (ficam no git); guardados o convite, o principal de 21/11, a voz do dono e a trilha. Uma ficha só, em `pedidos/`. Conversas antigas arquivadas; branches velhas não puderam ser apagadas daqui (o dono apaga no GitHub). Ambiente "x1-plantas" com o motor 3D na preparação. Retrospectiva e plano para refazer em `contexto/dono/RETROSPECTIVA.md`; retomada agendada para 13h15 (Brasília).


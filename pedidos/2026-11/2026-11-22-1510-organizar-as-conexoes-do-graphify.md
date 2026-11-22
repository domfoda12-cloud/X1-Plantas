# Organizar as conexões do Graphify

**Estado:** fechada em 22/11/2026

**Prompt (palavra por palavra):** Estou vendo MUITAS conexoes disorganizadas no graphify, como ajeito isso?

**O que ele pediu, parte por parte:** "Muitas conexões desorganizadas no Graphify": o grafo (2.121 círculos, 2.322 ligações, 330 grupos) não mostra um sistema, mostra um emaranhado de ilhas. "Como ajeito isso?": quer o caminho, e quer ver arrumado.

**Por que ele pediu, ou o que quer descobrir:** Ele quer abrir o Graphify e ver as partes do projeto conversando (já disse: "quero ver um monte de círculos interagindo como um sistema de verdade"). Hoje cada programa aparece solto, porque um chama o outro rodando um comando (subprocess, node), e o Graphify só desenha ligação de import, de chamada de função e de link em documento.

**Objetivo dele:** Ver o projeto como um sistema: a planta entra, vira dados, vira PDF, 3D e vídeo; e os agentes e regras em volta. E poder confiar no Graphify como mapa.

**Ligação com as ideias gerais do projeto:** Fio 3 (nada se perde: um mapa que liga tudo) e fio 8 (ele confere: quer ver, não só ouvir que está organizado).

**Perguntas que me fiz:** (ficha anterior à regra de 22/11/2026)

**Pronto quando:** Existe um mapa do sistema com cada programa e cada dado ligado na ordem em que um alimenta o outro; o checar.py falha se aparecer programa fora do mapa; depois do push, o Graphify reindexa e o número de grupos soltos cai (medido com graph_stats, antes 330).

**Suposições (o dono não disse):** Não vejo a tela do Graphify: trabalho pelos números que a ferramenta devolve. Não apago o sistema antigo de vídeo (v1 a v5, render.cjs, cena.js) sem o "sim" dele, porque são entregas e o fio 3 pede não perder nada.

**Quem executa:** Fable/Opus na conversa principal (é peça do sistema, uma vez só; o supervisor pode fazer).

**Conferência:** Medi com graph_stats antes e depois. Antes: 2.121 círculos, 2.322 ligações, 330 grupos. Depois do mapa: 2.177, 2.353, 348. **O mapa não ligou os programas**: o Graphify transformou cada nome do mapa num círculo novo (mapa_checar, mapa_livro...), sem ligação com o arquivo de verdade (graphify_file_neighbors do MAPA: 0 vizinhos). Ou seja, link em documento não liga código no Graphify; só import e chamada de função ligam. O mapa fica, porque serve aos agentes, mas não resolve o grafo. Depois de apagar o sistema antigo de vídeo e as mídias (22/11, commit 3f775da): 2.013 círculos, 2.231 ligações, 292 grupos (antes da limpeza: 2.177, 2.355, 348). Medido de novo: o grosso vem dos 126 documentos, não do código.

**Resultado:** O Graphify só liga código por import e chamada; link em documento não liga (o mapa do sistema criou 21 círculos soltos, medido). O que baixou os números foi apagar o sistema antigo de vídeo e as mídias: 2.177 → 2.013 círculos, 348 → 292 grupos. O grosso que resta vem dos 126 documentos: a organização da próxima sessão (ficha própria) junta documentos e tira código repetido. `MAPA-DO-SISTEMA.md` fica, para os agentes.


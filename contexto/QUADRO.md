# Quadro de avisos: o que o dono acabou de pedir

> **Todo agente e toda conversa lê este quadro antes de trabalhar** (regra do dono, 22/11/2026: "depois de cada pedido, SEMPRE informe todo mundo do que está acontecendo, crie um contexto a partir disso e alimente todos"). Quem atende o pedido escreve aqui, no topo, e apaga o mais antigo: ficam os 5 últimos. O histórico inteiro está em [`CONTEXTO-HISTORICO.md`](../CONTEXTO-HISTORICO.md).

## 22/11 · Vídeo: sequência de escaneamento e pedidos que não se perdem

- **O dono pediu:** uma sequência de "escaneamento" de 1,2 s no vídeo principal (cotas → malha 3D → etiquetas → casa pronta, só corte seco) e que toda informação que ele der sobre vídeo fique guardada. Vai filmar com o celular daqui a alguns dias.
- **O que mudou:** [`video/PEDIDOS-DO-DONO.md`](../video/PEDIDOS-DO-DONO.md) guarda toda ordem de vídeo com as palavras dele; `video/scan.py` gera a sequência; `video/saida/principal-condor/` tem o vídeo de 21 s, sem OpenArt.
- **Atenção, é rascunho:** a sequência usa a **E07** (única casa que bate com os números do dono: 72 m², 3 quartos, 1 suíte, 2 banheiros, 8 m de frente), e a série E está na fila do redesenho. Não publicar antes de o dono decidir: esperar o redesenho ou trocar de casa.
- **Editor de vídeo:** leia `video/PEDIDOS-DO-DONO.md` antes de qualquer edição. **Arquiteto:** se a E07 mudar, rode `python3 video/scan.py E07` e monte de novo. **Revisor de risco:** ainda não viu este vídeo.

## 22/11 · Todo pedido vira aviso para todos

- **O dono pediu:** depois de cada pedido, informar todos e alimentar o contexto de cada um.
- **O que mudou:** este quadro existe; a regra está no `CLAUDE.md`.
- **Para todos:** ao terminar um pedido do dono, escreva o aviso aqui (o que ele pediu, o que mudou, o que muda para cada papel) e atualize o `contexto/<agente>.md` de quem foi afetado.

## 22/11 · O arranjo das plantas foi reprovado

- **O dono pediu:** o Arquiteto estudar mais, em sites que arquitetos de verdade usam; "o último layout não fazia sentido".
- **O que mudou:** apostila 2 ([`arquiteto-sites-de-profissionais.md`](../ebook/referencias/arquiteto-sites-de-profissionais.md)) com o diagnóstico das 24 plantas e um método de 10 passos. **Nenhuma planta mudou ainda**; refazer espera o dono dizer quais e quando.
- **Arquiteto:** arranjo antes da medida; toda planta parte de um projeto real; olhe a prévia antes de opinar.
- **Designer e Editor de vídeo:** as plantas vão mudar. Não produza imagem, 3D ou vídeo novo das casas da série E, das compactas e da F02 até o redesenho; o que existe fica como rascunho.
- **Redator e Estrategista:** não escreva texto novo elogiando o arranjo ("sem corredor", "cômodos independentes") antes do redesenho. Planta que faz sentido é o que evita reembolso.
- **Revisor de risco:** casa em que o banheiro só se alcança por fora (série E, menos a E04) precisa dizer isso na ficha enquanto não for redesenhada.
- **Pesquisador:** faltam ler o manual da CDHU, as pranchas de concursosdeprojeto.org e 5 projetos do ArchDaily com a planta aberta.
- **Maestro:** a base da MinoAI diz que a pessoa compra porque confia no seu conhecimento (lição "Ideal Viewer Persona (IVP)"); planta sem sentido quebra essa confiança.

## 22/11 · Editor de vídeo tem conversa própria

- **O dono pediu:** uma conversa de verdade com o Editor (MinoAI Frontier).
- **O que mudou:** existe a conversa "Editor de vídeo · MinoAI Frontier (X1-Plantas)" na mesma branch. OpenArt continua parado; o dono quer vídeo realista.

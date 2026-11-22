# Vídeo: reel de referência no lugar do cachorro caramelo, POV do caramelo no WhatsApp, zoom out, memes brasileiros

**Estado:** aberta

**Prompt (palavra por palavra):** Ill be out for a while, go full potent back in the project if youre done fixing all systematical error, or improvements

**O que ele pediu, parte por parte:** 1) O reel DTw4bqHE5zj (menino dançando 'Tô de boa, desce um pouquinho' ao lado do cachorrinho, 2016) entra na lista de referências e toma o lugar do cachorro caramelo no **vídeo principal** (anúncio e Instagram). 2) No **vídeo do WhatsApp** (a prévia que vai ao cliente), a casa aparece do ponto de vista de um vira-lata caramelo. 3) Em algum momento, a câmera faz um zoom out com efeito especial, tirado das referências de edição. 4) Em toda busca de referência, procurar memes brasileiros atemporais como esse.

**Por que ele pediu, ou o que quer descobrir:** Ele quer referência brasileira que todo mundo reconhece e que não envelhece (antes recusou o 'morango do amor' por ser de 2025). O meme dá o reconhecimento instantâneo nos 3 primeiros segundos; o caramelo, que é afeto brasileiro, vira o olhar do vídeo do WhatsApp. O zoom out é o momento de 'uau' da edição.

**Objetivo dele:** Vídeos que o brasileiro reconhece na hora, param o dedo e fazem querer a casa.

**Ligação com as ideias gerais do projeto:** Fio 2 (Brasil de agora, humor de família, nada de referência velha... aqui 'atemporal'), fio 7 (MinoAI na frente, referência real como direção), fio 1 (parece de verdade).

**Perguntas que me fiz:** Pode usar o clipe original? Não sem autorização: é imagem de uma criança e de terceiros; em anúncio pago, só **recriado** (o clima, o gesto, a frase), nunca o vídeo dele (o Revisor confere). 'Vídeo do WhatsApp' é a prévia (21/11: 'vai para o cliente no WhatsApp'). A casa: a E07 está sendo redesenhada; o vídeo usa a casa aprovada quando o dono aprovar. Zoom out: o kit da MinoAI tem `05-motion-kits/pipeline/make_zoom2.py` (achado na busca). Ponto de vista do caramelo: câmera a uns 40 cm do chão, andando pela casa; sai no motor 3D (ilustração) ou na filmagem do dono com o celular baixo; realista no OpenArt só com o 'sim'.

**Pronto quando:** Plano vetado (2 rodadas do time e o Fable); roteiro dos dois vídeos com o momento do meme, o POV do caramelo e o zoom out marcados no tempo; resumo da produção e custo prontos para o 'sim' do dono; nada gerado nem gasto antes disso.

**Suposições (o dono não disse):** 'Vídeo do WhatsApp' = a prévia do WhatsApp. O meme é recriado, não copiado. A casa é a que o dono aprovar no redesenho (hoje a E07). Os memes atemporais vão ao caderno `pesquisas/video.md`.

**Quem executa:** Maestro (Opus): plano e conferência. Diretor (MinoAI): ideia principal e o zoom out do kit. `editor-video`: roteiro. `redator`: frase na tela. `revisor-de-risco`: direito de imagem do meme e da criança (Fable na peça final). `arquiteto`: a casa do POV bate com a planta. `pesquisador`: memes brasileiros atemporais. `supervisor` (Fable): veto final do plano.

**Conferência:** (no fim)

**Resultado:** (a preencher)


## Plano detalhado (para o veto do time e do Fable)

Objetivo de todos: o brasileiro reconhece na hora, para o dedo, e quer a casa.

| # | Tipo | Passo | Quem | Pronto quando |
|---|---|---|---|---|
| 1 | P | Reel na lista de referências (`video/REFERENCIAS.md`), com a análise do Diretor e a regra: recriar, nunca usar o clipe | Maestro | seção nova no arquivo |
| 2 | G | Memes brasileiros atemporais: 10 candidatos com fonte e ano (meme com 5 anos ou mais e ainda reconhecido), sem pessoa real identificável usada como propaganda | `pesquisador` (Sonnet) acha; `editor-video` conclui | lista no caderno `pesquisas/video.md` |
| 3 | P | Ideia principal de cada vídeo, com a fonte da MinoAI | Diretor (MinoAI) pelo Maestro | uma linha por vídeo, com fonte |
| 4 | G | **Principal (anúncio e Instagram):** onde o meme entra (de preferência nos 3 primeiros segundos, recriado: a dança e o "desce um pouquinho" na casa nova) e o que sai (a cena do caramelo) | `editor-video` | roteiro com tempo de cada quadro |
| 5 | G | **Prévia do WhatsApp:** passeio pela casa do ponto de vista do caramelo (câmera baixa, uns 40 cm), entrando pela porta, cozinha, sala, quintal | `editor-video`; `arquiteto` confere o caminho na planta | roteiro e caminho da câmera |
| 6 | P | Zoom out com efeito: escolher no kit (`make_zoom2.py`) e marcar o momento (sugestão: o fim do POV, quando a câmera sobe e abre e mostra a casa inteira no lote) | `editor-video` com o Diretor | momento e efeito no roteiro |
| 7 | P | Texto na tela de cada vídeo (primeiro quadro sempre com texto) | `redator` | frases com atributo e número da ficha |
| 8 | P | Direito de imagem e honestidade: meme recriado, sem a criança, sem marca; casa igual à planta; aviso "Planta de referência" | `revisor-de-risco` | SIM ou VETO com a correção |
| 9 | P | Resumo da produção e custo (motor próprio, filmagem do dono ou OpenArt) | Maestro | resumo pronto para o dono |
| 10 | Dono | "Sim" ao resumo e ao custo; qual casa | dono | resposta na ficha |
| 11 | G | Produzir (só depois do 10) | `editor-video`; edição final na MinoAI, no Mac | vídeos aprovados pelo dono |

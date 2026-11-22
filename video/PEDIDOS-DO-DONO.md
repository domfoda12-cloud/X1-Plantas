# Vídeo: tudo o que o dono pediu (não se perde)

> **Regra do dono (22/11/2026):** "Para todo vídeo, quando eu acrescentar uma informação, garanta que ela fique lá e não se perca na conversa."
> Por isso: **toda instrução dele sobre vídeo entra aqui na hora, com as palavras dele**, antes de qualquer edição. Quem edita lê este arquivo inteiro antes de mexer em roteiro ou clipe, e confere no fim se cada linha "vale" continua atendida. Nada sai daqui sem o dono mandar tirar.

## Ordens gerais (valem para todo vídeo)

| Data | O dono disse | Estado |
|---|---|---|
| 20/11 | Referência de edição: CONDOR XIII; "preste muita atenção" no B-roll e na música | Vale. Ver `REFERENCIA-CONDOR.md` |
| 21/11 | "O vídeo também deve ficar comprimido" | Vale |
| 21/11 | "Não use OpenArt" | Corrigido pelo dono em 22/11 (linha abaixo) |
| 22/11 | "Use o OPENART, que eu NÃO proibi, apenas necessita permissão para ser usado" | Vale. OpenArt pode, **com o "sim" do dono a cada uso** (resumo e custo antes) |
| 21/11 | "Quero REALISTA", "parece vida real" | Vale. O motor 3D próprio é ilustração, não foto |
| 22/11 | Vai filmar com o celular "daqui a alguns dias, mas não por enquanto" | Aguardando. Até lá, vídeo com planta, 3D próprio e páginas do e-book |
| 22/11 | "Quando eu acrescentar uma informação, garanta que ela fique lá" | Vale. É este arquivo |

## Vídeo principal

### Sequência de "escaneamento" (22/11/2026): a prova no meio do vídeo

Texto do dono, sem mudar:

| Timestamp | Visual | Overlay detail |
|---|---|---|
| 0,0-0,3s | Static blueprint image, flat 2D plan | Dimension/measurement lines snap on one at a time, like CAD annotation marks appearing along the 8m frontage |
| 0,3-0,6s | Same blueprint, hard cut | Wireframe/3D mesh grid snaps over the 2D plan, suggesting the computer is "building" it |
| 0,6-0,9s | Same blueprint, hard cut | Room label tags pop in rapid-fire, one per beat: "72 m²" then "3 quartos" then "1 suíte" then "2 banheiros," stacking faster each time |
| 0,9-1,2s | Hard cut, no transition | Finished 3D render or real house photo, full reveal, overlays gone, clean shot |

"Keep every cut in this sequence a hard cut, no crossfade, that abruptness is what sells the "scanning" feeling from the reference. This whole sequence replaces your current blueprint-tracing opener and slots in as the mid-video proof beat we discussed earlier (after the hook lands, before the CTA)."

O que isso obriga:

- 4 tempos de 0,3 s; **só corte seco**, nenhuma fusão dentro da sequência.
- Tempo 1: cotas entram uma de cada vez, na frente de 8 m.
- Tempo 2: malha 3D de arame por cima da planta 2D.
- Tempo 3: etiquetas "72 m²", "3 quartos", "1 suíte", "2 banheiros", cada uma mais rápida que a anterior.
- Tempo 4: casa pronta em 3D (ou foto real), limpa, sem as marcações.
- **Substitui** a abertura da planta se desenhando; fica **depois do gancho e antes da chamada**.

Como foi feito: ver a seção "Estado" abaixo.

### Estado

| Data | O que está feito | O que falta |
|---|---|---|
| 22/11 | Sequência de escaneamento feita com a planta **E07** (os números do dono batem com ela: 72 m², 3 quartos, 1 suíte, 2 banheiros, lote de 8 m de frente; todos saem do validador). `video/scan.py` gera os 3 primeiros tempos (`broll/clipes/scan-e07.mp4`, 0,9 s); o 4º tempo é a cena seguinte do roteiro (3D próprio da E07, limpo, 2,1 s). Encaixada em `roteiros/principal-condor.json` depois do gancho (4,8 s) e antes da chamada; a planta se desenhando saiu. O gancho passou da C01 (8×15) para a E07 (8×25), para o vídeo falar de uma casa só. O vídeo ficou sem nenhum clipe do OpenArt: 21 s, `saida/principal-condor/`. Conferido quadro a quadro | **É rascunho:** a E07 está na fila do redesenho das plantas (`contexto/QUADRO.md`); não publicar antes de o dono decidir entre esperar o redesenho ou trocar de casa. O dono assistir. Trocar o 4º tempo e o 3D por filmagem real quando ele filmar. Música licenciada (no Mac). O aviso legal e o selo "Ilustração do modelo 3D" ficam no 4º tempo (regra de honestidade), então ele não é 100% "limpo" |

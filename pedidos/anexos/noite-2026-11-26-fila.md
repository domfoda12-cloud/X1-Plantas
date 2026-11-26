# Noite de 26/11: autonomia e fila de trabalho

> O dono, 26/11 (~01:30 UTC), antes de dormir: "for this night i want you to go crazy, dont ask me for permission for ANYTHING, only rules: dont fuck me up and dont spend my money. This doesnt apply only for the ads and ebook, i still want to decide on the final but feel free to keep tweaking it and improving. Always remember, I M P R O V E M E N T, get every single detail, every single component that makes something and make it better, thats how you masterize things. A term for it: Min maxing except we can max everything."

## O que isso libera e o que não libera (leitura do Maestro)

- **Libera, sem perguntar:** mudar sistema, regras, agentes, skills, Canteiro, plano; instalar ferramenta grátis de licença aberta (licença lida e registrada); refazer e melhorar rascunhos, prévias, textos, protótipos; decidir o que é fácil de desfazer.
- **Não libera:** gastar dinheiro (nada pago, nenhum crédito do OpenArt, nenhuma pesquisa paga); o **final do e-book** e **anúncios** (ele decide: nada de gravar `ebook/saida/`, nada de publicar anúncio; melhorar à vontade em prévia e no gerador, com o Revisor lendo o que é texto público).
- **"Dont fuck me up" (o que eu não faço de jeito nenhum):** publicar em nome dele, mandar e-mail ou mensagem a alguém, criar conta, apagar o que não se recupera, reescrever histórico do git, pôr dado pessoal no repositório, contornar uma trava de permissão da sessão, afrouxar o `checar.py`. Tudo o que eu mudar fica em commit, com como desfazer.
- **O método:** melhorar cada componente de cada peça (min-maxing): listar as partes, achar a mais fraca, melhorar, conferir com olhos novos, repetir.

## Fila da noite (uma frente por vez; cada item fecha salvo antes do próximo)

1. **Configuração dos agentes** (4 mudanças aprovadas) e **diagnóstico do júri**: fluxo rodando.
2. **Canteiro do zero**: fluxo rodando; ao terminar, publicar no mesmo link e aplicar a migração do banco (nada apagado).
3. **E-book, passada de melhoria página por página** (prévia em duas partes, 24 páginas): cada página olhada por comprador, Designer, Arquiteto e Revisor; aplicar no gerador o que melhora sem mudar decisão dele; as 5 frases novas entram na prévia como proposta marcada. `ebook/saida/` não é tocado.
4. **Júri**: prova com erro plantado das mudanças do diagnóstico; o que passar vira regra na seção 5b.
5. **Instagram de IA**: 3 reels piloto no mesmo "mundo" (som melhor, gancho no extremo, verificador da conta), revisão adversarial em vez de júri caro.
6. **Funil para o sócio**: conversa de WhatsApp simulada do anúncio ao Pix, achando onde a venda se perde; textos melhorados em rascunho com o Revisor.
7. **Perfil do dono e voz do Claude** ("mais pessoal"): montar a partir das correções dele; sem dado pessoal.
8. **Agentes, um por hora**: melhorar o texto de cada um pelas lições.
10. **Nomes e conversa da equipe** (pedido das 01:40: "O seu nome próprio agora é Paydon Clabett. Escolha um nome para cada agente e faça eles interagirem ... como amigos/colegas de trabalho"): DEPOIS que o fluxo da configuração dos agentes fechar. Nomes: Paydon Clabett (Maestro), Tito Prumo (Planejador), Nilo Esquadro (Arquiteto), Bia Traço (Designer), Caio Vírgula (Redator), Vera Veto (Revisora de risco), Rui Lance (Estrategista), Ana Fonte (Pesquisadora), Zeca Corte (Editor de vídeo), Olga Lupa (Supervisora), Juca (Ajudante); o Diretor (MinoAI Frontier) mantém o nome. Cada agente: nome e jeito no próprio arquivo e em `contexto/EQUIPE.md`; lê as últimas falas de `contexto/CONVERSA.md` ao começar; termina o relatório com 1 a 3 falas curtas para colegas, só sobre o trabalho real. O Paydon copia as falas para `contexto/CONVERSA.md` e para o Canteiro (documentos `tipo: "conversa"`).
11. **Pasta `contexto/` enxuta** (dono, 01:50: "pasta do contexto tá bem grande"): o que cada papel lê ao começar fica curto; o histórico sai para arquivo próprio (nada apagado: movido e apontado); medir antes e depois.
12. **Passar para uma sessão nova** (dono, 01:55; regra em `contexto/maestro.md`): assim que os dois fluxos desta conversa (agentes e Canteiro) terminarem e forem salvos, escrever o ULTIMO.md, abrir a sessão nova, mover a tarefa de hora em hora para ela e continuar a fila lá.
9. **Resumo da manhã**: uma página curta do que mudou, com como desfazer cada coisa, e o que espera ele.

**Ritmo do limite (dono, 01:50):** "tente racionar o limite entre os horários, mas pode usar 100% por agora sem estresse": esta janela pode ir até o fim; nas próximas, dividir o limite ao longo das horas (no máximo um fluxo grande por hora).

## Registro (o Maestro acrescenta uma linha por item fechado)

- 26/11 ~01:40 UTC: limite de uso de 5 horas acabou no meio dos dois fluxos (agentes: só o conserto final falhou; Canteiro: 4 de 13 agentes prontos). As 4 mudanças dos agentes e o diagnóstico do júri já estão salvos (commits até b9bcb93; diagnóstico em `diagnostico-do-juri-2026-11-26.md`: 11 rodadas, 0 decisões fechadas, cerca de 5,67 milhões de tokens anotados).
- Limite renovado: os dois fluxos retomados do ponto em que pararam (o que já estava pronto não roda de novo).
- Item 4 (26/11, `CONSELHO.md` 5b): o que passar na prova vira proposta ao dono, não regra; a 5b pede o "sim" dele.
- Item 6 (26/11, ficha 0105): o Redator confere o rascunho contra `contexto/redator.md`; o Revisor lê uma vez, a conversa montada como vai ao sócio.
- 26/11 ~02:00 UTC: item 1 FECHADO (agentes: 4 mudanças, 25 achados dos verificadores, 20 consertados; diagnóstico do júri gravado). Ficha 0105 fechada.
- 26/11 ~02:45 UTC: item 2 FECHADO (Canteiro refeito: página nova no mesmo link, 54 cartões migrados ou criados, 99 antigos arquivados com `nivel: "arquivo"`, nada apagado; 3 revisores deram 7, 7,5 e 6,5; 38 de 39 achados consertados; cópia em `pedidos/canteiro/quadro-tarefas.html`).
- 26/11 ~02:50 UTC: item 12: passagem escrita em `contexto/entregas/ULTIMO.md`; a fila continua na sessão nova.
- 26/11 ~02:55 UTC: item 10 FECHADO (nomes e jeito nos 10 agentes e em `contexto/EQUIPE.md`; `contexto/CONVERSA.md` criado; Canteiro com a fala nova; `checar.py` confere). Ficha 0116 fechada. Achado: a cópia do Canteiro em `ebook/plantas/rascunhos/` é ignorada pelo git; restaurada só no disco a partir do artifact.
- 26/11 ~03:05 UTC: auditoria da Olga (fichas 1027, 0105, 0116: 0 alta, 6 média, 10 baixa) e consertos; fonte do Canteiro movida para `pedidos/canteiro/`.
- 26/11 ~03:15 UTC: item 11 FECHADO (`contexto/` de 244.938 para 89.708 bytes e de 27 para 23 arquivos: `PROMPTS.md`, `RETROSPECTIVA.md`, `intencoes/` e as passagens de 20 a 24/11 movidos para `pedidos/historico/`, 18 arquivos com links refeitos, nada apagado; nome do Paydon no `CONTEXTO.md`).
- 26/11 ~03:44 UTC: item 3 FECHADO (passada do e-book: Bia, Nilo e Vera nas 24 páginas; aplicados 9 consertos, entre eles o lado do sol espelhado no validador, com prova no `checar.py` (C01 e E03 melhores com a rua ao sul); 12 propostas guardadas; as 5 frases na prévia marcada em amarelo, SIM da Vera na página montada; nada em `ebook/saida/`). Detalhe: `pedidos/anexos/passada-do-ebook-2026-11-26.md`.
- 26/11 04:47 UTC: item 5 (Instagram de IA) fica FORA desta noite neste repositório: o dono, 25/11 16:05, "mainly focus on the ebook for now", e o Instagram de IA tem repositório e conversa próprios (`CONTEXTO.md`, "Instagram de IA"). No lugar, item 3b: aplicar as propostas maiores da passada do e-book (casa no lote legível, recuos em escala), em prévia.
- 26/11 ~05:00 UTC: item 3b FECHADO (Bia: planta de verdade no lote mínimo nas págs. 5, 9, 13 e 20, letra de 8 pt; faixa de recuo em escala nas págs. 4, 8 e 12; capa intocada, espera a identidade; só as 7 páginas mudaram, conferido pixel a pixel; o Paydon olhou as páginas).
- 26/11 05:47 UTC: item 12 de novo: esta conversa passou por resumo automático; passagem em `contexto/entregas/ULTIMO.md` e a fila segue numa sessão nova, com a tarefa de hora em hora apontada para ela.

- 26/11 ~06:45 UTC: item 6 FECHADO (funil do sócio, tudo em rascunho): Rui simulou 5 conversas com os textos de hoje e achou 10 vazamentos, os 4 mais caros do dono (dados do Pix, quem atende, o lote em que só cabe a Casa Compacta, o "gera" dos PDFs com o sol) (`funil-simulado-2026-11-26.md`); Caio escreveu 18 atalhos novos ou reescritos, a regra "perguntou preço, responde na hora", a folha do sócio e 19 perguntas ao dono (`funil-textos-rascunho-2026-11-26.md`); Vera leu uma vez: SIM SE, trocas aplicadas (`veto-funil-textos-2026-11-26.md`); calculadora: fecho em 3D, aviso interno sem botão de copiar quando só cabe a Casa Compacta, saiu a frase "encostar na divisa, a conta muda". `RESPOSTAS-RAPIDAS.md`, `WHATSAPP.md` e `ebook/saida/` intocados. Correção do Rui: o e-book à venda tem 3 casas; "3 casas" nas mensagens está certo.

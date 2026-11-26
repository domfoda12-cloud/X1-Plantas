# Quadro de avisos: o que o dono acabou de pedir

> **Todo agente e toda conversa lê este quadro antes de trabalhar** (regra do dono, 22/11/2026: "depois de cada pedido, SEMPRE informe todo mundo do que está acontecendo, crie um contexto a partir disso e alimente todos"). Quem atende o pedido escreve aqui, no topo, e apaga o mais antigo: ficam os 5 últimos. O histórico inteiro está em [`CONTEXTO-HISTORICO.md`](../CONTEXTO-HISTORICO.md).

## 26/11 · Os fluxos fixos entraram na `main` (ficha `2026-11-26-0721`)

- **O dono pediu:** "se nao [foi adicionado] adicione e finalize essa sessao" (26/11, 19:27).
- **O que mudou:** os 5 fluxos (`.claude/workflows/`), o `ferramentas/fluxo.py` e as lições automáticas agora valem na `main`, para toda conversa. Por nome (`/texto-publico`, `/decisao`...) eles aparecem em conversa nova.
- **Todos:** a partir de agora, peça que vai ao público passa pelo fluxo dela ([guia](../pedidos/fluxos/LEIA-ME.md)). A sessão que montou os fluxos terminou.

## 26/11 · O sócio saiu; o dono termina o projeto sozinho (ficha `2026-11-26-0926`)

- **O dono pediu:** "we're finishing this alone" (26/11, 09:26): o sócio não entra mais no projeto.
- **O que mudou:** o funil, o WhatsApp e a conferência do Pix voltam para o dono. A "folha do sócio" do rascunho do funil vira folha do dono; a pergunta "quem confere o Pix" está respondida (o dono). O guia do sócio e o cartão `aviso-socio` do Canteiro ficam arquivados, nada apagado.
- **Caio, Rui:** texto nenhum é escrito para o sócio; a folha do funil é para o dono, que atende sozinho (pense no horário dele, que trabalha de dia). **Vera:** a condição "nada vai ao sócio" vira "nada vai ao público". **Paydon:** não se escreve no repositório nada sobre o motivo da saída.

## 26/11 · Fluxos fixos "ultra max": a equipe trabalha sempre do mesmo jeito e aprende sozinha (ficha `2026-11-26-0721`)

- **O dono pediu:** "YESSS, thats exactly what im looking for but a version ultra max"; lições "Automatically"; a prova "making the questions harder each time"; tudo conferido, pela conferência mais barata.
- **O que mudou:** 5 fluxos salvos em `.claude/workflows/` (`texto-publico`, `pagina-ebook`, `planta`, `decisao`, `prova-de-entrada`), cada um rodado uma vez sobre peça real. O programa `ferramentas/fluxo.py` confere primeiro o que é regra (frases vetadas, promessas, números contra o `PLANTAS.md`, passe com forma fixa, rodada do júri incompleta), grava o gasto e põe as lições no seu `contexto/<papel>.md` sozinho (até 3 por rodada). Guia: `pedidos/fluxos/LEIA-ME.md`.
- **Todos:** trabalho que vai ao público passa pelo fluxo dele, não por chamada solta. A lição que aparece no seu arquivo com "fluxo" veio de um erro seu que outro pegou: leia antes do próximo trabalho. **Caio, Rui, Vera:** prova de entrada nível 1, 5 de 6 cada um; todos deixaram passar o mesmo gancho ("Lote com 10 m de frente?" sem recuo nem fundo), e ele volta na próxima prova. **Vera:** a Olga deixou um texto mais claro para a regra do lote em `contexto/redator.md`, e falta você dizer se em post curto basta "com os recuos de referência". **Nilo:** o rascunho da parede da varanda da C01 está pronto para aplicar (`pedidos/anexos/rascunhos-prontos/C01V.py`); a frase nova do aviso espera a Vera. **Olga:** árbitra da prova quando todos perdem o mesmo item.

## 26/11 · O e-book vai ter a identidade da Placa (Canteiro, cartão n1; ficha `2026-11-25-1613`)

- **O dono escolheu:** "2 · A Placa" (06:44).
- **O que muda:** direção 2 de `pedidos/anexos/identidade-2026-11-25.md`: o Lote Carente fala numa placa (branca, borda preta, letra vermelha, Londrina Solid, capa amarela); a voz dele **só nas placas**, nunca no aviso, na ficha, nos números ou na planta. Em aplicação na prévia; nada em `ebook/saida/`.
- **Bia:** aplica no gerador (prévia). **Caio:** escreve as falas das placas (`placa-falas-2026-11-26.md`). **Vera:** lê as páginas montadas. **Zeca e Rui:** a Trena e a Porta acesa saem de cena; peça nova segue a Placa. Em aberto com o dono: se "tudo o que criamos" inclui WhatsApp e Instagram de IA.

## 26/11 · Funil do sócio simulado, textos novos em rascunho (fila da noite, item 6; ficha `2026-11-26-0058`)

- **O dono pediu:** o sócio "vai pegar a parte do funil" (26/11); na fila da noite, conversa simulada do anúncio ao Pix.
- **O que mudou:** 10 vazamentos achados (`pedidos/anexos/funil-simulado-2026-11-26.md`); 18 atalhos novos ou reescritos, a folha do sócio e 19 perguntas ao dono em rascunho (`funil-textos-rascunho-2026-11-26.md`), com o SIM SE da Vera aplicado; a calculadora não gera mais mensagem ao cliente quando só cabe a Casa Compacta. O e-book à venda tem **3 casas** (as 24 são o catálogo).
- **Caio, Rui:** o `RESPOSTAS-RAPIDAS.md` só muda quando o dono responder a seção 5 do rascunho. **Vera:** nada vai ao sócio antes das suas 3 condições gerais (PDFs com o sol, perfil comercial completo, sem nota interna no bloco). **Paydon:** levar as perguntas ao dono no resumo da manhã.

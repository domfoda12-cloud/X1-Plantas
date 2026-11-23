# Proposta de integração das 5 adições do dono (versão 1, 23/11/2026)

> Para o júri criticar, rodada após rodada (pedido do dono: "make the jury criticise it a lot of times, and improve at each time"). Cada rodada gera uma versão nova. Contexto: o próprio júri, no veredito de 23/11 (ficha `2026-11-23-0156`), disse que o sistema já cresceu demais e que falta vender; o dono quer o sistema "funcionando como um cérebro".

## O que cada adição é, e o que propomos

| Adição | O que é (lido no repositório) | Licença | Proposta v1 | Por quê |
|---|---|---|---|---|
| **llm-council** (Karpathy) | 3 etapas: opiniões separadas de vários modelos, revisão anônima com ranking, presidente que sintetiza; app com chave paga do OpenRouter | **sem licença** (código não se copia) | Adotar só o **método**, com os nossos modelos (Haiku, Sonnet, Opus, Fable), como skill nossa `/juri`, para decisões grandes e para revisar o próprio sistema | Já deu o diagnóstico mais útil do projeto; sem gasto extra e sem dado saindo |
| **claude-chief-of-staff** | Assistente de CEO: triagem de e-mail e Slack, briefing da manhã, CRM, tudo filtrado por um arquivo de metas (`goals.yaml`) | MIT | **Não instalar** (precisa de Gmail e Calendar, troca o nosso CLAUDE.md); adotar a **ideia do arquivo de metas**: `METAS.md` curto (o primeiro Pix, com data e números), que toda ficha consulta, e uma conferência que avisa quando o trabalho da semana não serve à meta | É a "atenção" que faltou ao cérebro: o júri disse que o sistema pensou em si e não no Pix |
| **marketing-psychology** | Texto com modelos mentais e vieses (ancoragem, prova social, escassez...) | MIT | **Instalada** em `.claude/skills/marketing-psychology/` com a seção "Neste projeto" do Revisor (só o que é verdade e tem fonte) | Serve à venda, não ao sistema |
| **last30days** | Busca dos últimos 30 dias em Reddit, X, YouTube, TikTok, Polymarket; instala ferramentas de linha de comando no primeiro uso e pode usar a conta logada do dono | MIT | **Não instalar agora**; reavaliar quando houver anúncio rodando e for preciso medir tendência; se entrar, só na máquina do dono, com o "sim" dele e o Revisor | Instalação pesada; o público (25 a 50 anos, Brasil) está mais no Instagram e no WhatsApp do que no Reddit e no X |
| **find-skills** (vercel-labs) | Ajuda a achar e instalar skills com `npx skills` | MIT | **Não instalar**: a nossa porta de entrada é o roteiro do CONSELHO, seção 6 (licença lida, Revisor, Conselho); usar o site de skills só como lugar de busca, à mão | Instalar skill pela linha de comando fura o roteiro e faz o sistema crescer sem freio |

## Mudanças concretas da v1

1. Criar `.claude/skills/juri/SKILL.md` (nosso, só o método, com crédito a Karpathy pela ideia).
2. Criar `METAS.md` (uma página: a meta do mês, o número que manda, a data) e a conferência no `checar.py` que conta, por semana, fichas de sistema contra fichas de produto e avisa se o sistema passar de metade.
3. Registrar no `ECOSSISTEMA.md` as cinco, com o status (adotado como ideia, instalado, adiado, não instalado).

## O que não muda

Nada pago, nada publicado, nada instalado sem o veto do Revisor; as decisões de venda (título, preço, casas, plantas grátis) continuam do dono.

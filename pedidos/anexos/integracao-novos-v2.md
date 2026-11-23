# Proposta de integração das 5 adições do dono (versão 2, 23/11/2026)

> Rodada 1 do júri sobre a v1: notas 4, 5 e 5 (e a do Fable a chegar). O que mudou da v1 para a v2, em uma linha cada:
> - **Conflito explicitado:** o veredito de 23/11 mandou parar de criar sistema por 7 dias; o dono, depois, pediu estas 5 adições. Regra da v2: **o que o dono pediu pelo nome entra ou vira pergunta a ele; o que é invenção nossa (METAS.md, conferência nova, skill `/juri`) espera os 7 dias.**
> - **Nada decidido no lugar dele:** find-skills e last30days viram opções com recomendação, não recusa.
> - **Sem suposição:** sai a frase sem fonte sobre onde o público está; sai "a máquina do dono" (ele não tem Mac e não sabemos o que tem).
> - **Cada adição tem:** quem usa, como se mede, custo, como desfazer.

## As cinco, ligadas como num cérebro

| Adição | Parte do cérebro | Alimenta | Decisão |
|---|---|---|---|
| marketing-psychology | o jeito de convencer | o Redator e o Estrategista (texto e oferta) | **Já entrou** (veto do Revisor) |
| llm-council (o método) | o juízo de fora | as decisões grandes do Maestro | **Entra como modo do `/conselho`** que já existe (não uma skill nova) |
| chief-of-staff (a ideia) | a atenção (o que importa) e a memória de pessoas | o PAINEL: a linha de vendas e a lista de leads do WhatsApp | **Espera o dono** (a meta e a data só ele dá) |
| last30days | os sentidos (o que o povo fala agora) | o Pesquisador | **Pergunta ao dono** |
| find-skills | achar ferramenta nova | o roteiro de entrada (CONSELHO, seção 6) | **Pergunta ao dono** |

## Cada adição, com medida, custo e saída

| Adição | O que fazemos | Como se mede | Custo | Como desfazer |
|---|---|---|---|---|
| **marketing-psychology** | Fechar o passo que faltou do roteiro (CONSELHO, seção 6, passo 5): uma linha nos contextos do Redator e do Estrategista e no inventário de skills do ECOSSISTEMA | textos do Redator que passam no Revisor de primeira | zero (texto) | apagar a pasta `.claude/skills/marketing-psychology/` |
| **llm-council** | O `/conselho` ganha o "modo júri": 4 modelos opinam em separado, revisam anônimos, e o presidente é um modelo que **não opinou** na mesma rodada (corrige o viés da rodada de 23/11, em que o Fable presidiu e foi a opinião mais bem votada). Gatilho: só decisão que custa dinheiro, vai ao público ou muda o sistema inteiro, ou pedido do dono | se a decisão do júri resistiu (não precisou ser desfeita em 7 dias) | medido em 23/11: cada rodada inteira custa uns 900 mil tokens (4 opiniões de 85 a 130 mil, 4 revisões de 80 a 97 mil, presidente 90 mil) | tirar o modo do `/conselho` |
| **chief-of-staff** | Fica a ideia, sem arquivo novo agora: **uma linha de vendas no PAINEL** (contato, conversa, Pix, custo; só número real) e, quando houver leads, uma lista simples deles (o "CRM" que o funil do WhatsApp precisa) | contatos e Pix por semana | zero | apagar a linha |
| **last30days** | Pergunta ao dono (abaixo). Se sim: só depois de ele dizer que computador tem, e com o Revisor olhando a conta logada (Reddit, X) e o que sai da máquina | achados do Pesquisador usados numa peça | instalação pesada; fontes como Reddit, X, YouTube, TikTok | desinstalar |
| **find-skills** | Pergunta ao dono (abaixo). Se sim: entra **só o texto**, com "Neste projeto" que proíbe `npx skills add` e manda toda skill achada para uma ficha e o roteiro da seção 6 | skills achadas que passaram no roteiro | zero (texto) | apagar a pasta |

## Perguntas ao dono (uma linha cada, com a recomendação)

1. **last30days:** instalar (quando soubermos que computador você tem) ou deixar para quando houver anúncio rodando? *Recomendação: deixar para depois do primeiro anúncio.*
2. **find-skills:** adicionar só como guia de busca, sem instalar nada pela linha de comando? *Recomendação: sim.*
3. **Meta do mês (para a "atenção" do cérebro):** qual a data em que você quer o primeiro Pix? *Sem recomendação: é sua.*
4. **Que computador você tem** (Windows, só celular...)? Isso decide o last30days e corrige as 63 menções a Mac.

## O que não muda

Nada pago, nada publicado, nada instalado sem o veto do Revisor e o "sim" do dono; título, preço, casas e plantas grátis continuam com ele.

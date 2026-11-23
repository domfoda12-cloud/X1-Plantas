# Proposta de integração das 5 adições do dono (versão 3, 23/11/2026)

> **O que mudou da v2 para a v3** (escrita com as 8 críticas do júri; rodada 1: média 4,75; rodada 2: média 6,1)
> - **Saiu o que não tinha fonte:** os "900 mil tokens" do júri (nenhum arquivo guarda esse número); as "63 menções a Mac" (contei hoje, antes deste arquivo: 89, em 32 arquivos `.md`); "instalação pesada" e "depende do seu computador", no last30days (o README e a sessão dizem o contrário).
> - **Suposição nossa virou pergunta a você:** "llm-council é só o método", "chief-of-staff é só a ideia" e "os 7 dias sem sistema novo valem".
> - **O júri agora fecha a conta:** 3 opinam e o 4º preside; tem gatilho próprio e hora de parar.
> - **chief-of-staff sem nada novo:** a tabela de vendas já existe no PAINEL; saiu a lista de leads.
> - **marketing-psychology vai trabalhar pela venda:** uma rodada sobre o texto do WhatsApp e a oferta.
> - **Toda medida tem o número de hoje** e aponta para o custo por venda. **Toda pergunta tem "decida você"** e vai para a página única de decisões.

## O cérebro: por onde um pedido passa

Seu pedido → ficha → **sentidos** (Pesquisador: TinyFish e MinoAI; last30days, se você quiser) → **convencer** (Redator, com a marketing-psychology) → **juízo** (Revisor sempre; júri só em decisão cara) → **você diz sim** (página de decisões) → peça no ar → **atenção** (tabela semanal do PAINEL: contatos, vendas, custo por venda) → o número volta e muda o próximo texto. A find-skills só aparece quando falta ferramenta.

## Cada adição

| Adição | Entra agora | Espera | Quem usa | Medida (e o número de hoje) | Custo | Desfazer |
|---|---|---|---|---|---|---|
| **marketing-psychology** | Já instalada. Falta a **rodada de alcance** (CONSELHO, seção 6, passo 5): o Redator roda a skill uma vez sobre `ebook/vendas/WHATSAPP.md` e a oferta (`ESTRATEGIA.md`, seção 7) e traz até 3 opções; o Revisor confere antes de chegarem a você. Faltam também os passos 4 e 6: uma linha em `contexto/redator.md` e `contexto/estrategista.md` (hoje não citam a skill) e o status na seção 2 do ECOSSISTEMA (hoje ela só está na 2b) | Uso em peça final: depois do seu sim às opções | Redator e Estrategista (suposição da ficha `0200`: diga se quiser outro) | Opções que o Revisor aprova e você aceita; depois, a coluna **Conversão** da tabela semanal. Hoje: a skill nunca rodou; a tabela está vazia | Tokens da assinatura (não medido). Dinheiro: zero | Apagar a pasta da skill e as linhas |
| **llm-council** | Só o método, como **seção curta do `/conselho`** (sem skill nova): 3 modelos opinam em separado e revisam sem saber de quem é cada texto; o 4º preside e não opina; o presidente muda a cada júri. **Gatilho:** você pede; ou o Maestro propõe, numa decisão cara ou sem volta (primeira verba de anúncio, publicar o e-book, contratar), e você diz sim. Limite escrito: os nossos 4 modelos são todos Claude; o original mistura quatro empresas. Nenhum código copiado: o repositório não tem licença | O programa original (pergunta 1) | O Maestro conduz; Haiku, Sonnet, Opus e Fable opinam e presidem | Críticas com fato que viraram mudança feita. Hoje: conferi 3 ordens do veredito de 23/11 e nenhuma está feita ainda (a página de decisões não existe; o gerador troca o título em colchetes em vez de falhar; o `checar.py` não confere "Mac") | Tokens da assinatura; dinheiro: zero. Por rodada: **não medido** (o único número guardado é o de um veto do Fable, 92 mil tokens, ficha `0144`). Cada júri anota na ficha o gasto que a ferramenta devolver | Apagar a seção do `/conselho` |
| **chief-of-staff** | Nada novo. A ideia dele (a meta filtra tudo) já tem casa: a **tabela semanal do PAINEL, seção 7** (custo por contato, contatos, vendas, conversão, custo por venda). Falta a meta: pergunta 5 | A ferramenta (pergunta 2): o README exige Gmail e Google Calendar conectados (esta sessão não tem) e o `install.sh` grava um `CLAUDE.md` dele em `~/.claude/`, que vale para toda conversa. Lista de contatos: só quando houver o primeiro; o funil é do parceiro (PAINEL, seção 12) | O Estrategista escreve na tabela os números que você ou o parceiro mandarem | Contatos, vendas e custo por venda por semana. Hoje: uma linha em branco; "não há venda nem anúncio rodando" (PAINEL, seção 2) | Zero | Nada a desfazer |
| **last30days** | Nada instalado. O que o README diz: é um plugin; Reddit, Hacker News, Polymarket e GitHub funcionam de graça, sem chave; Instagram Reels, TikTok e anúncios da Meta pedem a chave ScrapeCreators (10.000 chamadas grátis, depois paga); os anúncios da Meta vêm desligados e apontados para os EUA. Roda onde a conversa roda (esta: nuvem, Linux, Python 3.13; ele pede 3.12 ou mais), não no seu computador | Pergunta 3 | Pesquisador | Achados que o TinyFish e a MinoAI não trouxeram na mesma busca e que entraram num anúncio; depois, o **custo por contato**. Hoje: 0 (não instalada; nenhum anúncio rodando) | Sem chave: dinheiro zero. Com chave: vira ferramenta paga depois das 10.000 chamadas. Para o Revisor olhar: os programas que o primeiro uso instala e a opção de buscar com a sua conta logada do Reddit ou do X (fica desligada) | Remover o plugin |
| **find-skills** | Nada (nenhuma pasta antes da sua resposta) | Pergunta 4. O que o texto dele diz: tudo gira em torno do comando `npx skills` (procurar, instalar, atualizar); o passo 6 instala com `-g -y` (na máquina toda, sem pedir confirmação); a qualidade é medida por número de instalações, fonte e estrelas. A sessão de hoje já tem busca própria de skills | Maestro, só quando faltar ferramenta | Skills achadas que passaram no roteiro (CONSELHO, seção 6) e foram usadas numa peça. Hoje: 0 | Zero (é texto) | Apagar a pasta |

## Perguntas para você

Vão para a página única de decisões, ao lado de título, preço, garantia e WhatsApp. "Decida você" quer dizer: vale a recomendação. Sem resposta, nada é instalado e nenhuma recomendação é aplicada sozinha.

1. **llm-council:** (a) só o método, com os nossos 4 modelos, como rodou em 23/11; (b) o programa original: pede chave do OpenRouter com créditos comprados, manda o projeto a modelos de outras empresas, e o código não tem licença (o Revisor opina antes); (c) decida você. *Recomendação: (a). Não gasta dinheiro e nada sai do projeto.*
2. **chief-of-staff:** (a) só a ideia, na tabela do PAINEL que já existe; (b) instalar: você conecta Gmail e Google Calendar e o Revisor lê o `install.sh` antes; (c) decida você. *Recomendação: (a). Ele foi feito para o e-mail e a agenda de um diretor de empresa; para vender o e-book faltam a meta e o número.*
3. **last30days:** (a) um teste só, sem chave e sem conta logada: o Revisor lê o que o plugin instala; depois, uma busca do nosso assunto em português, comparada com a mesma busca no TinyFish e na MinoAI; fica se trouxer o que os outros não trazem; (b) já com a chave ScrapeCreators (Instagram Reels, TikTok, anúncios da Meta); (c) esperar você fechar título e preço, que é quando o Redator escreve o primeiro anúncio; (d) decida você. *Recomendação: (a). Não conferido: se as fontes grátis têm conversa brasileira sobre planta de casa; o teste responde.*
4. **find-skills:** (a) entra só o texto, com todos os comandos `npx skills` proibidos (o `npx` baixa e roda um programa de fora) e a descrição estreitada para "só quando o dono pedir"; sobra: olhar o ranking do skills.sh, conferir a qualidade e trazer opções; skill achada vira ficha e passa pelo roteiro; (b) não criar a pasta e usar a busca da sessão; (c) decida você. *Recomendação: (a). É o que você pediu, custa zero e sai apagando uma pasta; o ganho é pequeno. A v1 dizia não e a v2, sim: fica o sim porque o risco está nos comandos, não no texto.*
5. **Meta:** em que data você quer o primeiro Pix? (a) você diz a data; (b) decida você: propomos uma e você confirma. *Sem recomendação: a data é sua.*
6. **Os 7 dias sem sistema novo** (recomendação do júri de 23/11): (a) valem, menos para o que você pedir pelo nome; (b) não valem; (c) decida você. *Recomendação: (a).*

## Ordem, quem faz e quando o júri para

Nada aqui passa na frente do e-book: os passos 1 e 2 são da oferta e do texto de venda.

1. **Maestro:** cria a página única de decisões (ordem 2 do veredito; ainda não existe) com título, preço, garantia, WhatsApp e as 6 perguntas.
2. **Redator, depois Revisor:** rodada de alcance da marketing-psychology; as opções entram na mesma página.
3. **Maestro:** seção do júri no `/conselho`; uma linha para cada uma das 5 no ECOSSISTEMA, com um status só (hoje só a marketing-psychology aparece lá), e na seção 7 do CONSELHO; aviso no topo do QUADRO; fichas `0156` a `0203` e "Em aberto" do CONTEXTO em dia; `checar.py`, `atualizar-painel.py`, commit.
4. **Você:** responde a página.
5. **Revisor, depois Maestro:** só o que recebeu o seu sim. O Revisor lê tudo antes de qualquer download (roteiro, passo 1).
6. **Estrategista:** tabela semanal, quando chegar o primeiro número.

**O júri para** (regra já escrita na ficha `0156`): nota 8,5 sem fato errado; ou nota que não sobe em duas rodadas; ou 6 rodadas. Esta é a rodada 3. Parou: a proposta chega a você como a página de decisões.

**Deu certo se** aparecerem o primeiro contato e o primeiro Pix na tabela semanal. No primeiro Pix, a adição que estiver em zero na própria medida sai.

**Fora desta proposta:** o seu 6º pedido, de 02:08 (everything-claude-code). Segue o mesmo caminho: ficha, leitura, pergunta.

## O que não muda

Nada pago, nada publicado, nada instalado sem o veto do Revisor e o seu sim; título, preço, casas e plantas grátis continuam com você.

*Conferido em 23/11:* os arquivos do repositório citados acima; o README do llm-council, do chief-of-staff (e o `install.sh`) e do last30days (e o `CONFIGURATION.md`); o `SKILL.md` da find-skills; as licenças (MIT nas três; o llm-council não tem arquivo de licença).

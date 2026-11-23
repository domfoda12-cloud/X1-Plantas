# MinoAI Frontier: o Diretor, a sessão no PC do dono e o estilo de edição

> Como a MinoAI Frontier trabalha no computador do dono, a rotina da semana (antes `MAESTRO.md`, na raiz) e as referências do Mino Lee. Juntado em 22/11/2026 (ficha de organizar os arquivos): cada seção é um documento antigo, inteiro.

<!-- era: instagram/MINOAI-FRONTIER.md -->
## Editor: MinoAI Frontier

> Parte da pasta Instagram: [`INSTAGRAM.md`](INSTAGRAM.md). Painel: [`../PAINEL.md`](../PAINEL.md).
>
> **O editor do projeto agora é a MinoAI Frontier**: o serviço de edição da MinoAI, que corta, legenda, coloca B-roll, música e efeitos em reels de rosto falando. Este arquivo é o **contexto** que ela precisa para editar do nosso jeito: o projeto, o público, o estilo, os arquivos e as regras.
>
> Referência de edição favorita do dono: [`../video/REFERENCIAS.md`](../video/REFERENCIAS.md) (CONDOR XIII, levado para o reel de planta).
>
> Ela também é o **Diretor** do conteúdo; quem decide é o Maestro, a sessão do Claude (seção "Maestro e Diretor", mais abaixo nesta página). Quando a edição faz parte da semana do maestro, use a mensagem de abertura de lá; a desta página é para editar um vídeo avulso.

### 1. Onde e como a MinoAI Frontier edita

- **No seu computador**, no app do Claude (aba **Code**), no seu PC com Windows 10/11. Ela roda pelo WSL e instala sozinha o que precisa (o WSL, ffmpeg, Node, Python); você não digita comando nenhum.
- **Não edita na nuvem.** Os chats na nuvem deste projeto podem planejar a edição, mas o vídeo só sai no seu computador.
- **Precisa:** plano pago do Claude (Pro ou Max) e o conector MinoAI Frontier ligado na aba Code. Se ainda não estiver no seu Claude: app.contentacademy.io/mcp, opção Claude.

### 2. Configuração (uma vez só)

| # | O que fazer | Por quê |
|---|---|---|
| 1 | No PC, criar a pasta **Vídeos/X1-Plantas** e copiar para ela a pasta **`broll/`** descrita na seção 4 | É onde a MinoAI Frontier procura os vídeos e o B-roll |
| 2 | Criar o seu **estilo de edição** no [Edit Style Generator](https://app.contentacademy.io/ai-editing/studio), com os 3 reels de referência do Mino Lee: [reel 1](https://www.instagram.com/reel/DflcLspiT9H/), [reel 2](https://www.instagram.com/reel/DfbA-o1u4FI/), [reel 3](https://www.instagram.com/reel/De9dwH9yDB9/) | Hoje a sua conta **não tem estilo salvo**: ela editaria com o padrão dela. Com o estilo salvo, ela segue o mesmo estilo que analisamos em [`MINOAI-FRONTIER.md`](MINOAI-FRONTIER.md#referências-de-vídeo-mino-lee-minoleemp4) |
| 3 | Conectar o **Instagram** em app.contentacademy.io/mcp/connect-socials?platform=instagram (TikTok e YouTube Shorts, se quiser postar lá também) | Hoje **nenhuma rede está conectada**. Conectada, ela pode preparar a publicação. Os reels de teste você confere no app do Instagram |
| 4 | Na primeira edição, quando ela pedir, **permitir os comandos do editor** uma vez | Para não aparecerem pedidos de aprovação a cada passo |

### 3. A mensagem de abertura

Cole esta mensagem na aba **Code**, com a pasta **Vídeos/X1-Plantas** aberta, toda vez que for editar. Troque só a primeira linha.

```text
Edite este vídeo no estilo MinoAI Frontier: [nome do arquivo] — tipo: [ANÚNCIO COM LOCUÇÃO | PLANTA DA SEMANA | É POSSÍVEL | ERRO QUE SAI CARO | CABE NO SEU LOTE].

CONTEXTO DO PROJETO
- Perfil brasileiro de plantas de casas. O produto é um e-book com dezenas de plantas originais em blueprint, planta humanizada e 3D.
- Público: quem tem um lote e vai construir, quase sempre com pedreiro e sem arquiteto, muitas vezes por etapas. Classe C, 25 a 50 anos. A pergunta dele é "que casa cabe no meu lote?".
- Objetivo de todo vídeo: a pessoa assistir até o fim e comentar PLANTA para receber uma planta grátis no WhatsApp.

IDIOMA
- Tudo em português do Brasil. Legendas com acentos (ç, ã, õ, é); confira que a fonte mostra todos.
- Dinheiro sempre com a unidade: "R$ 1.000", "mil reais". Medidas como "10 x 20", "50 m²".

ESTILO (vale onde o meu estilo salvo não disser outra coisa)
- Zero espaço morto: sem pausa entre frases. Só fica a pausa marcada como proposital no roteiro.
- Gancho escrito fixo no alto o vídeo todo, letra fina, 2 linhas. O texto do gancho é diferente da primeira frase falada.
- Legenda no meio da tela, letra fina, 2 a 3 palavras por vez, sem caixa alta. Só a palavra-chave em amarelo #FFC857.
- Etiqueta pequena em cima do título de cada item ("erro 1" em cima de "Ignorar o sol").
- Termo técnico (recuo, peitoril, nascente, hall, planta humanizada) com a explicação em letra miúda abaixo da legenda.
- Uma imagem nova a cada 2 a 4 segundos; 2 a 4 imagens diferentes nos primeiros 5 segundos. Nada de cortes a cada 0,75 s: o público tem mais de 25 anos.
- B-roll sempre das casas do projeto, da pasta broll/ (blueprint, planta humanizada, 3D, animação). Nada de banco de imagens, nada de casa de outro escritório.
- Paleta: azul blueprint #0B4FA8, amarelo #FFC857, branco.
- Música baixa, sem letra, por baixo da voz.

SE FOR O ANÚNCIO COM LOCUÇÃO
- Destino: WhatsApp e Facebook Ads, não Instagram nem TikTok. Siga o plano de corte e as regras de video/principal-e07/kit-minoai/LEIA-ME.md e a ficha video/ANUNCIO-LOCUCAO.md.
- Aviso legal pequeno, no canto, parado. Sem o selo "Imagem ilustrativa".
- As 5 versões antigas (v1 a v5, "R$ 1.000 do arquiteto") não se editam mais: usam o 3D velho da C01.

REGRAS QUE NUNCA MUDAM
- Nunca dizer nem dar a entender que a planta dispensa pedreiro, engenheiro ou arquiteto.
- Nunca prometer aprovação na prefeitura ou no banco, prazo de obra ou custo exato de construção.
- Chamada final sempre: "Comente PLANTA".
- Mostre o plano de edição antes de renderizar quando a edição for maior que só legenda.

ENTREGA
- 1080 x 1920, vertical, salvo em Vídeos/X1-Plantas/editados/ com o nome [data]-[tipo]-[versão].mp4.
- No fim, me diga: duração, quais imagens do B-roll usou e em que segundos, e o texto do gancho.
```

### 4. A pasta `broll/` no seu computador

Monte uma vez e acrescente cada planta nova. Tudo vem deste repositório:

```
Vídeos/X1-Plantas/
  broll/
    plantas/
      casa-compacta/        ← copie de animacoes-3d/plantas/casa-compacta/
        01-blueprint.png
        02-planta-humanizada.png
        03-perspectiva.png
        04-perspectiva-lateral.png
        animacao.mp4
      <cada planta nova>/
    anuncio/
      v1/camada-transparente.webm   ← copie de video/saida/v1/ … v5/
      …
  brutos/                   ← as gravações do apresentador
  editados/                 ← onde a MinoAI Frontier salva os vídeos prontos
```

- As imagens das plantas (2000 x 2500) e as animações (vertical, 12 s) já estão no formato certo para B-roll.
- Em toda pasta de B-roll a MinoAI Frontier pergunta **se as pessoas nos vídeos são você**. Nas pastas de planta não há pessoas; responda isso.

### 5. Como cada tipo de vídeo deve ficar

| Tipo | Duração | Estrutura | B-roll |
|---|---|---|---|
| **Anúncio (v1 a v5)** | 38 s | Já definida pela camada ([`../video/VIDEO.md`](../video/VIDEO.md)) | A própria camada |
| **Planta da semana** | 15 a 25 s | Gancho com a medida do lote → passeio pela casa → "Comente PLANTA" | `animacao.mp4` da planta, depois blueprint e perspectivas |
| **Cabe no seu lote** | 20 a 30 s | "Tem um lote [medida]?" → 3 casas que cabem, uma por bloco → chamada | Planta humanizada de cada casa |
| **Erro que sai caro** | 15 a 25 s | Gancho do erro → por que sai caro → a planta mostrando o certo → chamada | Blueprint e planta humanizada |
| **É possível…?** | 40 a 70 s | Pergunta → por que é difícil → processo, com o que deu errado → resultado → chamada | Gravação de tela do processo + animação da planta no fim |

### 6. Ganchos de referência da biblioteca da MinoAI Frontier

Ganchos reais e com muitas visualizações, achados na biblioteca da MinoAI Frontier, adaptados para o nosso nicho. O original fica entre aspas; a adaptação mantém a estrutura.

| Original | Adaptação |
|---|---|
| "The most expensive mistake that could cost you over $100,000 building a business in your 5 to 9 is to build it on your employer's computer." ([@itshannahzhang](https://www.instagram.com/p/DaBM835JTiM/)) | "O erro mais caro que pode te custar [valor] construindo a sua casa é [erro]." |
| "Before you cover the AC for winter, avoid these two huge mistakes." ([@weeklyhomecheck](https://www.instagram.com/p/Dd92bI9zsgx/)) | "Antes de bater a laje, evite esses dois erros enormes." |
| "My name is Bert and I'm going to build my house." + texto "PT.35 House update" ([@buildwithbert](https://www.instagram.com/p/DbXB9latjHl/)) | Série: "Eu vou desenhar 35 casas para o seu lote." + "Parte 1", "Parte 2"… mostrando cada planta nova |
| "Five things you need to know if you're going to batch create high quality content and ruin your white couch." ([@iamsarahsnow](https://www.instagram.com/p/DIZXgXLPyFt/)) | "Cinco coisas que você precisa saber se vai construir num lote 10 x 20 e não quer jogar dinheiro fora." |

Para achar mais: peça à MinoAI Frontier "ganchos virais sobre construir casa" (busca de ganchos) ou "analise o gancho deste vídeo: [link]" (análise de gancho).

### 7. Do método do Mino (biblioteca de aulas da MinoAI Frontier)

- **Um B-roll por frase**, coerente com o que está sendo dito, e **2 a 4 imagens diferentes nos primeiros 5 segundos** ([aula de edição do Content Bootcamp](https://whop.com/joined/contentacademy/content-bootcamp-3pqyjhwaG9gmeC/app/courses/cors_7pWrAMvSU9J9TvKJP0c8tK/lessons/lesn_Vcp6Z4ZU1v864AZYUFvCy/)).
- **Para público acima de 25 anos, nada de cortes hiperrápidos** (a cada 0,75 s): funciona para público mais jovem e cansa o nosso ([Mastering Superhooks](https://www.loom.com/share/991211e6490344b283941f4204a7b8df)).
- **O B-roll responde o que falta de contexto.** Quando o apresentador diz "lote 10 x 20", a planta com a cota 10 x 20 precisa estar na tela.
- **Zoom lento num detalhe** destaca um objeto. Use na planta humanizada para mostrar o cômodo de que se está falando.

### 8. Rotina semanal com a MinoAI Frontier

| Quando | O quê | Quem |
|---|---|---|
| Segunda | Escolher os vídeos da semana no [plano do perfil](INSTAGRAM.md#plano-de-conteúdo-perfil-de-arquitetura-no-instagram) e em "Em aberto" do [`CONTEXTO.md`](../CONTEXTO.md) | Você |
| Terça | Gravar e colocar as gravações em **brutos/** | Apresentador |
| Terça a quinta | Editar cada vídeo com a mensagem da seção 3; aprovar o plano de edição quando ela mostrar | MinoAI Frontier e você |
| Quinta | Publicar as versões como reels de teste | Você |
| Sexta | Anotar os resultados no [registro de testes](INSTAGRAM.md#6-registro-dos-testes) | Você |

**Antes de publicar**, confira o vídeo pronto com a [lista de conferência](MINOAI-FRONTIER.md#6-lista-de-conferência-para-cada-vídeo-novo) e o [checklist de anúncio](../video/VIDEO.md#checklist-de-revisão-antes-de-subir-o-anúncio).

<!-- era: MAESTRO.md -->
## Maestro e Diretor: a sessão do Claude no seu computador, com a MinoAI Frontier

> **Quem rege é o Maestro** (dono, 22/11/2026): a sessão do Claude no seu computador, no app (aba **Code**), com este repositório aberto. Ele decide, conduz a semana pelo [painel](../PAINEL.md) e chama a equipe ([`contexto/EQUIPE.md`](../contexto/EQUIPE.md)).
> **A MinoAI Frontier é o Diretor**, ligado nessa sessão: dá a ideia principal de todo conteúdo, edita o vídeo e gera a imagem.
>
> Você decide e aprova o que é seu (preço, título, gasto, publicação). O Maestro organiza, produz, mede e avisa.

### 1. O que o Maestro e o Diretor fazem

| Frente | Quem faz: **Maestro** (a sessão do Claude, que decide) ou **Diretor** (MinoAI, que dá a ideia e edita) | Como |
|---|---|---|
| **Painel** | Maestro. Abre a semana: puxa os números das redes, atualiza o painel, propõe as tarefas e os ganchos da semana | Números das contas conectadas + `ferramentas/atualizar-painel.py` |
| **Vídeo** | Diretor. **Responsável pela edição de todos os vídeos.** Escolhe ganchos, revisa roteiros, analisa ganchos de referência, edita | Biblioteca de ganchos virais, análise de gancho, método do Mino, edição no estilo MinoAI Frontier |
| **Instagram** | Maestro, com a ideia do Diretor. Prepara a publicação, acompanha os reels de teste, anota o registro de testes; a vencedora quem decide é você | Publicação nas contas conectadas (só depois do seu "sim") + números de cada vídeo |
| **Imagens** | Diretor, pelo OpenArt. **Cria todas as imagens geradas** (fachada realista, ambientes, capas de reel, B-roll) usando o OpenArt, sempre a partir da planta ou do 3D nosso e **só com o "sim" do dono a cada uso**, com resumo e custo antes | Plugin OpenArt (skills `openart:*`), [fluxo](../animacoes-3d/OPENART-MINOAI.md) |
| **Animações 3D** | Maestro. Gera as imagens e animações das plantas (render no seu computador) ou pede a um chat na nuvem | `video/render-planta.cjs` |
| **E-book** | Maestro. Gera o PDF quando há plantas novas e confere as páginas | Gerador do e-book |
| **Funil** | Maestro. Passa ao parceiro as dúvidas e o lote mais pedido; traz de volta os números dele para o painel | Painel, seção 7 |

**O que continua com você:** decisões (título, preço, versões), aprovar cada publicação, publicar os reels de teste no app do Instagram, gravar (com o apresentador) e criar contas.

**Limite honesto:** a MinoAI Frontier é um serviço de vídeo curto. Nas frentes de 3D e e-book ela roda os scripts do projeto, como qualquer sessão do Claude Code; o jeito de fazer está nos guias de cada frente.

### 2. Configuração (uma vez só)

1. **Pasta de trabalho:** no PC, `Vídeos/X1-Plantas`, com quatro subpastas: `projeto/`, `broll/`, `brutos/` e `editados/`. Ver [`instagram/MINOAI-FRONTIER.md`](MINOAI-FRONTIER.md), seção 4.
2. **App do Claude**, aba **Code**, pasta `Vídeos/X1-Plantas` aberta e o conector **MinoAI Frontier** ligado.
3. Colar a mensagem da seção 3. Na primeira vez, o Maestro baixa este repositório para `projeto/`, monta o `broll/` e instala o que faltar. Você só aprova quando ele pedir.
4. Fazer os passos de [`instagram/MINOAI-FRONTIER.md`](MINOAI-FRONTIER.md), seção 2: estilo de edição salvo com os 3 reels do Mino Lee e Instagram conectado.

### 3. A mensagem de abertura do Maestro

Cole no começo de cada semana (ou sempre que abrir uma conversa nova com o Maestro):

```text
Você é o Maestro do projeto X1-Plantas: decide e rege a equipe. A MinoAI Frontier, ligada aqui, é o Diretor: dá a ideia principal de todo conteúdo.

O PROJETO
- E-book brasileiro com dezenas de plantas de casas originais (blueprint, planta humanizada, 3D e animação), para quem tem um lote e vai construir, quase sempre com pedreiro e por etapas.
- Venda: vídeos no Instagram e no Facebook Ads → comentário "PLANTA" → planta grátis no WhatsApp → oferta do e-book.
- Repositório: https://github.com/domfoda12-cloud/X1-Plantas, branch main, em Vídeos/X1-Plantas/projeto/ (se não existir, clone; se existir, atualize com git pull).

LEIA ANTES DE QUALQUER COISA (em projeto/)
- CLAUDE.md (regras que não mudam), contexto/QUADRO.md (o que o dono acabou de pedir), contexto/EQUIPE.md (a equipe) e contexto/diretor.md (o papel da MinoAI).
- INDICE.md e o RESUMO.md da pasta da tarefa; o documento inteiro só quando a tarefa pedir. Para vídeo: video/VIDEO.md e instagram/MINOAI-FRONTIER.md.

O SEU PAPEL
- Conduzir a semana pela rotina de instagram/MINOAI-FRONTIER.md, seção 4.
- Vídeo e redes: você faz. Ganchos pela biblioteca de ganchos virais, análise de gancho, método do Mino, edição no estilo MinoAI Frontier, publicação e números das contas conectadas.
- 3D e e-book: rode os scripts do projeto, seguindo animacoes-3d/ANIMACOES-3D.md e ebook/EBOOK.md.
- Painel: depois de qualquer mudança, rode python3 ferramentas/atualizar-painel.py e deixe zero avisos. Números novos vão para PAINEL.md, seção 7; decisões, para a seção 8 com data.
- Commit e push na branch main (git pull --rebase antes), com mensagens em português. A main é a única branch de trabalho.

REGRAS
- Tudo em português do Brasil, no tom de ESTRATEGIA.md, seção 9.
- Nunca publique, agende ou apague nada sem eu dizer "sim" para aquele post.
- Nunca diga ou dê a entender que a planta dispensa pedreiro, engenheiro ou arquiteto; nunca prometa aprovação, prazo ou custo exato de obra.
- Só relate números que as ferramentas devolverem; nunca estime.
- Decisões (título, preço, versões, gasto com anúncio) são minhas: traga as opções e a sua recomendação.

COMECE ASSIM
1. Atualize o projeto e me diga em 5 linhas em que pé está cada frente (contexto/QUADRO.md e CONTEXTO.md, "Em aberto").
2. Puxe os números das minhas contas conectadas (se nenhuma estiver conectada, me diga como conectar).
3. Me proponha as tarefas desta semana e os 3 ganchos da semana, com a fonte de cada um.
```

### 4. Rotina da semana

| Quando | O Maestro faz (com a ideia do Diretor no conteúdo) | Você faz |
|---|---|---|
| **Segunda** | Puxa os números das redes e do parceiro, atualiza o painel (seções 1 e 7), propõe tarefas e 3 ganchos da semana com a fonte | Aprova as tarefas e escolhe os ganchos |
| **Terça** | Prepara os roteiros e o teleprompter dos vídeos escolhidos | Grava com o apresentador e põe em `brutos/` |
| **Terça a quinta** | Edita cada vídeo (5 versões de gancho quando for teste), gera plantas novas e, quando houver, o PDF do e-book | Aprova o plano de edição e o vídeo pronto |
| **Quinta** | Prepara cada publicação com legenda e horário | Diz "sim" a cada post; publica os reels de teste no app do Instagram |
| **Sexta** | Lê os números de cada reel, preenche o [registro de testes](INSTAGRAM.md#6-registro-dos-testes), aponta a versão vencedora e o que mudar | Decide o que vai para todos e o gancho da semana seguinte |

### 5. Primeira tarefa do Maestro

Atualizar o projeto (`git pull --rebase` na `main`), ler o [quadro](../contexto/QUADRO.md) e o seu [contexto](../contexto/diretor.md) e seguir a seção 3. Todo o trabalho dos chats da nuvem já está na `main`, a única branch (as `frente-*` e a `planta-de-casas-anuncio` acabaram em 22/11/2026): não há nada para juntar.

<!-- era: instagram/referencias-mino-lee.md -->
## Referências de vídeo: Mino Lee (@minolee.mp4)

> Parte da pasta Instagram. Guia da frente: [`INSTAGRAM.md`](INSTAGRAM.md). Painel geral: [`../PAINEL.md`](../PAINEL.md).
>
> Tudo o que vale a pena aproveitar dos três reels, para roteiro, gravação e edição.
> Assisti aos três quadro a quadro (um quadro a cada 1,5 s) e transcrevi o áudio.
> Copiamos o **método**, não o conteúdo nem a imagem dele.

| Reel | Duração | Texto no alto | Formato |
|---|---|---|---|
| [1. "Is it possible to…"](https://www.instagram.com/reel/DflcLspiT9H/) | 78 s | "This 4-word hook got me 70 million views" | Ensina um gancho contando a própria história |
| [2. "i pay Claude $200/month…"](https://www.instagram.com/reel/DfbA-o1u4FI/) | 104 s | "i pay Claude $200/month … it pays me $400k/month" | Lista de 3 itens com prova e valor crescente |
| [3. "POV: Making a viral video…"](https://www.instagram.com/reel/De9dwH9yDB9/) | 91 s | "POV: Making a viral video in 10 minutes with AI" | Bastidor de um desafio com prazo |

---

### 1. Regras que valem para os três

#### Roteiro

1. **O texto na tela e a fala são dois ganchos diferentes.** O texto promete o resultado ("70 milhões de views"); a voz começa outra frase ("Aqui vai uma ideia de vídeo…"). A pessoa lê uma coisa e ouve outra, e as duas puxam para o mesmo lugar.
2. **Número concreto no gancho.** 70 milhões, US$ 200 → US$ 400 mil, 10 minutos. Nunca "muito" ou "rápido".
3. **Prova nos primeiros 3 segundos.** Antes de explicar qualquer coisa, aparecem prints com números (visualizações, faturamento).
4. **Promessa de que vai melhorar.** "Cada coisa me dá cada vez mais dinheiro", "fica cada vez mais específico". Isso segura a pessoa até o último item.
5. **Fala como conversa.** Frases curtas, "e eu pensei: espera…", gírias, risada. Cerca de 3,4 palavras por segundo, sem pausa entre frases.
6. **Admite fraqueza.** "Eu estava quebrado na faculdade, sem credibilidade nenhuma." Isso faz a pessoa pensar "então eu também consigo".
7. **Contraria o senso comum uma vez.** "Muita gente vai te vender a fórmula ideal de roteiro, mas naquele momento eu percebi que…"
8. **Fecho em três negações e uma afirmação.** "Você não precisa ser especialista, não precisa ser bonito, não precisa de vida de luxo. Você precisa topar mostrar o esforço na câmera."
9. **Fala direto com a situação de quem assiste.** "Se você está muito ocupado agora, estudando ou trabalhando numa meta, perfeito: você já tem a história."
10. **Chamada de uma linha:** "Comenta CLASS que eu te mando meu guia grátis." No reel 3 a chamada aparece só escrita na tela, no meio do vídeo, sem ele falar.

#### Edição

1. **Gancho escrito no alto**, letra fina e pequena, duas linhas. Fica de 5 a 12 segundos e depois dá lugar à etiqueta da seção.
2. **Legenda no meio da tela**, letra fina, sem caixa alta, **2 a 3 palavras por vez**. Sempre na mesma altura, mesmo quando a imagem de fundo muda.
3. **Cor da legenda tem função.** Branco para ele; amarelo para a palavra-chave ou para a fala da outra pessoa (reel 3).
4. **Imagem de apoio logo abaixo da legenda**, na altura do peito, pequena. Troca a cada 1,5 a 4 segundos:
   - três miniaturas de vídeos lado a lado, com o número de views;
   - cartão de estatística ("12,4M views · 1,8M likes");
   - print de tela (CapCut, painel de vendas, fatura);
   - foto que vira piada visual (Einstein em "não precisa ser especialista").
5. **Glossário na tela.** Quando ele usa um termo técnico, aparece embaixo, em letra miúda: "midterm = a prova grande no meio do semestre", "clip farming = filmar tudo para virar conteúdo". Ninguém fica perdido.
6. **Desenho simples animado.** Um círculo para "fórmula de roteiro" e um zigue-zague para "altos e baixos emocionais", desenhados em linha branca sobre o vídeo.
7. **Etiqueta de seção** no alto, à esquerda: texto miúdo ("agent 1") em cima do título em negrito ("Websites").
8. **Tela cheia de apoio** com a legenda por cima: gravação de tela, dedo apontando o número, antes e depois. Entrada e saída com movimento rápido de câmera (borrão).
9. **Novo ângulo a cada seção.** Rosto de perto no gancho, plano médio sentado no item 2, câmera baixa no item 3. O cenário é o mesmo, mas a imagem nunca fica igual por mais de 10 segundos.
10. **Corte a cada frase**, com aproximação leve do rosto entre um corte e outro.
11. **Número riscado.** Fatura de US$ 9.675 aparece e o valor é riscado em vermelho: "em vez de pagar isso, usei…".
12. **Retorno visual no fim.** As mesmas três miniaturas do começo voltam no fecho, para amarrar o vídeo.

#### Gravação

- Celular na mão ou apoiado, **luz do ambiente** (janela de dia, luz colorida à noite).
- Roupa comum, fone de ouvido com microfone à vista.
- Gestos grandes com as mãos e expressão exagerada nas partes de emoção.
- Erros, risada e interrupção de amigo **ficam** no vídeo (reel 3).

---

### 2. Reel 1: o gancho "É possível…?"

**Modelo:** "É possível [resultado extremo]?"

**O que ele conta, na ordem:**

| Tempo | Parte | O que acontece |
|---|---|---|
| 0:00 | Gancho | "Uma ideia de vídeo garantida para um milhão de views." Três miniaturas com milhões de views na tela |
| 0:04 | Prova | "Vídeos com esse gancho me deram 100 mil seguidores" |
| 0:08 | Virada de credibilidade | "Quando consegui essas views, eu estava quebrado na faculdade" |
| 0:15 | História | Tinha prova, não queria estudar, pensou: "e se eu fizer um vídeo disso?" |
| 0:22 | O gancho nasce | "É possível gabaritar uma prova estudando só uma hora?" |
| 0:27 | Processo | Fez a prova filmando tudo; juntou os clipes no CapCut |
| 0:38 | Clímax | "Conseguimos, tiramos 83!" (cartão com a nota) |
| 0:43 | Lição | Não é a fórmula de roteiro: é ver alguém passar por **altos e baixos de verdade** |
| 0:57 | Fecho | Não precisa ser especialista; precisa mostrar o esforço |
| 1:07 | Para você | "Se você está ocupado correndo atrás de uma meta, já tem a história. Só filme." |

**Por que funciona:** a pergunta do gancho só é respondida no final, e o caminho tem risco real de dar errado.

**Para plantas de casas:**

1. "É possível desenhar a planta de uma casa em 1 hora?"
2. "É possível caber 3 quartos num terreno de 8 metros de frente?"
3. "É possível vender 10 plantas em 30 dias começando do zero?" (série semanal)
4. "É possível transformar um rabisco de guardanapo numa planta 3D?"
5. "É possível mobiliar essa casa de 50 m² sem apertar ninguém?" (C01, 50 m² desde o redesenho de 22/11/2026)

Roteiro de cada um: pergunta → por que é difícil → processo com o que deu errado → resultado → "comenta PLANTA".

---

### 3. Reel 2: lista com prova e valor crescente

**Modelo:** "Eu pago X por mês… e isso me rende Y." + "Número um, dois, três", cada um maior que o anterior.

**Cada item tem quatro partes:**

1. **Afirmação:** "Todo site do nosso negócio é feito por IA."
2. **O que isso substitui:** logos de ferramentas com o preço de cada uma.
3. **Quanto custaria sem isso:** "Eu teria pago US$ 4.000 a um designer."
4. **Prova na tela:** print do resultado, com o dedo apontando o número.

Depois dos três itens vem a **visão geral** ("você tem a força de 100 pessoas por uma assinatura pequena") e a chamada.

**Para plantas de casas:** "Eu ia pagar R$ [valor] por um projeto. Olha o que eu consegui por R$ [valor]." Itens: planta baixa, planta humanizada, vídeo 3D. Em cada um, o preço de mercado riscado e o resultado na tela. Só use valores que você consiga comprovar.

---

### 4. Reel 3: bastidor de um desafio com prazo

**Modelo:** "POV: fazendo [resultado] em [tempo curto]."

**Estrutura:**

| Parte | O que acontece | Recurso de edição |
|---|---|---|
| Promessa com prazo | "Me veja fazer um vídeo viral em menos de 10 minutos" | Título "POV:" no alto |
| Pedido da ideia | Um amigo dá o tema na hora | Balão no alto mostrando o que foi digitado |
| Atrito | "Por que está demorando tanto?" | Tela do celular em primeiro plano |
| Objeção | O amigo: "isso me deixa inseguro; dá para viralizar sem isso?" Resposta: "dá, só leva mais tempo" | Legenda amarela para o amigo, branca para ele |
| Comparação | "Um processo de 1 hora vira 2 minutos" | Duas barras de tempo: "1 h" e "2 min" |
| Decisão | Escolhe a opção 3 e pede um ajuste | Tela do celular |
| Gravação | Grava o vídeo ali mesmo | Janela pequena com a segunda câmera |
| Resultado | O vídeo pronto entra como final | O próprio resultado é o desfecho |

**Para plantas de casas:** "POV: fazendo a planta 3D da casa de um seguidor em 10 minutos." Alguém manda as medidas do terreno, você mostra o processo com os tropeços, e o vídeo termina com a casa ganhando vida.

---

### 5. O que já está no nosso vídeo e o que falta

| Recurso | Situação |
|---|---|
| Gancho com número concreto (R$ 1.000) | Feito |
| Gancho fixo no alto | Feito |
| Legenda fina, 2 a 3 palavras, palavra-chave em amarelo | Feito |
| Etiqueta de seção ("erro 1" + título) | Feito |
| Fala contínua, uma única pausa proposital | Feito |
| Imagem nova a cada 4 s, nada parado | Feito |
| Promessa de que o último é o pior | Feito (ganchos v3 e v4) |
| Chamada de uma linha ("Comente PLANTA") | Feito |
| Texto do gancho diferente da fala | Feito |
| Glossário na tela (recuo, peitoril, nascente, hall, planta humanizada) | Feito |
| Custo de cada erro, com o valor riscado | **Falta:** precisa de valores reais |
| Prova nos primeiros 3 s (plantas entregues, depoimentos) | **Falta:** só quando houver clientes |
| Novo ângulo de câmera a cada seção | Depende da gravação |
| Retorno visual do começo no fim | **Falta** |

### 6. Lista de conferência para cada vídeo novo

- [ ] O gancho tem um número concreto.
- [ ] O texto na tela e a primeira frase falada são diferentes.
- [ ] Há uma prova visual antes dos 3 segundos.
- [ ] A pergunta do gancho só é respondida no final.
- [ ] Nenhum trecho passa de 4 segundos sem imagem nova.
- [ ] Todo termo técnico tem explicação na tela.
- [ ] A fala não tem pausa, a não ser a da revelação.
- [ ] O vídeo mostra um tropeço ou uma fraqueza real.
- [ ] A chamada final é uma frase só, com uma palavra para comentar.

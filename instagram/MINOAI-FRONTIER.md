# Editor: MinoAI Frontier

> Parte da pasta Instagram: [`INSTAGRAM.md`](INSTAGRAM.md). Painel: [`../PAINEL.md`](../PAINEL.md).
>
> **O editor do projeto agora é a MinoAI Frontier**: o serviço de edição da MinoAI, que corta, legenda, coloca B-roll, música e efeitos em reels de rosto falando. Este arquivo é o **contexto** que ela precisa para editar do nosso jeito: o projeto, o público, o estilo, os arquivos e as regras.
>
> Referência de edição favorita do dono: [`../video/REFERENCIA-CONDOR.md`](../video/REFERENCIA-CONDOR.md) (CONDOR XIII, levado para o reel de planta).
>
> Ela também é o **maestro** da operação inteira: ver [`../MAESTRO.md`](../MAESTRO.md). Quando a edição faz parte da semana do maestro, use a mensagem de abertura de lá; a desta página é para editar um vídeo avulso.

## 1. Onde e como a MinoAI Frontier edita

- **No seu computador**, no app do Claude (aba **Code**), num Mac com chip Apple (M1 ou mais novo, macOS 14+) ou num PC com Windows 10/11. Ela instala sozinha o que precisa (ffmpeg, Node, Python); você não digita comando nenhum.
- **Não edita na nuvem.** Os chats na nuvem deste projeto podem planejar a edição, mas o vídeo só sai no seu computador.
- **Precisa:** plano pago do Claude (Pro ou Max) e o conector MinoAI Frontier ligado na aba Code. Se ainda não estiver no seu Claude: app.contentacademy.io/mcp, opção Claude.

## 2. Configuração (uma vez só)

| # | O que fazer | Por quê |
|---|---|---|
| 1 | No Mac, criar a pasta **Filmes/X1-Plantas** (no Windows, **Vídeos/X1-Plantas**) e copiar para ela a pasta **`broll/`** descrita na seção 4 | É onde a MinoAI Frontier procura os vídeos e o B-roll |
| 2 | Criar o seu **estilo de edição** no [Edit Style Generator](https://app.contentacademy.io/ai-editing/studio), com os 3 reels de referência do Mino Lee: [reel 1](https://www.instagram.com/reel/DflcLspiT9H/), [reel 2](https://www.instagram.com/reel/DfbA-o1u4FI/), [reel 3](https://www.instagram.com/reel/De9dwH9yDB9/) | Hoje a sua conta **não tem estilo salvo**: ela editaria com o padrão dela. Com o estilo salvo, ela segue o mesmo estilo que analisamos em [`referencias-mino-lee.md`](referencias-mino-lee.md) |
| 3 | Conectar o **Instagram** em app.contentacademy.io/mcp/connect-socials?platform=instagram (TikTok e YouTube Shorts, se quiser postar lá também) | Hoje **nenhuma rede está conectada**. Conectada, ela pode preparar a publicação. Os reels de teste você confere no app do Instagram |
| 4 | Na primeira edição, quando ela pedir, **permitir os comandos do editor** uma vez | Para não aparecerem pedidos de aprovação a cada passo |

## 3. A mensagem de abertura

Cole esta mensagem na aba **Code**, com a pasta **Filmes/X1-Plantas** aberta, toda vez que for editar. Troque só a primeira linha.

```text
Edite este vídeo no estilo MinoAI Frontier: [nome do arquivo] — tipo: [ANÚNCIO versão vN | PLANTA DA SEMANA | É POSSÍVEL | ERRO QUE SAI CARO | CABE NO SEU LOTE].

CONTEXTO DO PROJETO
- Perfil brasileiro de plantas de casas. O produto é um e-book com dezenas de plantas originais em blueprint, planta humanizada e 3D.
- Público: quem tem um lote e vai construir, quase sempre com pedreiro e sem arquiteto, muitas vezes por etapas. Classe C, 25 a 50 anos. A pergunta dele é "que casa cabe no meu lote?".
- Objetivo de todo vídeo: a pessoa assistir até o fim e comentar PLANTA para receber uma planta grátis no WhatsApp.

IDIOMA
- Tudo em português do Brasil. Legendas com acentos (ç, ã, õ, é); confira que a fonte mostra todos.
- Dinheiro sempre com a unidade: "R$ 1.000", "mil reais". Medidas como "10 x 20", "55 m²".

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

SE FOR ANÚNCIO (versão v1 a v5)
- A camada broll/anuncio/vN/camada-transparente.webm já tem gancho, legenda, cartões, glossário e barra de progresso.
- NÃO coloque outra legenda nem outro texto. Faça o corte da fala (zero espaço morto), coloque a camada por cima, começando no 0:00, e faça o áudio.
- Os tempos de cada item estão no teleprompter (video/VIDEO.md, seção 3). Se a fala cortada não bater com os tempos da camada, me mande a transcrição com os tempos de cada frase, em vez de esticar ou cortar fala.
- Nos trechos de tela cheia da camada (0:00 a 0:03 e 0:27 a 0:34) o apresentador some de propósito; a voz continua.

REGRAS QUE NUNCA MUDAM
- Nunca dizer nem dar a entender que a planta dispensa pedreiro, engenheiro ou arquiteto.
- Nunca prometer aprovação na prefeitura ou no banco, prazo de obra ou custo exato de construção.
- Chamada final sempre: "Comenta PLANTA".
- Mostre o plano de edição antes de renderizar quando a edição for maior que só legenda.

ENTREGA
- 1080 x 1920, vertical, salvo em Filmes/X1-Plantas/editados/ com o nome [data]-[tipo]-[versão].mp4.
- No fim, me diga: duração, quais imagens do B-roll usou e em que segundos, e o texto do gancho.
```

## 4. A pasta `broll/` no seu computador

Monte uma vez e acrescente cada planta nova. Tudo vem deste repositório:

```
Filmes/X1-Plantas/
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

## 5. Como cada tipo de vídeo deve ficar

| Tipo | Duração | Estrutura | B-roll |
|---|---|---|---|
| **Anúncio (v1 a v5)** | 38 s | Já definida pela camada ([`../video/VIDEO.md`](../video/VIDEO.md)) | A própria camada |
| **Planta da semana** | 15 a 25 s | Gancho com a medida do lote → passeio pela casa → "Comenta PLANTA" | `animacao.mp4` da planta, depois blueprint e perspectivas |
| **Cabe no seu lote** | 20 a 30 s | "Tem um lote [medida]?" → 3 casas que cabem, uma por bloco → chamada | Planta humanizada de cada casa |
| **Erro que sai caro** | 15 a 25 s | Gancho do erro → por que sai caro → a planta mostrando o certo → chamada | Blueprint e planta humanizada |
| **É possível…?** | 40 a 70 s | Pergunta → por que é difícil → processo, com o que deu errado → resultado → chamada | Gravação de tela do processo + animação da planta no fim |

## 6. Ganchos de referência da biblioteca da MinoAI Frontier

Ganchos reais e com muitas visualizações, achados na biblioteca da MinoAI Frontier, adaptados para o nosso nicho. O original fica entre aspas; a adaptação mantém a estrutura.

| Original | Adaptação |
|---|---|
| "The most expensive mistake that could cost you over $100,000 building a business in your 5 to 9 is to build it on your employer's computer." ([@itshannahzhang](https://www.instagram.com/p/DaBM835JTiM/)) | "O erro mais caro que pode te custar [valor] construindo a sua casa é [erro]." |
| "Before you cover the AC for winter, avoid these two huge mistakes." ([@weeklyhomecheck](https://www.instagram.com/p/Dd92bI9zsgx/)) | "Antes de bater a laje, evite esses dois erros enormes." |
| "My name is Bert and I'm going to build my house." + texto "PT.35 House update" ([@buildwithbert](https://www.instagram.com/p/DbXB9latjHl/)) | Série: "Eu vou desenhar 35 casas para o seu lote." + "Parte 1", "Parte 2"… mostrando cada planta nova |
| "Five things you need to know if you're going to batch create high quality content and ruin your white couch." ([@iamsarahsnow](https://www.instagram.com/p/DIZXgXLPyFt/)) | "Cinco coisas que você precisa saber se vai construir num lote 10 x 20 e não quer jogar dinheiro fora." |

Para achar mais: peça à MinoAI Frontier "ganchos virais sobre construir casa" (busca de ganchos) ou "analise o gancho deste vídeo: [link]" (análise de gancho).

## 7. Do método do Mino (biblioteca de aulas da MinoAI Frontier)

- **Um B-roll por frase**, coerente com o que está sendo dito, e **2 a 4 imagens diferentes nos primeiros 5 segundos** ([aula de edição do Content Bootcamp](https://whop.com/joined/contentacademy/content-bootcamp-3pqyjhwaG9gmeC/app/courses/cors_7pWrAMvSU9J9TvKJP0c8tK/lessons/lesn_Vcp6Z4ZU1v864AZYUFvCy/)).
- **Para público acima de 25 anos, nada de cortes hiperrápidos** (a cada 0,75 s): funciona para público mais jovem e cansa o nosso ([Mastering Superhooks](https://www.loom.com/share/991211e6490344b283941f4204a7b8df)).
- **O B-roll responde o que falta de contexto.** Quando o apresentador diz "lote 10 x 20", a planta com a cota 10 x 20 precisa estar na tela.
- **Zoom lento num detalhe** destaca um objeto. Use na planta humanizada para mostrar o cômodo de que se está falando.

## 8. Rotina semanal com a MinoAI Frontier

| Quando | O quê | Quem |
|---|---|---|
| Segunda | Escolher os vídeos da semana no [plano do perfil](plano-perfil.md) e no [painel](../PAINEL.md), seção 6 | Você |
| Terça | Gravar e colocar as gravações em **brutos/** | Apresentador |
| Terça a quinta | Editar cada vídeo com a mensagem da seção 3; aprovar o plano de edição quando ela mostrar | MinoAI Frontier e você |
| Quinta | Publicar as versões como reels de teste | Você |
| Sexta | Anotar os resultados no [registro de testes](INSTAGRAM.md#6-registro-dos-testes) | Você |

**Antes de publicar**, confira o vídeo pronto com a [lista de conferência](referencias-mino-lee.md#6-lista-de-conferência-para-cada-vídeo-novo) e o [checklist de anúncio](../video/anuncios/checklist-revisao.md).

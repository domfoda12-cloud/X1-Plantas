# Resumo: Caderno de pesquisa

> Tudo o que a equipe achou na web, por tema, com fonte, data e certeza. **Leia este resumo primeiro**; abra um documento inteiro só quando a tarefa pedir. Índice geral: [`INDICE.md`](../INDICE.md). Quem lê: todos.

## O essencial

<!-- essencial: escrito à mão, o gerador não apaga -->
- Toda busca na web de qualquer agente fica aqui, por tema, com data, quem, fonte e certeza (dono, 22/11/2026).
- Antes de buscar na web: `python3 ferramentas/pesquisa.py buscar <palavras>`. Já tem achado com fonte? Use e não busque de novo.
- Só se escreve com `pesquisa.py nova`; sem link ou `arquivo:` não entra. O `checar.py` confere o formato.
- Pesquisa longa (relatório, apostila) continua em `ebook/referencias/` ou `reports/`; aqui fica a linha com o achado e o link para ela.
<!-- /essencial -->

## Os 16 documentos

### [Pesquisa: Concorrentes e o que eles vendem](concorrentes.md)

Caderno compartilhado da equipe. Escreva só com `python3 ferramentas/pesquisa.py nova`; leia com `buscar`. Certeza: confirmado (texto oficial), secundaria (fonte secundária), hipotese.

Tamanho: 784 palavras.

### [Catálogos de terceiros: o que vale olhar (26/11/2026)](ferramentas/catalogos-2026-11-26.md)

Passo 1 da pesquisa (Pesquisador, Sonnet). Falta a conferência do Opus. Nada foi instalado, conectado ou rodado. Só se leu: README bruto das três listas e a documentação oficial dos itens abaixo. Data das leituras: 26/11/2026.

Seções: 1. public-apis/public-apis (https://github.com/public-apis/public-apis , raw README 26/11/2026); 2. ripienaar/free-for-dev (https://github.com/ripienaar/free-for-dev , raw README da `master`, 26/11/2026); 3. punkpeye/awesome-mcp-servers (https://github.com/punkpeye/awesome-mcp-servers , raw README, 26/11/2026); 4. Meta Graph API (Instagram) por API oficial: o que ela exige (fonte primária, lida 26/11/2026); 5. Os 5 de maior uso, em ordem; 6. O que NÃO confirmei.

Tamanho: 2795 palavras.

### [Marketing for Founders (EdoStra): o que serve ao X1-Plantas e ao Instagram de IA](ferramentas/marketing-for-founders-2026-11-26.md)

Pedido do dono, 26/11/2026. Só ferramentas grátis; nada instalado. Passo 1 da pesquisa em dois passos: o Opus confere e conclui depois.

Seções: O repositório; Os 10 itens; Dos 10, qual eu faria primeiro (suposição, o dono decide); Descartei (e por quê); O que não confirmei.

Tamanho: 1394 palavras.

### [Pesquisa: Ferramentas, skills, modelos e custos](ferramentas.md)

Caderno compartilhado da equipe. Escreva só com `python3 ferramentas/pesquisa.py nova`; leia com `buscar`. Certeza: confirmado (texto oficial), secundaria (fonte secundária), hipotese.

Tamanho: 1987 palavras.

### [Estudo: @science_in_8bit (Instagram 100% IA, ciência em pixel art)](instagram-ia/estudo-science-in-8bit.md)

Pedido do dono, 25/11/2026. Passo 1 da pesquisa (Pesquisador): achados com fonte e grau de certeza; o Opus confere e conclui. Só ferramentas grátis.

Seções: 1. Perfil (fonte: TinyFish fetch, 25/11/2026) -- CONFIRMADO na página; 2. Achados da busca (TinyFish search, 25/11/2026) -- fonte secundária/primária mista; 3. O método e a "máquina por trás" -- CONFIRMADO nas páginas oficiais deles (25/11/2026); 4. Análise de reels (MinoAI Frontier analyze_hook, 25/11/2026); 5. Mais achados de busca (TinyFish, 25/11/2026); 6. Como fazem de verdade: sem modelo de vídeo de IA (CONFIRMADO por 2 fontes que se confirmam; 25/11/2026); 7. Perfis parecidos (para mapear a concorrência; não confirmei métricas); 8. Regras do Instagram sobre IA (fonte SECUNDÁRIA, resultados de busca, set a nov/2026; não abri a regra oficial da Meta); 9. CONCLUSÕES (leitura do Pesquisador; o Opus confere. "Prova" = onde está o achado acima); 10. O que faltou estudar; 11. Segunda rodada (25/11/2026).

Tamanho: 3868 palavras.

### [Ferramentas grátis para animação em código (Instagram 100% IA)](instagram-ia/ferramentas-gratis-animacao.md)

Passo 1 da pesquisa (Pesquisador, Sonnet). Data da busca: 25/11/2026. Nada instalado. Falta conferência do Opus.

Seções: 1. Código -> vídeo 1080x1920; 2. Música/SFX chiptune; 3. Voz local pt-BR; 4. Fonte pixel OFL.

Tamanho: 655 palavras.

### [Jurado ALCANCE E PÚBLICO (nicho do Instagram 100% IA)](instagram-ia/juri-nicho/jurado-alcance.md)

Ângulo: quem compartilha, por que para de rolar, se rende série infinita de temas, língua. Só uso o que está em `estudo-science-in-8bit.md` (cito seção/linha). Nenhum número de seguidores ou métrica inventado. O que é meu julgamento está marcado como "leitura".

Seções: Critérios que tirei do estudo; Notas; Leitura final (curta).

Tamanho: 1224 palavras.

### [Júri do nicho: jurado 3, PRODUÇÃO E SUSTENTO](instagram-ia/juri-nicho/jurado-producao.md)

26/11/2026. Júri estrito, sem ver os outros jurados. Pergunta: dá para fazer 1 reel bom por dia, por meses, só com código e ferramentas grátis, sem cair em AI slop? Quanto custa verificar cada fato? Som e visual podem ser nossos (não o pixel 8 bits, que é a marca deles)? Há produto depois?

Seções: O que a prova já mostra (vale para as 8 ideias); Notas; Leitura do jurado.

Tamanho: 1332 palavras.

### [Júri do nicho: jurado de HONESTIDADE E RISCO](instagram-ia/juri-nicho/jurado-risco.md)

Data: 26/11/2026. Jurado estrito, sem ver os outros. Base: `pesquisas/instagram-ia/estudo-science-in-8bit.md` (lido inteiro, seções 1 a 11). Onde cito regra fora do estudo (OAB, CVM, CDC), digo que é conhecimento meu, não verificado com ferramenta nesta rodada: precisa ser aberto na fonte oficial…

Seções: Riscos que valem para TODAS as ideias; Avaliação das 5 ideias (seção 9), da ideia 6 do coordenador e uma sétima minha; O que o projeto precisa ter, qualquer que seja o nicho; Tabela final.

Tamanho: 2029 palavras.

### [Júri do nicho: PRESIDENTE (síntese da rodada 1)](instagram-ia/juri-nicho/presidente.md)

26/11/2026. Presidente: Fable 5.2, não opinou nesta rodada. Método: `CONSELHO.md`, seção 5b. Li os três pareceres desta pasta, `../estudo-science-in-8bit.md`, `../referencia-math-phonk.md`, `../ferramentas-gratis-animacao.md` e `../prototipo/`. Nenhum número de alcance aqui é meu: todos estão nos…

Seções: 1. Fatos conferidos no repositório (13; a regra pede 5); 2. Notas por ideia; 3. Síntese: o que o júri recomenda; 4. Chegou a 8,5?; 5. Os 3 testes de produção, em ordem.

Tamanho: 2360 palavras.

### [Referência do dono: "Buckshot Roulette, mas é matemática" (26/11/2026)](instagram-ia/referencia-math-phonk.md)

O dono mandou (26/11, 00:40): https://www.instagram.com/p/DeO_kdLAYSb/ ; "the sounds are really nice really gets the attention, nice visuals and i honestly like the math real world application idea (i like math)". Análise: MinoAI Frontier `analyze_hook`, 26/11.

Seções: Mais referências do dono (26/11, madrugada); Referência 5: música famosa animada em low-poly 3D (26/11); 4. Casa em L, "simulador de cidade" (26/11/2026).

Tamanho: 1402 palavras.

### [Pesquisa: Público, preço, demanda e números de mercado](mercado.md)

Caderno compartilhado da equipe. Escreva só com `python3 ferramentas/pesquisa.py nova`; leia com `buscar`. Certeza: confirmado (texto oficial), secundaria (fonte secundária), hipotese.

Tamanho: 470 palavras.

### [Pesquisa: Normas, leis e código de obras](normas.md)

Caderno compartilhado da equipe. Escreva só com `python3 ferramentas/pesquisa.py nova`; leia com `buscar`. Certeza: confirmado (texto oficial), secundaria (fonte secundária), hipotese.

Tamanho: 3225 palavras.

### [Pesquisa: O que não cabe nos outros](outros.md)

Caderno compartilhado da equipe. Escreva só com `python3 ferramentas/pesquisa.py nova`; leia com `buscar`. Certeza: confirmado (texto oficial), secundaria (fonte secundária), hipotese.

Tamanho: 1176 palavras.

### [Pesquisa: Projeto de casa: referências, medidas, arranjo](plantas.md)

Caderno compartilhado da equipe. Escreva só com `python3 ferramentas/pesquisa.py nova`; leia com `buscar`. Certeza: confirmado (texto oficial), secundaria (fonte secundária), hipotese.

Tamanho: 2298 palavras.

### [Pesquisa: Vídeo, gancho, edição e redes sociais](video.md)

Caderno compartilhado da equipe. Escreva só com `python3 ferramentas/pesquisa.py nova`; leia com `buscar`. Certeza: confirmado (texto oficial), secundaria (fonte secundária), hipotese.

Tamanho: 3146 palavras.

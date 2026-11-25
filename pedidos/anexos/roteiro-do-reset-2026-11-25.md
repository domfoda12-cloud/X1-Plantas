# Roteiro do reset: só o trabalho braçal (25/11/2026)

> **Pedido do dono** (ficha `2026-11-25-1612`): "Ate o reset quero que deixe tudo absolutamente planejado preparado e clean para quando chegar no reset voce só ter que fazer o trabalho bracal". **Recado da mesma hora** (ficha `2026-11-25-1613`): a identidade visual vem antes, "a ultima coisa importante a se fazer antes do reset".
> **Quem usa:** a conversa que abrir no reset. Leia este arquivo, o topo do `contexto/QUADRO.md` e o `contexto/entregas/ULTIMO.md`. Não releia o resto do projeto: tudo o que é preciso está aqui ou nos anexos citados.

## 0. Estado na hora de fechar (conferir antes de começar)

- `python3 ferramentas/checar.py` verde em 25/11 (só o aviso velho de "janela em cima de porta" nas plantas fora do lançamento, que não entram no PDF).
- Caminho do e-book (`python3 ferramentas/plano.py caminho D6`): feitos D1, D2, D16 a D22, D31 a D36, A1, A3, A4, A8 a A10, J1. **Faltam:** identidade aplicada (novo), as 5 frases (se o dono quiser), D3 (gerar), D4 (Revisor no Fable), D5 (emergência), D48 (título), D23 (profissional), D6 (Drive).
- Anexos prontos para colar: as 5 frases (`frases-das-5-paginas-2026-11-25.md`), a identidade (`identidade-2026-11-25.md`), os 3 títulos (`titulos-opcoes-2026-11-24.md`).

## 1. A mensagem ao dono, logo no reset (uma só, com tudo)

Mande isto e espere a resposta. O trabalho que não depende dela começa já (passo 2).

> 1. **Páginas da dor e saída** (frases prontas e lidas pelo Revisor: `veto-frases-das-5-paginas-2026-11-25.md`): mudar (a) as 5, (b) só as 2 das casas (8 e 12), (c) nenhuma agora. Se a pág. 8 mudar: o título da pág. 9 passa de "Cabe num lote de 8 x 15 m" para "Deve caber num lote de 8 x 15 m"?
> 2. **Título:** "A casa do seu lote", "Errar na planta sai caro", "Sua casa antes da obra" ou o atual, "Antes do primeiro tijolo".
> 3. **"Gera o PDF"**: posso gravar a versão oficial em `ebook/saida/`?
> 4. **Pasta no Drive:** posso criar? Com qual nome (sugestão: o título)?
> 5. **Profissional do checklist dos bônus:** já tem alguém? Se não, o PDF sai com o selo de rascunho nos bônus.
> 6. **Grátis** (cartão j3): a planta decorada da Casa Compacta, a ficha "Cabe no seu lote?" e o guia "Seu lote cabe?", sem 3D. Sim ou não?
>
> Sem resposta: as frases não entram, o título fica o atual, nada é gravado em `ebook/saida/` e nada vai ao Drive.

A identidade já foi escolhida antes do reset (ficha `1613`). Se não foi, ela é a pergunta 0 e o passo 2 espera.

## 2. Em ordem, um por vez

| # | Passo | Quem | Comando ou arquivo | Pronto quando | Espera |
|---|---|---|---|---|---|
| 1 | Aplicar a identidade escolhida no gerador (tokens no `livro.css`, sinal próprio, ritmo de página) | Designer faz, Maestro confere | a lista "onde entra" do `identidade-2026-11-25.md` | `python3 ebook/gerador/livro.py --previa <pasta> --duas-partes` sem página estourada; as páginas-amostra aprovadas batem com a prévia | identidade escolhida |
| 2 | Colar as frases escolhidas, já com as trocas do Revisor | Maestro (é só colar) | as linhas "trocar" do `frases-das-5-paginas-2026-11-25.md` + as trocas do `veto-frases-das-5-paginas-2026-11-25.md` | `pdftotext -f N -l N` de cada página mostra o texto novo, sem estouro | resposta 1 |
| 3 | Trocar o título (D48 dentro do D3) | Maestro; Redator troca os 2 arquivos da lista do J2 | `ebook/config.json`, `atributos-que-vendem.md`, `VISUAL.md` | `config.json` com o título da fala do dono; "de referência" na capa | resposta 2 |
| 4 | `python3 ferramentas/checar.py` | Maestro | | verde | 1 a 3 |
| 5 | Gerar o oficial (D3) | Maestro | `python3 ebook/gerador/livro.py` (grava `ebook.pdf` e `bonus.pdf`) | os 2 arquivos em `ebook/saida/` com a hora nova; `checar.py` com "o PDF não cita preço" | resposta 3 |
| 6 | Leitura final (D4) | `revisor-de-risco` com `model: fable` | os 2 PDFs | SIM escrito na ficha `1946-refazer`, com a data. NÃO: corrigir, voltar ao 5 | 5 |
| 7 | PDF de emergência (D5) | Maestro | `python3 ferramentas/pdf-leve.py ebook/saida/ebook.pdf <destino>` | o mesmo número de páginas do final, todas olhadas | 6 |
| 8 | Pasta no Drive (D6) | Maestro, conector do Drive | final, bônus e emergência | permissão "qualquer pessoa com o link: leitor", nunca "editor"; link mostrado ao dono | resposta 4 e 5 |
| 9 | Fechar: fichas, plano, quadro, salvar | Maestro | `plano.py feito`, `pedido.py fechar`, `atualizar-painel.py`, `salvar.py` | zero avisos | tudo |

**Marcar ao fazer:** `python3 ferramentas/plano.py feito D3 "..."` (e D4, D5, D48, D6); `python3 ferramentas/plano.py respondido <n> "fala do dono"` para as decisões 50 (gera), 34 (título), 32 (Drive), 41 (profissional), 47 (grátis).

## 3. Depois do e-book (não no mesmo dia, a menos que o dono peça)

1. O grátis final (D8), já com a identidade.
2. As mensagens do WhatsApp e o Instagram do X1, com a mesma identidade.
3. **O Instagram solo de IA:** repositório e conversa próprios (dono, 25/11: "Vai ter"). O kit de partida está em `kit-instagram-ia-2026-11-25.md`. Quem cria o repositório e a conta é o dono.

## 4. O que não fazer no reset

- Não reabrir o mapa da dor e saída, os 7 erros ou o cômodo a cômodo: estão decididos.
- Não lançar mais de 2 agentes juntos; não religar a tarefa de hora em hora.
- Não gerar imagem paga (OpenArt) sem o "sim" do dono.
- Não mexer na visita 3D (guardada pelo dono em 24/11).

# Resumo: Pedidos do dono

> Como cada prompt vira trabalho: quem interpreta, quem executa e as fichas dos pedidos. **Leia este resumo primeiro**; abra um documento inteiro só quando a tarefa pedir. Índice geral: [`INDICE.md`](../INDICE.md). Quem lê: todos.

## O essencial

<!-- essencial: escrito à mão, o gerador não apaga -->
- Todo prompt do dono é gravado sozinho em `pedidos/entrada/` pelo gancho `UserPromptSubmit`; a pasta fica fora do git (`LEIA-ME.md`).
- O Fable (a conversa principal) interpreta o prompt e escreve a ficha em `pedidos/AAAA-MM/`; depois confere o resultado e responde ao dono (`LEIA-ME.md`).
- Trabalho do projeto vai para o agente do papel, no Opus; pesquisa a fundo vai para o `pesquisador`, no Sonnet; tarefa simples e pessoal do dono vai para o `ajudante`, no Haiku (`LEIA-ME.md`).
- Pergunta curta que o Fable já sabe responder e tarefa de uma linha ele faz direto: delegar custaria mais (`LEIA-ME.md`).
- Assunto pessoal do dono não vira ficha no repositório (`LEIA-ME.md`).
- A ficha tem: prompt palavra por palavra, o que ele pediu, pronto quando, suposições, quem executa e resultado (`LEIA-ME.md`).
<!-- /essencial -->

## Os 1 documentos

### [Pedidos do dono: como cada prompt vira trabalho](LEIA-ME.md)

Regra do dono (22/11/2026). Todo prompt dele é guardado, interpretado por um modelo e executado por outro, para o modelo caro pensar e o barato fazer o que é simples.

Seções: O caminho de um prompt; Quem faz o quê; Modelo da ficha; Limites honestos.

Tamanho: 465 palavras.

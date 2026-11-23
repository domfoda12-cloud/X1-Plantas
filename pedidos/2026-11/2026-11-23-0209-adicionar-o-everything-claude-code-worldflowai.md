# Adicionar o everything-claude-code (worldflowai)

**Estado:** aberta

**Prompt (palavra por palavra):** https://github.com/worldflowai/everything-claude-code
add

*Recado de 23/11 02:13:* Dont give up because it would break, try to make it work without breaking

*Recado de 23/11 02:14:* Take that for every new agent added and make sure theyre properly introduced

**O que ele pediu, parte por parte:** Adicionar o everything-claude-code (github.com/worldflowai/everything-claude-code).

**Por que ele pediu, ou o que quer descobrir:** Quer o sistema mais capaz e que aprenda sozinho ("work like a brain"); este pacote traz agentes, skills, comandos e ganchos de quem venceu um hackathon da Anthropic.

**Objetivo dele:** Juntar ao sistema o melhor que já existe pronto.

**Ligação com as ideias gerais do projeto:** Fio 6 (qualidade), fio 4 (autonomia).

**Perguntas que me fiz:** Licença? É cópia (fork) de affaan-m/everything-claude-code; MIT, Copyright (c) 2026 Affaan Mustafa (lida no original). O que traz? 9 agentes de programação (planner, architect, tdd-guide, code-reviewer...), skills (coding-standards, backend e frontend patterns, continuous-learning, strategic-compact, tdd-workflow, security-review, eval-harness, verification-loop), comandos (/tdd, /plan, /learn, /checkpoint, /verify...), regras para ~/.claude/rules e ganchos. Os ganchos (hooks/hooks.json, lidos): um BLOQUEIA criar qualquer .md que não seja README, CLAUDE, AGENTS ou CONTRIBUTING (o nosso sistema inteiro é .md: fichas, caderno, contextos); outros rodam Node no começo e no fim de cada sessão, avisam sobre tmux, conferem console.log em TS. Serve ao e-book? A parte de programação, não; continuous-learning, verification-loop e strategic-compact casam com o "cérebro" e o aprendizado da noite.

**Pronto quando:** Entrar na proposta de integração (sexta adição) e passar pelo laço do júri; nada instalado antes do veto do Revisor e do "sim" do dono.

**Suposições (o dono não disse):** Que 'adicionar' pode ser pegar só as skills de aprendizado (lidas e adaptadas), sem o plugin e sem os ganchos, porque os ganchos quebram o projeto. Vira pergunta ao dono.

**Quem executa:** Maestro; júri (laço da noite); Revisor.

**Conferência:** (no fim)

**Resultado:** (a preencher)


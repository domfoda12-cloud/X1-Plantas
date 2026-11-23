# design system extraido do codigo (artefato)

**Estado:** fechada em 23/11/2026

**Prompt (palavra por palavra):** Extract the design system from this codebase and make a new design system.

**O que ele pediu, parte por parte:** (1) tirar do código o design system que já existe (cores, tipos, espaços, logos, ícones); (2) montar com isso um design system novo, como artefato do tipo Design System (a sessão foi aberta por esse modelo).

**Por que ele pediu, ou o que quer descobrir:** ter a marca num lugar só, para todo material novo (e-book, posts, vídeo, vitrine) sair igual sem cada agente reler o CSS.

**Objetivo dele:** material coerente, que passa confiança ao comprador ("projeto conferido"), feito mais rápido e com menos retrabalho.

**Ligação com as ideias gerais do projeto:** baixa custo e risco: o Designer e o Editor consultam um guia; as regras de honestidade (seção 9 da ESTRATEGIA) estão no guia.

**Perguntas que me fiz:** qual logo é o oficial? (o histórico de 21/11 recomenda o de perfil; o dono não confirmou); o tema escuro existe? (só na tela, plano-visual.html; o e-book é sempre papel); construir componentes? (não há biblioteca, só classes CSS: fica para o dono escolher).

**Pronto quando:** artefato publicado com tokens, guia da marca, logos, ícones e capa, e os dois temas conferidos.

**Suposições (o dono não disse):** nome "X1 Plantas"; logo de perfil como recomendado (não aprovado pelo dono); valores em pt e mm convertidos para px; logos com os nomes DOMINIC & DAVI ficaram de fora (precisam de autorização escrita).

**Quem executa:** Opus (Maestro), sozinho: tarefa interna que não vai ao público nem custa dinheiro; conselho de bolso (Designer, Revisor) aplicado às regras de cor, contraste e honestidade.

**Conferência:** contraste de 21 pares calculado (2 abaixo de 4,5:1 vêm do código e estão anotados); capa vista nos dois temas por captura do Playwright; tokens.json lido de volta como JSON válido.

**Resultado:** Design system X1 Plantas publicado como artefato (tokens, guia, logos, ícones, capa); componentes à escolha do dono. Link (privado): https://claude.ai/artifact/FMbvtEZcoKTyGbQzXTZDPw. 45 cores em 2 temas, 20 estilos de texto, 13 espaços, 7 raios, 4 sombras, 4 linhas, 3 logos, 4 ícones.

**O que aprendi:** designer: a marca já tem regras fortes no código (papel, azul de projeto, fita); o rótulo RUA e o texto da AMPLIAÇÃO ficam abaixo de 4,5:1 e valem conserto no livro.py.


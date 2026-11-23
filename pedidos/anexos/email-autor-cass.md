# E-mail ao autor do cass: ENVIADO em 23/11/2026 do Gmail do dono, com o sim dele, assinado "Dominic de Lima, a solo founder"

(Abaixo, o rascunho de origem.)

> Ficha `2026-11-22-2237-busca-nas-conversas-propria-opcao-c-e-e-mail-ao-autor-do-cas.md`. O dono troca os campos entre colchetes e manda **do e-mail dele, em particular** (não como issue pública). Esta sessão não manda e-mail. O endereço do autor não está aqui: pegue no perfil dele no GitHub (github.com/Dicklesworthstone) ou no site dele. Anexe `pedidos/anexos/conversas-para-o-autor.py` (a cópia limpa, sem nada do projeto), **não** a cópia do repositório. Os colchetes são escolha sua (o Fable marcou que eu não sei se "solo founder" é verdade).
>
> Veto do Revisor (22/11): sem nome do projeto, sem o negócio, sem trecho de conversa, sem caminho de arquivo, sem conclusão jurídica, sem sugerir ligação com a Anthropic; e com a verdade sobre a instalação de 22/11 (esconder isso seria VETO).

**Subject:** Permission request under the cass license rider

Hi Jeffrey,

I'm [your name], [a solo founder / como você quiser se apresentar]. I work with a small team of AI coding agents (Claude Code) on [my own project / my own projects], and I'd love for them to be able to look up what I've already told them in earlier sessions instead of asking me again. cass looks like exactly the right tool.

Reading your LICENSE, the OpenAI/Anthropic rider stood out: my agents run on Claude, and some of my sessions run in Anthropic's cloud. So I want to be upfront about two things:

1. On 22 November, at my request, one of my agents (in a cloud session) first started `cargo install --git` on your repository, which began downloading your source code; it was stopped before anything was built, and no source file was opened. It then installed the v0.11.0 release binary and ran `cass --version` once. It had seen the rider mentioned in the README but had not read it yet. As soon as it read it, the binary and the download were removed, and the saved copies of your README, LICENSE and Homebrew formula were deleted (short excerpts remain in that session's log). No index was ever built.
2. My agents will not use cass without your permission.

So I'd like to ask: would you give written permission for this use?
- cass running locally on my own computer, invoked by my Claude Code agents;
- read-only searches over my own session history, for [my own single project / my own projects];
- nothing redistributed, hosted for others, or used for training or evaluation.

In the meantime, so I'm not stuck, my agent wrote a very small search of its own from scratch (about 100 lines of Python). It only reads Claude Code's local session logs for one project folder, masks common patterns of personal data and keys, and never writes anything. It doesn't use or contain any cass code; we only read your README, LICENSE and Homebrew formula. It's attached in case it's useful or interesting to you.

Either way, thanks for building cass and for being clear about the terms.

Best,
[your name]
[your e-mail]

"""Guarda cada prompt do dono, palavra por palavra, em pedidos/entrada/ (um arquivo por prompt).

É chamado sozinho pelo Claude Code a cada mensagem do dono (gancho UserPromptSubmit em .claude/settings.json):
recebe pela entrada padrão um JSON com o campo "prompt". Devolve um lembrete curto para quem atende (a regra da ficha) e nunca falha a conversa.
A pasta entrada/ fica fora do git: quem interpreta o pedido decide o que vira ficha em pedidos/ (ver pedidos/LEIA-ME.md).
"""
import json
import sys
from datetime import datetime
from pathlib import Path

ENTRADA = Path(__file__).resolve().parent.parent / "pedidos" / "entrada"

try:
    dados = json.load(sys.stdin)
    texto = (dados.get("prompt") or "").strip()
    # só o que o dono escreveu: relatório de agente, aviso do sistema e gancho de parada não são pedido dele
    NAO_E_DO_DONO = ("Another Claude session", "<agent-message", "<task-notification", "[SYSTEM NOTIFICATION", "Stop hook feedback",
                     "<system-reminder", "[Request interrupted", "This session is being continued", "<local-command")
    if texto and not texto.startswith(NAO_E_DO_DONO):
        ENTRADA.mkdir(parents=True, exist_ok=True)
        agora = datetime.now()
        arq = ENTRADA / f"{agora:%Y-%m-%d-%H%M%S}.md"
        arq.write_text(f"<!-- {agora:%d/%m/%Y %H:%M:%S} · conversa {dados.get('session_id', '?')} -->\n{texto}\n", encoding="utf-8")
        abertas = sum(1 for f in ENTRADA.parent.glob("20*/*.md") if "**Estado:** aberta" in f.read_text(encoding="utf-8"))
        # lembrete curto para quem atende: o gancho guarda, mas a ficha é escrita por quem interpreta
        print(json.dumps({"hookSpecificOutput": {"hookEventName": "UserPromptSubmit", "additionalContext": (
            "Prompt do dono guardado em pedidos/entrada/. Regra (pedidos/LEIA-ME.md): trabalho novo = "
            "`python3 ferramentas/pedido.py nova \"assunto\"` e preencha a ficha (por quê, objetivo, ligação com "
            "contexto/dono/IDEIAS-GERAIS.md, quem executa por modelo) antes de delegar; recado de pedido aberto = "
            "`pedido.py recado <ficha>`; pergunta curta ou assunto pessoal = responda sem ficha. "
            f"Fichas abertas agora: {abertas}.")}}, ensure_ascii=False))
except Exception:
    pass

"""Guarda cada prompt do dono, palavra por palavra, em pedidos/entrada/ (um arquivo por prompt).

É chamado sozinho pelo Claude Code a cada mensagem do dono (gancho UserPromptSubmit em .claude/settings.json):
recebe pela entrada padrão um JSON com o campo "prompt". Não imprime nada e nunca falha a conversa.
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
    if texto:
        ENTRADA.mkdir(parents=True, exist_ok=True)
        agora = datetime.now()
        arq = ENTRADA / f"{agora:%Y-%m-%d-%H%M%S}.md"
        arq.write_text(f"<!-- {agora:%d/%m/%Y %H:%M:%S} · conversa {dados.get('session_id', '?')} -->\n{texto}\n", encoding="utf-8")
except Exception:
    pass

"""Gera o índice do projeto e o resumo de cada pasta de documentos, para os agentes lerem barato.

Uso: python3 ferramentas/resumos.py            (regenera INDICE.md e os RESUMO.md)
     python3 ferramentas/resumos.py --conferir (falha se algum documento ficou fora do índice)

Cada RESUMO.md tem duas partes: "O essencial" (escrito à mão, entre as marcas, nunca apagado) e a lista
dos documentos da pasta (gerada: título, do que trata, seções e tamanho). O agente lê o resumo primeiro
e só abre o documento inteiro quando a tarefa pede.
"""
import ast
import os
import re
import subprocess
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
INI, FIM = "<!-- essencial: escrito à mão, o gerador não apaga -->", "<!-- /essencial -->"

# pasta do resumo -> (categoria, para que serve, pastas cobertas, agentes que leem)
PASTAS = {
    ".": ("Comando e contexto", "As regras, as decisões do dono e quem decide o quê", [".", "ferramentas"],
          ["todos"]),
    "contexto": ("Contexto por papel", "O que cada agente precisa saber, o quadro de avisos e os prompts do dono", ["contexto", "contexto/dono", "contexto/dono/intencoes"],
                 ["todos"]),
    "pesquisas": ("Caderno de pesquisa", "Tudo o que a equipe achou na web, por tema, com fonte, data e certeza",
                  ["pesquisas"], ["todos"]),
    "ebook": ("Produto: o e-book", "O que o e-book é, o plano, o catálogo e as 24 plantas",
              ["ebook", "ebook/plantas", "ebook/fichas"], ["arquiteto", "designer", "redator", "revisor-de-risco"]),
    "ebook/referencias": ("Pesquisa e técnica", "Público, concorrentes, regras de projeto e apostilas do Arquiteto",
                          ["ebook/referencias", "ebook/referencias/plantas-ref"], ["arquiteto", "pesquisador", "estrategista"]),
    "ebook/vendas": ("Venda e WhatsApp", "O funil: planta grátis, mensagens, objeções e atributos que vendem",
                     ["ebook/vendas"], ["redator", "estrategista", "revisor-de-risco"]),
    "video": ("Vídeo e anúncio", "Pedidos do dono, roteiros, planos, referências de edição e textos de anúncio",
              ["video", "video/principal-e07", "video/principal-e07/kit-minoai", "video/referencias"],
              ["editor-video", "diretor", "redator", "revisor-de-risco"]),
    "instagram": ("Instagram", "Plano do perfil, calendário, posts prontos e o guia da MinoAI Frontier",
                  ["instagram", "instagram/posts"], ["editor-video", "diretor", "redator", "designer", "estrategista"]),
    "animacoes-3d": ("Animações 3D e imagens", "O motor 3D, o OpenArt e as referências de planta que ganha vida",
                     ["animacoes-3d"], ["arquiteto", "designer", "editor-video"]),
    "reports": ("Jurídico", "O que a lei exige de arquiteto e engenheiro, preços e critérios",
                ["reports"], ["revisor-de-risco", "pesquisador", "estrategista"]),
    "pedidos": ("Pedidos do dono", "Como cada prompt vira trabalho: quem interpreta, quem executa e as fichas dos pedidos",
                ["pedidos", "pedidos/anexos"], ["todos"]),
    "ferramentas": ("Código", "Os programas que validam as plantas e geram PDF, 3D, fichas e painel",
                    ["ferramentas", "ebook/gerador", "ebook/plantas", "ebook/fichas"], ["arquiteto", "designer", "planejador", "revisor-de-seguranca"]),
}
FORA = ("contexto/entregas/", ".claude/", "node_modules/", "pedidos/2")  # pedidos/2…: as fichas, uma por pedido  # têm leitor próprio (ULTIMO.md, a skill, o agente)
GERADOS = ("RESUMO.md", "INDICE.md", "FILA.md")


def rastreados(padrao):
    r = subprocess.run(["git", "ls-files", "-z", padrao], cwd=RAIZ, capture_output=True, text=True).stdout
    return sorted(Path(p) for p in r.split("\0") if p and not p.startswith(FORA))


def limpar(t):
    t = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", t)  # link vira só o texto
    return re.sub(r"\s+", " ", t.replace("**", "")).strip()


def do_que_trata(linhas):
    """A primeira citação (>) ou o primeiro parágrafo depois do título: é o resumo que o próprio documento dá."""
    for marca in (">", ""):
        bloco = []
        for linha in linhas[1:40]:
            s = linha.strip()
            ok = s.startswith(">") if marca else (s and not s.startswith(("#", "|", "-", ">", "<", "```")))
            if ok:
                bloco.append(s.lstrip("> "))
            elif bloco:
                break
        if bloco:
            t = limpar(" ".join(bloco))
            return t if len(t) <= 300 else t[:300].rsplit(" ", 1)[0] + "…"
    return ""


def ficha_md(arq, base):
    linhas = (RAIZ / arq).read_text(encoding="utf-8").split("\n")
    titulo = next((limpar(x[2:]) for x in linhas if x.startswith("# ")), arq.name)
    secoes = [limpar(x[3:]) for x in linhas if x.startswith("## ")]
    palavras = sum(len(x.split()) for x in linhas)
    rel = os.path.relpath(arq, base).replace(os.sep, "/")
    txt = f"### [{titulo}]({rel.replace(' ', '%20')})\n\n"
    if trata := do_que_trata(linhas):
        txt += f"{trata}\n\n"
    if secoes:
        txt += "Seções: " + "; ".join(secoes[:14]) + ("; …" if len(secoes) > 14 else "") + ".\n\n"
    return txt + f"Tamanho: {palavras} palavras.\n\n"


def ficha_py(arq, base):
    arv = ast.parse((RAIZ / arq).read_text(encoding="utf-8"))
    doc = (ast.get_docstring(arv) or "").strip().split("\n\n")[0]
    funcoes = [n.name for n in arv.body if isinstance(n, (ast.FunctionDef, ast.ClassDef)) and not n.name.startswith("_")]
    rel = Path("..") / arq if base == Path("ferramentas") and arq.parts[0] != "ferramentas" else Path(arq.name)
    txt = f"### [`{arq.as_posix()}`]({rel.as_posix()})\n\n{limpar(doc)}\n\n"
    return txt + ("Funções: " + ", ".join(f"`{f}`" for f in funcoes[:18]) + ".\n\n" if funcoes else "")


def essencial(arq):
    if arq.exists() and INI in (t := arq.read_text(encoding="utf-8")) and FIM in t:
        return t[t.index(INI) + len(INI):t.index(FIM)].strip()
    return "- (falta escrever: os 5 a 10 fatos desta pasta que todo agente precisa saber)"


def docs_da(chave):
    cobre = PASTAS[chave][2]
    if chave == "ferramentas":
        return [a for a in rastreados("*.py") if a.parent.as_posix() in cobre]
    return [a for a in rastreados("*.md") if a.parent.as_posix() in cobre and a.name not in GERADOS
            or (chave == "reports" and a.parts[0] == "reports" and a.name not in GERADOS)]


def gerar():
    indice = ("# Índice do projeto: onde está cada coisa\n\n"
              "> **Leia barato.** Ache a categoria, leia o resumo da pasta e só abra o documento inteiro quando a tarefa "
              "pedir. Gerado por `python3 ferramentas/resumos.py`; a parte \"O essencial\" de cada resumo é escrita à mão.\n\n"
              "| Categoria | Para que serve | Resumo | Quem lê |\n|---|---|---|---|\n")
    for chave, (cat, serve, _, agentes) in PASTAS.items():
        base = Path(chave)
        arq = RAIZ / base / ("RESUMO-RAIZ.md" if chave == "." else "RESUMO.md")
        docs = docs_da(chave)
        ficha = ficha_py if chave == "ferramentas" else ficha_md
        txt = (f"# Resumo: {cat}\n\n> {serve}. **Leia este resumo primeiro**; abra um documento inteiro só quando a tarefa "
               f"pedir. Índice geral: [`INDICE.md`]({'../' * len(base.parts) if chave != '.' else ''}INDICE.md). "
               f"Quem lê: {', '.join(agentes)}.\n\n## O essencial\n\n{INI}\n{essencial(arq)}\n{FIM}\n\n"
               f"## Os {len(docs)} {'programas' if chave == 'ferramentas' else 'documentos'}\n\n")
        txt += "".join(ficha(d, base) for d in docs)
        arq.write_text(txt.rstrip("\n") + "\n", encoding="utf-8")
        indice += f"| **{cat}** | {serve} | [`{arq.relative_to(RAIZ).as_posix()}`]({arq.relative_to(RAIZ).as_posix()}) ({len(docs)}) | {', '.join(agentes)} |\n"
    indice += ("\n## Por agente\n\n" + "".join(
        f"- **{ag}:** " + ", ".join(f"[{PASTAS[c][0]}]({(Path(c) / ('RESUMO-RAIZ.md' if c == '.' else 'RESUMO.md')).as_posix()})"
                                    for c in PASTAS if ag in PASTAS[c][3] or "todos" in PASTAS[c][3]) + "\n"
        for ag in ["arquiteto", "designer", "editor-video", "estrategista", "diretor", "pesquisador", "redator", "revisor-de-risco", "supervisor", "planejador", "revisor-de-seguranca"]))
    (RAIZ / "INDICE.md").write_text(indice, encoding="utf-8")


def conferir():
    cobertos = {d for c in PASTAS for d in docs_da(c)}
    soltos = [a for a in rastreados("*.md") if a not in cobertos and a.name not in GERADOS and a.name != "RESUMO-RAIZ.md"]
    vazios = [c for c in PASTAS if "(falta escrever" in essencial(RAIZ / c / ("RESUMO-RAIZ.md" if c == "." else "RESUMO.md"))]
    for a in soltos:
        print(f"  fora do índice: {a} (ponha a pasta em PASTAS, em ferramentas/resumos.py)")
    for c in vazios:
        print(f"  resumo sem 'O essencial': {c}")
    return not soltos and not vazios


if __name__ == "__main__":
    gerar()
    if "--conferir" in sys.argv and not conferir():
        sys.exit(1)
    print("índice e resumos atualizados")

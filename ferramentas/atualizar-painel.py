"""Atualiza a seção "Situação agora" do PAINEL.md a partir dos arquivos do projeto.

O que ele confere:
  - quantas plantas há no catálogo (ebook/catalogo.md) em cada situação e por lançamento;
  - quantas casas estão desenhadas (ebook/plantas/dados), com imagem 3D e com foto, e se o PDF existe;
  - quais vídeos existem em video/saida/;
  - se os links relativos de todos os arquivos .md apontam para arquivos que existem.

Uso (na raiz do projeto):
    python3 ferramentas/atualizar-painel.py            atualiza o painel e mostra os avisos
    python3 ferramentas/atualizar-painel.py --conferir  só confere; não altera nada

Sai com código 1 se houver aviso (link quebrado, arquivo faltando, situação incoerente).
"""
import re
import sys
import unicodedata
from urllib.parse import unquote
from datetime import date
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
PAINEL = RAIZ / "PAINEL.md"
CATALOGO = RAIZ / "ebook" / "catalogo.md"
PLANTAS_3D = RAIZ / "animacoes-3d" / "plantas"
VIDEO_SAIDA = RAIZ / "video" / "saida"
INICIO = "<!-- situacao:inicio -->"
FIM = "<!-- situacao:fim -->"

ARQUIVOS_3D = ["01-blueprint.png", "02-planta-humanizada.png", "03-perspectiva.png",
               "04-perspectiva-lateral.png", "animacao.mp4"]
SITUACOES = ["ideia", "dados", "3D", "pronta"]
CATEGORIAS = {"C": "Compactas", "E": "Terreno estreito", "F": "Família", "S": "Especiais", "O": "Sobrados"}


def pasta_da_planta(nome):
    """'Casa Compacta' -> 'casa-compacta' (mesmo nome usado em animacoes-3d/plantas/)."""
    s = unicodedata.normalize("NFKD", nome).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")


def ler_catalogo():
    """Lê as linhas das tabelas do catálogo: | ID | Nome | ... | Lançamento | Situação |."""
    plantas = []
    for linha in CATALOGO.read_text(encoding="utf-8").splitlines():
        m = re.match(r"\|\s*([CEFSO]\d{2})\s*\|", linha)
        if not m:
            continue
        celulas = [c.strip() for c in linha.strip().strip("|").split("|")]
        if len(celulas) < 9:  # outras tabelas que citam IDs (ex.: "Casas que crescem")
            continue
        situacao = re.sub(r"[`\s]", "", celulas[-1])
        lote_lancamento = celulas[-2]
        plantas.append({"id": celulas[0], "nome": celulas[1], "situacao": situacao,
                        "lote_lancamento": lote_lancamento.strip()})
    return plantas


def conferir_links():
    """Links relativos [texto](caminho) que não existem no disco."""
    quebrados = []
    for md in RAIZ.rglob("*.md"):
        if {"node_modules", ".git", "entrada"} & set(md.parts):
            continue
        texto = re.sub(r"```.*?```", "", md.read_text(encoding="utf-8"), flags=re.S)
        texto = re.sub(r"`[^`\n]*`", "", texto)  # exemplo entre crases não é link
        for alvo in re.findall(r"\]\(([^)\s]+)\)", texto):
            if re.match(r"^(https?:|mailto:|#)", alvo):
                continue
            caminho = unquote(alvo.split("#")[0])
            if caminho and not (md.parent / caminho).exists():
                quebrados.append(f"{md.relative_to(RAIZ)} → {alvo}")
    return quebrados


def barra(feitos, total, largura=20):
    cheio = round(largura * feitos / total) if total else 0
    return "█" * cheio + "░" * (largura - cheio)


def montar_situacao():
    """Conta pelo que existe de verdade (dados, imagens, PDF, vídeos), não pelo que o catálogo diz."""
    avisos = []
    plantas = ler_catalogo()
    desenhadas = sorted(p.stem for p in (RAIZ / "ebook" / "plantas" / "dados").glob("*.json") if re.fullmatch(r"[A-Z]\d\d", p.stem))
    com_3d = [i for i in desenhadas if (RAIZ / "ebook" / "visual" / "3d" / f"{i}.jpg").exists()]
    com_foto = [i for i in desenhadas if any((RAIZ / "ebook" / "visual" / "openart" / "fachadas" / f"{i}.{e}").exists() for e in ("jpg", "png"))]
    gratis = sorted((RAIZ / "ebook" / "saida").glob("planta-gratis-*.pdf"))
    pdf = RAIZ / "ebook" / "saida" / "ebook.pdf"
    videos = sorted(p.parent.name for p in VIDEO_SAIDA.glob("*/*.mp4") if not re.fullmatch(r"v\d", p.parent.name))
    antigos = [v for v in range(1, 6) if (VIDEO_SAIDA / f"v{v}" / "rascunho.mp4").exists()]
    for i in desenhadas:
        if i not in com_3d:
            avisos.append(f"Casa desenhada sem imagem 3D: {i} (rode python3 ferramentas/imagens3d.py {i})")
    if not pdf.exists():
        avisos.append("Falta o PDF do e-book: rode python3 ebook/gerador/livro.py")
    fora = [p["id"] for p in plantas if p["id"] not in desenhadas]

    avisos += [f"Link quebrado: {l}" for l in conferir_links()]

    linhas = [INICIO,
              f"_Gerado por `ferramentas/atualizar-painel.py` em {date.today():%d/%m/%Y}, a partir dos arquivos que existem. Não edite à mão._",
              "",
              "| Indicador | Situação |",
              "|---|---|",
              f"| **Casas desenhadas e validadas** | {len(desenhadas)} de {len(plantas)} no catálogo |",
              f"| Progresso do catálogo | `{barra(len(desenhadas), len(plantas))}` {len(desenhadas)}/{len(plantas)} |",
              f"| Casas com imagem 3D | {len(com_3d)} de {len(desenhadas)} |",
              f"| Casas com foto de fachada | {len(com_foto)} ({', '.join(com_foto) or 'nenhuma'}) |",
              f"| PDF do e-book | {'gerado, ' + format(pdf.stat().st_size / 1e6, '.0f') + ' MB' if pdf.exists() else 'não gerado'} · {len(gratis)} plantas grátis |",
              f"| Vídeos em `video/saida/` | {len(set(videos))} pastas ({', '.join(sorted(set(videos))) or 'nenhuma'}) · {len(antigos)} versões antigas (`v1` a `v5`, com a C01 velha) |",
              f"| Avisos de conferência | {len(avisos)} |",
              "",
              "**Por categoria:**",
              "",
              "| Categoria | No catálogo | Desenhadas | Com 3D |",
              "|---|---|---|---|"]
    for letra, nome in CATEGORIAS.items():
        linhas.append(f"| {nome} | {sum(1 for p in plantas if p['id'].startswith(letra))} | "
                      f"{sum(1 for i in desenhadas if i.startswith(letra))} | {sum(1 for i in com_3d if i.startswith(letra))} |")
    if fora:
        linhas += ["", f"Ainda só no catálogo (ideia): {', '.join(fora)}."]
    if avisos:
        linhas += ["", "**Avisos:**", ""] + [f"- {a}" for a in avisos]
    linhas.append(FIM)
    return "\n".join(linhas), avisos


def main():
    so_conferir = "--conferir" in sys.argv
    bloco, avisos = montar_situacao()
    texto = PAINEL.read_text(encoding="utf-8")
    if INICIO not in texto or FIM not in texto:
        sys.exit(f"O PAINEL.md precisa ter as marcas {INICIO} e {FIM}.")
    novo = re.sub(re.escape(INICIO) + r".*?" + re.escape(FIM), lambda _: bloco, texto, flags=re.S)
    if not so_conferir and novo != texto:
        PAINEL.write_text(novo, encoding="utf-8")
        print("PAINEL.md atualizado.")
    for a in avisos:
        print("AVISO:", a)
    if not avisos:
        print("Tudo conferido, nenhum aviso.")
    sys.exit(1 if avisos else 0)


if __name__ == "__main__":
    main()

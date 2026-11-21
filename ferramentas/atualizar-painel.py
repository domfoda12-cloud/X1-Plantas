"""Atualiza a seção "Situação agora" do PAINEL.md a partir dos arquivos do projeto.

O que ele confere:
  - quantas plantas há no catálogo (ebook/catalogo.md) em cada situação e por lançamento;
  - se cada planta marcada como `3D` ou `pronta` tem os 5 arquivos em animacoes-3d/plantas/<nome>/;
  - se as 5 versões do vídeo de anúncio existem em video/saida/v1 ... v5;
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
        if "node_modules" in md.parts or ".git" in md.parts:
            continue
        texto = md.read_text(encoding="utf-8")
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
    avisos = []
    plantas = ler_catalogo()
    total = len(plantas)
    contagem = {s: sum(1 for p in plantas if p["situacao"] == s) for s in SITUACOES}
    for p in plantas:
        if p["situacao"] not in SITUACOES:
            avisos.append(f"Situação desconhecida no catálogo: {p['id']} = '{p['situacao']}'")

    # Plantas com 3D: os 5 arquivos precisam existir
    for p in plantas:
        if p["situacao"] in ("3D", "pronta"):
            pasta = PLANTAS_3D / pasta_da_planta(p["nome"])
            faltam = [a for a in ARQUIVOS_3D if not (pasta / a).exists()]
            if faltam:
                avisos.append(f"{p['id']} está como `{p['situacao']}`, mas faltam em "
                              f"{pasta.relative_to(RAIZ)}/: {', '.join(faltam)}")
    # Pastas 3D sem planta correspondente no catálogo
    if PLANTAS_3D.exists():
        nomes = {pasta_da_planta(p["nome"]) for p in plantas}
        for pasta in sorted(PLANTAS_3D.iterdir()):
            if pasta.is_dir() and pasta.name not in nomes:
                avisos.append(f"Pasta 3D sem planta no catálogo: {pasta.relative_to(RAIZ)}")

    # Vídeo de anúncio
    versoes = [v for v in range(1, 6)
               if (VIDEO_SAIDA / f"v{v}" / "rascunho.mp4").exists()
               and (VIDEO_SAIDA / f"v{v}" / "camada-transparente.webm").exists()]
    if len(versoes) < 5:
        avisos.append(f"Vídeo de anúncio: só {len(versoes)} de 5 versões em video/saida/")

    avisos += [f"Link quebrado: {l}" for l in conferir_links()]

    lote1 = [p for p in plantas if p["lote_lancamento"] == "1"]
    lote1_prontas = sum(1 for p in lote1 if p["situacao"] == "pronta")
    lote1_com_3d = sum(1 for p in lote1 if p["situacao"] in ("3D", "pronta"))

    linhas = [INICIO,
              f"_Gerado por `ferramentas/atualizar-painel.py` em {date.today():%d/%m/%Y}. Não edite à mão._",
              "",
              "| Indicador | Situação |",
              "|---|---|",
              f"| **1º lançamento do e-book** | {lote1_prontas} de {len(lote1)} prontas · {lote1_com_3d} com 3D |",
              f"| Plantas no catálogo | {total} · ideia {contagem['ideia']} · dados {contagem['dados']} · "
              f"3D {contagem['3D']} · pronta {contagem['pronta']} |",
              f"| Progresso do 1º lançamento | `{barra(lote1_prontas, len(lote1))}` {lote1_prontas}/{len(lote1)} |",
              f"| Vídeo de anúncio | {len(versoes)} de 5 versões renderizadas · apresentador não gravado |",
              f"| Avisos de conferência | {len(avisos)} |",
              "",
              "**Por categoria:**",
              "",
              "| Categoria | Plantas | No 1º lançamento | Com 3D | Prontas |",
              "|---|---|---|---|---|"]
    for letra, nome in CATEGORIAS.items():
        cat = [p for p in plantas if p["id"].startswith(letra)]
        linhas.append(f"| {nome} | {len(cat)} | {sum(1 for p in cat if p['lote_lancamento'] == '1')} | "
                      f"{sum(1 for p in cat if p['situacao'] in ('3D', 'pronta'))} | "
                      f"{sum(1 for p in cat if p['situacao'] == 'pronta')} |")
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

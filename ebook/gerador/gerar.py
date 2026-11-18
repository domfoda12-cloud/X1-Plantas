"""Gera o PDF do e-book a partir do catálogo, das fichas e das imagens 3D.

Uso (na raiz do projeto ou em qualquer pasta):
    python3 ebook/gerador/gerar.py                 e-book completo + planta grátis
    python3 ebook/gerador/gerar.py --previa DIR    também salva um PNG de cada página em DIR

O que entra no PDF, sem trabalho manual:
  - toda planta do catálogo (ebook/catalogo.md) com Situação `3D` ou `pronta`,
    cujo Lançamento seja menor ou igual a "lancamento_atual" (ebook/config.json),
    e que tenha as 4 imagens em animacoes-3d/plantas/<nome>/;
  - a ficha de texto vem de ebook/fichas/<ID>.md. Sem ficha, a página sai com
    textos padrão da categoria e campos [entre colchetes], e o gerador avisa.

Saída: ebook/saida/ebook.pdf e ebook/saida/planta-gratis-<ID>.pdf.
Precisa de: Python 3 com Pillow; Node.js com Playwright (Chromium). QR code: pacote
`qrcode` do Python (opcional; sem ele, ou sem "link_animacao", sai um quadro reservado).
"""
import base64
import io
import json
import os
import re
import shutil
import subprocess
import sys
import unicodedata
from pathlib import Path

from PIL import Image

AQUI = Path(__file__).resolve().parent
EBOOK = AQUI.parent
RAIZ = EBOOK.parent
CATALOGO = EBOOK / "catalogo.md"
FICHAS = EBOOK / "fichas"
SAIDA = EBOOK / "saida"
CACHE = EBOOK / ".cache"
PLANTAS_3D = RAIZ / "animacoes-3d" / "plantas"

sys.path.insert(0, str(AQUI))
import paginas  # noqa: E402

IMAGENS = {  # arquivo de origem -> largura em pixels no PDF (300 dpi aprox. no tamanho impresso)
    "01-blueprint.png": 1400,
    "02-planta-humanizada.png": 1700,
    "03-perspectiva.png": 900,
    "04-perspectiva-lateral.png": 900,
}
ORDEM_CATEGORIAS = "CEFSO"
avisos = []


# ---------------------------------------------------------------- catálogo
def pasta_da_planta(nome):
    """'Casa Compacta' -> 'casa-compacta' (mesma regra de ferramentas/atualizar-painel.py)."""
    s = unicodedata.normalize("NFKD", nome).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")


def ler_catalogo():
    plantas, categorias = [], {}
    for linha in CATALOGO.read_text(encoding="utf-8").splitlines():
        m = re.match(r"##\s+([CEFSO])\.\s+([^:]+):?\s*(.*)", linha)
        if m:
            categorias[m.group(1)] = {"nome": m.group(2).strip(), "descricao": m.group(3).strip()}
            continue
        if not re.match(r"\|\s*[CEFSO]\d{2}\s*\|", linha):
            continue
        c = [x.strip() for x in linha.strip().strip("|").split("|")]
        if len(c) < 9:
            avisos.append(f"Linha do catálogo com colunas a menos: {c[0]}")
            continue
        p = dict(zip(["id", "nome", "area", "quartos", "banheiros", "lote", "destaque", "lancamento"], c[:8]))
        p["situacao"] = re.sub(r"[`\s]", "", c[8])
        p["letra"] = p["id"][0]
        p["pasta"] = pasta_da_planta(p["nome"])
        p["lancamento"] = int(p["lancamento"]) if p["lancamento"].isdigit() else 99
        plantas.append(p)
    for p in plantas:
        cat = categorias.get(p["letra"], {"nome": p["letra"], "descricao": ""})
        p["categoria"], p["categoria_desc"] = cat["nome"], cat["descricao"]
    plantas.sort(key=lambda p: (ORDEM_CATEGORIAS.index(p["letra"]), p["id"]))
    return plantas, categorias


# ---------------------------------------------------------------- fichas
def ler_ficha(pid):
    """Lê ebook/fichas/<ID>.md: seções '## Título' com parágrafo ou lista '- item'."""
    arq = FICHAS / f"{pid}.md"
    if not arq.exists():
        return None
    secoes, atual = {}, None
    for linha in arq.read_text(encoding="utf-8").splitlines():
        if linha.startswith("## "):
            atual = normalizar(linha[3:])
            secoes[atual] = []
        elif atual and linha.strip() and not linha.startswith(">"):
            secoes[atual].append(linha.strip())
    ficha = {}
    for chave, linhas in secoes.items():
        itens = [l[2:].strip() for l in linhas if l.startswith("- ")]
        ficha[chave] = itens if itens else " ".join(linhas)
    return ficha


def normalizar(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z]+", " ", s).strip()


def texto_ficha(p):
    """Junta a ficha escrita com os padrões da categoria."""
    f = ler_ficha(p["id"]) or {}
    if not f:
        avisos.append(f"{p['id']} entrou no PDF sem ficha própria (crie ebook/fichas/{p['id']}.md)")
    erros = []
    for item in f.get("erros que evita", []):
        m = re.match(r"(\d)\s*[:.\-]\s*(.+)", item)
        if m:
            erros.append((int(m.group(1)), m.group(2)))
    return {
        "para_quem": f.get("para quem e") or paginas.PARA_QUEM_PADRAO.get(p["letra"], "[para quem é]"),
        "por_que": f.get("por que funciona") or [p["destaque"] + ".", "[destaque 2]", "[destaque 3]"],
        "cuidados": f.get("cuidados antes de construir") or paginas.CUIDADOS_PADRAO,
        "erros": erros,
    }


# ---------------------------------------------------------------- imagens
def preparar_imagens(p):
    """Converte as PNG da planta em JPEG menores (em ebook/.cache) para o PDF não ficar enorme."""
    origem = PLANTAS_3D / p["pasta"]
    destino = CACHE / p["pasta"]
    destino.mkdir(parents=True, exist_ok=True)
    saida = {}
    for nome, largura in IMAGENS.items():
        png = origem / nome
        jpg = destino / nome.replace(".png", ".jpg")
        if not jpg.exists() or jpg.stat().st_mtime < png.stat().st_mtime:
            im = Image.open(png).convert("RGB")
            altura = round(im.height * largura / im.width)
            im.resize((largura, altura), Image.LANCZOS).save(jpg, "JPEG", quality=84, optimize=True, progressive=True)
        saida[nome.split("-")[0]] = os.path.relpath(jpg, SAIDA)
    return saida


def qr_da_animacao(p, config):
    modelo = config.get("link_animacao", "").strip()
    if not modelo:
        return None, None
    link = modelo.replace("{pasta}", p["pasta"]).replace("{id}", p["id"])
    try:
        import qrcode
    except ImportError:
        avisos.append("Pacote 'qrcode' não instalado (pip install qrcode): QR codes saíram como quadro reservado")
        return None, link
    buf = io.BytesIO()
    qrcode.make(link, border=1, box_size=10).save(buf, format="PNG")
    return "data:image/png;base64," + base64.b64encode(buf.getvalue()).decode(), link


# ---------------------------------------------------------------- montagem
def plantas_do_pdf(plantas, config):
    lanc = config["lancamento_atual"]
    entram = []
    for p in plantas:
        if p["situacao"] not in ("3D", "pronta"):
            continue
        if p["lancamento"] > lanc:
            avisos.append(f"{p['id']} tem 3D, mas é do {p['lancamento']}º lançamento: fica fora até "
                          f"\"lancamento_atual\" chegar a {p['lancamento']}")
            continue
        faltam = [a for a in IMAGENS if not (PLANTAS_3D / p["pasta"] / a).exists()]
        if faltam:
            avisos.append(f"{p['id']} está como `{p['situacao']}`, mas faltam em "
                          f"animacoes-3d/plantas/{p['pasta']}/: {', '.join(faltam)}. Ficou fora do PDF")
            continue
        entram.append(p)
    return entram


def montar(plantas, entram, config, so_planta=None):
    """Devolve a lista de páginas (HTML). so_planta: gera só a página dupla dessa planta (planta grátis)."""
    lanc = config["lancamento_atual"]
    previstas = [p for p in plantas if p["lancamento"] <= lanc]
    completo = len(entram) == len(previstas)
    ctx = {
        "config": config,
        "titulo": config["titulo"],
        "n_plantas": str(len(entram)) if completo else "[nº]",
        "completo": completo,
        "n_entram": len(entram),
        "n_previstas": len(previstas),
        "plantas": plantas,
        "entram": entram,
        "paginas_plantas": {},
    }
    for p in entram:
        p["imagens"] = preparar_imagens(p)
        p["ficha"] = texto_ficha(p)
        p["qr"], p["link"] = qr_da_animacao(p, config)

    if so_planta:
        return paginas.pagina_dupla(so_planta, ctx, gratis=True)

    capa_id = config.get("planta_da_capa")
    ctx["capa"] = next((p for p in entram if p["id"] == capa_id), entram[0] if entram else None)

    # Duas passadas: a 1ª descobre em que página cai cada parte; a 2ª escreve os números certos.
    for _ in range(2):
        lista, inicio = [], {}

        def parte(nome, pags, par=False):
            if par and len(lista) % 2 == 0:  # próxima página seria ímpar: completa com uma página útil
                lista.extend(paginas.enchimento(ctx, len(lista)))
            inicio[nome] = len(lista) + 1
            lista.extend(pags)

        parte("capa", paginas.capa(ctx))
        parte("aviso", paginas.capa_interna(ctx))
        parte("como_usar", paginas.como_usar(ctx))
        parte("como_ler", paginas.como_ler(ctx), par=True)
        parte("erros", paginas.sete_erros(ctx), par=True)
        parte("indice", paginas.indice(ctx))
        for p in entram:
            parte(p["id"], paginas.pagina_dupla(p, ctx), par=True)
        parte("terreno", paginas.terreno(ctx), par=True)
        parte("proximos", paginas.proximos_passos(ctx))
        parte("bonus", paginas.bonus(ctx))
        ctx["inicio"] = inicio
        ctx["paginas_plantas"] = {p["id"]: inicio[p["id"]] for p in entram}
    return lista


def escrever_html(paginas_html, arquivo, titulo):
    corpo = []
    for i, pg in enumerate(paginas_html, start=1):
        corpo.append(pg.replace("{{NUM}}", str(i)))
    html = (f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>{titulo}</title>'
            f'<link rel="stylesheet" href="{os.path.relpath(AQUI / "estilo.css", SAIDA)}"></head>'
            f'<body>{"".join(corpo)}</body></html>')
    arquivo.write_text(html, encoding="utf-8")


def gerar_pdf(html, pdf, previa=None):
    env = dict(os.environ)
    try:
        raiz_npm = subprocess.run(["npm", "root", "-g"], capture_output=True, text=True).stdout.strip()
        env["NODE_PATH"] = os.pathsep.join(filter(None, [env.get("NODE_PATH"), raiz_npm]))
    except FileNotFoundError:
        pass
    cmd = ["node", str(AQUI / "pdf.cjs"), str(html), str(pdf)] + ([str(previa)] if previa else [])
    r = subprocess.run(cmd, env=env, capture_output=True, text=True)
    sys.stdout.write(r.stdout)
    for linha in r.stderr.splitlines():
        if linha.startswith("AVISO"):
            avisos.append(f"{pdf.name}: {linha[7:]}")
        elif linha.strip():
            sys.stderr.write(linha + "\n")
    if r.returncode != 0:
        sys.exit(f"Falhou ao gerar {pdf.name}")


def main():
    previa = None
    if "--previa" in sys.argv:
        previa = Path(sys.argv[sys.argv.index("--previa") + 1]).resolve()
    config = json.loads((EBOOK / "config.json").read_text(encoding="utf-8"))
    plantas, _ = ler_catalogo()
    entram = plantas_do_pdf(plantas, config)
    SAIDA.mkdir(exist_ok=True)
    if not entram:
        sys.exit("Nenhuma planta com 3D no catálogo: nada para gerar.")

    pags = montar(plantas, entram, config)
    html = SAIDA / "ebook.html"
    escrever_html(pags, html, config["titulo"])
    if previa and previa.exists():
        shutil.rmtree(previa)
    gerar_pdf(html, SAIDA / "ebook.pdf", previa / "ebook" if previa else None)

    gratis = next((p for p in entram if p["id"] == config.get("planta_gratis")), None)
    if gratis:
        pags = montar(plantas, entram, config, so_planta=gratis)
        html = SAIDA / f"planta-gratis-{gratis['id']}.html"
        escrever_html(pags, html, f"{gratis['id']} · {gratis['nome']}")
        gerar_pdf(html, SAIDA / f"planta-gratis-{gratis['id']}.pdf", previa / "gratis" if previa else None)
    else:
        avisos.append(f"Planta grátis {config.get('planta_gratis')} não tem 3D: PDF da planta grátis não gerado")

    lanc = config["lancamento_atual"]
    print(f"\nPlantas no PDF: {len(entram)} de {sum(1 for p in plantas if p['lancamento'] <= lanc)} "
          f"previstas até o {lanc}º lançamento ({', '.join(p['id'] for p in entram)})")
    if avisos:
        print(f"\nAvisos ({len(avisos)}):")
        for a in avisos:
            print(f"  - {a}")
    else:
        print("Sem avisos.")


if __name__ == "__main__":
    main()

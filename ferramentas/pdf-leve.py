#!/usr/bin/env python3
"""PDF leve de emergência: copia um PDF reduzindo só as imagens (o texto e as plantas em vetor ficam iguais).

Pedido do dono (23/11/2026): "uma forma comprimida de mandar por PDF em caso de emergência" (WhatsApp ou internet ruim).
Uso: python3 ferramentas/pdf-leve.py ebook/saida/ebook.pdf /tmp/ebook-leve.pdf [--lado 1100] [--qualidade 62]
Nunca grava em cima do original. A peça que vai ao cliente por padrão é o PDF cheio (qualidade em primeiro lugar).
"""
import argparse, sys
from pathlib import Path
from pypdf import PdfReader, PdfWriter


def main():
    a = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    a.add_argument("origem"); a.add_argument("destino")
    a.add_argument("--lado", type=int, default=1100, help="maior lado da imagem, em pixels")
    a.add_argument("--qualidade", type=int, default=62, help="qualidade do JPEG, de 1 a 95")
    o = a.parse_args()
    origem, destino = Path(o.origem).resolve(), Path(o.destino).resolve()
    if origem == destino:
        sys.exit("O destino não pode ser o próprio original.")
    w = PdfWriter(clone_from=PdfReader(str(origem)))
    trocadas = 0
    for pagina in w.pages:
        for img in pagina.images:
            try:
                im = img.image
                if im.mode not in ("RGB", "L"):
                    continue  # imagem com transparência fica como está
                if max(im.size) > o.lado:
                    k = o.lado / max(im.size)
                    im = im.resize((round(im.width * k), round(im.height * k)))
                img.replace(im, quality=o.qualidade)
                trocadas += 1
            except Exception as e:  # imagem que a biblioteca não lê fica como está
                print(f"  (imagem mantida: {e})")
    for pagina in w.pages:
        pagina.compress_content_streams()
    w.write(str(destino))
    a_, d_ = origem.stat().st_size, destino.stat().st_size
    print(f"{origem.name}: {a_/1e6:.1f} MB -> {destino.name}: {d_/1e6:.1f} MB ({trocadas} imagens reduzidas, {len(w.pages)} páginas)")


if __name__ == "__main__":
    main()

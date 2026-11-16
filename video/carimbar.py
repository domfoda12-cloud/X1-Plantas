"""Carimba a imagem do gancho do alto em cada quadro do corpo e grava tudo em RGBA.

Os quadros de tela cheia saem do navegador sem canal de transparência (RGB) e os demais
com (RGBA). O ffmpeg reinicia os filtros quando o formato muda no meio da sequência, o que
fazia sumir quadros e o texto do alto. Aqui todos os quadros saem no mesmo formato.

Uso: python3 carimbar.py <pasta_corpo> <topo.png> <pasta_saida>
"""
import os
import sys
from multiprocessing import Pool

from PIL import Image


def carimbar(args):
    origem, topo_caminho, destino = args
    quadro = Image.open(origem).convert("RGBA")
    topo = Image.open(topo_caminho).convert("RGBA")
    Image.alpha_composite(quadro, topo).save(destino, compress_level=1)


def main():
    corpo, topo, saida = sys.argv[1:4]
    os.makedirs(saida, exist_ok=True)
    nomes = sorted(n for n in os.listdir(corpo) if n.endswith(".png"))
    tarefas = [(os.path.join(corpo, n), topo, os.path.join(saida, n)) for n in nomes]
    with Pool() as pool:
        pool.map(carimbar, tarefas, chunksize=16)
    print(f"{len(nomes)} quadros carimbados")


if __name__ == "__main__":
    main()

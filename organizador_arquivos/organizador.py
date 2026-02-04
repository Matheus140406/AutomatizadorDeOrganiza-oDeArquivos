import os
import shutil
from datetime import datetime

PASTA_ORIGEM = os.path.expanduser("~/Downloads")
LOG_FILE = "log.txt"

EXTENSOES = {
    "Imagens": [".jpg", ".png", ".jpeg"],
    "Videos": [".mp4", ".mkv"],
    "Documentos": [".pdf", ".txt", ".docx"],
    "Musicas": [".mp3"],
}

def registrar_log(texto):
    with open(LOG_FILE, "a", encoding="utf-8") as log:
        log.write(texto + "\n")

def criar_pastas():
    for pasta in list(EXTENSOES.keys()) + ["Outros"]:
        os.makedirs(os.path.join(PASTA_ORIGEM, pasta), exist_ok=True)

def nome_unico(destino):
    base, ext = os.path.splitext(destino)
    contador = 1
    while os.path.exists(destino):
        destino = f"{base}_{contador}{ext}"
        contador += 1
    return destino

def obter_categoria(ext):
    for cat, exts in EXTENSOES.items():
        if ext in exts:
            return cat
    return "Outros"

def organizar():
    for arq in os.listdir(PASTA_ORIGEM):
        origem = os.path.join(PASTA_ORIGEM, arq)

        if os.path.isfile(origem):
            _, ext = os.path.splitext(arq)
            cat = obter_categoria(ext.lower())

            destino = os.path.join(PASTA_ORIGEM, cat, arq)
            destino = nome_unico(destino)

            shutil.move(origem, destino)

            registro = f"{datetime.now()} - {arq} -> {cat}"
            registrar_log(registro)
            print(registro)

if __name__ == "__main__":
    criar_pastas()
    organizar()
    print("Organização concluída.")
    
    print(f"Log salvo em {LOG_FILE}.")
import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext

EXTENSOES = {
    "Imagens": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"],
    "Videos": [".mp4", ".avi", ".mkv", ".mov"],
    "Documentos": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Musicas": [".mp3", ".wav"],
    "Compactados": [".zip", ".rar", ".7z"],
    "Programas": [".exe", ".msi"],
    "Codigos": [".py", ".js", ".html", ".css"],
}

pasta_selecionada = ""

def escolher_pasta():
    global pasta_selecionada
    pasta = filedialog.askdirectory()
    if pasta:
        pasta_selecionada = pasta
        label_pasta.config(text=pasta)

def criar_pastas(base):
    for pasta in list(EXTENSOES.keys()) + ["Outros"]:
        os.makedirs(os.path.join(base, pasta), exist_ok=True)

def obter_categoria(ext):
    for cat, lista in EXTENSOES.items():
        if ext in lista:
            return cat
    return "Outros"

def organizar():
    if not pasta_selecionada:
        messagebox.showwarning("Aviso", "Selecione uma pasta primeiro!")
        return

    criar_pastas(pasta_selecionada)
    area_status.delete(1.0, tk.END)

    for arq in os.listdir(pasta_selecionada):
        origem = os.path.join(pasta_selecionada, arq)

        if os.path.isfile(origem):
            nome, ext = os.path.splitext(arq)
            categoria = obter_categoria(ext.lower())

            destino = os.path.join(pasta_selecionada, categoria, arq)
            shutil.move(origem, destino)

            area_status.insert(tk.END, f"{arq} → {categoria}\n")

    area_status.insert(tk.END, "\nOrganização concluída!")

janela = tk.Tk()
janela.title("Organizador de Arquivos")
janela.geometry("520x420")
janela.resizable(False, False)

titulo = tk.Label(janela, text="Organizador de Arquivos", font=("Arial", 18, "bold"))
titulo.pack(pady=10)

btn_pasta = tk.Button(janela, text="Escolher Pasta", width=20, command=escolher_pasta)
btn_pasta.pack()

label_pasta = tk.Label(janela, text="Nenhuma pasta selecionada", fg="blue")
label_pasta.pack(pady=5)

btn_organizar = tk.Button(
    janela,
    text="ORGANIZAR AGORA",
    width=25,
    height=2,
    bg="green",
    fg="white",
    command=organizar
)
btn_organizar.pack(pady=10)

area_status = scrolledtext.ScrolledText(janela, width=60, height=15)
area_status.pack(padx=10, pady=10)

janela.mainloop()
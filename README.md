# 📁 Organizador de Arquivos em Python

Um automatizador inteligente de organização de arquivos desenvolvido em **Python**, que classifica arquivos automaticamente em pastas específicas com base em suas extensões, facilitando a organização e produtividade no dia a dia.

---

## 🚀 Funcionalidades

- 🖥️ **Interface Gráfica (Tkinter)**  
  Seleção de pastas de forma visual e intuitiva.

- 🗂️ **Categorização Automática**  
  Suporte para:
  - Imagens  
  - Vídeos  
  - Documentos  
  - Músicas  
  - Compactados  
  - Programas  
  - Códigos  

- 📜 **Logs em Tempo Real**  
  Visualização dos arquivos movidos durante o processo.

- 🔒 **Tratamento de Conflitos**  
  Evita sobrescrever arquivos com nomes iguais.

- 📦 **Pasta "Outros"**  
  Arquivos não identificados são movidos automaticamente.

---

## 🛠️ Tecnologias Utilizadas

- Python 3.10+  
- Tkinter (GUI)  
- Bibliotecas padrão:
  - os  
  - shutil  

---

## 📥 Instalação

### 1️⃣ Pré-requisitos

- Python instalado  
  👉 https://www.python.org/downloads/

Durante a instalação, marque:


---

### 2️⃣ Clonar o Repositório ###

bash
cd "C:\Users\SeuUsuario\Desktop"
git clone https://github.com/Matheus140406/AutomatizadorDeOrganiza-oDeArquivos.git
cd AutomatizadorDeOrganiza-oDeArquivos


🧭 Como Usar

Abra o programa

Clique em Escolher Pasta

Selecione o diretório desejado

Clique em ORGANIZAR AGORA

Os arquivos serão organizados automaticamente.

📂 Categorias e Extensões
Pasta	Extensões Suportadas
Imagens	.jpg, .jpeg, .png, .gif, .webp
Vídeos	.mp4, .mkv, .avi, .mov
Documentos	.pdf, .docx, .txt, .xlsx, .pptx
Músicas	.mp3, .wav
Compactados	.zip, .rar, .7z
Programas	.exe, .msi
Códigos	.py, .js, .html, .css
🛠️ Solução de Problemas
❌ Arquivo não encontrado
dir


Verifique se app.py aparece na lista.

❌ Python não reconhecido
py --version


Se falhar, reinstale o Python e marque:

[✔] Add Python to PATH

❌ Pasta com espaços no nome

Use aspas:

cd "C:\Users\Mage Sistemas\Desktop"

⌨️ Comandos Úteis
Comando	Função
cd ..	Volta uma pasta
dir	Lista arquivos
cls	Limpa terminal
pwd	Mostra caminho atual
📌 Estrutura do Projeto
AutomatizadorDeOrganiza-oDeArquivos/
│
├── app.py
├── README.md

🤝 Contribuindo

Contribuições são bem-vindas!

Faça um Fork

Crie uma Branch:

git checkout -b feature/NovaExtensao


Commit:

git commit -m "Adicionando suporte a .iso"


Push:

git push origin feature/NovaExtensao


Abra um Pull Request

📄 Licença

Este projeto é de código aberto e livre para uso educacional e pessoal.

👨‍💻 Autor

Matheus Carvalho Dias

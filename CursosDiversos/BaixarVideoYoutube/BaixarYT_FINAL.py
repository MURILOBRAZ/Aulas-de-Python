import yt_dlp
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog  # Importe o módulo filedialog

# Defina as opções de formato predefinidas


def download_video():
    video_url = url_entry.get()
    output_directory = directory_entry.get()

    try:
        format_code = "22"  # Use a resolução padrão se a escolha do usuário for inválida ou vazia

        ydl_opts = {
            'format': format_code,
            'outtmpl': f'{output_directory}/%(title)s.%(ext)s',
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(video_url, download=False)
            video_title = info['title']
            download_label.config(text=f'Baixando: {video_title}')
            ydl.download([video_url])
            download_label.config(text='Concluído')
    except yt_dlp.utils.DownloadError as e:
        download_label.config(text="Erro ao baixar o vídeo: Resolução Indisponível para esse vídeo")

# Restante do código permanece inalterado


# Função para abrir o explorador de arquivos e escolher o diretório de saída
def browse_output_directory():
    directory = filedialog.askdirectory()
    directory_entry.delete(0, tk.END)  # Limpa o campo de entrada
    directory_entry.insert(0, directory)  # Insere o diretório selecionado no campo de entrada

# Função para sair do programa
def exit_program():
    root.quit()

root = tk.Tk()
root.title("Baixador de Vídeos do YouTube")

# Defina o tamanho mínimo e máximo da janela principal
root.minsize(width=400, height=250)
root.maxsize(width=800, height=250)

url_label = ttk.Label(root, text="Digite a URL do vídeo do YouTube:")
url_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

url_entry = ttk.Entry(root)
url_entry.grid(row=0, column=1, padx=10, pady=5, sticky="w")

quality_label = ttk.Label(root, text="Qualidade padrão de 720p!!")
quality_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")

directory_label = ttk.Label(root, text="Escolha o diretório de saída:")
directory_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")

# Campo de entrada para o diretório de saída
directory_entry = ttk.Entry(root)
directory_entry.grid(row=2, column=1, padx=10, pady=5, sticky="w")

# Botão para abrir o explorador de arquivos
browse_button = ttk.Button(root, text="Procurar", command=browse_output_directory)
browse_button.grid(row=2, column=2, padx=10, pady=5, sticky="w")

download_button = ttk.Button(root, text="Baixar Vídeo", command=download_video)
download_button.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky="w")

download_label = ttk.Label(root, text="")
download_label.grid(row=4, column=0, columnspan=2, padx=10, pady=5, sticky="w")

exit_button = ttk.Button(root, text="Sair", command=exit_program)
exit_button.grid(row=5, column=0, columnspan=2, padx=10, pady=5, sticky="w")

root.mainloop()
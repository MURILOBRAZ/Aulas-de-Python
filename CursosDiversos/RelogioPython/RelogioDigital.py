from tkinter import *
from time import strftime

def atualizar_relogio():
    hora_atual = strftime("%H:%M:%S %p")
    rotulo_relogio.config(text=hora_atual)
    rotulo_relogio.after(1000, atualizar_relogio)

janela = Tk()
janela.title("Relógio Digital V1")

rotulo_relogio = Label(
    janela,
    font=("Arial", 40, "italic"),
    background="dark blue",
    foreground="white"
)

rotulo_relogio.pack(anchor="center")

atualizar_relogio()
janela.mainloop()

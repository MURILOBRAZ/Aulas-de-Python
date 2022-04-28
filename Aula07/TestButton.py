#Importa Biblioteca Kivy
from turtle import color
import kivy
#Importa Janela de Exibição
from kivy.app import App
#Importa Label(Texto)
from kivy.uix.label import Label
#Importa Mudança de Cor da Janela de Exibição
from kivy.core.window import Window
#Improta Button
from kivy.uix.button import Button

#Window.clearcolor = [0.5,0.5,0.5,1]

class Teste(App):

    def build(self):
        return Button(text = 'clicar', font_size = '30sp', color = [0,0,0,1], background_color = [0,0,1,1], size_hint = [None,None], pos_hint = {'top': 0.5, 'center_x': 0.5})
        #background_color muda a cor do botão MAS NÃO DO CLIQUE
        #size_hint TAMANHO DO BOTÃO
        #pos_hint POSIÇÃO DO BOTÃO

Teste().run()

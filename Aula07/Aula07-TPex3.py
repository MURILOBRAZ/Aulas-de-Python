#Importa Biblioteca Kivy
import kivy
#Importa Janela de Exibição
from kivy.app import App
#Importa Label(Texto)
from kivy.uix.label import Label
#Importa Mudança de Cor da Janela de Exibição
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout

class Teste(App):

    def build(self):
        grid = GridLayout(cols = 4, rows = 4)

        list = ['7','8','9','+', '4', '5', '6', '-', '1', '2', '3', '*', 'clear', '0', '=', '/']

        for x in range(len(list)):
            grid.add_widget(Label(text = list[x], font_size = '25sp'))
        
        return(grid)
Teste().run()

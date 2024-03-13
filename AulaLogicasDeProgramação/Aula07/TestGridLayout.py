from tkinter.font import BOLD
#Importa Biblioteca Kivy
import kivy
#Importa Janela de Exibição
from kivy.app import App
#Importa Label(Texto)
from kivy.uix.label import Label
#Importa BoxLayout
from kivy.uix.gridlayout import GridLayout
#Importa Mudança de Cor da Janela de Exibição
from kivy.core.window import Window

Window.clearcolor = [0.5,0.5,0.5,1]

'''class Teste(App):

    def build(self):
        return Label(text = 'UNISANTA', font_size = '150sp', bold = True, underline = True, color = [209, 210, 211])
'''

class Teste(App):

    def build(self):
        #Chama Função GridLayout e define o numero de Colunas
    #   grid = GridLayout(cols = 3)
        #Chama Função GridLayout e define o numero de Linhas
        grid = GridLayout(rows = 10)
        label1 = Label(text = 'UNISANTA', font_size = '50sp', bold = True, underline = True, color = [209, 210, 211])
        label2 = Label(text = 'ENGENHARIA', font_size = '50sp', bold = True, underline = True, color = [209, 210, 211])
        label3 = Label(text = 'COMPUTAÇÃO', font_size = '50sp', bold = True, underline = True, color = [209, 210, 211])

        grid.add_widget(label1)
        grid.add_widget(label2)
        grid.add_widget(label3)

        for X in range(37):
            grid.add_widget(Label(text = 'Label' + str(X+1)))
        return(grid)

        #Adiciona as Labels nas Boxs do GridLayout
        grid.add_widget(label1)
        grid.add_widget(label2)
        grid.add_widget(label3)
        return(box1)

Teste().run()

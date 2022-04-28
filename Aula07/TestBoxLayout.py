from tkinter.font import BOLD
#Importa Biblioteca Kivy
import kivy
#Importa Janela de Exibição
from kivy.app import App
#Importa Label(Texto)
from kivy.uix.label import Label
#Importa BoxLayout
from kivy.uix.boxlayout import BoxLayout
#Importa Mudança de Cor da Janela de Exibição
from kivy.core.window import Window

Window.clearcolor = [0.5,0.5,0.5,1]

'''class Teste(App):

    def build(self):
        return Label(text = 'UNISANTA', font_size = '150sp', bold = True, underline = True, color = [209, 210, 211])
'''

class Teste(App):

    def build(self):
        #Chama Função BoxLayout
        box1 = BoxLayout(orientation = 'vertical')
        label1 = Label(text = 'UNISANTA', font_size = '50sp', bold = True, underline = True, color = [209, 210, 211])
        label2 = Label(text = 'ENGENHARIA', font_size = '50sp', bold = True, underline = True, color = [209, 210, 211])
        label3 = Label(text = 'COMPUTAÇÃO', font_size = '50sp', bold = True, underline = True, color = [209, 210, 211])

        #Adiciona as Labels nas Boxs do BoxLayout
        box1.add_widget(label1)
        box1.add_widget(label2)
        box1.add_widget(label3)
        return(box1)

Teste().run()

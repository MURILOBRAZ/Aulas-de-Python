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

class Teste(App):

    def build(self):
        #Chama Função BoxLayout
        box1 = BoxLayout()
        label1 = Label(text = 'João', font_size = '30sp', color = [1, 1, 0])
        label2 = Label(text = 'Maria', font_size = '65sp', color = [1, 0, 1])
        label3 = Label(text = 'José', font_size = '100sp', color = [0, 1, 1])

        #Adiciona as Labels nas Boxs do BoxLayout
        box1.add_widget(label1)
        box1.add_widget(label2)
        box1.add_widget(label3)
        return(box1)

Teste().run()

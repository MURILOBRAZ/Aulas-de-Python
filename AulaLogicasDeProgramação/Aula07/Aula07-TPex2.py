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
from kivy.uix.gridlayout import GridLayout

class Teste(App):

    def build(self):
        grid = GridLayout(cols = 2)

        #Chama Função BoxLayout
        box1 = BoxLayout(orientation = 'vertical')
        label1 = Label(text = 'ENGENHARIA', font_size = '60sp')
        label2 = Label(text = 'UNISANTA', font_size = '60sp')

        #Adiciona as Labels nas Boxs do BoxLayout
        box1.add_widget(label1)
        box1.add_widget(label2)

        box2 = BoxLayout()
        label3 = Label(text = 'COMPUTAÇÃO', font_size = '25sp')
        label4 = Label(text = 'CIVÍL', font_size = '25sp')
        label5 = Label(text = 'QUÍMICA', font_size = '25sp')

        box2.add_widget(label3)
        box2.add_widget(label4)
        box2.add_widget(label5)

        grid.add_widget(box1)
        grid.add_widget(box2)
        
        return(grid)
Teste().run()

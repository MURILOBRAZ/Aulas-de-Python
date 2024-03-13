import math
from tkinter.tix import Select
class pontos:

  def __init__(self,x,y):
      self.Cx = x
      self.Cy = y
  
  def __str__(self):
      return 'Coordenada X: ' + str(self.Cx) + '\nCoordenada Y: ' + str(self.Cy)

  def __eq__(self, objeto2):
      if (self.Cx == objeto2.Cx) and (self.Cy == objeto2.Cy):
        return True
      else:
        return False

  def __ne__(self, objeto2):
      if (self.Cx != objeto2.Cx) or (self.Cy != objeto2.Cy):
        return True
      else:
        return False
  
  def __sub__(self,objeto2):
    self.D = pow(objeto2.Cx - self.Cx,2) + pow(objeto2.Cy - self.Cy,2)
    return round(math.sqrt(self.D))

  def __add__(self,objeto2):
    self.Xm = (self.Cx + objeto2.Cx)/2
    self.Ym = (self.Cy + objeto2.Cy)/2

    
    return 'As coordenadas do Ponto Médio são: ' + str(self.Xm) + ', ' + str(self.Ym)

  def __mul__(self,objeto2):
    self.A = ((objeto2.Cy - self.Cy)/(objeto2.Cx - self.Cx))

    self.B = (self.Cy - (self.A * self.Cx))
    
    return 'A equação da Reta que liga os pontos é: ' + str(self.Cy) + ' = ' + str(self.A) + ' * ' + str(self.Cx) + ' + ' + str(self.B)

  def __truediv__(self,objeto2):
    self.A = ((objeto2.Cy - self.Cy)/(objeto2.Cx - self.Cx))

    return 'O coeficiente Angular é: ' + str(self.A)

# Test 1
# ExibeClass = pontos(5,6)
# print(ExibeClass)

# Test 2
# ExibeClass = pontos(5,6)
# ExibeClass1 = pontos(6,3)
# ExibeClass2 = ExibeClass == ExibeClass1
# ExibeClass2 = ExibeClass != ExibeClass1
# print(ExibeClass2)

# Test 3
# ExibeClass = pontos(5,6)
# ExibeClass1 = pontos(6,3)
# ExibeClass2 = ExibeClass - ExibeClass1
# print(ExibeClass2)

# Test 4
# ExibeClass = pontos(5,6)
# ExibeClass1 = pontos(6,3)
# ExibeClass2 = ExibeClass + ExibeClass1
# print(ExibeClass2)

# Test 5
# ExibeClass = pontos(5,6)
# ExibeClass1 = pontos(6,3)
# ExibeClass2 = ExibeClass * ExibeClass1
# print(ExibeClass2)

# Test 6
ExibeClass = pontos(5,6)
ExibeClass1 = pontos(6,3)
ExibeClass2 = ExibeClass / ExibeClass1
print(ExibeClass2)

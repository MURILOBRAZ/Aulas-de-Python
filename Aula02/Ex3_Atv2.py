Valor = int(input('Insira um Valor: '))
while(Valor < 0):
	Valor = int(input('Insira um Valor: '))
Aux = 1
while(Aux <= 10):
	print(Valor,'X',Aux,'=',Valor * Aux)
	Aux = Aux+1

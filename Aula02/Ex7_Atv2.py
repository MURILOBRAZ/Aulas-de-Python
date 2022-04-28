Lista = []
Aux = 0
while(Aux < 20):
	Num = int(input('Insira um Valor: '))
	Lista.insert(Aux,Num)
	Aux = Aux+1

Lista.sort()
print(Lista)
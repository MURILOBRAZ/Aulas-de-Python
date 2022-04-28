Lista = []
Aux = 0
while(Aux < 10):
	Num = int(input('Insira um Valor: '))
	Lista.insert(Aux,Num)
	Aux = Aux+1

print(Lista)

vez = int(input('Insira o Número Multiplicador: '))

cont = 0
while(cont < len(Lista)):
	seq = Lista[cont]
	Lista.pop(cont)
	Lista.insert(cont, (seq * vez))
	cont += 1
print(Lista)
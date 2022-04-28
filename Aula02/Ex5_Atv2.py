Lista = []
Aux = 0
while(Aux < 10):
	Num = int(input('Insira um Valor: '))
	if(Num < 0):
		Num = int(input('Insira um Valor POSITIVO: '))
	Lista.insert(Aux,Num)
	Aux = Aux+1
Lista.sort()
print('O maior valor è', max(Lista))
soma = 0
cont = 0
while(cont < len(Lista)):
	soma += Lista[cont]
	cont += 1
print('A soma de todos os valores è',soma)
print('A mèdia aritmetica è', soma/10)
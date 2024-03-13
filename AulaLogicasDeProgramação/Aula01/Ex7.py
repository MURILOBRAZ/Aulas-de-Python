n1 = int(input('Insira o 1°Valor: '))

n2 = int(input('Insira o 2°Valor: '))

if n1 < n2:
    print('{} é o menor valor!!'.format(n1))
elif n2 < n1:
    print('{} é o menor valor!!'.format(n2))
else:
    print('Ambos valores são IGUAIS!!')
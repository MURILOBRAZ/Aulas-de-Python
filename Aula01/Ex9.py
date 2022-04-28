from ast import And


peso = float(input('Insira o peso: '))

altura = float(input('Insira a Altura: '))

relacao = peso/(altura*altura)

if relacao < 20:
    print('Abaixo do Peso!')
elif 20 <= relacao and relacao < 25:
    print('Peso Ideal!!')
else:
    print('Acima do Peso!!!') 
def media(v1,v2,v3):
    media = (v1 + v2 + v3)/3

    return media

valor1 = int(input('Insira o primeiro valor: '))

valor2 = int(input('Insira o segundo valor: '))

valor3 = int(input('Insira o terceiro valor: '))

resultado = media(valor1, valor2, valor3)

print('A média dos 3 valores é: ', round(resultado,2))
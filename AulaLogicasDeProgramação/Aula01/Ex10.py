a = float(input('Insira o valor da Aceleração(em m/s²): '))

vO = float(input('Insira a Velocidade Inicial(em m/s): '))

t = float(input('Insira o Tempo de Percurso(em s): '))

v = vO + (a*t)
vkm = v * 3.6

if vkm <= 40:
    print('Veículo Muito Lento!!')
elif 40 < vkm and vkm <= 60:
    print('Velocidade Permitida')
elif 60 < vkm and vkm <= 80:
    print('Velocidade de Cruzeiro!')
elif 80 < vkm and vkm <= 120:
    print('Veículo Rápido!!!')
elif vkm > 120:
    print('Veículo Muito Rápido!!!')
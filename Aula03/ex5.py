
while 1 != 0:
    N = int(input('Insira um valor N: '))
    SeqL = 2
    SeqI = 3
    soma = 2
    if N > 0 and N < 100:
        for i in range(1, N):
            
            SeqL = SeqL + SeqI

            SeqI = SeqI + 2

            soma += SeqL
        print(soma)
    else:
        print('ERROR!!! Insira um valor válido!!')



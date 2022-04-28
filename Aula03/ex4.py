
Resp = 1 

# 1 = S --- 0 = N

while Resp  == 1:

    Num = int(input('Insira um Valor: '))

    if(Num <= 0):
        Num == ''
        print('INSIRA UM NUMERO POSITIVO!!!')
        Resp == 1

    else:

        #Calculo Vetorial
        i = Num
        calc = 1
        for i in range(1,Num + 1):

            calc *= i 
        
        print(calc)



        #Menu de saida
        Resp2 = input('Deseja fazer um novo Cálculo?(S/N) ')
        if Resp2 == 'S' or Resp2 == 's':
            Resp = 1
        elif Resp2 == 'N' or Resp2 == 'n':
            print('Encerrando o Programa!!')
            Resp = 0

    


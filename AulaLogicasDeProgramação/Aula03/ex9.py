while 1 != 0:
    
    #cartoes = ["Bronze","Prata","Ouro","Diamante"]

    pontos = {
        "bronze" : 1.0,
        "prata": 1.2,
        "ouro": 1.5,
        "diamante":2.0
    }

    dol = float(input("Insira a cotação atual do dolar: "))
    v = float(input("Insira o valor gasto: "))

    resul = v/dol

    for i in pontos.keys():
        print(f"{i}")
        
    opc = str(input("Escreva a opção de entrada: "))
    
    pontuacao = resul* pontos[opc.casefold()]
    
    print('\nO cartão selecionado foi {}'.format(opc))
    print('O valor da compra foi de R${}'.format(v))
    print(f'A pontuação foi de {pontuacao}')

    input("\nPRESSIONE ENTER! \n")
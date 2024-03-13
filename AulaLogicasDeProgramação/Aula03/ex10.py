while 1:

    lista = ["1 - Retângulo","2 - Quadrado","3 - Triângulo","4 - Circulo","5 - Encerrar"]

    

    AreaRet = 0
    AreaQuad = 0
    AreaTri = 0
    AreaCirc = 0

    menu = {

        1 : "Area do Retângulo" ,
        2 : "Area do Quadrado",
        3 : "Area do Triângulo",
        4 : "Area do Circulo",
        5 : "Encerrar"
    }
    
    for i in lista:

        print(i)

    opc = int(input("Digite o Número da opção desejada: "))
    if opc <= 5 and opc > 0:

        print(menu[opc])
        print("\n")

    else:

        print("Escolha outra opção: ") 

    if opc == 1:
        BaseRet = int(input('Insira o valor da base: '))
        AlturaRet = int(input('Insira o valor da Altura: '))

        AreaRet = BaseRet*AlturaRet

        print('A area do Retângulo é {}'.format(AreaRet))

    elif opc == 2:
        BaseQuad = int(input('Insira o valor do lado: '))

        AreaQuad = BaseQuad*4

        print('A area do Quadrado é {}'.format(AreaQuad))

    elif opc == 3:
        BaseTri= int(input('Insira o valor da base: '))
        AlturaTri= int(input('Insira o valor da Altura: '))

        AreaTri = (BaseTri*AlturaTri)/2

        print('A area do Triângulo é {}'.format(AreaTri))

    elif opc == 4:
        BaseCirc= int(input('Insira o valor do raio: '))

        AreaCirc = (3.14*BaseCirc)^2

        print('A area do Quadrado é {}'.format(AreaQuad))

    elif opc == 5:
        print('Encerrando...')
        break

    input("\nPRESSIONE ENTER! \n")
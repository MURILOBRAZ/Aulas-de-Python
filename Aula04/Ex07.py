def menu():

    aux = 1
    while aux == 1:
        lista = ["1 - opção","2 - opção","3 - opção","4 - opção","5 - opção"]

        menu = {

            1 : "1",
            2 : "2",
            3 : "3",
            4 : "4",
            5 : "5"
        }


        for i in lista:

            print(i)

        opc = int(input("Escolha a opção: \n"))

        if opc <= 5 and opc > 0:
            aux = 0
            return menu[opc]

        else:

            print("Escolha outra opção!!!")


resultado =  menu()
print('Opção escolhida foi a ' + str(resultado))

a = True
while a == True:

    lista = ["1-Abrir","2-Salvar","3-Excluir","4-Exportar"]

    menu = {

        1 : "Programa aberto",
        2 : "Arquivo salvo",
        3 : "Arquvo excluido",
        4 : "Programa exportado"
    }


    for i in lista:

        print(i)

    opc = int(input("Escolha a opção: \n"))

    if opc < 5 and opc > 0:

        print(menu[opc])
        print("\n")

    else:

        print("Escolha outra opção!!!!")

    input("PRESSIONE ENTER! \n")
        

    
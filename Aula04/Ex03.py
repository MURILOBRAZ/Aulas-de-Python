while 1 != 0:

    number = str(input("Digite um numero de 1 à 99: "))
    if number.isnumeric():
     if int(number) > 99 or int(number) < 0:

         print("Digite DNV!!!")
        
         number = str(input("Digite um numero de 0 à 99: "))
    else:
        print('Digitar NÚMERO!!!')
        break
    

    n = ["Zero","um","dois","tres","quatro","cinco","seis","sete","oito","nove",
    
    # desgarados
    "dez","onze","doze","treze","quatorze","quinze","dezesseis","dezessete","dezoito","dezenove"]
    
    dez = [" ","dez","vinte","trinta","quarenta","cinquenta","sessenta","setenta","oitenta","noventa"]


    if int(number)  >= 0 and int(number) <= 19:

        print(n[int(number)])

    elif int(number)  < 100 and int(number) > 19:

        if int(number[-1:]) != 0:
            print(dez[int(number[:1])], 'e' ,n[int(number[-1:])])
        
        else:
            print(dez[int(number[:1])])








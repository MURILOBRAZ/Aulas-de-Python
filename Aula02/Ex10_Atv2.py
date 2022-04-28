Lista = []
Aux = 0
while(Aux < 10):
    if(Aux == 0):
        
        Num = int(input('Insira o 1° Valor: '))
        Lista.insert(Aux,Num)
        Aux = Aux+1
        Cont = Aux

    else:
        
        Num = int(input('Insira o '+ str(Cont+1) +'° Valor: '))

        if(Num > Lista[Aux-1]):
            Lista.insert(Aux,Num)
            Aux = Aux+1
            Cont = Aux

        elif(Num == Lista[Aux-1]):
            Lista.pop(Aux-1)
            Aux = Aux-1
            Cont = Aux
print(Lista)
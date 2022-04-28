def Calc_M(P1, P2):
            Media = (P1 + 2*P2)/3

            return Media

def Ver_Sit(Media):
    if Media >= 5:
        print('Aluno APROVADO!!!')
        return -1
            
    else:
        print('Aluno REPROVADO!!!')
        return 0

aux = 1
while aux != -1:
    P1 = int(input('Insira a 1°Nota: '))
    P2 = int(input('Insira a 2°Nota: '))
    resultado1 = Calc_M(P1, P2)
    resultado2 = Ver_Sit(resultado1)
    aux = resultado2
    if resultado2 == 0:
        P3 = int(input('Insira a 3°Nota: '))
        if P1 >= P2:

            resultado3 = Calc_M(P1,P3)
        else:
            resultado3 = Calc_M(P2,P3)
        
        resultado4 = Ver_Sit(resultado3)
    print('Encerrando...')
    break
    
    

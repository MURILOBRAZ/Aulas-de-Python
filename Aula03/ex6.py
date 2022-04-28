Qtde_Alunos = int(input('Insira a quantidade de alunos na sua sala: '))
lista_Nota = []
for i in range(Qtde_Alunos):
    
    Resp = int(input('Insira a nota do {}° Aluno: '.format(i+1)))
    lista_Nota.append(Resp)

Soma = sum(lista_Nota)
Media = Soma/Qtde_Alunos
print('A média Aritmética da sala é {}'.format(Media))

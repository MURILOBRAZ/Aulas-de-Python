import sqlite3

BDconection2 = sqlite3.connect('C:/Users/unisanta/Desktop/Aula - 1703/AulaBD/Alunos2.db')

BDconection2.execute('CREATE TABLE IF NOT EXISTS notas (id integer PRIMARY KEY AUTOINCREMENT, nome text, p1 decimal, p2 decimal)')

def Inserir():

#PRIMARY KEY(Inseri o Id Automatico)   
#ident = int(input('Insira o ID: '))
    nome = input('Insira o Nome: ')
    p1 = float(input('Insira a Nota da P1: '))
    p2 = float(input('Insira a nota da P2: '))
    BDconection2.execute('INSERT INTO notas VALUES(NULL, ?, ?, ?)',(nome, p1, p2))

    BDconection2.commit()

#BDconection2.execute('DELETE FROM notas WHERE id = 6')

def Excluir():
    ident = int(input('Insira o ID a ser CANCELADO: '))
    BDconection2.execute('DELETE FROM notas WHERE id = ?',(ident,))
    
    BDconection2.commit()
cont = 0

def Consultar():

    nome = input('Insira o nome a ser Pesquisado: ')
    cursor = BDconection2.cursor()
    
    #cursor.execute('SELECT * FROM notas')
    cursor.execute('SELECT * FROM notas WHERE nome = ?', (nome,))
    lista = cursor.fetchall()
    print(lista)
    print('ID \t Nome \t P1 \t p2')
    for x in lista:
        print(str(x[0]) + '\t' + x[1] + '\t' + str(x[2]) + '\t' + str(x[3]))

while cont == 0:
    op = int(input('\n----------- \n1. Inserir \n2. Excluir \n3. Consultar \n4. Sair\n----------- \n OP: ')); 

    if op == 1:
        Inserir()
    elif op == 2:
        Excluir()
    elif op == 3:
        Consultar()
    else:
        cont = 1
        exit()


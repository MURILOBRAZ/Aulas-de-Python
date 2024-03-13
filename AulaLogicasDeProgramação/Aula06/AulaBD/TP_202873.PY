import sqlite3

#FINALIZADO

BDconection2 = sqlite3.connect('C:/Users/unisanta/Desktop/Aula - 1703/AulaBD/FutTable.db')

BDconection2.execute('CREATE TABLE IF NOT EXISTS notas (id integer PRIMARY KEY AUTOINCREMENT, clube text, pontos integer, vitorias integer, empates integer, jogos integer, golsMarcados integer, golsSofridos integer, saldoGols integer, aproveitamento decimal)')

def Inserir():

#PRIMARY KEY(Inserir o Id Automatico)  
 
    clube = input('Insira o Nome do Clube: ')
    #NOPE pontos = float(input('Insira a Nota da P1: '))
    vitorias = int(input('Insira a quantidade de Vitórias: '))
    empates = int(input('Insira a quantidade de Empates: '))
    jogos = int(input('Insira a quantidade de Jogos: '))
    golsMarcados = int(input('Insira a quantidade de Gols Marcados: '))
    golsSofridos = int(input('Insira a quantidade de Gols Sofridos: '))
    #NOPE saldoGols = int(input('Insira a nota da P2: '))
    #NOPE aproveitamento = int(input('Insira a nota da P2: '))

    #vitoria = 3 - empate = 1
    pontos = 3*vitorias + empates
    saldoGols = golsMarcados - golsSofridos

    pontosPossiveis = jogos * 3
    #pontosPossiveis = jogos * 3 (pontos totais possiveis)
    #aproveitamento = pontos/pontosposiveis

    aproveitamento = round(pontos/pontosPossiveis, 2)
    aproveitamento = aproveitamento*100

    BDconection2.execute('INSERT INTO notas VALUES(NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?)',(clube, pontos, vitorias, empates, jogos, golsMarcados, golsSofridos, saldoGols, aproveitamento))

    BDconection2.commit()

def Pesquisa():

    clube = input('Insira o Clube a ser Pesquisado: ')
    cursor = BDconection2.cursor()
    
    cursor.execute('SELECT * FROM notas WHERE clube = ?', (clube,))
    lista = cursor.fetchall()
    print(lista)
    print('ID \t clube \t Pontos \t Vitórias \t Empates \t Jogos \t GolsMarcados \t GolsSofridos \t SaldoGols \t Aproveitamento')
    for x in lista:
        print(str(x[0]) + '\t' + x[1] + '\t' + str(x[2]) + '\t' + str(x[3]) + '\t' + str(x[4])  + '\t' + str(x[5]) + '\t' + str(x[6]) + '\t' + str(x[7]) + '\t' + str(x[8]) + '\t' + str(x[9]))

def Pontuacao():

    pontos = input('Insira a Pontuação a ser Pesquisada: ')
    cursor = BDconection2.cursor()
    
    cursor.execute('SELECT * FROM notas WHERE pontos >= ?', (pontos,))
    lista = cursor.fetchall()
    print(lista)
    print('ID \t clube \t Pontos \t Vitórias \t Empates \t Jogos \t GolsMarcados \t GolsSofridos \t SaldoGols \t Aproveitamento')
    for x in lista:
        print(str(x[0]) + '\t' + x[1] + '\t' + str(x[2]) + '\t' + str(x[3]) + '\t' + str(x[4])  + '\t' + str(x[5]) + '\t' + str(x[6]) + '\t' + str(x[7]) + '\t' + str(x[8]) + '\t' + str(x[9]))

def Aproveitamento():

    aproveitamento = int(input('Insira a : '))
    cursor = BDconection2.cursor()
    
    cursor.execute('SELECT * FROM notas WHERE aproveitamento >= ?', (aproveitamento,))
    lista = cursor.fetchall()
    print(lista)
    print('ID \t clube \t Pontos \t Vitórias \t Empates \t Jogos \t GolsMarcados \t GolsSofridos \t SaldoGols \t Aproveitamento')
    for x in lista:
        print(str(x[0]) + '\t' + x[1] + '\t' + str(x[2]) + '\t' + str(x[3]) + '\t' + str(x[4])  + '\t' + str(x[5]) + '\t' + str(x[6]) + '\t' + str(x[7]) + '\t' + str(x[8]) + '\t' + str(x[9]))

cont = 0
while cont == 0:
    op = int(input('\n------------------- \n1. Inserir \n2. Pesquisa de Clube \n3. Pontuação \n4. Aproveitamento \n5. Sair \n------------------- \n OP: ')); 

    if op == 1:
        Inserir()
    elif op == 2:
        Pesquisa()
    elif op == 3:
        Pontuacao()
    elif op == 4:
        Aproveitamento()
    else:
        cont = 1
        exit()
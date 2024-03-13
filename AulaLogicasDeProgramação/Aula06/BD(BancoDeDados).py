import sqlite3

BDconection = sqlite3.connect('C:/Users/unisanta/Desktop/Aula - 1703/AulaBD/Alunos.db')

BDconection.execute('CREATE TABLE IF NOT EXISTS notas (id integer, nome text, p1 decimal, p2 decimal)')

BDconection.execute('INSERT INTO notas VALUES(1, "cleiton", 8, 8)')

BDconection.execute('INSERT INTO notas VALUES(2, "junin", 2, 8)')

BDconection.execute('INSERT INTO notas VALUES(3, "cleber", 5, 3)')

BDconection.execute('INSERT INTO notas VALUES(1, "JAIR", 1, 1)')

BDconection.commit()
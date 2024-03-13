
frase = input("Insira uma frase: ")
p = []
frase2 = ''
a = 0

for i in range(len(frase)):
    if((frase[i].isalpha())) or (frase[i].isspace()):
        frase2 = frase2 + frase[i]
p = frase2.split(' ')

for i in range(len(p)):
    if(p[i].isalpha()):
        a += 1
print(a,'Palavras')

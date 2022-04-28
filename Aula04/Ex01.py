string1 = input("Digite a primeira string: ")
string2 = input("Digite a segunda string: ")

print(f"Conteudo da 1º string: {string1} ; Coprimento: {len(string1)} characteres ")

print(f"Conteudo da 2º string: {string2} ; Coprimento: {len(string2)} characteres ")

if len(string1) == len(string2):

    print("Comprimentos iguais")
else:
    
    print("Comprimentos diferentes")


if string1 == string2:

    print("As duas strings são iguais")

else:

    print("As duas strings são diferentes")
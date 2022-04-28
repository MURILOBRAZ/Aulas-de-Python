

from calendar import month


d = str(input("digite o dia de seu nascimento: "))

m = input("digite o mês de seu nascimento: ")

a = str(input("digite o ano de seu nascimento: "))

month = ["dummy","Janeiro","Fevereiro","Março",
"Abril","Maio","Junho",
"Julho","Agosto","Setembro",
"Outubro","Novembro","Dezembro"]

print(f"voce nasceu no dia {d} de {month[int(m)]} de {a}")
"""
Desenvolva um programa em Pythonque receba via teclado um valor e a partir disso faça:(1)seforumvalornegativo,mostreomódulo(valorsemsinal)dovalor;(2)seforumvalormaiordoque10,soliciteoutrovaloremostreadiferençaentreeles;(3)Casoovalornãosejadenenhumacondiçãoanterior,mostreovalordivididopor5
"""
valor = int(input("Digite um valor: "))

print("João Rafael Sturion Mantoanelli, RA: 1051392411012")
if valor < 0:
    print(f"O modulo do valor é {abs(valor)}")
elif valor > 10:
    valor2 = int(input("Digite outro valor: "))
    print(f"A diferença entre os valores é {valor - valor2}")
else:
    print(f"O valor dividido por 5 é {valor / 5}")






""""
Nesse programa o usuário deve entrar com um número e o sistema retornar se ele é divisível por 10 ou se é divisível por 5 ou se é divisível por 2, caso contrário retornar que o valor não é divisível por nenhum desses valores.
"""

numero = int(input("Digite um número: "))

print("João Rafael Sturion Mantoanelli, RA: 1051392411012")
if numero % 10 == 0:
    print(f"O número {numero} é divisivel por 10")
elif numero % 5 == 0:
    print(f"O número {numero} é divisivel por 5")
elif numero % 2 == 0:
    print(f"O número {numero} é divisivel por 2")
else:
    print(f"O número {numero} não é divisivel por 10, 5 ou 2")




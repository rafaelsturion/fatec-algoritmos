import math

print("João Rafael Sturion Mantoanelli, RA: 1051392411012")
# Solicitar ao usuário que insira um número
num = float(input("Digite um número inteiro entre 1 e 8: "))
# Se o número for 1, 2 ou 3, calcular o quadrado do número e exibir o resultado
if num in [1, 2, 3]:
    print(num ** 2)

# Se o número for 4 ou 9, calcular a raiz quadrada do número e exibir o resultado
elif num in [4, 9]:
    print(math.sqrt(num))

# Se o número for 6, 7 ou 8, dividir o número por 9 e exibir o resultado
elif num in [6, 7, 8]:
    print(round(num / 9, 4))

else:
    print("Número não reconhecido")


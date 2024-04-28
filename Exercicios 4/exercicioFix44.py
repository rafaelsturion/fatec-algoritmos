import math

def process_number():
    # Solicitar ao usuário que insira um número
    num = int(input("Digite um número: "))

    # Nome e RA João Rafael
    print("João Rafael Sturion Mantoanelli, RA: 1051392411012")

    # Se o número for 1 ou 2, calcular o cubo do número e exibir o resultado
    if num in [1, 2]:
        print(num ** 3)

    # Se o número for múltiplo de 3, calcular o fatorial do número e exibir o resultado
    elif num % 3 == 0:
        print(math.factorial(num))

    # Se o número for 4, 5, 7 ou 8, dividir o número por 9 e exibir o resultado
    elif num in [4, 5, 7, 8]:
        print(num / 9)

    # Se o número não for nenhum dos valores acima, exibir "valor inválido"
    else:
        print("Valor inválido")

# Chamar a função para executar o código
process_number()
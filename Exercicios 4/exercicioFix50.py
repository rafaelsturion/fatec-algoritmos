from math import fabs

def process_number():
    num = float(input("Digite um número: "))

    # Nome e RA João Rafael
    print("João Rafael Sturion Mantoanelli, RA: 1051392411012")

    # Se o número for negativo, mostrar o módulo do número
    if num < 0:
        print(fabs(num))

    # Se o número for maior que 10, solicitar outro número e mostrar a diferença entre eles
    elif num > 10:
        num2 = float(input("Digite outro número: "))
        print(abs(num - num2))

    # Se o número não atender a nenhuma das condições acima, mostrar o número dividido por 5
    else:
        print(num / 5)

# Call the function to execute the code
process_number()
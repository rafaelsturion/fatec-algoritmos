def calcular_aumento_salario():
    # Solicitar ao usuário que insira seu nome e salário
    nome = input("Digite seu nome: ")
    salario = float(input("Digite seu salário: "))

    # Se o salário for menor ou igual a 1500, adicionar um aumento de 20%
    if salario <= 1500:
        salario += salario * 0.20

    # Se o salário for maior que 1500 e menor que 2500, adicionar um aumento de 10%
    elif 1500 < salario < 2500:
        salario += salario * 0.10

    # Se o salário for maior ou igual a 2500, adicionar um aumento de 5%
    else:
        salario += salario * 0.05

    # Nome e RA João Rafael
    print("João Rafael Sturion Mantoanelli, RA: 1051392411012")

    # Exibir o nome do usuário e o novo salário
    print("Nome: ", nome)
    print("Novo salário: R$", salario)
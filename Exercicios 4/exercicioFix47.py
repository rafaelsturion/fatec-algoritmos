def check_divisibility():
    # Solicitar ao usuário que insira um número
    num = int(input("Digite um número: "))

    # Nome e RA João Rafael
    print("João Rafael Sturion Mantoanelli, RA: 1051392411012")

    # Se o número for divisível por 10, exibir a mensagem correspondente
    if num % 10 == 0:
        print("O número é divisível por 10.")

    # Se o número for divisível por 5, exibir a mensagem correspondente
    elif num % 5 == 0:
        print("O número é divisível por 5.")

    # Se o número for divisível por 2, exibir a mensagem correspondente
    elif num % 2 == 0:
        print("O número é divisível por 2.")

    # Se o número não for divisível por 10, 5 ou 2, exibir a mensagem correspondente
    else:
        print("O número não é divisível por 10, 5 ou 2.")
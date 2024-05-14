def calcular_aumento_salario(salario):
    if salario <= 1500.00:
        aumento = salario * 0.20
    elif salario > 1500.00 and salario < 2500.00:
        aumento = salario * 0.10
    else:
        aumento = salario * 0.05
    
    salario_atualizado = salario + aumento
    return salario_atualizado

def main():
    salario = float(input("Digite o seu salário: R$ "))
    salario_atualizado = calcular_aumento_salario(salario)
    print("Seu novo salário é: R$ {:.2f}".format(salario_atualizado))

    print("João Rafael Sturion Mantoanelli, RA: 1051392411012")

if __name__ == "__main__":
    main()

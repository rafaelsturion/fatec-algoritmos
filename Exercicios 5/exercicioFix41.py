def calcular_fatorial(numero):
    fatorial = 1
    for i in range(1, numero + 1):
        fatorial *= i
    return fatorial

def main():
    numero = int(input("Digite um número inteiro positivo: "))
    if numero < 0:
        print("Por favor, digite um número inteiro positivo.")
    else:
        resultado = calcular_fatorial(numero)
        print(f"O fatorial de {numero} é: {resultado}")

    print("João Rafael Sturion Mantoanelli, RA: 1051392411012")

if __name__ == "__main__":
    main()

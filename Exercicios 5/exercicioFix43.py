def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def verificar_peso_ideal(imc, sexo):
    if sexo == 'f':
        if imc < 19:
            return "Abaixo do peso"
        elif 19 <= imc < 24:
            return "Peso ideal"
        else:
            return "Acima do peso"
    elif sexo == 'm':
        if imc < 20:
            return "Abaixo do peso"
        elif 20 <= imc < 25:
            return "Peso normal"
        else:
            return "Acima do peso"
    else:
        return "Sexo não reconhecido"

def main():
    peso = float(input("Digite o peso (em kg): "))
    altura = float(input("Digite a altura (em metros): "))
    sexo = input("Digite o sexo (f - feminino, m - masculino): ").lower()

    imc = calcular_imc(peso, altura)
    situacao_peso = verificar_peso_ideal(imc, sexo)
    
    print(f"Seu IMC é: {imc:.2f}")
    print(f"Você está {situacao_peso}.")

    print("João Rafael Sturion Mantoanelli, RA: 1051392411012")

if __name__ == "__main__":
    main()

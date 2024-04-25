h = float(input("Digite a sua altura em metros: "))
sexo = input("Digite o seu sexo (M para masculino e F para feminino): ")


if sexo == "M":
    peso_ideal = (72.7*h) - 58
    print("O seu peso ideal é: ", peso_ideal)
elif sexo == "F":
    peso_ideal = (62.1*h) - 44.7
    print("O seu peso ideal é: ", peso_ideal)

print("RA 1051392411012, Nome: João Rafael Sturion Mantoanelli, Turma I DSM")
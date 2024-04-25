# Solicitar ao usuário que insira seu nome
nome = input("Digite seu nome: ")

# Solicitar ao usuário que insira seu RA
ra = input("Digite seu RA: ")

# Solicitar ao usuário que insira a primeira nota
nota1 = float(input("Digite a primeira nota: "))

# Solicitar ao usuário que insira a segunda nota
nota2 = float(input("Digite a segunda nota: "))

# Calcular a média das notas
media = (nota1 + nota2) / 2

# Nome e RA João Rafael
print("João Rafael Sturion Mantoanelli, RA: 1051392411012")

# Se a média for maior ou igual a sete, exibir a mensagem de aprovação
if media >= 7:
    print("Parabéns, você está aprovado!")

# Se a média for menor que sete, exibir a mensagem de estudo para o exame
else:
    print("Você ainda tem uma chance! Estude mais para o exame.")
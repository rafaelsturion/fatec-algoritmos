# Solicitar ao usuário que insira seu nome
nome = input("Digite seu nome: ")

# Solicitar ao usuário que insira seu RA
ra = input("Digite seu RA: ")

# Solicitar ao usuário que insira a primeira nota
nota1 = float(input("Digite a primeira nota: "))

# Solicitar ao usuário que insira a segunda nota
nota2 = float(input("Digite a segunda nota: "))

# Solicitar ao usuário que insira a nota do exame
nota_exame = float(input("Digite a nota do exame: "))

# Calcular a média das notas
media = (nota1 + nota2) / 2

# Calcular a média aritmética entre a média anterior e a nota do exame
media_final = (media + nota_exame) / 2

# Nome e RA João Rafael
print("João Rafael Sturion Mantoanelli, RA: 1051392411012")

# Se a média for maior ou igual a cinco, exibir a mensagem de aprovação
if media_final >= 5:
    print("Parabéns, você aproveitou a sua chance! Está aprovado.")

# Se a média for menor que cinco, exibir a mensagem de reprovação
else:
    print("Estude mais para a próxima. Você não alcançou o mínimo necessário.")
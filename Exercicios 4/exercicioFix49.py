# Solicitar ao usuário que insira seu nome e idade
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

# Nome e RA João Rafael
print("João Rafael Sturion Mantoanelli, RA: 1051392411012")

# Se a idade for maior ou igual a 18 e menor que 65, exibir a mensagem "Bem vindo NOME, você é maior de idade."
if 18 <= idade < 65:
    print(f"Bem vindo {nome}, você é maior de idade.")

# Se a idade for menor que 18, exibir a mensagem "Bem vindo NOME, você é menor de idade."
elif idade < 18:
    print(f"Bem vindo {nome}, você é menor de idade.")

# Se a idade for maior ou igual a 65, exibir a mensagem "Bem vindo NOME, você é maior de 65 anos."
else:
    print(f"Bem vindo {nome}, você é maior de 65 anos.")
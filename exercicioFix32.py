"""
    Faça um algoritmo que calcule a média do aluno. Ele deve entrar com seu nome, ra, nota 1 e nota 2. O sistema deverá informar a ele as seguintes mensagens:a)Se a média for maior ou igual a sete: Parabéns, você está aprovado!b)Se  a média  for  menor  que  sete:  Você  ainda  tem  uma  chance!  Estude  mais  para  o exame.
"""

nome = str(input("Digite o nome do aluno: "))
ra = int(input("Digite o RA do aluno:"))
nota1 = float(input("Digite a Nota 1 do aluno: "))
nota2 = float(input("Digite a Nota 2 do aluno: "))

media = nota1 + nota2 / 2

print("João Rafael Sturion Mantoanelli, RA: 1051392411012")
if media >= 7:
    print("Parabens, você está aprovado e a sua média é: ", media)
else:
    print("Você ainda tem uma chance! Estude mais para o exame e a sua média é: ", media)




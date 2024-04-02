"""
Altere o algoritmo anterior (Fix32)para que o usuário entre com a nota do exame. Lembre-se que deve se realizar a média aritmética entre a média e a nota do exame. O sistema deverá informar a ele as seguintes mensagens:a)Se a média for maior ou igual a cinco: Parabéns, você aproveitou a sua chance! Está aprovado.b)Se a média for menor que cinco: Estude mais para a próxima. Você não alcançou o mínimo necessário.
"""

nome = str(input("Digite o nome do aluno: "))
ra = int(input("Digite o RA do aluno:"))
nota1 = float(input("Digite a Nota 1 do aluno: "))
nota2 = float(input("Digite a Nota 2 do aluno: "))
nota_exame = float(input("Digite a Nota do Exame: "))

media = (nota1 + nota2) / 2
media_final = (media + nota_exame) / 2

print("João Rafael Sturion Mantoanelli, RA: 1051392411012")
if media_final >= 5:
  print(f"Parabéns, {nome}, você foi aprovado com média final {media_final:.2f}!")
else:
  print(f"Infelizmente, {nome}, você não foi aprovado. Sua média final foi {media_final:.2f}.")

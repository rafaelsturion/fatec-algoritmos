"""
ElaboreumprogramaemPythonqueousuárioentrecom seu e seu salário. Se o salário for menor  ou  igual  a  R$1500,00  coloque  um  acréscimo  de  20%  de  aumento.  Se  for  maior  que R$1500,00 e menor que R$"2500,00 o acréscimo será de 10%, senão o acréscimo será de 5% para os demais valores.
"""

salario = float(input("Digite o seu salário: "))

print("João Rafael Sturion Mantoanelli, RA: 1051392411012")
if salario <=1500:
    print(f"O seu salário teve um acréscimo de 20% e agora é {salario * 1.2}")
elif salario > 1500 and salario < 2500:
    print(f"O seu salário teve um acréscimo de 10% e agora é {salario * 1.1}")
elif salario >= 2500:
    print(f"O seu salário teve um acréscimo de 5% e agora é {salario * 1.05}")


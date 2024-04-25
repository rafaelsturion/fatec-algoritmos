# Solicita os valores das compras ao usuário
compra1 = float(input("Digite o valor da primeira compra: "))
compra2 = float(input("Digite o valor da segunda compra: "))
compra3 = float(input("Digite o valor da terceira compra: "))

# Calcula o valor total das compras
valor_total = compra1 + compra2 + compra3

# Inicializa a variável desconto
desconto = 0

# Calcula o desconto de acordo com as condições especificadas
if valor_total > 300:
    desconto = valor_total * 0.2
elif valor_total > 200:
    desconto = valor_total * 0.15
elif valor_total > 100:
    desconto = valor_total * 0.1

# Calcula o valor com desconto
valor_com_desconto = valor_total - desconto

# Mostra na tela o valor total e o valor com desconto
print(f"Valor total das compras: R${valor_total:.2f}")
print(f"Desconto aplicado: R${desconto:.2f}")
print(f"Valor com desconto: R${valor_com_desconto:.2f}")
print("RA 1051392411012, Nome: João Rafael Sturion Mantoanelli, Turma I DSM")
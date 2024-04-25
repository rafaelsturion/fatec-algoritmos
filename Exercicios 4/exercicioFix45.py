# Solicitar ao usuário que insira o valor total da compra
valor_total = float(input("Digite o valor total da compra: "))

# Se o valor for maior que 300, calcular o desconto de 20% e o valor final
if valor_total > 300:
    desconto = valor_total * 0.20
    valor_final = valor_total - desconto

# Se o valor for entre 200 e 299.99, calcular o desconto de 10% e o valor final
elif 200 <= valor_total <= 299.99:
    desconto = valor_total * 0.10
    valor_final = valor_total - desconto

# Se o valor for menor que 200, calcular o desconto de 5% e o valor final
else:
    desconto = valor_total * 0.05
    valor_final = valor_total - desconto

# Nome e RA João Rafael
print("João Rafael Sturion Mantoanelli, RA: 1051392411012")

# Exibir o valor total e o valor final a pagar
print("Valor total: R$", valor_total)
print("Valor final a pagar: R$", valor_final)
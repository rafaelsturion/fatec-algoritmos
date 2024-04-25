"""
Elabore  um programa em PYTHON, que mostre  os descontos  concedidos  pela  loja  ABC  em suas mercadorias. Em  compras  acima  de  R$  300,00  forneça  20%  de  desconto,  entre  R$  200,00  a  R$  299,99 desconto de 10% e abaixo de R$ 199,99 o desconto será de 5%. Mostre na tela o valor total e o valor final a pagar (com o desconto).
"""
compra = (float(input("Digite o valor da sua compra: ")))

print("João Rafael Sturion Mantoanelli, RA: 1051392411012")
if compra >= 300:
    desconto = compra * 0.8
    print(f"Você ganhou 20% de desconto. O valor total da sua compra é {compra} e o seu valor com desconto é {desconto} ")
elif compra >= 200 and compra < 300:
    desconto = compra * 0.9
    print(f"Você ganhou 10% de desconto. O valor total da sua compra é {compra} e o seu valor com desconto é {desconto} ")
elif compra <200:
    desconto = compra * 0.95
    print(f"Você ganhou 5% de desconto. O valor total da sua compra é {compra} e o seu valor com desconto é {desconto} ")




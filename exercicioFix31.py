"""
    Desenvolva um programa em Pythonque receba via tecladoum valor e a partir disso faça:(1) se o valor for 1, 2 ou 3, mostre o valor elevado ao quadrado;(2) se o valor for o número 4 ou 9, mostre a raiz quadrada do número; (3) se for os valores 6, 7 e 8, mostre o valor dividido 9.
"""

import math
valor = int(input("Digite um valor:"))

print("João Rafael Sturion Mantoanelli, RA: 1051392411012")
if valor in (1, 2, 3):
    quadrado = valor ** 2
    print("O quadrado do número é: ", quadrado)
elif valor in (4, 9):
    raiz = math.sqrt(valor)
    print("A raiz quadrada do número é: ", raiz)
elif valor in (6, 7, 8):
     div_nove = valor / 9
     print("A divisão por nove do número é: ", div_nove)
else:
    print(f"O valor {valor} não está entre as opções válidas (1, 2, 3, 4, 6, 7, 8, 9).")
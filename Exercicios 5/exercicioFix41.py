def dados():
    return "João Rafael Sturion Mantoanelli, RA1051392411012, turma DSM 1"

def calcular_fatorial(n):
    fatorial = 1
    for i in range(1, n + 1):
        fatorial *= i
    return fatorial

print(dados())

# Solicitar ao usuário que insira um número inteiro positivo
numero = int(input("Digite um número inteiro positivo: "))

# Verificar se o número é positivo
if numero < 0:
    print("Por favor, insira um número inteiro positivo.")
else:
    # Calcular e exibir o fatorial
    resultado = calcular_fatorial(numero)
    print(f"O fatorial de {numero} é {resultado}")

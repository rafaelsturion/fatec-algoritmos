def calcular_media(nota1, nota2):
    return (nota1 * 4 + nota2 * 6) / 10

def atribuir_conceito(media):
    if media >= 9.0:
        return "A - Aprovado"
    elif 7.0 <= media < 9.0:
        return "B - Aprovado"
    elif 3.0 <= media < 7.0:
        return "C - Exame"
    else:
        return "D - DP"

def autenticar_professor():
    senha_correta = "senha123"  # Defina a senha correta aqui

    senha = input("Digite a senha do professor: ")
    if senha == senha_correta:
        return True
    else:
        print("Senha incorreta. Acesso negado.")
        return False

def main():
    if autenticar_professor():
        nome_aluno = input("Digite o nome do aluno: ")
        nota1 = float(input("Digite a nota da primeira avaliação: "))
        nota2 = float(input("Digite a nota da segunda avaliação: "))

        media = calcular_media(nota1, nota2)
        conceito = atribuir_conceito(media)

        print(f"Média do aluno {nome_aluno}: {media:.2f}")
        print(f"Conceito: {conceito}")
        print("João Rafael Sturion Mantoanelli, RA: 1051392411012")
if __name__ == "__main__":
    main()

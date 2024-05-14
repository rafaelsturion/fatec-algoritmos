def encontrar_maior_nota():
    contador = 1
    maior_nota = float(input("Digite a nota do aluno 1: "))
    
    while contador < 5:
        nota = float(input(f"Digite a nota do aluno {contador + 1}: "))
        if nota > maior_nota:
            maior_nota = nota
        contador += 1
    
    return maior_nota

def main():
    maior_nota = encontrar_maior_nota()
    print(f"A maior nota da turma é: {maior_nota}")

    print("João Rafael Sturion Mantoanelli, RA: 1051392411012")

if __name__ == "__main__":
    main()

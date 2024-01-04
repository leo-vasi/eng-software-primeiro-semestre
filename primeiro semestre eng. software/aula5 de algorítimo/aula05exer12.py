import os
os.system("cls")
print("Calculando média de notas de um aluno ponderadas")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
somaNotas = (nota1 * 3) + (nota2 * 2) + (nota3 * 5)
media = somaNotas / 10  # A soma das ponderações é 3 + 2 + 5 = 10
print(f"A média do aluno é: {media:.2f}")
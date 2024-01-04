import os 
os.system("cls") 
print("""\n\tAlgoritmo para cadastrar o controle de  
\tqualidade, imprime os números das peças reprovadas, e o total de peças  
\taprovadas e reprovadas no final do dia.""") 
contA = 0
contR = 0
for i in range(1, 4, +1):
    print(f"{i} ª peça")
    codigo = int(input("Digite aqui o número da peça: "))
    estado = str(input("Digite aqui o estado da peça, 'A' para aprovado e 'R' para reprovado: ")).lower()
    while estado != "a" and estado != "r":
        print("Digite um estado válido, digite 'A' para aprovado e 'R' para reprovado")
        estado = str(input("Digite aqui o estado da peça, 'A' para aprovado e 'R' para reprovado: ")).lower()
    if estado == "a":
            contA += 1
    else:
        contR += 1
        print("Peça com o código", codigo, " está reprovada" )
    if i <= 3:
        print("Pressione enter para continuar")
        input()
        os.system("cls")
    else:
        print("Pressione enter para ver o relatório final")
        input()
        os.system("cls")
print("\n\t"*130)
print(contA, "peças aprovadas", contR, "peças reprovadas entre as 400")
import os
os.system("cls")
print("\t\tChecando cargo correspondente de um funcionário")
codigo = int(input("Digite aqui o seu código: "))
if codigo > 5 or codigo <= 0:
    print("Erro, código inválido")
else:
    match codigo:
        case 1:
            print("\nSeu cargo é escriturário")
        case 2:
            print("\nSeu cargo é Secretária")
        case 3:
            print("\nSeu cargo é caixa")
        case 4:
            print("\nSeu cargo é gerente")
        case 5:
            print("\nSeu cargo é diretor")
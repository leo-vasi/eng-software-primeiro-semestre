import os
os.system("cls")
print("Código correspondete ao cargo")
codigo = int(input("Digite aqui o seu código: "))
if codigo == 1:
    print("Escriturário")
elif codigo == 2:
    print("Secretária")
elif codigo == 3:
    print("Caixa")
elif codigo == 4:
    print("Gerente")
elif codigo == 5:
    print("Diretor")
else:
    print("Código inválido, digite um número de 1 a 5 para saber o cargo correspondente ao código.")
import os
os.system("cls")
print("\t\tCalculadora")
operacao = str(input("Digite aqui a operação desejada: "))
if operacao != "+" and operacao != "-" and operacao != "*" and operacao !="/":
    print("Erro, digite uma operação válida!")
else:
    digito1 = float(input("Digite aqui o primeiro digito: "))
    digito2 = float(input("Digite aqui o segundo digito: "))
match operacao:
    case "+":
        resultado = digito1 + digito2
        print(f"O resultado é: {resultado}")
    case "-":
        resultado = digito1 - digito2
        print(f"O resultado é: {resultado}")
    case "*":
        resultado = digito1 * digito2
        print(f"O resultado é: {resultado}")
    case _:
        if digito2 == 0:
            print("Erro, não pode dividir por zero")
        else:
            resultado = digito1 / digito2
            print(f"O resultado é: {resultado}")
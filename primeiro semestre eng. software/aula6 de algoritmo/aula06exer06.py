import os
os.system("cls")
print("Calculando se há execesso")
peso = float(input("\nDigite o peso do peixe: "))
pesoPagar = peso - 50
pagar = pesoPagar * 4
if peso < 0:
    print("Erro, valor invalido.")
elif peso < 50:
    print(f"O peso não excede")
elif peso > 50:
    print(f"O valor a ser pago é: {pagar}")

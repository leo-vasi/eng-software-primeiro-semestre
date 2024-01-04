import os
os.system("cls")
print("Calculando um número positivo e maior que zero")
numero = float(input("Digite aqui um número (precisa ser maior que zero): "))
if numero > 0:
    quadrado = numero**2
    raiz = numero** 0.5 
    print(f"{numero:.0f} ao quadrado é: {quadrado:.0f} e a raiz de {numero:.0f} é: {raiz:.2f}")
else:
    print("Número inválido")
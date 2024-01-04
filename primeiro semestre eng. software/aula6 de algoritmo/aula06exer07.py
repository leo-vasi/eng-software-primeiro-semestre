import os
os.system("cls")
print("Média")
digito1 = int(input("DIgite o primeiro valor: "))
digito2 = int(input("Digite o segundo valor: "))
digito3 = int(input("Digite o terceiro valor: "))
media = (digito1 + digito2 + digito3) / 3
if digito1 >= digito2 and digito1 >= digito3:
    print(f"\nO maior valor é o digito: { digito1}")
    print(f"A média é: {media}")
elif digito2 >= digito1 and digito2 >= digito3:
    print(f"\nO maior valor é o digito: {digito2}")
    print(f"A média é: {media}")
elif digito3 >= digito1 and digito3 >= digito2:
    print(f"\nO maior valor é o digito: {digito3}")
    print(f"A média é: {media}")
else:
    print("Valor inválido")
    
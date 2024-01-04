import os
os.system("cls")
print("Meta de vendas para abater o valor do espetacúlo")
valorEspetaculo = float(input("Digite quanto você gastou com o espetáculo: "))
precoIngresso = float(input("Digite o preço do ingresso: "))
abaterMeta = valorEspetaculo / precoIngresso
print(f"Você precisará vender: {abaterMeta} ingressos para abater o valor do show.")
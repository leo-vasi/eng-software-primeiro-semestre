import os
os.system("cls")
print("Programa que receba os dados de 5 produtos")
imposto = {
    "Ate100": 0.05,
    "Maior100": 0.10
}
ptcp = {1: 50.00, 2: 35.00, 3: 24.00}  # Preço do Transporte de Cargas Perigosas
ptcn = {1: 12.00, 2: 35.00, 3: 60.00}  # Preço do Transporte de Cargas Normais
tp = 0
for i in range(1, 6):
    print(f"Produto {i}:")
    vu = float(input("Digite aqui o valor unitário: "))
    o = int(input("Digite aqui o número correspondente do país de origem, '1', '2' ou '3': "))
    t = input("Digite aqui o tipo de transporte, 'A' para aéreo, 'T' para terrestre e 'F' para fluvial: ").upper()
    cp = input("Sua carga é perigosa? Se sim, digite 'S', caso não, digite 'N': ").upper()
    if vu <= 100:
        calculo_imposto = vu * imposto["Ate100"]
    else:
        calculo_imposto = vu * imposto["Maior100"]
    if cp == "S":
        vt = ptcp[o]
    else:
        vt = ptcn[o]
    if o == 2 or t == 'A':
        seguro = vu / 2
    else:
        seguro = 0
    vf = vu + calculo_imposto + vt + seguro
    tp += vf
    print(f"Preço unitário: R$ {vu:.2f}")
    print(f"Imposto: R$ {calculo_imposto:.2f}")
    print(f"Valor de transporte: R$ {vt:.2f}")
    print(f"Seguro: R$ {seguro:.2f}")
    print(f"Preço final: R$ {vf:.2f}")
    print()
print(f"Valor total do pedido: R$ {tp:.2f}")
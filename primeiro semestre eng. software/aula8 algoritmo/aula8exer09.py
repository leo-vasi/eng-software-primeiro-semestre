import os 
os.system("cls")
print("Recebendo duas notas de 10 alunos e calculando a média")
s = 0
for i in range(1,10+1):
    N1 = float(input("Digite a primeira nota: "))
    N2 = float(input("Digite a segunda nota: "))
    m = (N1 + N2) / 2
    print(f"{m}")
    s = s +m
mt = s / 10
print(f"Media total: {mt}")
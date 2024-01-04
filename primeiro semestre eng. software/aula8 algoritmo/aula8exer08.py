import os 
os.system("cls")
print("Recebendo notas de alunos e calculando média")
N = int(input("Digite aqui o número de alunos: "))
s = 0
for i in range(1,N+1):
    num = int(input("Digite sua nota: "))
    s = s + num
    m = s / N
print(f"A média é: {m:.2f}")

import os
os.system("cls")
print("""Quantos anos serão necessários para que a população do país A, ultrapasse ou
iguale a população do país B""")
anos = 0
pop_A = 98000000
ganho_A = 0.035
pop_B = 200000000
ganho_B = 0.015
while pop_A < pop_B:
    pop_A += pop_A * ganho_A
    pop_B += pop_B * ganho_B
    anos += 1
    print(f"A população do país A ultrapassará a do país B em {anos} anos")
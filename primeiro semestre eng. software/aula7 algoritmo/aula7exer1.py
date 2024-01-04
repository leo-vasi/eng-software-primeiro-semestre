import os
os.system("cls")
print("\t\tChecando vogais ou consoantes")
letra = str(input("\nDigite aqui uma letra: ")).lower()
if letra >= "a" and letra <= "z":
    match letra:
            case "a"| "e" | "i" | "o" | "u":
                print("Vogal")
            case __:
                print("Consoante")
else:
    print("Erro, digite uma letra!")
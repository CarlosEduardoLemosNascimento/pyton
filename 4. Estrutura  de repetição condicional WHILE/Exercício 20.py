# Escrever um programa que solicite do uma nota e enquanto essa nota for menor que zero ou maior que 10 peça novamente 

import os
os.system("cls || clear")

# Variáveis

nota: float

while True:
    nota=int(input(f"Digite a nota: "))

    if nota < 0 or nota > 10:
        print("Nota inválida. A nota deve estar entre 0 e 10. Tente novamente.")
    else:
        print(f"Nota válida: {nota:.2f}")
        break
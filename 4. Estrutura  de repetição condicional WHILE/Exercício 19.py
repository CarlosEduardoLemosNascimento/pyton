# Escrever um programa que solicite do uma nota e enquanto essa nota for menor que zero ou maior que 10 peça novamente 

import os
os.system("cls || clear")

# Variáveis

nota: float


os.system("cls || clear")
nota=-1

# Pedindo os números ao usuário
print("=== INSERÇÃO DE DADOS ===")
while nota < 0 or nota > 10:
    os.system("cls || clear")
    nota=int(input(f"Digite a nota: "))
            
# Exibindo resultados
print(f"Nota do aluno: {nota:.2f}")
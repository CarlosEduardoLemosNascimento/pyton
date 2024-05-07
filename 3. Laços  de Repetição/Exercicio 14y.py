# Escrever um programa de computador que solicite do usuário 5 números inteiros e,
# ao final, apresente a soma de todos os números lidos.
import os
os.system("cls || clear")

# Variáveis

numero: int
soma: int
i: int

# Pedindo os números ao usuário
os.system("cls || clear")
soma=0
for i in range(1, 6):
    numero=int(input(f"Digite o {i}º número de 5: "))
    soma=soma+numero
    numero=0

print(f"\nSoma dos números digitados: {soma}")

# Escreva um algoritmo que leia 5 valores inteiros e ao final mostre:
# quantos números são pares;
# quantos números são ímpares;

import os
os.system("cls || clear")

# Variáveis

numero: int
contaPar: int
contaImpar: int
contaNulo: int
i: int

# Pedindo os números ao usuário
os.system("cls || clear")
contaPar=0
contaImpar=0
contaNulo=0

for i in range(1, 6):
    numero=int(input(f"Digite o {i}º número - inteiro diferente de zero, de 5: "))
    # Testando se o número é par ou impar e incrementando o contador correspondente
    if numero==0:
        contaNulo=contaNulo+1
    if numero%2==0:
        contaPar=contaPar+1
    else:
        contaImpar=contaImpar+1
# Exibindo resultados
print ("\n")
print(f"Quantidade de zeros digitados: {contaNulo}")
print(f"Quantidade de números pares: {contaPar}")
print(f"Quantidade de números ímpares: {contaImpar}")
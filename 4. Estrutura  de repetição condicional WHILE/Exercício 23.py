# Escrever um programa que pergunte ao usuário se deseja inserir mais uma notas.
# Se a resposta for N o programa fará a média das notas informadas e a exibirá.

import os
os.system("cls || clear")

contadorNotas = 0
soma = 0

while True:
    nota=float(input(f"Digite uma nota: "))
    resposta=input(f"Deseja inserir mais uma nota? ")

    resposta = resposta.upper()

    contadorNotas += 1
    soma += nota

    if resposta == "N":
        break
        
    else:
        break

        # Calculando valores

media=soma/contadorNotas

# Exibindo resultados
print(f"Média do aluno: {media:.2f}")

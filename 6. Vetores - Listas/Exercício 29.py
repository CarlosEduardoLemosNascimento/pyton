# Crie um programa que leia 5 numeros armazenando em um vetor e informa qual é o menor número e o maior
# Mostre os números informados pelo usuário

import os

os.system("cls || clear")

# Criando constante
QUANTIDADE_NUMEROS = 5

# Criando variáveis e lista
numeros = []

# Solicitando ops numeros para o usuário
for i in range(QUANTIDADE_NUMEROS):
    numero = float(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)
    
# Limpando a tela para exibir os resultados
os.system("cls || clear")

# Calculando o maior e o menor número
numero_max = max(numeros)
numero_min = min(numeros)

# Exibindo os números inseridos pelo usuário
# ForEach
for i, numero in enumerate(numeros):
    print(f"{i+1}º número: {numero}")
    
print()

# Exibindo o maior e o menor número
print(f"Maior número: {numero_max}")
print(f"Menor número: {numero_min}")
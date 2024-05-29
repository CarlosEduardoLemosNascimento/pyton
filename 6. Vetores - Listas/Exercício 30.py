# Crie um programa que leia uma quantidade indefinida de numeros armazenando em um vetor e informa qual é o menor número e o maior
# Mostre os números informados pelo usuário

import os

os.system("cls || clear")

numeros = []

# Lendo os números até que zero seja digitado
while True:
    num = int(input("Digite um número (0 para parar): "))
    if num == 0:
        break
    numeros.append(num)

# Mostrando os números informados
os.system("cls || clear")
for i, numero in enumerate(numeros):
    print(f"{i+1}º número: {numero}")
print()

# Encontrando o menor e o maior número
menor = min(numeros)
maior = max(numeros)
print("Menor número:", menor)
print("Maior número:", maior)
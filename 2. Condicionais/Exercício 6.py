# Elabore um algoritmo para receber dois inteiros como entrada do teclado e escreva na tela:
# A média, a soma, o produto, o menor valor e o maior valor.
# Usando uma linha para cada resultado.

import os
os.system("cls || clear")

# Variáveis

numero1:int
numero2:int

# Solicitando dados

print("=== INSIRA OS DADOS SOLICITADOS ===")

numero1 = float(input("Digite o 1º número: "))
numero2 = float(input("Digite o 2º número: "))

# Calculando valores
soma = int(numero1 + numero2)
media = float(soma/2)
produto = int(numero1 * numero2)
"""
Função de pyton para teste de maior número
maiorNumero = max (numero1, numero2)
menorNumero = min (numero1, numero2)
"""

# Mostrando os resultados
os.system("cls || clear")
print("=== EXIBINDO RESULTADOS ===")
print(f"Média: {media}")
print(f"Soma: {soma}")
print(f"Produto: {produto}")

# Testando o maior e o menor número

if numero1 < numero2:
    maiorNumero = numero2
    menorNumero = numero1
    print(f"Menor número: {menorNumero}")
    print(f"Maior número: {maiorNumero}")

elif numero1 > numero2:
    maiorNumero = numero1
    menorNumero = numero2
    print(f"Menor número: {menorNumero}")
    print(f"Maior número: {maiorNumero}")
else:
    print("Os números digitados são iguais")

print("=== FIM ===")

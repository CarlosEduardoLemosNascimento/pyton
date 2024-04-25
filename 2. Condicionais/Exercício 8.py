# Elabore um algoritmo usando operações lógicas para informar se uma pessoa é obrigada a votar
# Considere a regra:
# Menosres de 18 anos e maiores de 65 anos não são obrigados a votar

import os
os.system("cls || clear")

# Variáveis

idade:int

# Solicitando dados

print("=== INSIRA O DADO SOLICITADO PARA VALIDAÇÃO ===\n")

idade = int(input("Digite a idade: "))

# Validando teste
os.system("cls || clear")

print("=== RESULTADO DA VALIDAÇÃO ===\n")

if idade < 18 or idade > 65:
    print("Voto NÃO obrigatório.")

else:
    print("Obrigatoriedade de voto confirmada!")

print("\n=== FIM ===")

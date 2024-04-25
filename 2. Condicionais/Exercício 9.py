# Faça um algoritmo para ler
# 1 - A descrição de um produto (nome)
# 2 - A quantidade adquirida
# 3 - O preço unitário
# Calcular e escrever o preço total (total = quantidade adquirida x preço unitário)
# O desconto e o total a pagar (total a pagar = total - desconto), sabendo-se que:
# Se quantidade <= 5 o desconto será de 2%
# Se quantidade > 5 e <= 10 o desconto será de 3%
# Se quantidade > 10 o desconto será de 5%

import os
os.system("cls || clear")

# Variáveis

produto:str
quantidadeAdquirida:float
precoUnitario:float
totalParcial:float
totalFinal:float
desconto:float
percentual:str


# Solicitando dados

print("=== INSIRA OS DADOS SOLICITADOS ===\n")

produto = str(input("Digite o produto: "))
quantidadeAdquirida = float(input("Digite a quantidade: "))
precoUnitario = float(input("Digite o valor unitário: "))

# Calculando o valor da compra

totalParcial=quantidadeAdquirida*precoUnitario

# Calculando o desconto

if quantidadeAdquirida <= 5:
    desconto=totalParcial*0.02
    percentual="2%"
    
elif quantidadeAdquirida > 10:
    desconto=totalParcial*0.05
    percentual="5%"
else:
    desconto=totalParcial*0.03
    percentual="3%"

totalFinal=totalParcial-desconto

# Exibindo os resultados

os.system("cls || clear")

print("=== EXTRADO DA COMPRA ===\n")
print(f"Quantidade total de produtos adquiridos: {quantidadeAdquirida}")
print(f"Valor dos produtos adquiridos: R$ {totalParcial}")
print(f"Valor do desconto: R$ {desconto}")
print(f"Total a pagar: R$ {totalFinal}")
print(f"Percentual de desconto aplicado: {percentual}")

print("\n=== FIM ===")

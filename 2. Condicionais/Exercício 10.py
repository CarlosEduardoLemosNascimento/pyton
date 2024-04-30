# Escreva um algoritmo para ler a quantidade em kg de morangos e a quantidade em kg de maçâs adquiridos
# Escreva o valor a ser pago

import os
os.system("cls || clear")

# Variáveis

qdeMorangos: float
qdeMacas: float
qdeTotal: float
valorKgMorangos:float
valorKgMacas:float
valorTotalMorangos:float
valorTotalMacas:float
valorTotalParcial:float
valorTotalFinal:float

# EXIBINDO TABELA

print("           TABELA DE PREÇOS           ")
print(" ____________________________________")
print("|            | ATÉ 5 Kg  | + 5 Kg    |")
print("|------------------------------------|")
print("|  Morangos  |  R$ 2,50  |  R$ 2,20  |")
print("|------------------------------------|")
print("|    Maçã    |  R$ 1,80  |  R$ 1,50  |")
print("|____________________________________|\n\n\n")

print("           REGISTRO DE VENDAS           ")
qdeMorangos=float(input("Digite a quantidade de morangos (em kg): "))
qdeMacas=float(input("Digite a quantidade de maçãs (em kg): "))
qdeTotal=qdeMorangos+qdeMacas

# Análise e definição de valores
if qdeMorangos<=5:
    valorKgMorangos=2.5
else:
    valorKgMorangos=2.2

if qdeMacas<=5:
    valorKgMacas=1.8
else:
    valorKgMacas=1.5

valorTotalMorangos=qdeMorangos*valorKgMorangos
valorTotalMacas=qdeMacas*valorKgMacas
valorTotalParcial=valorTotalMorangos+valorTotalMacas

# Calculando descontos

if qdeTotal>8 or valorTotalParcial>25:
    valorTotalFinal=valorTotalParcial-(valorTotalParcial*0.1)
else:
    valorTotalFinal=valorTotalParcial

# Imprimindo resultados
os.system("cls || clear")

print("           TABELA DE PREÇOS           ")
print(" ____________________________________")
print("|            | ATÉ 5 Kg  | + 5 Kg    |")
print("|------------------------------------|")
print("|  Morangos  |  R$ 2,50  |  R$ 2,20  |")
print("|------------------------------------|")
print("|    Maçã    |  R$ 1,80  |  R$ 1,50  |")
print("|____________________________________|\n\n\n")
print("                    NOTA FISCAL                   ")
print("===================================================")
print(f"Morango -------------------------   {qdeMorangos} kg")
print(f"Valor total do item -------------   R$ {valorKgMorangos:.2f}")
print(f"Maçã ----------------------------   {qdeMacas} kg")
print(f"Valor total do item -------------   R$ {valorTotalMacas:.2f}")
print(f"Quantidade total dos produtos ---   {qdeTotal} kg")
#print(f"Valor dos produtos --------------   R$ {round(valorTotalParcial,2)}")
print(f"Valor dos produtos --------------   R$ {valorTotalParcial:.2f}")
print(f"Valor a pagar -------------------   R$ {valorTotalFinal:.2f}")
print("===================================================")
# Crie um programa que leia 6 numeros armazenando-os em um vetor e informa quantos são pares e quantos são ímpares
# Mostre os números informados pelo usuário

import os

os.system("cls || clear")

# Criando constante
QUANTIDADE_NUMEROS = 6

# Criando variáveis e lista
numeros = []
contaPar=0
contaImpar=0


# Solicitando ops numeros para o usuário
for i in range(QUANTIDADE_NUMEROS):
    numero = float(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)
    if numero % 2 == 0:
        contaPar = contaPar + 1
    else:
        contaImpar = contaImpar + 1
      
# Limpando a tela para exibir os resultados
os.system("cls || clear")
for i, numero in enumerate(numeros):
    print(f"{i+1}º número: {numero}")

# Imprimindo os quantitativos
print("Quantidade de números pares: ", contaPar)
print("Quantidade de números ímpares:", contaImpar)
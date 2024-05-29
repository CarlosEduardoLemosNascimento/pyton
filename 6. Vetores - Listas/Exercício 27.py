# Crie um programa que leia 3 notas adicionando em vetor calcule a media e exiba as notas e a media

import os

os.system("cls || clear")

# Criando variáveis e lista
media: float = 0
soma: float = 0
notas = []

# Solicitando 3 notas para o usuário
for i in range(3):
    nota = float(input("Digite a  nota: "))
    notas.append(nota)
    soma = soma + nota

# Calculando a média
media=soma/3

# Limpando a tela para exibir os resultados
os.system("cls || clear")

# Exibindo as notas para o usuário
for i in range(3):
    print(f"{i+1}ª nota: {notas[i]}")
    
print()

# Exibindo a media
print(f"Média do aluno: {media:.2f}")
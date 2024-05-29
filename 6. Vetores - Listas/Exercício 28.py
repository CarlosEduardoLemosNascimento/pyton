# Crie um programa que leia 3 notas adicionando em vetor calcule a media e exiba as notas e a media

import os

os.system("cls || clear")

# Criando constante
QUANTIDADE_NOTAS = 3
# Criando variáveis e lista
media: float = 0
#soma: float = 0
notas = []

# Solicitando 3 notas para o usuário
for i in range(QUANTIDADE_NOTAS):
    nota = float(input("Digite a  nota: "))
    notas.append(nota)
    #soma = soma + nota

# Calculando a média
#media=soma/QUANTIDADE_NOTAS
media = sum(notas)/ QUANTIDADE_NOTAS

# Limpando a tela para exibir os resultados
os.system("cls || clear")

# Exibindo as notas para o usuário
for i in range(QUANTIDADE_NOTAS):
    print(f"{i+1}ª nota: {notas[i]}")

'''ForEach
for nota in notas:
    print(F"Nota: {nota}")'''
    
print()

# Exibindo a media
print(f"Média do aluno: {media:.2f}")
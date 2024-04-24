# Elabore um algoritmo para ler o nome de um aluno, sua idade e 2 notas.
# Calcular a média aritmética do alluno
#mostrar nome, idade, notas e média
import os

os.system("cls || clear")

nome:str
idade:int
nota1: float
nota2: float
media:float

print("=== OBTENDO DADOS ===\n")
nome = str(input("Digite o nome do aluno: "))
idade = int(input("Digite a idade do aluno: "))
nota1 = float(input("Digite a 1ª nota do aluno: "))
nota2 = float(input("Digite a 2ª nota do aluno: "))

media = (nota1 + nota2) / 2

os.system("cls || clear")

print("=== EXIBINDO DADOS ===\n")
print(f"Nome do aluno: {nome}")
print(f"Idade do aluno: {idade}")
print(f"1ª nota do aluno: {nota1}")
print(f"2ª nota do aluno: {nota2}")
print(f"Média do aluno: {media}")
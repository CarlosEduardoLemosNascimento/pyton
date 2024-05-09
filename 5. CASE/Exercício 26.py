# Foi feita uma pesquisa entre os habitantes de uma região. 
# Foram coletados os dados de idade, sexo (M/F) e salário. 
# Faça um algoritmo que informe:  

# a) a média de salário do grupo;
# b) maior e menor idade do grupo;
# c) quantidade de mulheres com salário a partir de R$ 5.000,00.

# Crie um menu com duas opções.

# Código |        Descrição
#     1      |   Adicionar pessoa
#     2      |   Exibir resultados e sair

#O final da leitura de dados se dará com quando o usuário digitar o número código 2.

import os
import sys

os.system("cls || clear")

maiorIdade = 0
menorIdade = sys.maxsize
mulheres5k = 0
somaSalarios = 0
quantidadeSalarios = 0
mediaSalarios = 0

while True:
    os.system("cls || clear")
    print("Código \t Descrição")
    print("1 \t Adicionar pessoa")
    print("2 \t Exibir resultados e sair")
    opcao = int(input("Digite a opção desejada: "))
   
    match(opcao):
        case 1:
            os.system("cls || clear")
            print("=== Solicitando dados ===")

            while True:
                idade = int(input("Digite a idade: "))
                if idade < 0:
                    print("A idade precisa ser maior que zero. \n")
                else:
                    break

            while True:
                sexo = input("Digite o sexo (M ou F): ")
                sexo = sexo.upper()
               
                if sexo != "M" and sexo != "F":
                    print("O sexo precisa ser M ou F. \n")
                else:
                    break

            while True:
                salario = float(input("Digite o salário: "))
                if salario < 0:
                    print("O salário precisa ser maior que zero. \n")
                else:
                    break
           
            somaSalarios += salario
            quantidadeSalarios += 1
   
            maiorIdade = max(idade, maiorIdade)
            menorIdade = min(idade, menorIdade)

            if sexo == "F" and salario >= 5000:
                mulheres5k += 1

            if quantidadeSalarios != 0:
                mediaSalarios = somaSalarios / quantidadeSalarios
       
        case 2:
            os.system("cls || clear")
            print("=== Mostrando resultados ===")
            print(f"Média de salários do grupo: R$ {mediaSalarios:.2f}")
            print(f"Maior idade do grupo: {maiorIdade}")
            print(f"Menor idade do grupo: {menorIdade}")
            print(f"Mulheres com salário a partir de 5 mil: {mulheres5k}")
            break
        case _:
            print("Opção inválida. \nTente novamente.")
import os
import sys
os.system("cls || clear")

# Função para cadastrar um novo funcionário
def cadastrar_funcionario(funcionarios):
    nome = input("Digite o nome do funcionário: ")
    cpf = input("Digite o CPF do funcionário: ")
    funcionario = {
        'nome': nome,
        'cpf': cpf,
        'data_admissao': None,
        'data_demissao': None,
        'ferias_agendadas': []
    }
    funcionarios.append(funcionario)
    print("\nFuncionário cadastrado com sucesso!")
    input("Digite qualquer tecla para continuar...")

# Função para registrar a admissão de um funcionário
def registrar_admissao(funcionarios):
    cpf = input("Digite o CPF do funcionário: ")
    encontrado = False
    for func in funcionarios:
        if func['cpf'] == cpf:
            data_admissao = input("Digite a data de admissão (DD/MM/AAAA): ")
            func['data_admissao'] = data_admissao
            print(f"Admissão de {func['nome']} registrada em {data_admissao}.")
            input("Digite qualquer tecla para continuar...")
            encontrado = True
            break
    if not encontrado:
        print("Funcionário não encontrado.")
        input("Digite qualquer tecla para continuar...")

# Função para registrar a demissão de um funcionário
def registrar_demissao(funcionarios):
    cpf = input("Digite o CPF do funcionário: ")
    encontrado = False
    for func in funcionarios:
        if func['cpf'] == cpf:
            data_demissao = input("Digite a data de demissão (DD/MM/AAAA): ")
            func['data_demissao'] = data_demissao
            print(f"Demissão de {func['nome']} registrada em {data_demissao}.")
            input("Digite qualquer tecla para continuar...")
            encontrado = True
            break
    if not encontrado:
        print("Funcionário não encontrado.")
        input("Digite qualquer tecla para continuar...")

# Função para agendar férias para um funcionário
def agendar_ferias(funcionarios):
    cpf = input("Digite o CPF do funcionário: ")
    encontrado = False
    for func in funcionarios:
        if func['cpf'] == cpf:
            inicio = input("Digite a data de início das férias (DD/MM/AAAA): ")
            fim = input("Digite a data de término das férias (DD/MM/AAAA): ")
            func['ferias_agendadas'].append((inicio, fim))
            print(f"Férias de {func['nome']} agendadas de {inicio} até {fim}.")
            input("Digite qualquer tecla para continuar...")
            encontrado = True
            break
    if not encontrado:
        print("Funcionário não encontrado.")
        input("Digite qualquer tecla para continuar...")

# Função para exibir os dados de um funcionário
def exibir_dados(funcionarios):
    cpf = input("Digite o CPF do funcionário: ")
    encontrado = False
    for func in funcionarios:
        if func['cpf'] == cpf:
            print(f"Nome: {func['nome']}")
            print(f"CPF: {func['cpf']}")
            if func['data_admissao']:
                print(f"Data de admissão: {func['data_admissao']}")
            else:
                print("Funcionário não admitido.")
            if func['data_demissao']:
                print(f"Data de demissão: {func['data_demissao']}")
            if func['ferias_agendadas']:
                print("Férias agendadas:")
                for inicio, fim in func['ferias_agendadas']:
                    print(f"- De {inicio} até {fim}")
                    input("Digite qualquer tecla para continuar...")
            else:
                print("Nenhuma férias agendadas.")
                input("Digite qualquer tecla para continuar...")
            encontrado = True
            break
    if not encontrado:
        print("Funcionário não encontrado.")
        input("Digite qualquer tecla para continuar...")

# Função para exibir o menu de opções
def exibir_menu():
    os.system("cls || clear")
    print("\n===== Sistema de Recursos Humanos =====")
    print("1 - Cadastrar novo funcionário")
    print("2 - Registrar admissão de funcionário")
    print("3 - Registrar demissão de funcionário")
    print("4 - Agendar férias para funcionário")
    print("5 - Exibir dados de um funcionário")
    print("6 - Sair do sistema")
    opcao = input("\nEscolha uma opção: ")
    return opcao

# Função principal que controla o fluxo do programa
def main():
    funcionarios = []

    while True:
        opcao = exibir_menu()

        if opcao == '1':
            cadastrar_funcionario(funcionarios)

        elif opcao == '2':
            registrar_admissao(funcionarios)

        elif opcao == '3':
            registrar_demissao(funcionarios)

        elif opcao == '4':
            agendar_ferias(funcionarios)

        elif opcao == '5':
            exibir_dados(funcionarios)

        elif opcao == '6':
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida. Escolha novamente.")
            input("Digite qualquer tecla para continuar...")

if __name__ == "__main__":
    main()
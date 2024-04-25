# Elabore um algoritmo para receber o login e senha de um usuário.
# Caso o usuário e a senha estejam corretos, mostre a mensagem "Bem-vindo!"
# Caso contrário, mostre a mensagem "Login ou senha inválidos"

import os
os.system("cls || clear")

# Variáveis

usuarioCadastrado:str
usuarioAcesso: str
senhaCadastrada:int
senhaAcesso:int

# Solicitando dados

print("=== INSIRA OS DADOS SOLICITADOS PARA CADASTRO ===\n")

usuarioCadastrado = str(input("Digite o login: "))
senhaCadastrada = int(input("Digite a senha: "))

os.system("cls || clear")

print("=== INSIRA OS DADOS PARA ACESSO AO SISTEMA ===\n")

usuarioAcesso = str(input("Digite o login: "))
senhaAcesso = int(input("Digite a senha: "))

# Testando a senha

if usuarioCadastrado == usuarioAcesso and senhaCadastrada == senhaAcesso:
    print("Bem-vindo!")

else:
    print("Login e/ou senha inválido(s).")

print("\n=== FIM ===")

import os

os.system("cls || clear")

TAM=3
notas = []
media:float = 0
resultado:str
nota:float = 0

def calcular_media(notas):
    soma:float = 0
    for i in range(TAM):
        soma=soma+notas[i]
    media = soma / TAM
    return media

def verificar_situacao(media):
    if media >=7:  
        resultado = "Aprovado"
    else:
        resultado = "Reprovado"
    return resultado

def mostrar_resultado():
    print(f"Média: {calcular_media(notas):.2f}")
    print(f"Resultado: {verificar_situacao(media)}")


for i in range(TAM):
     nota=float(input(f"Digite a {i+1}ª nota: "))
     notas.append(nota)

mostrar_resultado()



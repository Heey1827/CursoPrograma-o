# DESAFIO 1: Analise de triangulos

print("Digite os lados do triangulo:")
lado1 = float(input("Lado 1: "))
lado2 = float(input("Lado 2: "))
lado3 = float(input("Lado 3: "))


def verificar_triangulo(lado1, lado2, lado3):
    if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
        if lado1 == lado2 == lado3:
            return "O triangulo é equilátero."
        elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
            return "O triangulo é isósceles."
        else:
            return "O triangulo é escaleno."
    else:
        return "Os lados fornecidos não formam um triangulo."

print(verificar_triangulo(lado1, lado2, lado3))

# DESAFIO 2 - Multiplicação até dez

print("\nDigite um número para ver sua tabuada de multiplicação até 10:")
print("Digite um número:")
numero = int(input())

def tabuada(numero):
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")
print(tabuada(numero))

# DESAFIO 3 - Dicionario com nomes e notas dos alunos

print ("\nDigite o nome e a nota de 5 alunos:")
alunos = {}
notas = []
for i in range(5):
    nome = input(f"Nome do aluno {i + 1}: ")
    nota = float(input(f"Nota do aluno {i + 1}: "))
    alunos[nome] = nota
    notas.append(nota)

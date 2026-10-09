# DESAFIOS 1 - 10

#  MENU
print("\n<---DESAFIOS 1 - 10--->")
print("1 - Analise de triangulo")
print("2 - Tabuada")
print("3 - Media de notas")
print("4 - Quadrado de um numero")
print("5 - Calculo de IMC")

i = int(input("Digite o numero do desafio que deseja executar: "))

if i == 1:
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
elif i == 2:
    # DESAFIO 2 - Multiplicação até dez

    print("\nDigite um número para ver sua tabuada de multiplicação até 10:")
    print("Digite um número:")
    numero = int(input())

    def tabuada(numero):
        for i in range(1, 10):
            resultado = numero * i
            print(f"{numero} x {i} = {resultado}")
    print(tabuada(numero))
elif i == 3:
    #DESAFIO 3 - Verificar a media de notas de cada aluno e retornar se foi aprovado ou reprovado

    alunos = {}

    def dicionario_alunos():
        while True:
            nome = input("digite o nome do aluno ou 'sair' para encerrar): ")
            if nome == "sair":
                break
            nota = float(input(f"Digite a nota de {nome}: "))
            nota2 = float(input(f"Digite a segunda nota de {nome}: "))
            nota3 = float(input(f"Digite a terceira nota de {nome}: "))
            nota4 = float(input(f"Digite a quarta nota de {nome}: "))
            media = (nota + nota2 + nota3 + nota4) / 4
            alunos[nome] = media

    def media (alunos):
        if not alunos:
            return 0
        s_n = sum(alunos.values())
        return s_n / len(alunos)

    def verificar(alunos):
        for nome, media in alunos.items():
            if media >= 7:
                print(f"{nome} foi aprovado com média {media:.2f}.")
            else:
                print(f"{nome} foi reprovado com média {media:.2f}.")
    print("Digite os nomes e notas dos alunos:")
    dicionario_alunos()
    verificar(alunos)
elif i == 4:
    # DESAFIO 4 - Calcular o quadrado de um numero

    print("\nDigite um número para calcular seu quadrado:")
    numero = float(input())

    def quadrado(numero):
            return numero ** 2

    print(f"O quadrado de {numero} é {quadrado(numero)}.")
from random import randint


def geraMatrizes(n):
    matriz = []

    for _ in range(n):
        linha = []
        for _ in range(n):
            numero_aleatorio = randint(0, 10)
            linha.append(numero_aleatorio)

        matriz.append(linha)

    return matriz


def geraMatrizesContadorInstrucoes(n):
    quantidade_instrucoes = 0

    matriz = []
    quantidade_instrucoes += 1

    for _ in range(n):
        linha = []
        quantidade_instrucoes += 1

        for _ in range(n):
            numero_aleatorio = randint(0, 10)
            quantidade_instrucoes += 1

            linha.append(numero_aleatorio)
            quantidade_instrucoes += 1

        matriz.append(linha)
        quantidade_instrucoes += 1

    return quantidade_instrucoes


for i in range(3, 101):
    print(i)
    quantidade_instrucoes = geraMatrizesContadorInstrucoes(i)
    print(quantidade_instrucoes)

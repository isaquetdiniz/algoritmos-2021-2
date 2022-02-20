
matriz1 = [[2, 3], [3, 4]]
matriz2 = [[1, 1], [1, 1]]


def multiplicaMatrizes(matriz1, matriz2):
    matriz_resultante = []

    for i in range(len(matriz1)):
        linha_resultante = []

        for j in range(len(matriz1[i])):
            resultado = matriz1[i][j] * matriz2[i][j]

            linha_resultante.append(resultado)

        matriz_resultante.append(linha_resultante)

    return matriz_resultante


def multiplicaMatrizesContadorInstrucoes(matriz1, matriz2):
    quantidade_instrucoes = 0

    matriz_resultante = []
    quantidade_instrucoes += 1

    for i in range(len(matriz1)):
        linha_resultante = []
        quantidade_instrucoes += 1

        for j in range(len(matriz1[i])):
            resultado = matriz1[i][j] * matriz2[i][j]
            quantidade_instrucoes += 1

            linha_resultante.append(resultado)
            quantidade_instrucoes += 1

        matriz_resultante.append(linha_resultante)
        quantidade_instrucoes += 1

    return quantidade_instrucoes


print(multiplicaMatrizes(matriz1, matriz2))
print(multiplicaMatrizesContadorInstrucoes(matriz1, matriz2))

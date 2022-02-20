
matriz1 = [[2, 3], [3, 4]]
matriz2 = [[1, 1], [1, 1]]


def multiplicaMatrizes(matriz1, matriz2):
    matriz_resultante = len(matriz1) * []

    for i in range(len(matriz1)):
        linha_resultante = len(matriz1) * []

        for j in range(len(matriz1[i])):
            resultado = matriz1[i][j] * matriz2[i][j]
            print(i)
            print(j)
            linha_resultante[i] = resultado

        matriz_resultante.append(linha_resultante)

    print(matriz_resultante)


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

    print(matriz_resultante)
    quantidade_instrucoes += 1

    print(quantidade_instrucoes)


multiplicaMatrizes(matriz1, matriz2)
multiplicaMatrizesContadorInstrucoes(matriz1, matriz2)

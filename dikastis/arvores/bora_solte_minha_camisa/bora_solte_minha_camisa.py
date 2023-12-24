class Node:
    def __init__(self, valor):
        self.valor = valor
        self.pai = None
        self.direita = None
        self.esquerda = None

class Arvore:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        item = Node(valor)

        if self.raiz == None:
            self.raiz = item
        
        else:
            adicionado = False
            itemAtual = self.raiz
            while not adicionado:
                if itemAtual.valor < item.valor:
                    if itemAtual.direita == None:
                        itemAtual.direita = item
                        item.pai = itemAtual
                        adicionado = True
                    else:
                        itemAtual = itemAtual.direita
                else:
                    if itemAtual.esquerda == None:
                        itemAtual.esquerda = item
                        item.pai = itemAtual
                        adicionado = True
                    else:
                        itemAtual = itemAtual.esquerda
    
    def buscaCulpado(self):
        root = self.raiz
        root_value = root.valor
        esquerda = root.esquerda
        menor = 0

        while esquerda:
            menor = esquerda.valor
            esquerda = esquerda.esquerda

        print(f'{menor} puxou a camisa de {root_value}')


arvore = Arvore()

input_string = input()

numbers_string = input_string.split()

for num_string in numbers_string:
    num = int(num_string)

    arvore.inserir(num)

arvore.buscaCulpado()
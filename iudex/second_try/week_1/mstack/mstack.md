# MStack

Uma pilha é um tipo abstrato de dado e estrutura de dados baseado no princípio de Last In First Out (LIFO), ou seja "o último que entra é o primeiro que sai" caracterizando um empilhamento de dados. Pilhas são fundamentalmente compostas por duas operações: push que adiciona um elemento no topo da pilha e pop que remove o último elemento adicionado. Seu objetivo é desenvolver um tipo diferente de pilha, a qual é composta pelas seguintes operações:

- **push x** : Insere um novo elemento.
- **getMax** : Consulta o maior elemento da pilha.
- **getMin** : Consulta o menor elemento da pilha.
- **pop** : Remove o elemento no topo da pilha.

## Input Specification

- Um inteiro N , indicando a quantidade de comandos.
- Comando 1
- Comando 2
- ...
- Comando N

## Output Specification

- Após o comando getMax, imprima um inteiro N tal que N é o maior elemento da pilha.
- Após o comando getMin, imprima um inteiro N tal que N é o menor elemento da pilha.
- Após o comando pop, imprima um inteiro N tal que N é o elemento no topo da pilha.
- Caso a pilha se encontre vazia durante alguma operação, imprima "empty stack".

| Input | Output |
| ------ | ----- |
| 12     | 3     |
| push 3 | 2     |
| push 2 | 1     |
| getMax | 3     |
| push 2 | 1     |
| getMin | 15    |
| push 1 |       |
| getMin |       |
| getMax |       |
| push 10 |      |
| getMin |       |
| push 15 |      |
| getMax |       |
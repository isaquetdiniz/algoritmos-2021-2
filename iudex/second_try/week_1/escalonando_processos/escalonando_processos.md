# Escalonando Processos

Uma das partes mais cruciais nos sistemas operacionais é a forma que o sistema escalona o tempo de execução para um processo. Em outras palavras, é como o SO divide o tempo que o processador vai executar um certo programa.

Você será encarregado de, ao receber uma lista de Processos, agenda-los em uma linha de execução e executa-los de acordo com o tempo que o processador disponibilizar. Um processo termina de executar quando seu tempo requerido chega à zero. Cada processo tem um id e um tempo requerido. Ao fim de cada execução, você deve informar quantos processos ainda estão na linha de execução.

A primeira linha do Input será sempre um inteiro N que diz o número de comandos que serão enviados.

Comandos:
- ADD ID T -> Insere uma música de id ID e tempo requerido T.
- EXE D -> O processador disponibiliza D segundos para a execução.

OBS:
1. Os processos são executados de acordo com a frente da linha de execução.
2. Se um processo não terminou a execução, ele deve ser enviado para o fim da linha de execução, com o seu tempo requerido atualizado.
3. Todos os processos, ao serem agendados, devem ser enviados para o fim da linha de execução.
4. Se sobrar tempo disponibilizado e o atual processo na frente da linha finalizar, o próximo da linha deve ser executado, até que a linha esteja vazia ou o tempo disponibilizado finalize.

## Input Specification

- N
- Comando 1
- Comando 2
- ...
- Comando N

## Output Specification

- Após o comando ADD, imprimir: "O programa P foi agendado com sucesso!" onde P é o id do programa agendado.
- Após o comando EXE, imprimir:
- "O programa P executou por T segundos.", onde P é o id do programa executado, e T o tempo que ele executou.
- Se o programa finalizar após a execução, imprima "O programa P terminou.", onde P é o id do programa executado.
- Após o fim da execução, imprima "A linha possui S programas.", onde S é o número de programas na linha de execução.

## Notes

| Nº comando   | COMANDO    | LINHA (ID, TEMPO)     |
| -------------| ---------  | -----------------     |
| 1            | ADD 0 10   | (0,10)                |
| 2            | ADD 1 15   |(1,15)->(0,10)         |
| 3            | ADD 2 8    | (2,8)->(1,15)->(0,10) |
| 4            | EXE 22     | (1,3)->(2,8)          |
| 5            | ADD 3 18   | (3,18)->(1,3)->(2,8)  |
| 6            | EXE 18     | (3,11)                |

Saída:

1. ADD 0 10
O programa 0 foi agendado com sucesso!

2. ADD 1 15
O programa 1 foi agendado com sucesso!

3. ADD 2 8
O programa 2 foi agendado com sucesso!

4. EXE 22
O programa 0 executou por 10 segundos.
O programa 0 terminou.
O programa 1 executou por 12 segundos.
A linha possui 2 programas.

5. ADD 3 18
O programa 3 foi agendado com sucesso!

6. EXE 18
O programa 2 executou por 8 segundos.
O programa 2 terminou.
O programa 1 executou por 3 segundos.
O programa 1 terminou.
O programa 3 executou por 7 segundos.
A linha possui 1 programas.

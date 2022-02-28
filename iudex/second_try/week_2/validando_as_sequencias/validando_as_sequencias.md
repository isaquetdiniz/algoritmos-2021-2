# Validando as Sequencias

Crie um programa que recebe duas sequências numéricas positivas, onde a primeira sequência está ordenada, e retorna duas sequências: T, que é formada pelos números da 2ª sequência que estão contidos na 1ª e F, formada pelos numeros da 2ª sequência que não estão contidos na 1ª.

## Input Specification

- S[1] S[2] S[3] ... S[x]
- N[1] N[2] N[3] ... N[y]

### Notes

- len(S,N) <= 100000

## Output Specification

- T[1] T[2] T[3] ... T[z]
- F[1] F[2] F[3] ... F[w]

| Input | Output |
| ----- | ------ |
| 3 4 5 7 12 13 15 16 17 19 | 4 5 7 12 15 16 17 |
| 1 4 5 7 9 10 12 15 16 17 | 1 9 10             |
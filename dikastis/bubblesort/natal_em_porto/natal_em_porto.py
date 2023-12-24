def bubblesort(list, pos = None):
    size = len(list)

    for i in range(size -1, 0, -1):
        for j in range(i):
            if pos:
                if list[j][pos] > list[j+1][pos]:
                    change(list, j, j+1)
            else:
                if list[j] > list[j+1]:
                    change(list, j, j+1)

def change(list, i, j):
    temp = list[i]
    list[i] = list[j]
    list[j] = temp

num_lines = int(input())

squares = []

for i in range(num_lines):
    line = input()

    [square_informations, peoples_string] = line.split(":")
    [square_name, square_number_string] = square_informations.split()

    square_number = int(square_number_string)
    peoples = peoples_string.split()

    squares.append((square_number, peoples))


bubblesort(squares, 0)

for square in squares:
    bubblesort(square[1])

for square in squares:
    square_pos = square[0]
    peoples = square[1]
    peoples_string = ' '.join(peoples)

    print(f'Praça {square_pos}: {peoples_string}')
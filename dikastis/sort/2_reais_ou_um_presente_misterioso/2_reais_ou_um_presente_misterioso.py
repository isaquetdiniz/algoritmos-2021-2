def selection_sort(list):
    size = len(list)

    for i in range(size):
        min = i
        for j in range(i + 1, size):
            if list[min] > list[j]:
                min = j

        change(list, i, min)

def insertion_sort(list):
    size = len(list)

    for i in range(1, size):
        aux = list[i]
        j = i - 1

        while j >= 0 and list[j] > aux:
            list[j+1] = list[j]
            j -= 1
            list[j+1] = aux

def shell_sort(list):
    size = len(list)
    h = 1

    while h < size // 3:
        h = (3*h) + 1

    while h >= 1:
        for i in range(h, size):
            j = i
            while j >= h and list[j] < list[j - h]:
                change(list, j, j - h)
                j -= h

        h = h // 3

def merge_sort(list):
    size = len(list)

    aux = list.copy()

    k = 1
    while k < size:
        for left in range(0, size - k, 2 * k):
            merge(list, aux, left, left + k - 1, min(left + (2*k) - 1, size -1))
        k *= 2

    del aux

def merge(list, list_copy, left, middle, right):
    i = left
    j = middle + 1

    for k in range(left, right + 1):
        list_copy[k] = list[k]
    for k in range(left, right + 1):
        if i > middle:
            list[k] = list_copy[j]
            j += 1
        elif j > right:
            list[k] = list_copy[i]
            i += 1
        elif list_copy[i] > list_copy[j]:
            list[k] = list_copy[j]
            j += 1
        else:
            list[k] = list_copy[i]
            i += 1

def quick_sort(list):
    size = len(list)

    qs(list, 0, size - 1)

def qs(list, left, right):
    if left > right: return

    p = partition(list, left, right)

    qs(list, left, p - 1)
    qs(list, p + 1, right)

def partition(list, left, right):
    pivot = list[left]
    i = left
    j = right + 1

    while True:
        i += 1
        while i < len(list) and list[i] < pivot:
            if i >= right: break
            i += 1

        j -= 1
        while j < len(list) and list[j] > pivot:
            if j <= left: break
            j -= 1

        if i >= j: break
        change(list, i, j)

    change(list, left, j)
    return j

def change(list, i, j):
    temp = list[i]
    list[i] = list[j]
    list[j] = temp

quantity_lines = 3

numbers = []
sort_type = ''

for i in range(quantity_lines):
    input_string = input()

    if i == 0:
        numbers_string = input_string.split(',')

        for ch in numbers_string:
            number = int(ch)
            numbers.append(number)

    if i == 1:
        sort_type = input_string

    if i == 2:
        if input_string == 'dobre!':
            numbers = [number * 2 for number in numbers]

        if input_string == 'não dobre!':
            pass

if sort_type == 'Insertion Sort':
    insertion_sort(numbers)

if sort_type == 'Quick Sort':
    quick_sort(numbers)

if sort_type == 'Merge Sort':
    merge_sort(numbers)

if sort_type == 'Shell Sort':
    shell_sort(numbers)

if sort_type == 'Selection Sort':
    selection_sort(numbers)

print(numbers)
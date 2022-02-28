import sys


def binary_search(size, list, item_to_search):
    start = 0
    end = size - 1

    while start <= end:
        middle = (end + start) // 2

        if list[middle] > item_to_search:
            end = middle - 1
        elif list[middle] < item_to_search:
            start = middle + 1
        else:
            return True

    return False


def main():
    lists = []
    quantity_numbers = 0

    for line in sys.stdin:
        line_splited = line[:-2].split(" ")

        line_numbers = []

        for ch in line_splited:
            number = int(ch)
            quantity_numbers += 1

            line_numbers.append(number)

        lists.append(line_numbers)

    numbers_exists = ''
    numbers_not_exists = ''

    for num in lists[1]:
        if binary_search(quantity_numbers, lists[0], num):
            numbers_exists += '{} '.format(str(num))
        else:
            numbers_not_exists += '{} '.format(str(num))

    print(numbers_exists[:-1])
    print(numbers_not_exists[:-1])


if __name__ == '__main__':
    main()

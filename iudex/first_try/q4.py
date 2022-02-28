def main():
    numbers_in_string = input()

    numbers_in_string_splited = numbers_in_string.split(' ')

    list_numbers = []

    for number_in_string in numbers_in_string_splited:
        if(number_in_string == ''): continue
        number = int(number_in_string)

        list_numbers.append(number)

    numbers_in_string_to_search = input()

    numbers_in_string_to_search_splited = numbers_in_string_to_search.split(' ')

    stringao = ''

    for number_in_string_to_search in numbers_in_string_to_search_splited:
        if(number_in_string_to_search == ''): continue
        number_to_search = int(number_in_string_to_search)

        list_numbers_size = len(list_numbers)
        end = list_numbers_size - 1
        begining = 0

        while begining <= end:
            middle_position = (begining + end) // 2

            middle_number = list_numbers[middle_position]

            if number_to_search == middle_number:
                break

            if number_to_search < middle_number:
                end = middle_position - 1

            if number_to_search > middle_number:
                begining = middle_position + 1

        if(begining > end): number_in_string_to_search = '0'

        stringao += number_in_string_to_search

    print(stringao)


if __name__ == '__main__':
    main()

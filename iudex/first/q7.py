def main():
    class Product:
        def __init__(self, product_price, initial_position):
            self.product_price = product_price
            self.initial_position = initial_position

        def get_product_price(self):
            return self.product_price

        def get_initial_position(self):
            return self.initial_position

    line = input().split(' ')
    total_inputed_products = int(line[0])
    total_combo_products = int(line[1])

    list_inputed_products = [0] * total_inputed_products

    for product_position in range(0, total_inputed_products):
        product_price = int(input()) - 1

        new_product = Product(product_price, str(product_position))

        list_inputed_products[product_position] = new_product

    def partition(alist,first,last):
        pivotvalue = alist[first]

        leftmark = first+1
        rightmark = last

        done = False
        while not done:

            while leftmark <= rightmark and alist[leftmark].get_product_price() <= pivotvalue.get_product_price():
                leftmark = leftmark + 1

            while alist[rightmark].get_product_price() >= pivotvalue.get_product_price() and rightmark >= leftmark:
                rightmark = rightmark -1

            if rightmark < leftmark:
                done = True
            else:
                temp = alist[leftmark]
                alist[leftmark] = alist[rightmark]
                alist[rightmark] = temp

        temp = alist[first]
        alist[first] = alist[rightmark]
        alist[rightmark] = temp


        return rightmark

    def median_better_three(alist, first, middle, last):
        first_element = alist[first].get_product_price()
        middle_element = alist[middle].get_product_price()
        last_element = alist[last].get_product_price()

        if first_element == middle_element:
            return first_element

        if first_element > middle_element:
            if middle_element > last_element:
                return middle
            if middle_element < last_element:
                if last_element > first_element:
                    return first
                if last_element < first_element:
                    return last

        if first_element < middle_element:
            if first_element > last_element:
                return first
            if first_element < last_element:
                if last_element > middle_element:
                    return middle
                if last_element < middle_element:
                    return last

    def quickSortHelper(alist,first,last):
        if first<last:

            m = median_better_three(alist, first, (last - first) // 2, last)
            aux = alist[first]
            alist[first] = alist[m]
            alist[m] = aux

            splitpoint = partition(alist,first,last)

            quickSortHelper(alist,first,splitpoint-1)
            quickSortHelper(alist,splitpoint+1,last)

    def quickSort(alist, n):
        quickSortHelper(alist,0, n - 1)

    quickSort(list_inputed_products, total_inputed_products)

    sum_combo = 0
    products_position_string = ''
    for index in range(total_inputed_products - 1, total_inputed_products - 1 - total_combo_products, -1):
        product = list_inputed_products[index]
        sum_combo += product.get_product_price()
        products_position_string += ' ' + product.get_initial_position()

    print('O combo vai custar {} reais, e os produtos escolhidos foram:{}'.format(sum_combo, products_position_string))


if __name__ == '__main__':
    main()

import numpy as np


class List:
    def __init__(self, max_items):
        self.values = np.empty(max_items, int)
        self.total_items = 0
        self.max_items = max_items

    def is_empty(self):
        return self.total_items == 0

    def value_exists_in_position(self, position, value_to_search):
        values = self.values
        max_items = self.max_items

        if position < max_items and values[position] == value_to_search:
            return True

        return False

    def rank(self, value):
        start = 0
        end = self.max_items - 1
        values = self.values

        while start <= end:
            middle = (end + start) // 2

            if values[middle] > value:
                end = middle - 1
            elif values[middle] < value:
                start = middle + 1
            else:
                return middle

        return start

    def add_item(self, value):
        values = self.values
        position = self.rank(value)

        if self.value_exists_in_position(position, value):
            return

        for j in range(self.max_items - 1, position, -1):
            values[j] = values[j - 1]

        values[position] = value

        self.total_items += 1

    def get_item_by_value(self, value):
        if self.is_empty():
            return None

        values = self.values
        position = self.rank(value)

        if self.value_exists_in_position(position, value):
            return values[position]

        return None

    def print_all_items(self):
        print(self.values)


list = List(10)

for i in range(10, 0, -1):
    list.add_item(i)

list.print_all_items()

print(list.get_item_by_value(30))

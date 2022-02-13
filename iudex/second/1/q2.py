import sys


class Item:
    def __init__(self, value, next_item, before):
        self.value = value
        self.next = next_item
        self.before = before


class Stack:
    def __init__(self):
        self.start = 0
        self.max = -9999999999
        self.min = 9999999999

    def push(self, number):
        if(not self.start):
            new_item = Item(number, 0, 0)
            self.start = new_item
            self.max = new_item.value
            self.min = new_item.value
            return

        if(self.start):
            first_item = self.start

            new_item = Item(number, first_item, 0)

            first_item.before = new_item

            self.start = new_item

            if(self.max < new_item.value):
                self.max = new_item.value

            if(self.min > new_item.value):
                self.min = new_item.value

    def pop(self):
        if(not self.start):
            print('empty stack')
            return

        item_to_pop = self.start
        item_value = item_to_pop.value

        if(item_to_pop.next):
            item_to_pop.next.before = 0
            self.start = item_to_pop.next

            if(item_value == self.max or item_value == self.min):
                max_value = -9999999999
                min_value = 9999999999

                while item_to_pop.next:
                    if(item_to_pop.next.value > max_value):
                        max_value = item_to_pop.next.value

                    if(item_to_pop.next.value < min_value):
                        min_value = item_to_pop.next.value

                    item_to_pop.next = item_to_pop.next.next

                self.max = max_value
                self.min = min_value
        else:
            self.start = 0

        print(item_value)

    def get_max(self):
        if(not self.start):
            print('empty stack')
            return

        print(self.max)

    def get_min(self):
        if(not self.start):
            print('empty stack')
            return

        print(self.min)


def main():
    stack = Stack()

    for line in sys.stdin:
        if('push' in line):
            [_, number_string] = line.split(' ')
            number = int(number_string)

            stack.push(number)

        if('pop' in line):
            stack.pop()

        if('getMax' in line):
            stack.get_max()

        if('getMin' in line):
            stack.get_min()


if __name__ == '__main__':
    main()

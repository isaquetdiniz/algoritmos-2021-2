class Item_Stack:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def has_next(self):
        return self.next != None

    def has_prev(self):
        return self.prev != None

    def __str__(self):
        return f'{self.value}'


class Stack:
    def __init__(self):
        self.start = None
        self.end = None
        self.total_items = 0

    def is_empty(self):
        return self.total_items == 0

    def add_item(self, item):
        item_in_stack = Item_Stack(item)

        if self.is_empty():
            self.start = item_in_stack
            self.end = item_in_stack
            self.total_items += 1
            return

        item_in_stack.prev = self.end
        self.end.next = item_in_stack
        self.end = item_in_stack

        self.total_items += 1

    def pop(self):
        if self.is_empty():
            return None

        item_to_remove = self.end

        if self.total_items == 1:
            self.start = None
            self.end = None
            self.total_items = 0
            return item_to_remove

        item_to_remove.prev.next = None
        self.end = item_to_remove.prev

        self.total_items -= 1
        return item_to_remove

    def print_all_items(self):
        if self.is_empty():
            print('List is empty')
            return

        item = self.start
        list_string = ''

        while item != None:
            if self.start == item:
                list_string += f'S -> {item.value} > '
            elif self.end == item:
                list_string += f'{item.value} <- E'
            else:
                list_string += f'{item.value} > '

            item = item.next

        print(list_string)


stack = Stack()

stack.add_item(2)
stack.add_item(3)
stack.add_item(4)
stack.add_item(5)

stack.print_all_items()

stack.pop()

stack.print_all_items()

stack.pop()

stack.print_all_items()

stack.add_item(10)

stack.print_all_items()

stack.pop()

stack.print_all_items()

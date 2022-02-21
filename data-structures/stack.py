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
        if self.is_empty():
            self.start = item
            self.end = item
            self.total_items += 1
            return

        item.prev = self.end
        self.end.next = item
        self.end = item

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


item_stack1 = Item_Stack(2)
item_stack2 = Item_Stack(3)
item_stack3 = Item_Stack(4)
item_stack4 = Item_Stack(5)
item_stack5 = Item_Stack(10)

stack = Stack()

stack.add_item(item_stack1)
stack.add_item(item_stack2)
stack.add_item(item_stack3)
stack.add_item(item_stack4)

stack.print_all_items()

stack.pop()

stack.print_all_items()

stack.pop()

stack.print_all_items()

stack.add_item(item_stack5)

stack.print_all_items()

stack.pop()

stack.print_all_items()

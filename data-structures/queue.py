class Item_Queue:
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


class Queue:
    def __init__(self):
        self.start = None
        self.end = None
        self.total_items = 0

    def is_empty(self):
        return self.total_items == 0

    def add_item(self, item):
        item_in_queue = Item_Queue(item)

        if self.is_empty():
            self.start = item_in_queue
            self.end = item_in_queue
            self.total_items += 1
            return

        item_in_queue.prev = self.end
        self.end.next = item_in_queue
        self.end = item_in_queue

        self.total_items += 1

    def go(self):
        if self.is_empty():
            return None

        item_to_remove = self.start

        if self.total_items == 1:
            self.start = None
            self.end = None
            self.total_items = 0
            return item_to_remove

        item_to_remove.next.prev = None
        self.start = item_to_remove.next

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


queue = Queue()

queue.add_item(2)
queue.add_item(3)
queue.add_item(4)
queue.add_item(5)

queue.print_all_items()

# print(list.get_item_by_value(2))

queue.go()

queue.print_all_items()

queue.go()

queue.print_all_items()

queue.add_item(10)

queue.print_all_items()

queue.go()

queue.print_all_items()

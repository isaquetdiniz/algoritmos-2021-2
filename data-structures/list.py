class Item_List:
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


class List:
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

    def get_item_by_value(self, value):
        found = None
        item = self.start

        while found is None and item.has_next():
            if item.value == value:
                found = item

            item = item.next

        return found

    def remove_item_by_value(self, value):
        item_to_remove = self.get_item_by_value(value)

        if item_to_remove == None:
            return None

        if self.total_items == 1:
            self.start = None
            self.end = None
            self.total_items = 0
            return item_to_remove

        if item_to_remove.has_next() and item_to_remove.has_prev():
            item_to_remove.prev.next = item_to_remove.next
            item_to_remove.next.prev = item_to_remove.prev

        elif item_to_remove.has_next():
            item_to_remove.next.prev = item_to_remove.prev
            if self.start == item_to_remove:
                self.start = item_to_remove.next

        elif item_to_remove.has_prev():
            item_to_remove.prev.next = item_to_remove.next
            if self.end == item_to_remove:
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


item_list1 = Item_List(2)
item_list2 = Item_List(3)
item_list3 = Item_List(4)
item_list4 = Item_List(5)
item_list5 = Item_List(10)

list = List()

list.add_item(item_list1)
list.add_item(item_list2)
list.add_item(item_list3)
list.add_item(item_list4)

list.print_all_items()

# print(list.get_item_by_value(2))

list.remove_item_by_value(2)

list.print_all_items()

list.remove_item_by_value(4)

list.print_all_items()

list.add_item(item_list5)

list.print_all_items()

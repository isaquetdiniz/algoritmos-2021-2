def main():
    class Item:
        def __init__(self, name):
            self.name = name
            self.previous_item = None
            self.next_item = None

        def get_name(self):
            return self.name

        def get_next_item(self):
            return self.next_item

        def update_previous_item(self, previous_item):
            self.previous_item = previous_item

        def update_next_item(self, next_item):
            self.next_item = next_item

    class Belt:
        def __init__(self, code):
            self.code = code
            self.first_item = None
            self.last_item = None
            self.previous_belt = None
            self.next_belt = None

        def get_code(self):
            return self.code

        def get_next_belt(self):
            return self.next_belt

        def get_first_item(self):
            return self.first_item

        def update_previous_belt(self, previous_belt):
            self.previous_belt = previous_belt

        def update_next_belt(self, next_belt):
            self.next_belt = next_belt

        def add_item(self, item):
            item_name = item.get_name()
            belt_code = self.code

            last_item = self.last_item

            item_added_message = 'O produto: "{}" foi adicionado na esteira {}.'.format(item_name, belt_code)

            if last_item == None:
                self.last_item = item
                self.first_item = item
                print(item_added_message)
                return self

            item.update_previous_item(last_item)

            last_item.update_next_item(item)

            self.last_item = item

            print(item_added_message)
            return self

        def add_item_without_message(self, item):
            item_name = item.get_name()
            belt_code = self.code

            last_item = self.last_item

            if last_item == None:
                self.last_item = item
                self.first_item = item
                return self

            item.update_previous_item(last_item)

            last_item.update_next_item(item)

            self.last_item = item

            return self

        def remove_item(self):
            first_item = self.first_item

            belt_code = self.code

            if first_item == None:
                print('Nao ha produtos para empacotar na esteira {}!'.format(belt_code))
                return self

            item_name = first_item.get_name()

            item_removed_message = 'O produto: "{}" foi empacotado com sucesso!'.format(item_name)

            new_first_item = first_item.get_next_item()

            if new_first_item == None:
                self.first_item = None
                self.last_item = None
                print(item_removed_message)
                print('A esteira {} ficou vazia...'.format(belt_code))
                return self

            new_first_item.update_previous_item(None)

            self.first_item = new_first_item

            print(item_removed_message)

            return self

        def remove_item_without_message(self):
            first_item = self.first_item

            item_name = first_item.get_name()
            new_first_item = first_item.get_next_item()

            if new_first_item == None:
                self.first_item = None
                self.last_item = None
                return self

            new_first_item.update_previous_item(None)

            self.first_item = new_first_item

            return self

        def is_empty(self):
            return self.first_item == None and self.last_item == None

        def show_items(self):
            belt_code = self.code

            first_item = self.first_item

            if first_item == None:
                print('Esteira {}:'.format(belt_code))
                print('')
                return self

            first_item_next_item = first_item.get_next_item()

            items_message = first_item.get_name()

            while first_item_next_item != None:
                firts_item_next_item_name = first_item_next_item.get_name()
                items_message += ' {}'.format(firts_item_next_item_name)
                first_item_next_item = first_item_next_item.get_next_item()

            print('Esteira {}:'.format(belt_code))
            print(items_message)
            return self

    class Belts_Controller:
        def __init__(self):
            self.first_belt = None
            self.last_belt = None

        def add_belt(self, belt):
            first_belt = self.first_belt

            if first_belt == None:
                self.first_belt = belt
                self.last_belt = belt
                return self

            belt.update_next_belt(first_belt)

            first_belt.update_previous_belt(belt)

            self.first_belt = belt

        def find_belt_by_code(self, code):
            first_belt = self.first_belt
            first_belt_code = first_belt.get_code()

            while first_belt_code != code:
                first_belt = first_belt.get_next_belt()
                first_belt_code = first_belt.get_code()

            return first_belt

        def move_item_between_belts(self, belt_to_remove_item_code, belt_to_add_item_code):
            belt_to_remove_item = self.find_belt_by_code(belt_to_remove_item_code)

            if belt_to_remove_item.is_empty():
                print('Erro ao mover produto.')
                return self

            belt_to_add_item = self.find_belt_by_code(belt_to_add_item_code)

            item_to_add = belt_to_remove_item.get_first_item()

            item_name = item_to_add.get_name()
            belt_code = belt_to_add_item.get_code()

            belt_to_remove_item.remove_item_without_message()

            item_to_add.update_previous_item(None)
            item_to_add.update_next_item(None)

            belt_to_add_item.add_item_without_message(item_to_add)

            print('O produto: "{}" foi movido para a esteira {}.'.format(item_name, belt_code))

    belts_controller = Belts_Controller()
    number_belts = int(input())

    for i in range(number_belts+1):
        new_belt = Belt(i)
        belts_controller.add_belt(new_belt)

    option = input()

    while(option != 'END'):
        if(option.find('INS') != -1):
            option_splited = option.split(' ')

            belt_code = int(option_splited[1])
            item_name = option_splited[2]

            new_item = Item(item_name)

            belt_to_insert_item = belts_controller.find_belt_by_code(belt_code)

            belt_to_insert_item.add_item(new_item)

        if(option.find('RMV') != -1):
            option_splited = option.split(' ')

            belt_code = int(option_splited[1])

            belt_to_remove_item = belts_controller.find_belt_by_code(belt_code)

            belt_to_remove_item.remove_item()

        if(option.find('MOV') != -1):
            option_splited = option.split(' ')

            belt_to_remove_item_code = int(option_splited[1])
            belt_to_add_item_code = int(option_splited[2])

            belts_controller.move_item_between_belts(belt_to_remove_item_code, belt_to_add_item_code)
        if(option.find('SHW') != -1):
            option_splited = option.split(' ')

            belt_code = int(option_splited[1])

            belt_to_show_items = belts_controller.find_belt_by_code(belt_code)

            belt_to_show_items.show_items()

        option = input()

if __name__ == '__main__':
    main()

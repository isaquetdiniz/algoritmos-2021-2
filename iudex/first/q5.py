import sys

def main():
    class Space:
        def __init__(self):
            self.capacity = 100
            self.capacity_used = 0
            self.historic = ''

        def get_historic(self):
            return self.historic

        def get_capacity_used(self):
            return self.capacity_used

        def add_coin(self, quantity_gold_coins):
            self.historic += str(quantity_gold_coins) + ' '

            self.capacity_used += quantity_gold_coins

    class Backpack:
        def __init__(self, name, number_spaces):
            self.name = name
            self.number_spaces = number_spaces
            self.spaces = [None] * self.number_spaces

            for i in range(self.number_spaces):
                self.spaces[i] = Space()

            self.capacity_coins = number_spaces * 100
            self.total_coins = 0
            self.initial_position = 0
            self.final_position = 0

        def update_initial_position(self, initial_position):
            self.initial_position = initial_position

        def update_final_position(self, final_position):
            self.final_position = final_position

        def get_initial_position(self):
            return self.initial_position

        def get_final_position(self):
            return self.final_position

        def get_name(self):
            return self.name

        def get_number_spaces(self):
            return self.number_spaces

        def add_coins(self, position, quantity_gold_coins):
            relative_position = position - self.initial_position

            if quantity_gold_coins > 100:
                return False

            if self.total_coins + quantity_gold_coins > self.capacity_coins:
                return False

            space_to_add_coin = self.spaces[relative_position]
            space_to_add_coin_capacity = space_to_add_coin.get_capacity_used()

            if space_to_add_coin_capacity + quantity_gold_coins > 100:
                return False

            space_to_add_coin.add_coin(quantity_gold_coins)
            self.total_coins += quantity_gold_coins

            if(self.total_coins == self.capacity_coins):
                print('{} esta cheia!'.format(self.name))

            return True

        def get_space_information(self, position, space_to_search):
            relative_position = position - self.initial_position

            space = self.spaces[relative_position]
            space_capacity_used = space.get_capacity_used()

            space_is_full = space_capacity_used == 100

            if space_is_full:
                print('Espaco Cheio!')
                return

            free_space = 100 - space_capacity_used
            space_historic = space.get_historic()

            print('Contem {} espacos restantes.'.format(free_space))
            print(space_historic[:-1])

    class UserBackpacks:
        def __init__(self, quantity_backpacks):
            self.total_spaces = 0
            self.quantity_backpacks = quantity_backpacks
            self.number_backpacks_added = 0
            self.backpacks = [None] * quantity_backpacks

        def add_backpack(self, backpack):
            backpack_capacity = backpack.get_number_spaces()

            self.total_spaces += backpack_capacity

            backpacks_added = self.number_backpacks_added

            if  backpacks_added == 0:
                backpack.update_initial_position(0)
                backpack.update_final_position(backpack_capacity - 1)

                self.backpacks[0] = backpack
                self.number_backpacks_added += 1

                return

            last_backpack = self.backpacks[backpacks_added - 1]
            last_backpack_initial_position = last_backpack.get_initial_position()
            last_backpack_final_position = last_backpack.get_final_position()

            backpack.update_initial_position(last_backpack_final_position + 1)
            backpack.update_final_position(backpack.get_initial_position() + backpack_capacity - 1)

            self.backpacks[backpacks_added] = backpack
            self.number_backpacks_added += 1

        def hash(self, quantity_gold_coins):
            return quantity_gold_coins % self.total_spaces

        def rehash(self, quantity_gold_coins):
            return ((self.hash(quantity_gold_coins) + 100) * (self.hash(quantity_gold_coins))) % self.total_spaces

        def search_backpack(self, position):
            absolute_position = 0
            backpack_index = 0
            backpack_found = self.backpacks[backpack_index]

            while (absolute_position <= position) and (backpack_index < self.quantity_backpacks):
                backpack_found = self.backpacks[backpack_index]
                absolute_position += backpack_found.get_number_spaces()
                backpack_index += 1

            return backpack_found

        def add_gold_coins(self, quantity_gold_coins):
            position = self.hash(quantity_gold_coins)

            backpack = self.search_backpack(position)

            coins_are_add = backpack.add_coins(position, quantity_gold_coins)

            if coins_are_add == True:
                print('Adicionadas em {} na {}.'.format(position, backpack.get_name()))
            else:
                new_position = self.rehash(quantity_gold_coins)

                backpack = self.search_backpack(new_position)

                coins_are_add = backpack.add_coins(new_position, quantity_gold_coins)

                if coins_are_add == True:
                    print('Adicionadas em {} na {}.'.format(new_position, backpack.get_name()))
                else:
                    print('Nao foi possivel adicionar a mochila...')

        def get_space_informations(self, space_to_search):
            backpack = self.search_backpack(space_to_search)
            backpack.get_space_information(space_to_search, space_to_search)

    quantity_backpacks = int(input())
    user_backpacks = UserBackpacks(quantity_backpacks)

    for i in range(quantity_backpacks):
        backpack_name = input()

        if(backpack_name == 'Backpack'):
            new_backpack = Backpack('Backpack', 20)
            user_backpacks.add_backpack(new_backpack)

        if(backpack_name == 'Jewelled Backpack'):
            new_backpack = Backpack('Jewelled Backpack', 22)
            user_backpacks.add_backpack(new_backpack)

        if(backpack_name == 'Winged Backpack'):
            new_backpack = Backpack('Winged Backpack', 24)
            user_backpacks.add_backpack(new_backpack)

        if(backpack_name == 'Ghost Backpack'):
            new_backpack = Backpack('Ghost Backpack', 26)
            user_backpacks.add_backpack(new_backpack)

    for line in sys.stdin:
        command_splited = line.split(' ')

        action, number_in_string = command_splited

        if(action == 'ADD'):
            quantity_gold_coins = int(number_in_string)
            user_backpacks.add_gold_coins(quantity_gold_coins)

        if(action == 'CAP'):
            space_to_search = int(number_in_string)
            user_backpacks.get_space_informations(space_to_search)

if __name__ == '__main__':
    main()

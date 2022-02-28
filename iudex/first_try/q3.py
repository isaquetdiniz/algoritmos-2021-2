def main():
    class Player:
        def __init__(self, name, pontuation):
            self.name = name
            self.pontuation = pontuation
            self.before_player = None
            self.higher_player = None
            self.minor_player = None

        def get_name(self):
            return self.name

        def get_pontuation(self):
            return self.pontuation

        def get_higher_player(self):
            return self.higher_player

        def get_minor_player(self):
            return self.minor_player

        def get_before_player(self):
            return self.before_player

        def update_higher_player(self, higher_player):
            self.higher_player = higher_player

        def update_minor_player(self, minor_player):
            self.minor_player = minor_player

        def update_before_player(self, before_player):
            self.before_player = before_player

    class Pontuation_Table:
        def __init__(self):
            self.rank_first_player = None

        def search_pontuation(self, pontuation):
            if self.rank_first_player == None:
                return None

            actual_player = self.rank_first_player

            while actual_player != None and actual_player.get_pontuation() != pontuation:
                if pontuation < actual_player.get_pontuation():
                    actual_player = actual_player.get_minor_player()
                elif pontuation > actual_player.get_pontuation():
                    actual_player = actual_player.get_higher_player()

            return actual_player

        def add(self, player_name, player_pontuation):
            new_player = Player(player_name, player_pontuation)
            new_player_name = new_player.get_name()
            new_player_pontuation = new_player.get_pontuation()

            actual_player = self.rank_first_player
            if actual_player == None:
                self.rank_first_player = new_player
            else:
                while actual_player != None:
                    before_player = actual_player
                    if new_player_pontuation < actual_player.get_pontuation():
                        actual_player = actual_player.get_minor_player()
                    elif new_player_pontuation > actual_player.get_pontuation():
                        actual_player = actual_player.get_higher_player()
                    else:
                        print('{} ja esta no sistema.'.format(new_player_name))
                        return

                new_player.update_before_player(before_player)

                before_player_pontuation = before_player.get_pontuation()

                if new_player_pontuation < before_player_pontuation:
                    before_player.update_minor_player(new_player)
                elif new_player_pontuation > before_player_pontuation:
                    before_player.update_higher_player(new_player)

            print('{} inserido com sucesso!'.format(new_player_name))
            return self

        def search_sucessor(self, player):
            player_has_higher_player = player.get_higher_player()

            if player_has_higher_player:
                sucessor = player_has_higher_player

                while player_has_higher_player != None:
                    sucessor = player_has_higher_player
                    player_has_higher_player = player_has_higher_player.get_minor_player()

                return sucessor

            before_player = player.get_before_player()

            while before_player != None and player == before_player.get_higher_player():
                player = before_player
                before_player = before_player.get_before_player()

            return before_player

        def search_predecessor(self, player):
            player_has_minor_player = player.get_minor_player()

            if player_has_minor_player:
                predecessor = player_has_minor_player

                while player_has_minor_player != None:
                    predecessor = player_has_minor_player
                    player_has_minor_player = player_has_minor_player.get_higher_player()

                return predecessor

            before_player = player.get_before_player()

            while before_player != None and player == before_player.get_minor_player():
                player = before_player
                before_player = before_player.get_before_player()

            return before_player

        def get_hierarchy(self, pontuation):
            player = self.search_pontuation(pontuation)
            player_name = player.get_name()

            minor_player = player.get_minor_player()
            higher_player = player.get_higher_player()
            before_player = player.get_before_player()

            if minor_player == None and higher_player == None and before_player == None:
                print('Apenas {} existe no sistema...'.format(player_name))
                return

            sucessor = self.search_sucessor(player)
            predecessor = self.search_predecessor(player)

            if sucessor == None:
                print('{} e o maior! e logo atras vem {}'.format(player_name, predecessor.get_name()))
                return

            if predecessor == None:
                print('{} e o menor! e logo apos vem {}'.format(player_name, sucessor.get_name()))
                return

            print('{} vem apos {} e antes de {}'.format(player_name, predecessor.get_name(), sucessor.get_name()))


    pontuation_table = Pontuation_Table()
    number_commands = int(input())

    for command in range(0, number_commands):
        command = input()
        command_splited = command.split(' ')

        if command.find('ADD') != -1:
            player_name = command_splited[1]
            player_pontuation = int(command_splited[2])

            pontuation_table.add(player_name, player_pontuation)

        if command.find('PROX') != -1:
            pontuation = int(command_splited[1])

            pontuation_table.get_hierarchy(pontuation)

if __name__ == '__main__':
    main()

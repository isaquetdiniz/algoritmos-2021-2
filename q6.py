import sys

def main():
    def search_name_in_holy_tree(no, name):
        if no is None:
            return False

        no_name = no.get_name()

        if no_name == name:
            return no

        if no_name > name:
            no_left = no.get_left()
            return search_name_in_holy_tree(no_left, name)

        if no_name < name:
            no_right = no.get_right()
            return search_name_in_holy_tree(no_right, name)

    def calculate_holy_tree_height(no):
        if no is None:
            return 0

        no_left = no.get_left()
        height_left = calculate_holy_tree_height(no_left)

        no_right = no.get_right()
        height_right = calculate_holy_tree_height(no_right)

        if height_left > height_right:
            return height_left + 1
        elif height_left == height_right:
            return height_left + 1
        else:
            return height_right + 1

    def calculate_factor_balancing(no):
        no_left = no.get_left()
        no_right = no.get_right()

        no_left_height = calculate_holy_tree_height(no_left)
        no_right_height = calculate_holy_tree_height(no_right)

        factor_balancing = no_right_height - no_left_height

    def holy_tree_balancing(no):
        factor_balancing = calculate_factor_balancing(no)

        if factor_balancing == 2:
            if no_left.get_factor_balancing() == 1:
                holy_tree_left_rotation()
                factor_balancing = calculate_factor_balancing(no)
            else:
                holy_tree_right_rotation()
                holy_tree_left_rotation()
                factor_balancing = calculate_factor_balancing(no)

        if factor_balancing == -2:
            if no_right.get_factor_balancing() == -1:
                holy_tree_right_rotation()
                factor_balancing = calculate_factor_balancing(no)
            else:
                holy_tree_left_rotation()
                holy_tree_right_rotation()
                factor_balancing = calculate_factor_balancing(no)

        no_parent = no.get_parent()

        no.update_factor_balancing(factor_balancing)

        if no_parent != None:
            return holy_tree_balancing(no_parent)

    def holy_tree_left_rotation(no):
        no_right = no.get_right()
        T2 = no_right.get_left()

        no_right.update_left(no)
        no.update_right(T2)

    def holy_tree_right_rotation(no):
        no_left = no.get_left()
        T3 = no_left.get_right()

        no_left.update_right(no)
        no.update_left(T3)

    def add_name_to_holy_tree(no, new_no):
        no_name = no.get_name()
        new_no_name = new_no.get_name()

        if no_name < new_no_name:
            no_right = no.get_right()

            if no_right is None:
                new_no.update_parent(no)
                no.update_right(new_no)
                holy_tree_balancing(no)
            else:
                add_name_to_holy_tree(no_right, new_no)

        if no_name > new_no_name:
            no_left = no.get_left()

            if no_left is None:
                new_no.update_parent(no)
                no.update_left(new_no)
                holy_tree_balancing(no)
            else:
                add_name_to_holy_tree(no_left, new_no)

    def holy_tree_pre_order(no):
        no_name = no.get_name()

        no_left = no.get_left()
        no_right = no.get_right()

        if no_left != None:
            return holy_tree_pre_order(no_left)

        if no_right != None:
            return holy_tree_pre_order(no_right)

        return no_name

    class No:
        def __init__(self, name):
            self.name = name
            self.parent = None
            self.left = None
            self.right = None
            self.factor_balancing = 0

        def get_name(self):
            return self.name

        def get_left(self):
            return self.left

        def get_right(self):
            return self.right

        def get_parent(self):
            return self.parent

        def get_factor_balancing(self):
            return self.factor_balancing

        def update_right(self, right):
            self.right = right

        def update_left(self, left):
            self.left = left

        def update_parent(self, parent):
            self.parent = parent

        def update_factor_balancing(self, factor_balancing):
            self.factor_balancing = factor_balancing

    class Holy_Tree:
        def __init__(self):
            self.root = None

        def search_name(self, name):
            root = self.root

            if root is None:
                print('A arvore esta vazia...')
                return

            return search_name_in_holy_tree(root, name)

        def add_name(self, name):
            new_no = No(name)
            new_no_name = new_no.get_name()

            if self.root is None:
                self.root = new_no
                print('{} foi adicionado com sucesso!'.format(new_no_name))
                return

            name_exists = self.search_name(new_no_name)

            if name_exists != False:
                print('{} ja existe.'.format(new_no_name))
                return

            add_name_to_holy_tree(self.root, new_no)
            print('{} foi adicionado com sucesso!'.format(new_no_name))

        def smaller_name(self):
            root = self.root

            if root is None:
                print('A arvore esta vazia...')
                return

            smaller = root.get_name()
            left_no = root.get_left()

            while left_no != None:
                smaller = left_no.get_name()
                left_no = left_no.get_left()

            return smaller

        def higher_name(self):
            root = self.root

            if root is None:
                print('A arvore esta vazia...')
                return

            higher = root.get_name()
            right_no = root.get_right()

            while right_no != None:
                higher = right_no.get_name()
                right_no = right_no.get_right()

            return higher

        def get_height(self):
            root = self.root

            if root is None:
                print('A arvore esta vazia...')
                return

            height = calculate_holy_tree_height(root)

            print('A altura da arvore eh: {}'.format(height))

        def pre_order(self):
            root = self.root

            if root == None:
                print('PRE-ORDER DA ARVORE:')
                return

            pre_order_string = ''

            pre_order_string += holy_tree_pre_order(root) + ' '

            print('PRE-ORDER DA ARVORE:', pre_order_string[:-1])

    holy_tree = Holy_Tree()
    number_commands = int(input())

    for i in range(number_commands + 1):
        command = input()

        if command == 'Oh, arvore sagrada, quero adicionar o seguinte nome':
            name = input()

            holy_tree.add_name(name)

        if command == 'Arvore sagrada, gostaria que voce removesse para mim o seguinte nome':
            name = input()

            print('remover da arvore')

        if command == 'Coe planta, qual o menor nome ai?':
            holy_tree.smaller_name()

        if command == 'Salve minha floresta amazonica de uma arvore so, qual o maior nome ai?':
            holy_tree.higher_name()

        if command == 'Nossa, ce ta tao grande, qual tua altura?':
            holy_tree.get_height()

    holy_tree.pre_order()

if __name__ == '__main__':
    main()

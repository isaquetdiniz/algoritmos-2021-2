class Node:
    def __init__(self, value) -> None:
        self._value = value
        self._father = None
        self._right = None
        self._left = None

    def get_value(self):
        return self._value

    def get_father(self):
        return self._father

    def set_father(self, father):
        self._father = father

    def get_right(self):
        return self._right

    def set_right(self, right):
        self._right = right

    def get_left(self):
        return self._left

    def set_left(self, left):
        self._left = left

class BinaryTree:
    def __init__(self) -> None:
        self._root = None
        self.smaller_to_biggest_string = ''

    def get_root(self):
        return self._root

    def add(self, value):
        root = self._root
        new_node = Node(value)

        if not root:
            self._root = new_node
            return

        added = False
        node = root

        while not added:
            new_value = new_node.get_value()
            node_value = node.get_value()

            if new_value < node_value:
                node_left = node.get_left()

                if not node_left:
                    node.set_left(new_node)
                    new_node.set_father(node)
                    added = True
                else:
                    node = node_left
            else:
                node_right = node.get_right()

                if not node_right:
                    node.set_right(new_node)
                    new_node.set_father(node)
                    added = True
                else:
                    node = node_right

    def smaller_to_biggest(self, node):
        if node:
            self.smaller_to_biggest(node.get_left())
            self.smaller_to_biggest_string += f'{str(node.get_value())} '
            self.smaller_to_biggest(node.get_right())


tree = BinaryTree()

input_string = input()

numbers_string = input_string.split()

for number_string in numbers_string:
    number = int(number_string)

    tree.add(number)

tree.smaller_to_biggest(tree.get_root())

print(tree.smaller_to_biggest_string[:-1])

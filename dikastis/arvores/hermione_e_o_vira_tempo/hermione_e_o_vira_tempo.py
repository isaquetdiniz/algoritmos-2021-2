class Node:
    def __init__(self, value):
        self._value = value
        self._father = None
        self._right = None
        self._left = None
        self._balancing_factor = 0

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

    def get_balancing_factor(self):
        return self._balancing_factor

    def set_balancing_factor(self, value):
        self._balancing_factor = value

    def is_balanced(self):
        return self._balancing_factor >= -1 and self._balancing_factor <= 1


class AVLBinaryTree:
    def __init__(self) -> None:
        self._root = None

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


tree = AVLBinaryTree()

total_lines = 4

total_classes = 0
total_hours = 0

for i in range(total_lines):
    input_string = input()

    if i == 0:
        line_splitted = input_string.split()

        for ch in line_splitted:
            total_classes += int(ch)

    if i == 1:
        line_splitted = input_string.split()

        for ch in line_splitted:
            tree.add(int(ch))

    if i == 2:
        line_splitted = input_string.split()

        for ch in line_splitted:
            tree.add(int(ch))

    if i == 3:
        total_hours = int(input_string)

print(total_classes)
print(total_hours)

class Node:
    def __init__(self, value):
        self._value = value
        self._right = None
        self._left = None
        self._balancing_factor = 0

    def get_value(self):
        return self._value

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

    def add(self, value: int):
        new_node = Node(value)
        root = self._root

        if not root:
            self._root = new_node
            return

        self.util_add(new_node, root)

    def util_add(self, new_node: Node, node: Node):
        if not node:
            return new_node

        value = new_node.get_value()
        actual_value = node.get_value()

        if value < actual_value:
            node.set_left(self.util_add(new_node, node.get_left()))

        if value > actual_value:
            node.set_right(self.util_add(new_node, node.get_right()))

        return node

    def pre_order(self):
        node = self._root

        self.util_pre_order(node)

    def util_pre_order(self, node: Node):
        if not node:
            return

        print("{0} ".format(node.get_value(), end=""))

        self.util_pre_order(node.get_left())
        self.util_pre_order(node.get_right())

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

print(tree.pre_order())

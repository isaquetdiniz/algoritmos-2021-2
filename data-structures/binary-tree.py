class No:
    def __init__(self, value):
        self.father = None
        self.left = None
        self.right = None

        self.value = value

    def __str__(self):
        return f'[CHAVE]: {self.value} [ESQUERDA]: {self.left and self.left.value} [DIREITA]: {self.right and self.right.value}'


class BinaryTree:
    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root == None

    def search(self, value):
        no = self.root

        while no != None and value != no.value:
            if value < no.value:
                no = no.left
            else:
                no = no.right

        return no

    def insert_value(self, value):
        new_no = No(value)

        if self.is_empty():
            self.root = new_no
            return

        last_no = None
        no = self.root

        while no != None:
            last_no = no
            if value < no.value:
                no = no.left
            else:
                no = no.right

        new_no.father = last_no

        if value < last_no.value:
            last_no.left = new_no
        else:
            last_no.right = new_no

    def remove_value(self, value):
        pass

    def pre_order(self, no):
        if no != None:
            print(no.value)
            self.pre_order(no.right)
            self.pre_order(no.left)

    def in_order(self, no):
        if no != None:
            self.in_order(no.right)
            print(no.value)
            self.in_order(no.left)

    def pos_order(self, no):
        if no != None:
            self.pos_order(no.right)
            self.pos_order(no.left)
            print(no.value)

    def max_value(self):
        no = self.root

        while no.right != None:
            no = no.right

        return no

    def min_value(self):
        no = self.root

        while no.left != None:
            no = no.left

        return no

    def successor(self, value):
        pass

    def antecessor(self, value):
        pass

    def transplant(self, value):
        pass


tree = BinaryTree()

for i in range(1, 11):
    tree.insert_value(i)

# print(tree.search(7))
# print(tree.min_value())
# print(tree.max_value())


# tree.pre_order(tree.root)
# tree.in_order(tree.root)
# tree.pos_order(tree.root)

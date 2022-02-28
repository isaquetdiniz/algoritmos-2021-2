def tree_height(no):
    if no is None:
        return 0

    no_left = no.get_left()
    height_left = tree_height(no_left)

    no_right = no.get_right()
    height_right = tree_height(no_right)

    if height_left > height_right:
        return height_left + 1
    elif height_left == height_right:
        return height_left + 1
    else:
        return height_right + 1


class No:
    def __init__(self, left = None, right = None):
        self.left = left
        self.right = right

    def get_name(self):
        return self.name

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right
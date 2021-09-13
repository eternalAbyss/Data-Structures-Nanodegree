class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def set_value(self, value=None):
        self.value = value

    def get_value(self):
        return self.value

    def set_left_child(self, value):
        self.left = value

    def set_right_child(self, value):
        self.right = value

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def has_left_child(self):
        return self.left is not None

    def has_right_child(self):
        return self.right is not None


class Tree:
    def __init__(self, value=None):
        self.root = Node(value)

    def get_root(self):
        return self.root


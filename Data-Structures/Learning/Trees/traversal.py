from trees import *

test = Tree(Node(2))
print("Adding element to right")
test.get_root().set_right_child(3)
print(test.get_root().has_right_child())
print(test.get_root().has_left_child())

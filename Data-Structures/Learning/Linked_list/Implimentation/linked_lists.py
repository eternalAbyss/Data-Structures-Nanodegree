class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


head = Node(2)
head.next = Node(1)


def node_insert(head, values):
    cur_node = head
    while cur_node.next is not None:
        cur_node = cur_node.next
    for i in values:
        cur_node.next = Node(i)
        cur_node = cur_node.next
    return None


def print_nodes(head):
    cur_node = head
    while cur_node.next is not None:
        print(cur_node.value)
        cur_node = cur_node.next
    print(cur_node.value)
    return None


def remove_nodes(head):
    pop_value = ''
    while head.next.next is not None:
        head = head.next
    pop_value = head.next.value
    head.next = None
    print(pop_value)


# print_nodes(head)
node_insert(head, [23, 54, 34, 65, 3])
remove_nodes(head)
remove_nodes(head)
print_nodes(head)

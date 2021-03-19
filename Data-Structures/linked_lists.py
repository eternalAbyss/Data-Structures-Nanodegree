class Node:
    def __init__(self, value):
        self.value = value 
        self.next = None 
    
head = Node(2)
head.next = Node(1)

def node_insert(head, values):
    cur_node = head
    while(cur_node.next != None):
        cur_node = cur_node.next
    for i in values:
        cur_node.next = Node(i)
        cur_node = cur_node.next 
    return None 

def printNodes(head):
    cur_node = head
    while(cur_node.next != None):
        print(cur_node.value)
        cur_node = cur_node.next
    print(cur_node.value)
    return None 

printNodes(head)
node_insert(head,[23,54,34,65,3])
printNodes()
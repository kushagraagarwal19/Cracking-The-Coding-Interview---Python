class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

def traverse(head):
    while head is not None:
        print(head.value)
        head = head.next

def deleteMiddle(node):
    if node is None:
        return
    if node.next is None:
        node = None
        return
    nextNode = node
    nextNode = node.next
    node.value = nextNode.value
    node.next = nextNode.next

head = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

head.next= node2
node2.next = node3
node3.next = node4

deleteMiddle(node2)
traverse(head)
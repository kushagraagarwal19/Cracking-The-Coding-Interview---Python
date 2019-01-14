class Node:
    def __init__(self,value):
        self.value = value
        self.nextNode = None

def traverse(head):
    while head is not None:
        print(head.value)
        head = head.nextNode

def delete(head,value):
    if head.value == value:
        head = head.nextNode
        return head
    headN = head
    headP = head
    while headN.value != value and headN is not None:
        headP = headN
        headN = headN.nextNode
    headP.nextNode = headN.nextNode
    return head
head = Node(1)
node2 = Node(2)
node3 = Node(3)

head.nextNode = node2
node2.nextNode = node3

head = delete(head, 1)
traverse(head)
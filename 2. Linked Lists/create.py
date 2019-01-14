class Node:
    def __init__(self,value):
        self.value = value
        self.nextNode = None

def traverse(head):
    while head is not None:
        print(head.value)
        head = head.nextNode

def insertAtHead(head,value):
    newNode = Node(value)
    newNode.nextNode = head
    head = newNode
    return head

def insertAfter(head,valueAfterInsert,valueToInsert):
    headTraverse = head
    newNode = Node(valueToInsert)
    while headTraverse.value != valueAfterInsert:
        headTraverse = headTraverse.nextNode
    newNode.nextNode = headTraverse.nextNode
    headTraverse.nextNode = newNode

head = Node(1)
node2 = Node(2)
node3 = Node(3)

head.nextNode = node2
node2.nextNode = node3
# traverse(head)
# head = insertAtHead(head, 10)
# traverse(head)

insertAfter(head, 1,56)
traverse(head)
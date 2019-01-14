class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

def traverse(head):
    while head is not None:
        print(head.value)
        head = head.next

def addList(h1,h2):
    if h1 is None and h2 is None:
        return None
    sum = 0
    while (h1.next is not None or h2.next is not None):
        sum = h1.value + h2.value
        nodeValue = sum if sum < 10 else sum % 10
        carry = sum//10
        newHead = Node(nodeValue)
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

def traverse(head):
    while head is not None:
        print(head.value)
        head = head.next

# Iterative - First find the length of linkedList and then traverse again till length-n and then print
def nthFromLast(head,n):
    leng = 0
    tempHead = head
    while head is not None:
        head = head.next
        leng += 1
    if leng < n:
        print('Sorry')
        return
    toTraverse = leng - n
    for index in range(toTraverse):
        tempHead = tempHead.next
    print(tempHead.value)

head = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

head.next= node2
node2.next = node3
node3.next = node4

nthFromLast(head,0)
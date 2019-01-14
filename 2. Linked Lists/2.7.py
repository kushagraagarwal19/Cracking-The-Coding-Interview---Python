class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

def traverse(head):
    while head is not None:
        print(head.value)
        head = head.next

def intersection(head1,head2):
    ihead = ''
    list1Len = 0
    list2Len = 0
    origHead1 = head1
    origHead2 = head2
    # Find length of list 1
    while head1 is not None:
        list1Len += 1
        head1 = head1.next
    # Find length of list 2
    while head2 is not None:
        list2Len += 1
        head2 = head2.next

    # now find which list you want to traverse to make the length equal
    traverse = origHead1 if list1Len > list2Len else origHead2
    now = origHead2 if list1Len > list2Len else origHead1
    # traverse until abs(list1Len-list2Len)
    for i in range (abs(list1Len-list2Len)):
        traverse = traverse.next
    
    while traverse is not None:
        if traverse.next == now.next:
            return now.next

head = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
head.next= node2
node2.next = node3
node3.next = node4

head2 = Node(10)
head2.next = node4

newHead = intersection(head,head2)
traverse(newHead)
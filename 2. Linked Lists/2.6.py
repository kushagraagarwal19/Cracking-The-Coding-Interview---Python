class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

def traverse(head):
    while head is not None:
        print(head.value)
        head = head.next

def isListPalindrome(head):
    if head is None:
        return None
    array = []
    while (head is not None):
        array.append(head.value)
        head = head.next
    lenArray = len(array)
    for index in range(0, lenArray// 2):
        if array[index] != array[lenArray-index-1]:
            print ('NotAPalindrome')
            return
    print('APalindrome!!!')

head = Node(1)
node2 = Node(2)
node3 = Node(2)
node4 = Node(2)

head.next= node2
node2.next = node3
node3.next = node4

isListPalindrome(head)
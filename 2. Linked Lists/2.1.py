class Node:
    def __init__(self,value):
        self.value = value
        self.nextNode = None

def traverse(head):
    while head is not None:
        print(head.value)
        head = head.nextNode

# def removeDups(head):
#     if head.nextNode is None:
#         return head
#     hMapList = {}
#     newHead = Node(head.value)
#     newHeadN = newHead
#     hMapList[head.value] = 1
#     head = head.nextNode
#     while head is not None:
#         if head.value not in hMapList:
#             hMapList[head.value] = 1
#             newNode = Node(head.value)
#             newHeadN.nextNode = newNode
#             newHeadN = newNode
#         head = head.nextNode
#     return newHead

def removeDups(head):
    if head.nextNode is None:
        return head
    newHead = head
    prev = head
    hMap = {}
    while newHead is not None:
        if newHead.value in hMap:
            prev.nextNode = newHead.nextNode
        else:
            hMap[newHead.value] = 1
            prev = newHead
        newHead = newHead.nextNode


head = Node(1)
node2 = Node(1)
node3 = Node(1)
node4 = Node(1)

head.nextNode = node2
node2.nextNode = node3
node3.nextNode = node4

removeDups(head)
traverse(head)
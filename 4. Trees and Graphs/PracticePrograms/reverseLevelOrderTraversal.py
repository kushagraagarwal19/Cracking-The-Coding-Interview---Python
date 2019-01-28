# This is reverse
# level order traversal

from collections import deque
class Tree():
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

def reverseLevelOrder(root):
    if root is None:
        return
    queue = deque()
    queue.append(root)
    stack = []
    while len(queue) != 0:
        a = queue.popleft()
        stack.append(a.value)
        if a.left:
            queue.append(a.left)
        if a.right:
            queue.append(a.right)
    for each in stack[::-1]:
        print(each, end = ' ')

root = Tree(10)
node1 = Tree(3)
node2 = Tree(2)
node3 = Tree(5)
root.left = node1
node1.left = node2
node1.right = node3

node4 = Tree(17)
node5 = Tree(15)
node6 = Tree(18)

root.right = node4
node4.left = node5
node4.right = node6

reverseLevelOrder(root)
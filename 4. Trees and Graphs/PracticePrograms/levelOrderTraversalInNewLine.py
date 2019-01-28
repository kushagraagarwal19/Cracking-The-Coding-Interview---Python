# This is level order
# traversal with each level
# printed on a new line

from collections import deque
class Tree():
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

# Here I am goint to use two different techniques
# i)  Using a queue and delimiter
# ii) Using a queue and counters

# i) With delimiter
# This is similar to the normal Level Order Traversal

def levelOrderTraversal(root):

    if root is None:
        return
    queue = deque()
    queue.append(root)
    queue.append('DELIMITER')
    while queue:
        elem = queue.popleft()
        if elem == 'DELIMITER':
            if len(queue) == 0:
                break
            print()
            queue.append('DELIMITER')
        else:
            print(elem.value, end = ' ')
            if elem.left:
                queue.append(elem.left)
            if elem.right:
                queue.append(elem.right)

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

levelOrderTraversal(root)
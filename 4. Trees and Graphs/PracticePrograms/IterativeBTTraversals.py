# This is the DFS traversal
# Inorder, Preorder, Postorder
# traversal of Binary tree
# (iteratively)

class Tree():
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

# We will be using one stack
# to write this
def preOrder(root):
    if root is None:
        return
    stack = []
    stack.append(root)
    while len(stack) != 0:
        a = stack.pop()
        print(a.value, end = ' ')
        if a.right:
            stack.append(a.right)
        if a.left:
            stack.append(a.left)

# We will be using two 
# stacks to write this
def postOrder(root):
    if root is None:
        return
    stack1 = []
    stack2 = []
    stack1.append(root)
    while len(stack1) != 0:
        a = stack1.pop()
        stack2.append(a.value)
        if a.left:
            stack1.append(a.left)
        if a.right:
            stack1.append(a.right)
    for i in stack2[::-1]:
        print(i, end = ' ')

def inOrder(root):
    if root is None:
        return
    stack = []
    while True:
        if root is not None:
            stack.append(root)
            root = root.left
        else:
            if len(stack) == 0:
                break
            root = stack.pop()
            print(root.value, end = ' ')
            root = root.right

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

# preOrder(root)
# postOrder(root)
inOrder(root)
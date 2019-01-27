class Tree():
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

def BSTInsertion(root,key):
    if root is None:
        node = Tree(key)
        return node
    parent = child = root
    while child is not None:
        if child.value > key:
            parent = child
            child = child.left
            continue
        else:
            parent = child
            child = child.right
            continue
    if parent.value > key:
        newNode = Tree(key)
        parent.left = newNode
    else:
        newNode = Tree(key)
        parent.right = newNode
    return parent

def preorder(root):
    if root is None:
        return
    print(root.value, end = ' ')
    preorder(root.left)
    preorder(root.right)

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

BSTInsertion(root, 150)
preorder(root)
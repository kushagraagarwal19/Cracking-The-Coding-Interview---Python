# This is the DFS traversal
# Inorder, Preorder, Postorder
# traversal of Binary tree
# (recursively)

class Tree():
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


def preorder(root):
    if root is None:
        return
    print(root.value, end = ' ')
    preorder(root.left)
    preorder(root.right)

def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.value, end = ' ')
    inorder(root.right)

def postorder(root):
    if root is None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.value, end = ' ')

root = Tree(10)
node1 = Tree(9)
node2 = Tree(8)
root.left = node1
root.right = node2
node3 = Tree(34)
node4 = Tree(78)
node1.right = node3
node2.left = node4

preorder(root)
print()
inorder(root)
print()
postorder(root)
# This is the BST search

class Tree():
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

def BSTSearch(root,key):
    if root is None:
        print('Not Found')
        return
    # if root is None and root.value != key:
    #     print('Not Found')
    #     return
    if root.value == key:
        print('Found')
        return
    if root.value > key:
        BSTSearch(root.left, key)
    if root.value <= key:
        BSTSearch(root.right, key)


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

BSTSearch(root,170)
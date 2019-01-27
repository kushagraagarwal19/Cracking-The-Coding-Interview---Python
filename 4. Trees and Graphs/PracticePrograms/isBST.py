# This program checks if the given Binary Tree
# is the Binary Search Tree or not

class Tree():
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

def isBST(root, minVal, maxVal):
    if root is None:
        return True
    
    if root.value <= minVal or root.value >maxVal:
        return False
    
    leftValue = isBST(root.left, minVal, root.value)
    rightValue = isBST(root.right, root.value, maxVal)
    return leftValue and rightValue

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

maxVal = float('inf')
minVal = float('-inf')

a = isBST(root,minVal,maxVal)
print(a)
class Tree():
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

def heightOfBT(root):
    if root is None:
        return 0
    return 1 + max(heightOfBT(root.left), heightOfBT(root.right))

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

a = heightOfBT(root)
print(a)
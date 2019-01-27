class Tree():
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

def sameBT(root1,root2):
    if root1 is None and root2 is None:
        return True
    if root1 is None or root2 is None:
        return False
    return root1.value == root2.value and \
    sameBT(root1.left, root2.left) and \
    sameBT(root1.right, root2.right)

root = Tree(10)
node1 = Tree(9)
node2 = Tree(8)
root.left = node1
root.right = node2

root2 = Tree(10)
node3 = Tree(90)
node4 = Tree(8)
root2.left = node3
root2.right = node4

a = sameBT(root,root)
print(a)
class Tree():
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

def leveOrderTraversalSpiral(root):
    if root is None:
        return

    stack1 = []
    stack2 = []
    stack1.append(root)
    while stack1 or stack2:
        while stack1:
            a = stack1.pop()
            print(a.value)
            if a.left:
                stack2.append(a.left)
            if a.right:
                stack2.append(a.right)
        while stack2:
            a = stack2.pop()
            print(a.value)
            if a.right:
                stack1.append(a.right)   
            if a.left:
                stack1.append(a.left)
            

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

leveOrderTraversalSpiral(root)
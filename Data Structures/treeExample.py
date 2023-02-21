class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

def insert(root, node):
    if root is None:
        root = node
    else:
        if root.val > node.val:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)
        else:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)

names = ["Jake", "Dom", "Will", "Curran", "Kyle", "Jonathan", "Jamie", "Sam", "Joe", "Nate"]
root = Node(names[0])
for i in range(1, len(names)):
    insert(root, Node(names[i]))

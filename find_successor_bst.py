class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

def findSuccessor(tree, node):
    # Write your code here.
    if node.right is not None:
        successor = node.right
        while successor.left is not None:
            successor = successor.left
        return successor

    else:
        if node.parent is None:
            return None
        elif node == node.parent.left:
            return node.parent
        else:
            return node.parent.parent
"""
A function to validate a binary search tree constructed
"""
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def validateBst(tree, min, max):

    if tree is None:
        return True
    if tree.value < min or tree.value > max:
        return False
    return (validateBst(tree.left, min, tree.value - 1) and validateBst(tree.value, tree.value + 1, max))
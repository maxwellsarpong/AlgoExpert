class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def binaryTreeDiameter(tree):
    # Write your code here.
    if tree is None:
        return 0
    
    left_height = height(tree.left)
    right_height = height(tree.right)

    left_diameter = binaryTreeDiameter(tree.left)
    right_diameter = binaryTreeDiameter(tree.right)

    return max(left_height + right_height, max(right_diameter, left_diameter))

def height(tree):
    if tree is None:
        return 0
    return 1 + max(height(tree.left), height(tree.right))
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def heightBalancedBinaryTree(tree):
    # Write your code here.
    if tree is None:
        return True
    
    left_height = height(tree.left)
    right_height = height(tree.right)
    diff = abs(left_height - right_height)

    if (diff <= 1) and heightBalancedBinaryTree(tree.left) is True and heightBalancedBinaryTree(tree.right) is True:
        return True
    return False 

def height(tree):
    if tree is None:
        return 0
    return 1 + max(height(tree.right), height(tree.left))
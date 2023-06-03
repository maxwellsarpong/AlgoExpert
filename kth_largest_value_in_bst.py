# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def findKthLargestValueInBst(tree, k):
    # Write your code here.
    stack = []
    current_bst = tree_traversal(tree, stack)
    position = len(stack) - k
    return current_bst[position]

def tree_traversal(tree, stack):
    if tree is not None:
        tree_traversal(tree.left, stack)
        stack.append(tree.value)
        tree_traversal(tree.right, stack)
    return stack

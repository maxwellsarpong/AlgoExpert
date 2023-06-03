# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def reconstructBst(preOrderTraversalValues):
    # Write your code here.
    current_data = preOrderTraversalValues[0]
    root = BST(current_data)
    left_values = []
    right_values = []

    for data in preOrderTraversalValues[1:]:
        nodes = BST(data)

        if nodes.value < root.value:
            left_values.append(nodes.values)
        else:
            right_values.append(nodes.values)

    if left_values:
       root.left = reconstructBst(left_values)
    if right_values:
        root.right = reconstructBst(right_values) 
       
    return root
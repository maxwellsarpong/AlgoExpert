def Inorder(root, array):
    """
    Gives nodes in non-decreasing order
    root.left->root->root.right
    """
    if root:
        Inorder(root.left, array)
        array.append(root.value)
        Inorder(root.right, array)
    return array

def Preorder(root, array):
    """
    Pre-order traversal is used to make a copy of the tree
    root->root.left->root.right
    """
    if root:
        array.append(root.value)
        Preorder(root.left, array)
        Preorder(root.right, array)
    return array

def Postorder(root, array):
    """
    Post-order traversal is used to delete the tree
    root.left ->root.right->root
    """
    if root:
        Postorder(root.left, array)
        Postorder(root.right, array)
        array.append(root.value)
    return array 
class BST:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

    def minHeight(array):
        return contructMinHeightBst(array, None, 0, len(array) - 1)

    def contructMinHeightBst(array, bst, start, end):
        if start > end:
            return
        
        mid = (start + end) // 2
        current_binary_data = array[mid]
        bst_data = BST(current_binary_data)

        if bst is None:
            bst = bst_data
        
        else:
            if bst.value < current_binary_data:
                bst.left = bst_data
                bst = bst.left
            elif bst.value > current_binary_data:
                bst.right = bst_data
                bst = bst.right
        contructMinHeightBst(array, bst, start, mid - 1)
        contructMinHeightBst(array, bst, mid + 1, end)

        return bst
 
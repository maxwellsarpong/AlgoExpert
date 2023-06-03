# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.
class BST:
    
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        # Write your code here.
        # Do not edit the return statement of this method.
            
        if value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BST(value)
        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BST(value) 
        return self

    def contains(self, value):
        # Write your code here.

        if value < self.value:
            if self.left:
                return self.left.contains(value)
            return False
        
        elif value > self.value:
            if self.right:
                return self.right.contains(value)
            return False
        
        return True

    def remove(self, value):
        # Write your code here.
        # Do not edit the return statement of this method.

        if not self:
            return self
            
        if value < self.value:
            if self.left:
                self.left = self.left.remove(value)
            
        elif value > self.value:
                if self.right:
                    self.right = self.right.remove(value)
            
        else:

            if not self.right and not self.left:
                return None
                
            elif not self.left:
                self.value = self.right.value
                self.left = self.right.left
                self.right = self.right.right
                return self

            elif not self.right:
                self.value = self.left.value
                self.right = self.left.right
                self.left = self.left.left
                return self
            
            else:
                successor = self.right.inOrderSuccessor()
                self.value = successor.value
                self.right = self.right.remove(successor.value)
            
        return self

    def inOrderSuccessor(self):
        while self.left:
            self = self.left
        return self
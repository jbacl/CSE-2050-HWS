from BSTMap import BSTMap, BSTNode # provided for you

# Inherit from BSTMap, but overload `newnode` to use this one instead
class MyBSTMap(BSTMap):
    
    def newnode(self, key, value = None): 
        return MyBSTNode(key, value)    # overloads the `newnode` method to use MyBSTNode() instead of BSTNode()

    # TODO: implement the three methods below
    def __eq__(self, other):
        """Sees if two trees share the same pairs; returns True if they do equal"""
             # The heavy lifting here is done in the corresponding
             # function in MyBSTNode - just tell it which node to
             # start with.
        return other.root == self.root
    # these are "static" methods - they belong to the class but do not take an instance of 
    # the class as a parameter (no `self``).
    # note the "decorator" @staticmethod - this let's python know this is not a typical "bound" method
    @staticmethod
    def frompreorder(L):
        """Root to Children Transversal"""
        map = MyBSTMap()
        map.put(L[0][0], L[0][1])
        for i in range(1, len(L)):
            map.put(L[i][0], L[i][1])
        
        return map


    @staticmethod
    def frompostorder(L):
        """Children to Root Transversal"""
        map = MyBSTMap()
        map.put(L[-1][0], L[-1][1])
        for i in range(len(L)-1, -1, -1):
            map.put(L[i][0], L[i][1])
        
        return map

class MyBSTNode(BSTNode):
    
    newnode = MyBSTMap.newnode  # overloads the `newnode` method to use the correct Node class

    # TODO: implement the method below
    def __eq__(self, other):
        """Checks if two nodes are equal"""
        if self and other is None:
            return True
        elif self is None:
            return False
        elif self.value == other.value and self.left == other.left and self.right == other.right:
            return True

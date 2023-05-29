class Node:
    """
    This class holds the node data in a structured obj,
    l will contain a pointer to its left child or none if a leaf
    r will contain a pointer to its right child or none if a leaf
    """
    def __init__(self, val):
        self.l = None
        self.r = None
        self.v = val

class KDTree:
    """
    A K-dimensional tree, similiar to a binary tree but utuilizes alternating dimensions at each level of the tree.
    This tree starts at with x dimension for the first height layer, then alternates with the y dimension.
    
    This class includes a KD tree, insert, findnearestPoint, and some other functions to be utuilized within
    """

    def __init__(self): # Creates a completely empty tree
        self.root = None
        self.height = 0

    def findNearestPoint(self, val): # Public function to find the nearest point to the val point
        if self.root is None:
            return None
        else:
            return self._findNearestPoint(val, self.root, 1)

    def _findNearestPoint(self, val, node, height): # Private implementation of findNearestPoint
        if node is None: return None

        plane = None
        if height % 2 == 0:
            plane = 1 # use Y cordinate
        else:
            plane = 0 # use X cordinate
        
        # Determines if we need to traverse left or righ down the tree
        nextBranch = otherBranch = None
        if val[plane] < node.v[plane]:
            nextBranch = node.l
            otherBranch = node.r
        else: 
            nextBranch = node.r
            otherBranch = node.l
        
        # Recursivly move further down the tree till we hit a leaf
        temp = self._findNearestPoint(val, nextBranch, height+1)

        # Based off what is the current node and what the child returned which is closer
        best = self._closest( temp, node, val)
        radiusSquared = self._distSqr(best, val)
        dist = val[plane] - node.v[plane]

        # If the current best is equal or greater than the current node continue the search
        if radiusSquared >= dist * dist:
            temp = self._findNearestPoint(val, otherBranch, height+1)
            best = self._closest(temp, best, val)
        
        # Return the closest point in the tree
        return best

    def insert(self, val): # Public Insert for KD-tree
        if self.root is None:
            self.root = Node(val)
            self.height += 1
        else:
            self._insert(val, self.root, 1)

    def _insert(self, val, node, height): # Private implementation for KD-tree
        plane = None
        if height % 2 == 0:
            plane = 1 # use Y cordinate
        else:
            plane = 0 # use X cordinate
        
        # Depending on the curren plane to insert we alternate which dimension to compare
        if val[plane] <= node.v[plane]: # if current dimension is less the existing node insert as left child
            if node.l is not None:
                self._insert(val, node.l, height+1)
            else: # if left child already exists continue down another level and re-evauluate 
                node.l = Node(val)
                self.height += 1
        else:
            if node.r is not None:  # if current dimension is less the existing node insert as right child
                self._insert(val, node.r, height+1)
            else: # if right child already exist continue down another level and re-evauluate
                node.r = Node(val)
                self.height += 1
    
    def _distSqr(self, node, target): # Find distance between points, does not find square root
        x = target[0] - node.v[0]
        y = target[1] - node.v[1]
        return (x*x + y*y)

    def _closest(self, n1, n2, target): # Determine which node is closest
        if n1 == None:
            return n2
        if n2 == None:
            return n1
        
        d1 = self._distSqr(n1, target)
        d2 = self._distSqr(n2, target)

        if (d1 < d2):
            return n1
        else:
            return n2
        

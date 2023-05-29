import copy

class Node:
    def __init__(self, val):
        self.l = None
        self.r = None
        self.v = val

    def getValue(self):
        print(self)
        return self.v

class KDTree:
    ""
    
    ""

    def __init__(self):
        self.root = None
        self.height = 0

    def getRoot(self):
        return self.root
    
    def findNearestPoint(self, val):
        if self.root is None:
            return None
        else:
            return self._findNearestPoint(val, self.root, 1)

    def _findNearestPoint(self, val, node, height):
        if node is None: return None

        plane = None
        if height % 2 == 0:
            plane = 1 # use Y cordinate
        else:
            plane = 0 # use X cordinate
        
        nextBranch = otherBranch = None
       
        if val[plane] < node.v[plane]:
            nextBranch = node.l
            otherBranch = node.r
        else: 
            nextBranch = node.r
            otherBranch = node.l
        
        temp = self._findNearestPoint(val, nextBranch, height+1)

        best = self._closest( temp, node, val)
        radiusSquared = self._distSqr(best, val)
        dist = val[plane] - node.v[plane]
        if temp is not None:
            print("Temp node: ", temp.__dict__)
        
        if best is not None:
            print("Best node: ", best.__dict__)
        
        if node is not None:
            print("Curr node: ", node.__dict__) 

        if radiusSquared >= dist * dist:
            temp = self._findNearestPoint(val, otherBranch, height+1)
            best = self._closest(temp, best, val)
        print("best", best.v)
        return best

    def insert(self, val):
        if self.root is None:
            print("Root node: ", val)
            self.root = Node(val)
            self.height += 1
        else:
            self._insert(val, self.root, 1)

    def _insert(self, val, node, height):
        plane = None
        if height % 2 == 0:
            plane = 1 # use Y cordinate
        else:
            plane = 0 # use X cordinate

        if val[plane] <= node.v[plane]:
            if node.l is not None:
                self._insert(val, node.l, height+1)
            else:
                node.l = Node(val)
                self.height += 1
        else:
            if node.r is not None:
                self._insert(val, node.r, height+1)
            else:
                node.r = Node(val)
                self.height += 1
    
    def _distSqr(self, node, target):
        x = target[0] - node.v[0]
        y = target[1] - node.v[1]
        return (x*x + y*y)

    def _closest(self, n1, n2, target):
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
        

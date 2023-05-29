import math

from .kd_tree import KDTree

class NearestNeighborIndex:
    """
    Given the array two dimensional points, we sort them into a KD-tree from the kd_tree module in this directory.
    The tree allows us to quickly determine the nearest neighbor with the minimal number of index traversals

    NearestNeighborIndex is intended to index a set of provided points to provide fast nearest
    neighbor lookup. For now, it is simply a stub that performs an inefficient traversal of all
    points every time.
    """

    def __init__(self, points):
        """
        takes an array of 2d tuples as input points to be indexed.
        """
        self.points = points
        self.kdTree = None

    @staticmethod
    def find_nearest_slow(query_point, haystack):
        """
        find_nearest_slow returns the point that is closest to query_point. If there are no indexed
        points, None is returned.
        """

        min_dist = None
        min_point = None

        for point in haystack:
            deltax = point[0] - query_point[0]
            deltay = point[1] - query_point[1]
            dist = math.sqrt(deltax * deltax + deltay * deltay)
            if min_dist is None or dist < min_dist:
                min_dist = dist
                min_point = point

        return min_point

    def find_nearest_fast(self, query_point):
        """
        find_nearest_fast returns the point that is closest to query_point. If there are no indexed
        points, None is returned.

        uses two dimensional KD-tree to sort the provided array. Once sorted we store the tree for re-use and use a
        nearest neighbor search to traverse the tree
        """

        min_dist = None
        min_point = None
        if self.kdTree == None:
            self.kdTree = KDTree()
            for point in self.points:
                self.kdTree.insert(point)
        
        result = self.kdTree.findNearestPoint(query_point)

        if result.v is not None:
            return result.v
        else:
            return None

    def find_nearest(self, query_point):
        """
        TODO comment me.
        """

        # TODO implement me so this class runs much faster.
        return self.find_nearest_fast(query_point)

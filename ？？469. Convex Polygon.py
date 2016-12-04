class Solution(object):
    def isConvex(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        lenp = len(points)
        if lenp == 3:
            return True
        else:
            # return false when there is a point in the square
            # in means the x & y both smaller/larger than one point
            # out means there is one bigger and one smaller
            for i in xrange(3, lenp):
                for j in xrange(i):
                    if points[i][0] < points[j][0] and points[i][1] < points[j][1]:
                        return False
                    elif points[i][0] > points[j][0] and points[i][1] > points[j][1]:
                        return False
            return True

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1:
            return 0
        elif m == 0 or n == 0:
            return 0
        elif m == 1 and n == 1:
            return 1 - obstacleGrid[0][0]
        elif m > 1 and n > 1:
            res = [[0 for p in range(n)] for q in range(m)]
            for i in xrange(1, m):
                if not obstacleGrid[i][0]:
                    res[i][0] = 1
                else:
                    break
            for j in xrange(1, n):
                if not obstacleGrid[0][j]:
                    res[0][j] = 1
                else:
                    break
            for i in xrange(1, m):
                for j in xrange(1, n):
                    if not obstacleGrid[i][j]:
                        res[i][j] = res[i][j - 1] + res[i - 1][j]
                    else:
                        res[i][j] = 0
            return res[m - 1][n - 1]
        elif m == 1:
            for j in xrange(0, n):
                if obstacleGrid[0][j] == 1:
                    return 0
        elif n == 1:
            for i in xrange(0, m):
                if obstacleGrid[i][0] == 1:
                    return 0
        return 1

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        https://discuss.leetcode.com/topic/67900/dp-solution-in-python
        # basic dynamic programming
        """
        if m > 1 and n > 1:
            grid = [[0 for col in xrange(n)] for row in xrange(m)]
            for row in xrange(1, m):
                grid[row][0] = 1
            for col in xrange(1, n):
                grid[0][col] = 1 
            for row in xrange(1, m):
                for col in xrange(1, n):
                    grid[row][col] = grid[row][col - 1] + grid[row - 1][col]
            return grid[m - 1][n - 1]
        elif not m or not n:
            return 0
        else: # m = 1 or n = 1
            return 1

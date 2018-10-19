class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        if m == 1:
            return sum(grid[0])
        elif n == 1:
            return sum(grid[:][0])
        elif m > 1 and n > 1:
            S = [[0 for c in xrange(n)] for r in xrange(m)]
            S[0][0] = grid[0][0]
            for r in xrange(m):
                S[r][0] = S[r - 1][0] + grid[r][0]
            for c in xrange(n):
                S[0][c] = S[0][c - 1] + grid[0][c]
            for r in xrange(1, m):
                for c in xrange(1, n):
                    S[r][c] = (min(S[r - 1][c], S[r][c - 1]) + grid[r][c])
            return S[r][c]

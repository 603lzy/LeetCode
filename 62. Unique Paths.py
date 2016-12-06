class Solution(object):
    def countOfPath(self, m, n, i, j, cnt):
        """
        type i: int current row position
        type j: int current col position
        type cnt: int current path count to point(i, j)
        
        """
        curcnt = cnt
        if i != 0 and j != 0:
            return self.countOfPath(m, n, i - 1, j, curcnt) + self.countOfPath(m, n, i, j - 1, curcnt)
        elif i == 0 and j != 0:
            return self.countOfPath(m, n, i, j - 1, curcnt)
        elif i != 0 and j == 0:
            return self.countOfPath(m, n, i - 1, j, curcnt)
        if i == 0 and j == 0:
            return cnt
        
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        cnt = self.countOfPath(m, n, m - 1, n - 1, 0)
        return cnt
        

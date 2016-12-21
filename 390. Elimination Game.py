class Solution(object):
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 3:
            return 1 if n == 1 else 2
        else:
            return 4 * self.lastRemaining(n/4) - 2 if n % 4 == 0 or n % 4 == 1 else 4 * self.lastRemaining(n/4) 

class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        # count the number of factor 5
        """
        k = 5
        count = 0
        while k <= n:
            count += (n // k)
            n //= 5
        return count
        

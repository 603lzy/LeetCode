class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        i = 0
        while (3 ** i) < n:
            i += 1
        if (3 ** i) == n:
            return True
        else:
            return False
        

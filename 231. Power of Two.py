class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        i = 0
        while (2 ** i) < n:
            i += 1
        if 2 ** i == n:
            return True
        else:
            return False

class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == n:
            return m
        else:
            i = 0
            while m != n:
                m >>= 1
                n >>= 1
                i += 1
            while i != 0:
                m <<= 1
                i -= 1
            return m

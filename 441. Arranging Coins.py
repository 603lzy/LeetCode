class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        nrow = 0
        ncoin = 0
        while ncoin < n:
            nrow += 1
            ncoin += nrow
        if ncoin == n:
            return nrow
        else:
            return nrow - 1

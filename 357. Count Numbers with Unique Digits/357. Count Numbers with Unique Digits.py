class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        # as the hint, f(k) = 9*9*8*(9-k+2)
        if n == 0:
            res = 1
        elif n == 1:
            res = 10
        else:
            j = 1
            res = 10
            j += 1
            while j <= n:
                i = 2
                tmp = 9
                for i in range(2, j+1):
                    tmp *= (9-i+2)
                res += tmp
                j += 1
                
        return res

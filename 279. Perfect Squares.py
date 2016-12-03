class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        :ref: https://www.cnblogs.com/grandyang/p/4800552.html
        :Solution 1.
        """
        while not n % 4:  # if a number has a factor 4, it does not matter. 2/8,3/12
            n //= 4
        if n % 8 == 7:  # if a number can be devided by 8 mod 7, it returns 4
            return 4
        else:
            a = 0
            while (a ** 2 <= n):
                b = int((n - a ** 2) ** 0.5)
                if a ** 2 + b ** 2 == n:
                    return (a > 0) + (b > 0)
                a += 1
            return 3

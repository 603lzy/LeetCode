class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = n // 3
        j = n % 3
        if i == 0:
            return 1
        elif i == 1:
            if j == 0:
                return 2
            elif j == 1:
                return 4
            else:
                return 6
        elif 2 <= i <= 57:
            if j == 0:
                return 3 ** i
            elif j == 1:
                return (3 ** (i - 1)) * 4
            else:
                return (3 ** i) * 2
        else:
            k = n // 58
            j = n % 58
            return (k ** (58-j)) * ((k+1) ** j)

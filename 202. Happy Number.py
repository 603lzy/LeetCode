class Solution(object):
    def digitSquareSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        dss = 0 # digit Square Sum
        while n > 0:
            dss += ((n%10)**2)
            n //= 10
        return dss
        
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while n > 10:
            n = self.digitSquareSum(n)
        if n == 1 or n == 7 or n == 10:
            return True
        else:
            return False
        

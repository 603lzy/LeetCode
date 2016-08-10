class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        i = 0
        while (4 ** i) < num:
            i += 1
        if (4 ** i) == num:
            return True
        else:
            return False
        

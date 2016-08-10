class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        k = num % 9
        if num == 0:
            return 0
        elif k == 0:
            return 9
        return k

class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        sumi = 0
        i = 1
        while sumi < num:
            sumi += i
            i += 2
        if sumi == num:
            return True
        else:
            return False
# a perfect positive square number is the sum of odd numbers from 1

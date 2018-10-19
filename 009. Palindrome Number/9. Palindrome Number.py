class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        return True if(str(x) == str(x)[::-1]) else False

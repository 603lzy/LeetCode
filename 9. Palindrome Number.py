class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if (x < 0):
            return False
        else:
            a = str(x)
            if(a == a[::-1]):
                return True
            else:
                return False
        

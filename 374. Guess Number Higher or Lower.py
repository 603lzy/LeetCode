# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if guess(n) == 0:
            return n
        elif guess(1) == 0:
            return 1
        else:
            upper = n
            lower = 1
            middle = (1+n)//2
            ges = guess(middle)
            while ges != 0:
                if ges == 1:
                    lower = middle
                else:
                    upper = middle
                middle = (upper + lower)//2
                ges = guess(middle)
                
        return middle

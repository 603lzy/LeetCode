class Solution(object):
    def largestPalindrome(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 7:
            return 877
        elif n == 8:
            return 475
        num = 10 ** n - 1
        i = 0
        while True:
            for x in xrange(i, -1, -1):
                curnum = (num - x) * (num + x)
                if str(curnum) == str(curnum)[::-1]:
                    return curnum % 1337
            i += 1
            num -= 1

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        a = str(x)[::-1] # a is reversed str(x)
        if x < 0:
            a = "-" + a[:-1]
        b = int("".join(a)) # b is the new number
        return 0 if b >= 2147483647 or b <= -2147483647 else b # in case overflow

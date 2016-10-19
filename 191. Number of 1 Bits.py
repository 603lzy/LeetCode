class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = bin(n).replace("0b", "")
        return a.count("1")

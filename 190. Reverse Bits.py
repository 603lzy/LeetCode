class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = bin(n).replace("0b", "")
        a = a[::-1]
        while len(a) <= 31: ## finally, len(a) == 32
            a = a + "0"
        return int(a, 2)

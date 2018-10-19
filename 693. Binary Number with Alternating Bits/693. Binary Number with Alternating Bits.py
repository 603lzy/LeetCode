class Solution:
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        nBinStr = str(bin(n))[2:]
        for i in range(1, len(nBinStr)):
            if nBinStr[i] == nBinStr[i - 1]:
                return False
        return True
        

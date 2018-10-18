class Solution(object):
    def getMaxRepetitions(self, s1, n1, s2, n2):
        """
        :type s1: str
        :type n1: int
        :type s2: str
        :type n2: int
        :rtype: int
        """
        isin = 0
        lens1 = len(s1)
        lens2 = len(s2)
        j = 0
        for i in xrange(lens1):
            if j == lens2:
                isin  = 1
                break
            elif s2[j] == s1[i]:
                j += 1
        if i == lens1 and j == lens1 and s2[-1] in s1:
            isin = 1
        if s2[-1] not in s1 or not isin:
            return 0
        else:
            return n1 // n2

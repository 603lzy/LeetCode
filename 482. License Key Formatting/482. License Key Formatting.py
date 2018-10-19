class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        S, k = S.replace('-',"").upper(), 1
        for i in xrange(len(S) - 1, 0, -1):
            if not k % K:
                S, k = S[:i] + '-' + S[i:], 0
            k += 1
        return S

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        https://leetcode.com/problems/decode-ways/
        """
        if not s or s[0] == '0':
            return 0
        lens = len(s)
        dw = [1] + [0] * lens #1d array length = lens + 1
        for i in xrange(1, lens + 1):
            if s[i - 1] != '0': # can be one independent number
                dw[i] += dw[i - 1]
            if i > 1 and '09' < s[i-2:i] <= '26':
                dw[i] += dw[i - 2] # s[i-2:i] can be a letter
        return dw[-1]

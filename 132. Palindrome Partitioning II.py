class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == s[::-1]:
            return 0
        lens = len(s)
        dp = [-1] + [lens - 1 for _ in xrange(lens)]
        for i in xrange(lens):
            for j in xrange(i + 1, lens + 1):
                if s[i:j] == s[i:j][::-1]:
                    dp[j] = min(dp[j], dp[i] + 1)
        return dp[-1]

#https://discuss.leetcode.com/topic/6465/a-dp-solution-with-clarification-and-explanation/9
class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        lent = len(t)
        dp = [1] + [0] * lent
        for i in xrange(len(s)):
            for j in reversed(xrange(lent)):
                if t[j] == s[i]:
                    dp[j + 1] += dp[j]
        return dp[-1]

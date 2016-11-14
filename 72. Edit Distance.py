# ref: https://discuss.leetcode.com/topic/6965/standard-dp-solution
class Solution(object):
    def minDistance(self, word1, word2):
        len1 = len(word1)
        len2 = len(word2)
        
        if not len1:
            return len2
        if not len2:
            return len1
 # define a 2d array in python
 #ref https://discuss.leetcode.com/topic/19877/python-solutions-o-m-n-o-n-space
        dp = [[0 for _ in xrange(len2 + 1)] for _ in xrange(len1 + 1)]
        for i in xrange(len1 + 1):
            dp[i][0] = i
        for j in xrange(len2 + 1):
            dp[0][j] = j
        
        for i in xrange(1, len1 + 1):
            for j in xrange(1, len2 + 1):
                dp[i][j] = min(min(dp[i - 1][j] + 1, dp[i][j - 1] + 1), dp[i - 1][j - 1] + (word1[i - 1] != word2[j - 1]))
        return dp[len1][len2]

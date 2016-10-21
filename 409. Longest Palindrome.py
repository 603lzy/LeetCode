class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        k = set(s)
        h = {key: 0 for key in k} # init dict with 0
        for i in s:
            h[i] += 1
        
        sign = 0 # whether there is odd char
        for i in k:
            if h[i] % 2 != 0:
                sign = 1
                h[i] -= 1
        return sum(list(h.values()))+sign
        

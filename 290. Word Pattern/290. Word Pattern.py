class Solution(object):
    def wordPattern(self, p, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        :https://discuss.leetcode.com/topic/26562/python-code-in-36-ms
        """
        s = s.split(" ")
        if len(p) != len(s):
            return False
            
        h = {}    
        for i, n in enumerate(p):
            if n not in h:
                h[n] = s[i]
            elif h[n] != s[i]:
                return False
        # find whether there are duplicate values in dictionary
        return len(h) == len(set(h.values()))

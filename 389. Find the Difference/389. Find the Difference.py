class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        s = list(s)
        t = list(t)
        hs = {}
        for i in s:
            if i in hs:
                hs[i] += 1
            else:
                hs[i] = 1
        for j in t:
            if j in hs:
                hs[j] -= 1
            else:
                return j
            if hs[j] == -1:
                return j
                
        
                

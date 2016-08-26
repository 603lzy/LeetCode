class Solution(object):
    def isIsomorphic(self, s, t):
        if not s and not t:
            return True
        h = {}
        for i, j in enumerate(s):
            if j not in h:
                h[j] = t[i]
            elif h[j] != t[i]:
                return False
        h = {}
        for i, j in enumerate(t):
            if j not in h:
                h[j] = s[i]
            elif h[j] != s[i]:
                return False

        return True

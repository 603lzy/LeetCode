class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s:
            return True
        lens = len(s)
        lent = len(t)
        i = 0
        j = 0
        try:
            while True:
                while t[j] != s[i]:
                    j += 1
                j += 1
                i += 1
                if i == lens:
                    return True
        except IndexError:
            return False

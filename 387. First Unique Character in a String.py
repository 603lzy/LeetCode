class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        use a list to save the letters which have appeared
        """
        i = 0
        lens = len(s) 
        A = []
        lena = len(A)
        while (i < lens) and (lena <= 26):
            si = s[i]
            if si in A:
                i += 1
            elif s.count(si) == 1:
                return i
            else:
                A.append(si)
                lena += 1
        return -1

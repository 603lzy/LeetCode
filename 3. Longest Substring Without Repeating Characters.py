class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        sLen = len(s)
        if sLen <= 1: return sLen  # s is shorter than 2 letters
        subStrLen, i, j = 0, 0, 1
        L = [1]
        while j < sLen and L[i - 1] < 95:
            for j in xrange(i, sLen):
                if s[j] in s[i:j]:
                    break
                else:
                    j += 1
            L.append(j - i)
            i += 1
            subStrLen = max(L[-1], subStrLen)
        return subStrLen

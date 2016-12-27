class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        sLen = len(s)
        if sLen <= 1: return sLen  # s is shorter than 2 letters
        subStrLen, p1, p2 = 0, 0, 1  # use 2 pointers
        while p2 < sLen and subStrLen < 95:
            for p2 in xrange(p1, sLen):
                if s[p2] in s[p1:p2]:
                    break
                else:
                    p2 += 1
            subStrLen = max(p2 - p1, subStrLen) 
            p1 += 1
        return subStrLen

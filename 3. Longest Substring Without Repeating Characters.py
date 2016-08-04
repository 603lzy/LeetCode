class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        j = 0
        l = 0
        sign = 0
        print(len(s))
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        j = 1
        i = 0
        L = [1]
        while (i < len(s) and i + L[i - 1] < len(s) and L[i - 1] < 95):
            for j in range(1, len(s)):
                if s[j] in s[i:j]:
                    break
                else:
                    j = j + 1
            L.append(j - i)
            i = i + 1
            l = max(L)
        return l

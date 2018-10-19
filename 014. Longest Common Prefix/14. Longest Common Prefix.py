class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = ""
        try:  # if not beyond the boundary
            i = 0
            while 1: 
                if all(s[i] == strs[0][i] for s in strs):  # use first element as a test
                    prefix += strs[0][i]
                    i += 1
                else:
                    return prefix
        except IndexError:
            return prefix

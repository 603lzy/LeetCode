class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if (strs == []) or (strs == [""]):
            return ""
            
        prefix = ""
        if len(strs[0]) == 0:
            return prefix
        else:
            curfix = strs[0][0]
        i = 0
        while True:
            for s in strs:
                if i >=  len(s):
                    return prefix
                elif s[i] != curfix:
                    return prefix
                else:
                    next
            i = i + 1
            prefix = prefix + curfix
            if i < len(strs[0]):
                curfix = strs[0][i]
            else:
                return prefix
            

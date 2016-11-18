class Solution(object):
    def repeatedSubstringPattern(self, str):
        """
        :type str: str
        :rtype: bool
        """
        lens = len(str)
        for i in range(lens//2):
            if str[:i+1] * (lens // (i+1)) == str:
                return True
        return False

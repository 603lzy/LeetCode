class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        #ord("A") == 65
        sheetnum = 0
        lens = len(s)
        i = lens - 1
        tmp = lens - 1
        while i >= 0:
            sheetnum += (ord(s[i]) % 64) * (26 ** (tmp - i))
            i -= 1
        return sheetnum

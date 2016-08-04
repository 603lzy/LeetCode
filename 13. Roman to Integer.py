class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        lens = len(s)
        roman = ["I", "V", "X", "L", "C", "D", "M"]
        integ = [1, 5, 10, 50, 100, 500, 1000]
        ridict = dict(zip(roman, integ))
        if len(s) == 1:
            return ridict[s]
        else:
            prenum = ridict[s[lens - 1]]
            tmpnum = prenum
            for i in range((lens-2),-1,-1):
                curnum = ridict[s[i]]
                if prenum <= curnum:
                    tmpnum = tmpnum + curnum
                else:
                    tmpnum = tmpnum - curnum
                prenum = curnum
                    
            return tmpnum

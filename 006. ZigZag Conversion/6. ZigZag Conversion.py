class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        lens = len(s)
        if lens <= numRows or numRows <= 1:
            return s
        else:
            strre = ""
            lenstr = (numRows - 1) * 2
            i = j = k = m = 0
            lenstrre = 0
            while lenstrre < lens:
                strre = strre + s[j]
                lenstrre += 1
                if not j % (lenstr / 2):
                    j += lenstr
                else:
                    m += 1
                    k = lenstr - j if m == 1 else lenstr + k
                    if k >= lens:
                        i += 1
                        j = i
                        m = 0
                    else:
                        strre = strre + s[k]
                        lenstrre += 1
                        j += lenstr
                if j >= lens:
                    i += 1
                    j = i
                    m = 0
            return strre

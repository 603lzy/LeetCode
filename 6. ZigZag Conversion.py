class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if len(s) <= numRows:
            return s
        if numRows == 2:
            strre = ""
            strre = s[0::2] + s[1::2]
            return strre
        else:
            if numRows <= 1:
                return s
            else:
                strre = ""
                lenstr = (numRows - 1) * 2
                lens = len(s)
                i = 0 # row
                j = 0 # local
                k = 0 
                m = 0 # each pair of every row
                while len(strre) < lens:
                    if j % (lenstr / 2) == 0:
                        strre = strre + s[j]
                        j = j + lenstr
                        if j >= lens:
                            i = i + 1  
                            j = i
                            m = 0 
                        else:
                            next
                    else:
                        strre = strre + s[j]
                        m = m + 1
                        if m == 1:
                            k = lenstr - j
                        else:
                            k = k + lenstr
                        if k >= lens:
                            i = i + 1
                            j = i
                            m = 0
                        else:
                            strre = strre + s[k]
                            j = j + lenstr
                            if j >= lens:
                                i = i + 1
                                j = i
                                m = 0
                            else:
                                next
                return strre

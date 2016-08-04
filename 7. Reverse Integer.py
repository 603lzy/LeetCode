class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        a = list(str(x))
        if  a[0] != '-':
            a.reverse()
            stra = "".join(a)
            b = int(stra)
            if b >= 2147483647:
                return 0
            else:
                return b
        else:
            a.reverse()
            a.pop()
            a.insert(0,"-")
            stra = "".join(a)
            b = int(stra)
            if b <= -2147483647:
                return 0
            else:
                return(b)

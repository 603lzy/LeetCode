class Solution(object):
    def isContinous(self, s):
        """
        :param s: list[ascii]
        :return: int 1: is 0 not
        """
        if len(s) == 1:
            return 0
        for i in range(len(s)-1):
            if s[i] == 122 and s[i+1] != 97:
                return 0
            elif s[i] != 122 and s[i + 1] - s[i] != 1:
                return 0
        return 1


    def findSubstringInWraproundString(self, p):
        """
        :type p: str
        :rtype: int
        
        """
        lenp = len(p)
        if lenp == 1:
            return 1
        else:
            cnt = len(set(p))
            A = []

            for i in p:
                A.append(ord(i))

            for i in range(lenp):
                for j in range(lenp, i, -1):
                    cnt += self.isContinous(A[i:j])

            return cnt

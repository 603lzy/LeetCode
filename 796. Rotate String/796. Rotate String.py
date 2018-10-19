class Solution:
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if A == "" and B == "":
            return True
        
        lenStrA = len(A)
        lenStrB = len(B)
        if lenStrA != lenStrB:
            return False
        
        cnt = 0
        while cnt < lenStrA:
            if A == B:
                return True
            A = A[1:] + A[0]
            cnt = cnt + 1
        return False
        

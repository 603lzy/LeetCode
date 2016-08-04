class Solution(object):
    def reprint(self, i, A, B, C):
        """
        :type i: num
        :type digit:str
        :rtype: List[str], num
        """
        integ = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        alphabet = [" ", "*", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        index = dict(zip(integ, alphabet))

        if i < 0:
            return (i, A, B, C)
        elif A[i] == len(index[B[i]]):
            for j in range(i, len(A)):
                A[j] = 0
            i = i - 1
            A[i] = A[i] + 1
            return self.reprint(i, A, B, C)
        else:
            a = ""
            for k in range(0, len(A)):
                a = a + index[B[k]][A[k]]
            C.append(a)
            m = len(A) - 1
            A[m] = A[m] + 1
            return self.reprint(m, A, B, C)
            
        

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        A = [0 for j in range(0, len(digits))] # index of print
        B = [int(i) for i in digits] # index of orignial numbers
        C = [] # result list
        sign = len(digits) # sign number
        i = len(A) - 1
        if len(digits) == 0:
            return C
            
        while i >= 0:
            reList = self.reprint(i, A, B, C)
            i = reList[0]
        
        return reList[3]
        

    
        

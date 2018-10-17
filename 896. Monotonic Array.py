class Solution:
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A) <= 2:
            return True
        isNotInc = 0
        isNotDec = 0
        if A[0] <= A[-1]:
            for i in range(len(A) - 1):
                if A[i] > A[i + 1]:
                    isNotInc = 1
                    break
        else:
            for i in range(len(A) - 1):
                if A[i] < A[i + 1]:
                    isNotDec = 1
                    break
                
        
        return not (isNotInc or isNotDec)

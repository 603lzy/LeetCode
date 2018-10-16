class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        lineNum = len(A[0])
        
        for row in A:
            row.reverse()
            
            for i in range(lineNum):
                row[i] = 1 - row[i]
                
        return A

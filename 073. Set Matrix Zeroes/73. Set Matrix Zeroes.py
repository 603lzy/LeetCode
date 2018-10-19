class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        row = set()
        col = set()
        nrow = len(matrix)
        ncol = len(matrix[0])
        for i in range(nrow):
            for j in range(ncol):
                if not matrix[i][j]:
                    row.add(i)
                    col.add(j)
        for i in range(nrow):
            for j in range(ncol):
                if i in row or j in col:
                    matrix[i][j] = 0
        

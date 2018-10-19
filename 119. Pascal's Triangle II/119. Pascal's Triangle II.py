class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        numRows = rowIndex
        if numRows == 0:
            return [1]
        elif numRows == 1:
            return [1, 1]
        else:
            A = [[1],[1, 1]]
            i = 2
            while i <= numRows:
                B = [1]
                for j in range(1, i):
                    B.append(A[i-1][j-1] + A[i-1][j])
                B.append(1)
                A.append(B)
                i += 1
            return B

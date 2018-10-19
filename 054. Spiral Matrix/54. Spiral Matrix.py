class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        nrow = len(matrix)
        A = []
        if nrow <= 1:
            return A if not nrow else matrix[0]
        
        ncol = len(matrix[0])
        if ncol == 1:
            for i in xrange(nrow):
                A.append(matrix[i][0])
            return A
        
        i, cnt, istart, iend, jstart, jend, direct = 0, nrow * ncol, 1, nrow, 0, ncol, -1
        while(True):
            direct = 0 - direct
            for j in range(jstart, jend, direct):
                A.append(matrix[i][j])
                cnt -= 1
            if cnt == 0:
                break
            for i in range(istart, iend, direct):
                A.append(matrix[i][j])
                cnt -= 1
            if cnt == 0:
                break
            direct = 0 - direct
            for j in range(jend - 2, jstart - 1, direct):
                A.append(matrix[i][j])
                cnt -= 1
            if cnt == 0:
                break
            for i in range(iend - 2, istart - 1, direct):
                A.append(matrix[i][j])
                cnt -= 1
            if cnt == 0:
                break
            jstart = jstart + 1
            jend = jend - 1
            istart = istart + 1
            iend = iend - 1
        return A if len(A) >= 1 else A[0]

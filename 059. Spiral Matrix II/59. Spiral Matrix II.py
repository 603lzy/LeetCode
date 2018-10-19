class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if not n:
            return []
        elif n == 1:
            return [[1]]
        elif n == 2:
            return [
                    [1, 2],
                    [4, 3],
                    ]
        
        jstart = 0
        jend = n
        istart = 1
        iend = n
        i = 0
        cnt = 1
        c = n ** 2 + 1
        direct = -1
        matrix = [[0 for col in xrange(n)] for row in xrange(n)]
        while(True):
            direct = 0 - direct
            for j in range(jstart, jend, direct):
                matrix[i][j] = cnt
                cnt += 1
            if cnt == c:
                break
            for i in range(istart, iend, direct):
                matrix[i][j] = cnt
                cnt += 1
            if cnt == c:
                break

            direct = 0 - direct
            for j in range(jend - 2, jstart - 1, direct):
                matrix[i][j] = cnt
                cnt += 1
            if cnt == c:
                break
            for i in range(iend - 2, istart - 1, direct):
                matrix[i][j] = cnt
                cnt += 1
            if cnt == c:
                break
            jstart = jstart + 1
            jend = jend - 1
            istart = istart + 1
            iend = iend - 1
        return matrix 

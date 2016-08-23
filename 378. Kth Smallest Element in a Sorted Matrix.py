class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        A = []
        n = len(matrix)
        for i in range(n):
            A.extend(matrix[i])
        A.sort()
        return A[k-1]

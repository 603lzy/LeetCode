class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        : Fibonacci sequence
        """
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            A = [1, 2]
            i = 2
            while i < n:
                A.append(A[i-1] + A[i-2])
                i += 1
            return A[-1]

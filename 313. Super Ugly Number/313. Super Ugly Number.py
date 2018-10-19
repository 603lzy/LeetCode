class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        A = [1]
        lena = 1
        if n == lena:
            return A[-1]
        k = len(primes)
        B = [0 for c in range(k)]
        C = []
        for i in range(k):
            C.append(A[0] * primes[i])
        minv = min(C)
        A.append(minv)
        lena += 1
        j = C.index(minv)
        B[j] += 1
        
        while lena < n:
            C[j] = A[B[j]] * primes[j]
            minv = min(C)
            if A[-1] != minv:
                A.append(minv)
                lena += 1
            j = C.index(minv)
            B[j] += 1
        return A[-1]

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            isPrime = []
        else:
            isPrime = [True for i in range(n)]
            isPrime[0] = False
            isPrime[1] = False

            # Loop's ending condition is i * i < n instead of i <sqrt(n)
            i = 2 # start from prime 2
            while i * i < n:
                if isPrime[i]:
                    for j in range(i*i, n, i):
                        isPrime[j] = False
                i += 1
        return isPrime.count(True)

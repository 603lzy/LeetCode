class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        A = []
        for i in range(1, 10, 1):
            p = "".join(str(j) for j in range(i, 0, -1))
            A.append(int(p))
        #get list A = [1, 21, 321,...,87654321]
        B = [k * 9 for k in A]
        #get list B = [9, 189, 2889, 38889, ..., 8888888889]
        C = [m + 1 for m in B]
        #get list C = [10, 190, 2890, 38890, ... 8888888890]
        if n <= B[0]:
            return n
        for i in range(2, 10):
            if C[i-2] <= n <= B[i-1]:
                b = n - B[i-2]
                break
        return int(str(b // i + 10 ** (i-1))[b % i - 1]) if b % i else int(str(b // i + 10 ** (i - 1) - 1)[i-1])
            
        
        

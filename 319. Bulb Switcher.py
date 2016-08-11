"""
# just test to find the regularities
# 0111222223333333444444444...
for n in range(200):
    A = []
    for i in range(n):
        A.append(0)
    k = 1
    while k <= n:
        i = k-1
        while i < n:
            A[i] = 1 - A[i]
            i += k
        k = k + 1
    print(A.count(1))
"""
class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        else:
            i = 1
            tmp = ((i+1)**2) - 1
            while tmp < n:
                i += 1
                tmp = ((i+1)**2) - 1
            return i

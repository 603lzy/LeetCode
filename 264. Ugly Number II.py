class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        :ref:http://blog.csdn.net/taoxiuxia/article/details/47813327
        """
        A = [1]
        lena = 1
        i, j, k = 0, 0, 0  #start point of three pointers
        while lena < n:
            Ai = A[i] * 2
            Aj = A[j] * 3
            Ak = A[k] * 5
            minv = min(Ai, Aj, Ak)
            if A[-1] != minv:
                A.append(minv)
                lena += 1
                if minv == Ai:
                    i += 1
                elif minv == Aj:
                    j += 1
                else:
                    k += 1
            else:
                if minv == Ai:
                    i += 1
                elif minv == Aj:
                    j += 1
                else:
                    k += 1
        return A[-1]

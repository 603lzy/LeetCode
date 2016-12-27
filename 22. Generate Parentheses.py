class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        B = [i for i in xrange(n)]
        p = ""
        for k in xrange(0, 2 * n):
            p += "(" if k in B else ")"
        A = [p]
        j = i = n - 1
        while True:
            if B[j] != 2 * j: # adjustment b
                B[j] += 1
            else:
                while j != 0:
                    j -= 1
                    if B[j] != 2 * j:
                        B[j] += 1
                        for m in xrange(j + 1, n):
                            B[m] = B[m - 1] + 1
                        j = n - 1
                        break
                if j <= 0:
                    return A
            p = "" # then print
            for k in xrange(0, 2 * n):
                p += "(" if k in B else ")"
            A.append(p)

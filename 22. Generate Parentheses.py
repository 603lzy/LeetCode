class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        i = 0
        output = 2*n
        B = [i for i in range(n)]
        p = ""
        for k in range(0, output):
            if k in B:
                p = p + "("
            else:
                p = p + ")"
        A = [p]
        i = n-1
        j = i
        while True:
            if B[j] != 2*j: # adjustment b
                B[j] += 1
            else:
                while j != 0:
                    j -= 1
                    if B[j] != 2*j:
                        B[j] += 1
                        for m in range(j+1, n):
                            B[m] = B[m-1] + 1
                        j = n-1
                        break
                if j <= 0:
                    return A
                
            p = "" # then print
            for k in range(0, output):
                if k in B:
                    p = p + "("
                else:
                    p = p + ")"
            A.append(p)

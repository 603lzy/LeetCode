class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        # http://blog.csdn.net/booirror/article/details/47173399
        """
        area = (C - A) * (D - B) + (G - E) * (H - F)
        if (E > C or G < A or F > D or H < B):
            return area
        else:
            area -= (min(C, G) - max(A, E)) * (min(D, H) - max(B, F)) 
        return area

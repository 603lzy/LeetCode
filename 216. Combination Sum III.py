import itertools
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        A = [list(i) for i in itertools.combinations(range(1, 10), k)]
        B = []
        for i in A:
            if sum(i) == n:
                B.append(i)
        return B
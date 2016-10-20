import itertools
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        return [i for i in [list(i) for i in itertools.combinations(range(1, 10), k)] if sum(i) == n]

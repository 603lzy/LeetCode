class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(bin(i^j).count("1") for (i, j) in [k for k in itertools.combinations(nums, 2)])

import itertools
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        A = [[]]  # init return list, including the empty subset
        lenn = len(nums)
        if lenn >= 1:
            A.append(nums)  # nums contains more than one element
        if lenn >= 2:
            for i in nums:
                A.append([i])  # convert single element to list
            for j in xrange(2, lenn):
                A.extend([list(x) for x in itertools.combinations(nums, j)])  # consider subsets with 2 to lenn-1 elements
        return A

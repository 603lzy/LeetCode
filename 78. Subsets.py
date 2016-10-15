import itertools
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        A = [[]]
        lenn = len(nums)
        if lenn == 0:
            return [[]]
        elif lenn == 1:
            return [[], nums]
        else:
            A.append(nums)
            for i in nums:
                A.append([i])
            for i in xrange(2, lenn):
                A.extend([list(x) for x in itertools.combinations(nums, i)])
            return A

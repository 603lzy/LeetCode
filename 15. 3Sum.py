class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """ 
        nums.sort()
        C, maxi = set(), len(nums) - 2 # maxi: max index of pointer i backward
        for i in xrange(maxi):
            for j in xrange(i + 1, maxi + 1):
                if -nums[i] - nums[j] in nums[j + 1: ]:
                    C.add((nums[i], nums[j], -nums[i] - nums[j]))
        return list(C)

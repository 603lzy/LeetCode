class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lenn = len(nums)
        for i in xrange(lenn - 1):
            for j in xrange(i+1, lenn):
                if nums[i] + nums[j] == target:
                    return [i, j]

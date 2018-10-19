class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        B = []
        n = len(nums)
        for i in xrange(1, n):
            if nums[i] == nums[i - 1]:
                B.append(nums[i])
        return B

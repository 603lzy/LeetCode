class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        if not nums or nums[-1] <= 0: # nums[-1] = max(nums)
            return 1
        i = 1
        while i in nums:
            i += 1
        return i

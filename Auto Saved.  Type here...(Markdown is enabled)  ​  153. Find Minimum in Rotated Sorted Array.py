class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lenn = len(nums)
        i = 1
        while i < lenn:
            if nums[i] < nums[i-1]:
                return nums[i]
            else:
                i += 1
        return nums[0]

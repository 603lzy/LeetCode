class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i, lenn = 0, len(nums) - 1
        while i < lenn:
            if nums[i] != nums[i + 1]:
                return nums[i]
            else:
                i += 2
        return nums[-1]

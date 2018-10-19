class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        lenn = len(nums)
        nums.sort()
        for i in range(lenn):
            if nums[i] != i:
                return i
        return i+1

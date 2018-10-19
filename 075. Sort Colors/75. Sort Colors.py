class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i0 = nums.count(0)
        i1 = nums.count(1)
        i2 = nums.count(2)
        for i in range(i0):
            nums[i] = 0
        for i in range(i0, i0+i1):
            nums[i] = 1
        i = i0 + i1
        while i != len(nums):
            nums[i] = 2
            i += 1
        return 

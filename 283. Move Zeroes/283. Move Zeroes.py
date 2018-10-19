class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        lenn = len(nums)
        while 0 in nums:
            nums.remove(0)
        while len(nums) != lenn:
            nums.append(0)
        return 

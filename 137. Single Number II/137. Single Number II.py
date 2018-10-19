class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        lenn = len(nums)
        i = 0
        if lenn == 1:
            return nums[0]
        else:
            while i < (lenn - 1):
                if nums[i] != nums[i+1]:
                    return nums[i]
                else:
                    i += 3
            return nums[-1]

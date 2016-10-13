class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = list(set(nums))
        nums.sort(reverse = True)
        try:
            return nums[2]
        except IndexError:
            return nums[0]

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        j = len(nums) - 1
        while True:
            for k in range(0, j):
                if nums[j] + nums[k] == target:
                    return [k, j]
            j = j - 1
            k = 0
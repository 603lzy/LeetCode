class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lenn = len(nums)
        i = 0
        for j in range(1, lenn):    # refer to the key, two pointers
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return lenn if lenn <= 1 else i + 1

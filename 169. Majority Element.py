class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lenn = len(nums)
        lenn2 = lenn / 2
        numset = set(nums)
        for i in numset:
            if nums.count(i) > lenn2:
                return i

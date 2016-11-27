class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        http://blog.csdn.net/awawfwfw/article/details/53257872
        """
        ret = 0
        if nums:
            nums.sort()
            median = nums[len(nums)//2]
            ret = sum([abs(i - median) for i in nums])
        return ret

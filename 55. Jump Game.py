class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        :https://discuss.leetcode.com/topic/6386/the-fastest-solution-in-python
        """
        start = len(nums) - 1
        m = reversed(xrange(start))
        for i in m:
            if i + nums[i] >= start:
                start = i
        return not start

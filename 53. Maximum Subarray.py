class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        https://discuss.leetcode.com/topic/69415/python-solution-o-n-beat-99-94-other-solutions
        """
        s1 = s2 = 0
        for num in nums:
            s1 = max(0, s1 + num)
            s2 = max(s1, s2)
        return max(nums) if not s2 else s2

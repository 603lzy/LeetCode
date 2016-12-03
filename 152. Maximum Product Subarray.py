class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        https://discuss.leetcode.com/topic/65470/python-one-pass-o-n-time-o-1-space-solution-8-lines-super-simple-elegant-easy-to-understand
        """
        maxi = float("-inf")
        p1 = p2 = 1 # p2 may be negative
        for num in nums:
            p1, p2 = max(num, p1 * num, p2 * num), min(num, p1 * num, p2 * num)
            maxi = max(maxi, p1)
        return maxi
        

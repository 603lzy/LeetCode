class Solution(object):
    def minMoves(self, nums):
        
        """
        ref:http://blog.csdn.net/yeqiuzs/article/details/53078666
        :type nums: List[int]
        :rtype: int
        """
        return sum(nums) - min(nums) * len(nums)

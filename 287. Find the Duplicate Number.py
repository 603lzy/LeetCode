class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        # though I cannot modify nums, but I can create 'num'
        """
        lenn = len(nums)
        num = nums
        num.sort()
        
        for i in range(lenn):
            if num[i] == num[i+1]:
                return num[i]

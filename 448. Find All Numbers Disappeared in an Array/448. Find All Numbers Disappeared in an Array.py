class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        A = []
        for i in xrange(1, n + 1):
            if i not in nums:
                A.append(i)
        return A

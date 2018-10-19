class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        lenn = len(nums)
        i = 0
        A = []
        if lenn == 2:
            return nums
        else:
            while i < lenn - 1:
                if nums[i] != nums[i + 1]:
                    A.append(nums[i])
                    i += 1
                else:
                    i += 2
            if len(A) == 1:
                A.append(nums[-1])
            return A

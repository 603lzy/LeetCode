class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        A = []
        B = []
        lenn = len(nums)
        right = 1
        left = 1
        for i in range(lenn-1):
            right *= nums[i]
            left *= nums[lenn-1-i]
            A.append(right)
            B.append(left)
        C = [B[-1]]
        for i in range(lenn-2):
            C.append(A[i] * B[-2-i])
        C.append(A[-1])
        return C
            

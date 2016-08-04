class Solution(object):
    def twoSum(self, num2, re1, re2, C, target):
        """
        :type nums： List[int]
        :rtype: set()
        """
        j = len(num2) - 1
        a2 = 0
        b2 = 0
        while 0 != j:
            a2 = num2[j]
            for k in range(0, j):
                b2 = num2[k]
                if a2 + b2 + re1 + re2== target:
                    C.add((re1, re2, b2, a2))
            j = j - 1
        return C
                    
    def threeSum(self, num3, re1, C, target):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        i = 0
        tmp3 = len(num3) - 2
        while i < tmp3:
            i = i + 1
            lennum = tmp3 - i + 1
            self.twoSum(num3[i:], re1, num3[i-1], C, target)
        return C
        
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        C = set()
        k = 0
        tmp = len(nums) - 3
        while k < tmp:
            k = k + 1
            self.threeSum(nums[k:], nums[k-1], C, target)
        C = list(C)
        C.sort()
        return C
        

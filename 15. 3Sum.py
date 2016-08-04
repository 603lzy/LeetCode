class Solution(object):
    def twoSum(self, num, target, C, lennum):
        j = lennum
        a = 0
        b = 0
        while 0 != j:
            a = num[j]
            for k in range(0, j):
                b = num[k]
                if a + b == target:
                    C.add((-target, b, a))
            j = j - 1
        return C
                    
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        C = set()
        i = 0
        tmp = len(nums) - 2
        while i < tmp:
            i = i + 1
            lennum = tmp - i + 1
            self.twoSum(nums[i:], -nums[i-1], C, lennum)
            
        C = list(C)
        C.sort()
        return C
        

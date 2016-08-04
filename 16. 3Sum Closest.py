class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        lennum = len(nums)
        if lennum == 3:
            return sum(nums)
        else:
            result = nums[0] + nums[1] + nums[2]
            mintar = abs(nums[0] + nums[1] + nums[2] - target)
            tmp = result
            tmp1 = 0
            tmp2 = 0
            a = 0
            b = 0
            c = 0
    
            for i in range(2, lennum):
                a = nums[i]
                for j in range(0, i):
                    tmp2 = nums[j] + a
                    for k in range(0, j):
                        result = tmp2 + nums[k]
                        tmp1 = abs(result - target)
                        if tmp1 < mintar:
                            tmp = result
                            mintar = tmp1
        return tmp

class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        if k == 1:
            return max(nums)
        elif k == len(nums):
            return float(sum(nums))/k
        else:  # k > 1
            num = [float(i) / k for i in nums]
            snum = []
            tmp = sum(num[:k])
            snum.append(tmp)
            for i in range(len(num) - k):
                tmp = tmp - num[i] + num[i + k]
                snum.append(tmp)
                
            return max(snum)

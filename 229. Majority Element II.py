class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        A = []
        lenn = len(nums)
        if lenn == 2: #if the length <= 2, return unique nums
            return list(set(nums))
        B = set(nums)
        i = 0
        for j in B:
            if nums.count(j) > (lenn // 3):
                A.append(j)
                i += 1
                if i > 2: # the count of majority number cannot be more than 3
                    break
        return A

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        : HashTable O(1)
        """
        lenn = len(nums)
        if lenn == 2:
            return list(set(nums))
        else:
            H = {}
            for j in nums:
                if j in H:
                    H[j] += 1
                else:
                    H[j] = 1
            A = []
            lend3 = lenn // 3 # lenn divide by 3
            for j in H:
                if H[j] > lend3:
                    A.append(j)
            return A

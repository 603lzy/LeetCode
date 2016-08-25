class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        lenn = len(nums)
        if k == 0 or lenn <= 1:
            return False
        elif lenn <= k:
            return len(set(nums)) < len(nums)
        else:
            A = set(nums[0:k+1])
            if len(A) <= k:
                return True
            endi = lenn-k-1
            j = k+1 # pointer to the new number
            for i in range(endi):
                A.remove(nums[i])
                A.add(nums[j])
                j += 1 #update the pointer
                if len(A) <= k:
                    return True
            return False

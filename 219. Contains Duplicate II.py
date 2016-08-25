class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if k == 0:
            return False
        elif nums == []:
            return False
        else:
            i = 0
            lenn = len(nums)
            if k >= lenn:
                return len(set(nums)) < len(nums)
            else:
                A = set(nums[0:k+1])
                if len(A) < k+1:
                    return True
                for i in range(lenn-k-1):
                    A.remove(nums[i])
                    A.add(nums[i+k+1])
                    if len(A) < k+1:
                        return True
                return False
                
                

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        m = len(nums1)
        n = len(nums2)
        nums = nums1 + nums2
        nums.sort()
        if (m + n) % 2 == 0:
            return (nums[(m + n)/2]+nums[(m + n)/2-1])/2.0
        else:
            return nums[(m + n - 1)/2]

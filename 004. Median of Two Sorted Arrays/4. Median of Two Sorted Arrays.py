class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """  
        m, n = len(nums1), len(nums2)
        nums = nums1 + nums2
        nums.sort()
        return (nums[(m + n)/2]+nums[(m + n)/2 - 1])/2.0 if not (n + m) % 2 else nums[(m + n - 1)/2]

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        use two pointers
        https://discuss.leetcode.com/topic/27365/python-understand-easily-from-binary-search-idea/2
        by iwatch
        """
        i = 1
        j = n
        while i < j:
            k = (i+j)/2
            if isBadVersion(k): # version k is bad
                j = k
            else: # version k is good 
                i = k + 1
        return i

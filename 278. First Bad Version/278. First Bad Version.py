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
        """
        head, tail = 1, n
        while head < tail:
            mid = (head + tail) / 2
            if isBadVersion(mid):
                tail = mid
            else:
                head = mid + 1
        return head

class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        :https://discuss.leetcode.com/category/176/excel-sheet-column-title
        """
        return "" if n == 0 else self.convertToTitle((n-1)/26) + chr((n-1)%26 + ord('A'))

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        lenh = len(height)
        maxvol = 1
        if len(height) == 2:
            return min(height)
        else:
            i = 0
            j = lenh - 1
            while i != j:
                tmp = min(height[i], height[j])
                vol = (j - i) * tmp
                if maxvol < vol:
                    maxvol = vol
                if tmp == height[i]:
                    i = i + 1
                else:
                    j = j - 1
        return maxvol

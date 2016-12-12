class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        h = {}
        for i in s:
            h[i] = h[i] + 1 if i in h else 1
        H = sorted(h.items(), key = lambda val:val[1], reverse = True) # sort the dict by val decreasing
        return "".join(i[0] * i[1] for i in H)

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        :https://discuss.leetcode.com/topic/23352/a-python-solution
        """
        try:
            citations.sort(reverse = True)
            h = 0
            while not citations[h] <= h:
                h += 1
            return h
        except IndexError:
            return len(citations)

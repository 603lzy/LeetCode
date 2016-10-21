class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations = citations[::-1]
        try:
            N = len(citations)
            h = 0
            while not citations[h] <= h:
                h += 1
            return h
        except IndexError:
            return N

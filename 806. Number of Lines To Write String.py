class Solution:
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        DICTWIDTHS = {}
        ALPHABET = string.ascii_lowercase
        for i in range(26):
            DICTWIDTHS[ALPHABET[i]] = widths[i]
        row = 1
        lastline = 0
        for s in S:
            if lastline + DICTWIDTHS[s] > 100:  # the letter should be written in the next row
                row = row + 1
                lastline = DICTWIDTHS[s]
            else:
                lastline = lastline + DICTWIDTHS[s]
        
        return [row, lastline]
        

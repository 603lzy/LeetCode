class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        #http://www.bubuko.com/infodetail-1339385.html
        A = []
        for k in words:
            tag = 0
            for i in k:
                tag |= 1 << ord(i) - ord("a")
            A.append(tag)
        B = list(map(len, words))
        
        res = 0
        lenw = len(words)
        for i in range(lenw):
            for j in range(i+1, lenw):
                if (A[i] & A[j]) == 0 and B[i] * B[j] > res:
                    res = B[i] * B[j]
                    
        return res

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        lens = len(s)
        if lens <= 2:
            return s
        A = {}
        R = {}
        
        srev = s[::-1]
        if srev == s:
            return s
            
        
        # row is srev, col is s
        for i in range(0, lens):
            if s[i] == srev[0]:
                R[i] = 1
        A = R
        R = {}
        
        maxnum = 0
        maxi = 0
        for i in range(1, lens):
            c = srev[i]
            if s[0] == c:
                R[0] = 1
            for j in range(1, lens):
                if s[j] == c:
                    if (j-1) in A.keys():
                        tmp = A[j-1] + 1
                        R[j] = tmp
                        if maxnum < tmp:
                            maxi = i
                            maxnum = tmp
                    else:
                        R[j] = 1
            A = R
            R = {}
        tmp = maxi  + 1
        return srev[tmp-maxnum:tmp]

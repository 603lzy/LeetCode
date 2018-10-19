class Solution:
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        R = ""
        lenS = len(S)
        p, q = 0, lenS - 1
        ALPHABET = string.ascii_lowercase + string.ascii_uppercase
        while p < lenS:
            if S[p] not in ALPHABET:
                R = R + S[p]    # no change if not lower letter 
            else:
                while S[q] not in ALPHABET:
                    q = q - 1
                R = R + S[q]
                q = q - 1
            p = p + 1
        return R

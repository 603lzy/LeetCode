class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        # use two pointers point to the forward and backward vowel letter
        """
        lens = len(s)
        s = list(s)
        i = 0
        j = lens - 1
        A = ['a', "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        while i < j:
            while (s[i] not in A) and (i < lens - 1):
                i += 1
            while (s[j] not in A) and (j > 0):
                j -= 1
            if i < j:
                tmp = s[i]
                s[i] = s[j]
                s[j] = tmp
                i += 1
                j -= 1
        return "".join(s)

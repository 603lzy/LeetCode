class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s or len(s) % 2 == 1: # if the length is shoter than 1 or odd length
            return False
        A = []
        B = ['(', '[', '{']
        C = [')', ']', '}']
        for i in s:
            if i in B:
                A.append(i)
            elif not A:
                return False
            elif A[-1] == B[C.index(i)]:
                A.pop()
            else:
                return False
        return A == []

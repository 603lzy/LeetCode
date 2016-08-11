class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        A = list(map(str, digits))
        a = "".join(A)
        b = int(a) + 1
        b = str(b)
        B = [c for c in b]
        B = list(map(int, B))
        return B

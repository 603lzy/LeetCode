class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        A = []
        for i in range(num+1):
            a = bin(i).replace("0b", "")
            A.append(a.count("1"))
        return A

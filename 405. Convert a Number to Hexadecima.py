class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        return hex(num).replace("0x","") if num >= 0 else hex(2 ** 32 + num).replace("0x","")

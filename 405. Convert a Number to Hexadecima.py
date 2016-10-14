class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num >= 0:
            ret = hex(num)
            return ret.replace("0x", "")
        else:
            ret = hex(2 ** 32 + num)
            return ret.replace("0x", "")

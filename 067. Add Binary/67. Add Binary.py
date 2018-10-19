class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a = "0b" + a
        b = "0b" + b
        a = eval(a)
        b = eval(b)
        c = a + b
        return bin(c).replace("0b", "")
        

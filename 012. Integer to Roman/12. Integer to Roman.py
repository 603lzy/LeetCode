class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        :ref: http://www.cnblogs.com/dosxp/archive/2008/08/13/1266781.html
        """
        hrom = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        trom = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        rom = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        intdex = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        hdic = dict(zip(intdex, hrom))   
        tdic = dict(zip(intdex, trom))
        dic = dict(zip(intdex, rom))
        
        rostr = ""
        k = num // 1000
        num = num % 1000
    
        h = num // 100
        num = num % 100
        
        t = num // 10
        num = num % 10
        
        rostr = "M"*k + hdic[h] + tdic[t] + dic[num]
        return rostr
        

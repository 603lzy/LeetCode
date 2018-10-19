class Solution:
    def getRealImagPart(self, s):
        """
        :type s: str
        :rtype: List[int, int] = [Real, Imaginary]
        """
        p = s.index("+")
        a = int(s[:p])
        b = int(s[p+1:-1])
        return [a, b]
    
    def getComplexNumberStr(self, real, imag):
        """
        :type real: int
        :type imag: int
        :rtype: str
        """
        return str(real) + "+" + str(imag) + "i"
        
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        [aReal, aImag] = self.getRealImagPart(a)
        [bReal, bImag] = self.getRealImagPart(b)
        [cReal, cImag] = [aReal * bReal - aImag * bImag, aReal * bImag + bReal * aImag]
        return self.getComplexNumberStr(cReal, cImag)
        

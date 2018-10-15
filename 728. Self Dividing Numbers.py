class Solution:
    def isselfDividingNumber(self, N):
        """
        :type N: int
        :rtype: Bool
        """
        nums = str(N)
        if "0" in nums:
            return False
        else:
            for num in nums:
                if N % int(num) != 0:
                    return False
        return True
        
        
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        sDN = []
        for n in range(left, right + 1):
            if self.isselfDividingNumber(n):
                sDN.append(n)
        return sDN

class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        http://blog.csdn.net/xudli/article/details/46798619
        http://blog.csdn.net/wangyunyun00/article/details/47342983
        """
        count = 0
        m = 1
        while m < n+1:
            a = n // m
            b = n % m
            if a % 10 == 1:
                count += (a+8)//10 * m + b + 1
            else:
                count += (a+8)//10 * m
            m *= 10
        return count
        

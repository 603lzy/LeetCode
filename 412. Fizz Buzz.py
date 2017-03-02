class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        A = []
        for i in xrange(1,n+1):
            if not i % 3 and not i % 5:
                A.append("FizzBuzz")
            elif not i % 3:
                A.append("Fizz")
            elif not i % 5:
                A.append("Buzz")
            else:
                A.append(str(i))
        return A

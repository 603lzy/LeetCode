class Solution(object):
    def small(self, s, i, A):
        """
        :type s: str
        :type i: int
        :rtype: list
        """
        i = i + 1
        if i == len(s):
            return [False, i]
        elif s[i] == ')':
            i = i + 1
            return [True, i]
        elif s[i] == ']':
            return [False, i]
        elif s[i] == '}':
            return [False, i]
        elif s[i] == '(':
            return self.small(s, i)
        elif s[i] == '[':
            return self.middle(s, i)
        elif s[i] == '{':
            return self.big(s, i)
        else:
            return self.small(s, i)
    
    def middle(self, s, i):
        """
        :type s: str
        :type i: int
        :rtype: bool
        """
        i = i + 1
        if i == len(s):
            return [False, i]
        elif s[i] == ')':
            return [False, i]
        elif s[i] == ']':
            i = i + 1
            return [True, i]
        elif s[i] == '}':
            return [False, i]
        elif s[i] == '(':
            return self.small(s, i)
        elif s[i] == '[':
            return self.middle(s, i)
        elif s[i] == '{':
            return self.big(s, i)
        else:
            return self.middle(s, i)

    def big(self, s, i):
        """
        :type s: str
        :type i: int
        :rtype: bool
        """
        i = i + 1
        if i == len(s):
            return [False, i]
        elif s[i] == ')':
            return [False, i]
        elif s[i] == ']':
            return [False, i]
        elif s[i] == '}':
            i = i + 1
            return [True, i]
        elif s[i] == '(':
            return self.small(s, i)
        elif s[i] == '[':
            return self.middle(s, i)
        elif s[i] == '{':
            return self.big(s, i)
        else:
            return self.big(s, i)
            
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) <= 1:
            return False
        i = 0
        sign = True
        while i != len(s):
            if s[i] == ')':
                return False
            elif s[i] == ']':
                return False
            elif s[i] == '}':
                return  False
            elif s[i] == '(':   
                sign = self.small(s, i)
            elif s[i] == '[':
                sign = self.middle(s, i)
            elif s[i] == '{':
                sign = self.big(s, i)
            else:
                sign = [True, i+1]
            i = sign[1]
            print sign

        return sign[0]
            
        

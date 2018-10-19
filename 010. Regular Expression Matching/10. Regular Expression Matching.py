class Solution(object):
    def re(self, sc, pc):
        '''
        :type sc: str of a single
        :type pc: str of a single
        :rtype: bool
        '''
        if sc == pc:
            return True
        elif pc == ".":
            return True
        else:
            return False
            
    def star(self, s, si, p, pi):
        '''
        :type s: str
        :type p: str
        :type si: num
        :type pi: num
        :rtype: List[bool, si, pi]
        '''
        if si+1 == len(s):
            return si+1, pi+1
        if self.re(s[si], s[si+1]):
            return si+1, pi
        else:
            return si+1, pi+1
            
    def star0(self, s, si, p, pi):
        '''
        :type s: str
        :type p: str
        :type si: num
        :type pi: num
        :rtype: List[bool, si, pi]
        '''
        if self.re(s[si], p[pi - 1]) == False:
            return si, pi+1

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        lens = len(s)
        lenp = len(p)
        si = 0
        pi = 0
        while (si < lens) and (pi < lenp):
            if self.re(s[si], p[pi]):
                si = si + 1
                pi = pi + 1
            elif p[pi] == "*":
                restmp = self.star(s, si, p, pi)
                si = restmp[0]
                pi = restmp[1]
            elif (pi+1) < lenp and (p[pi+1] == "*"):
                restmp = self.star0(s, si, p, pi)
                si = restmp[0]
                pi = restmp[1]
            else:
                break
        if (si != lens) or (pi != lenp):
            return False
        else:
            return True
            
        

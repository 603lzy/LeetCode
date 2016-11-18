class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort(reverse = False)
        s.sort(reverse = False)
        cnt = k = j = 0
        lens = len(s)
        leng = len(g)
        
        for i in xrange(leng):
            if k < lens:
                for j in xrange(k, lens):
                    if s[j] >= g[i]:
                        cnt += 1
                        k = j + 1
                        break
        return cnt

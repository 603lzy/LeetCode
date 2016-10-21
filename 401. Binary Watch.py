# be careful with the boundary
import itertools
class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        h = [1, 2, 4, 8]
        m = [1, 2, 4, 8, 16, 32]
        t = []
        for i in range(num + 1):
            Hcur = [str(sum(j)) for j in itertools.combinations(h, min(i, 4)) if sum(j) <= 11] # get the current hours 0-11
            Mcur = [str(sum(k)) for k in itertools.combinations(m, min(num-i, 6)) if sum(k) <= 59] # get the current minutes
            for j in Hcur:
                for k in Mcur:
                    t.append(j + ":" + k.zfill(2)) # automatically change '0' -> '00'

        return t
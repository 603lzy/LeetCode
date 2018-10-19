class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        :https://discuss.leetcode.com/topic/28438/python-10-lines-solution
        """
        v1 = [int(v) for v in version1.split(".")]
        v2 = [int(v) for v in version2.split(".")]
        lenv1 = len(v1)
        lenv2 = len(v2)
        endi = max(lenv1, lenv2)
        for i in xrange(endi):
            vi1 = v1[i] if i < lenv1 else 0
            vi2 = v2[i] if i < lenv2 else 0
            if vi1 > vi2:
                return 1
            elif vi1 < vi2:
                return -1
        return 0

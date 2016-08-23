class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        :ref：https://discuss.leetcode.com/topic/47947/python-code-difference-between-array-and-set
        :get all the seq more than once
        """
        lens = len(s)
        rec = set()
        ret = []
        endi = lens - 9
        for i in range(endi):
            si = s[i:i+10]
            if si not in rec:
                rec.add(si)
            else:
                if si not in ret:
                    ret.append(si)
        return ret

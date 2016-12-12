class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        A = []
        if not nums:
            return A
        s = e = nums[0] # s: start of current range;e: end of current range
        for i in range(len(nums) - 1):
            if nums[i + 1] != (nums[i] + 1):
                if e == s:
                    A.append("%d" % s)
                else:
                    A.append("%d->%d" % (s, e))
                s = nums[i + 1]
            e = nums[i + 1]
        if s == e:
            A.append("%d" % nums[-1])
        else:
            A.append("%d->%d" % (s, nums[-1]))
        return A

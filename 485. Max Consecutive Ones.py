class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt, maxcnt = 0, 0 # maxcnt save the max consecutive1s
        for i in nums:
            cnt += 1
            cnt *= i # if i = 0 then cnt = 0
            maxcnt = max(cnt, maxcnt) # update maxcnt
        return max(cnt, maxcnt) #incase the last is longest cons1s.

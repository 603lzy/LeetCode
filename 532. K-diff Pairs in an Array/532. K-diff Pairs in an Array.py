class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        cnt = 0
        if k == 0:
            num, cnt = set(nums), 0
            lens, lenn = len(nums), len(num)
            if lenn != lens:  # there are duplicate in the array
                for i in num:
                    if nums.count(i) > 1:
                        cnt += 1
        elif k > 0:
            num = set(nums)
            lenn, num, cnt = len(num), list(num), 0
            num.sort()
            for i in xrange(lenn - 1): # use two pointers to count
                for j in xrange(i + 1, lenn):
                    if num[j] - num[i] == k:
                        cnt += 1
                        break
                    elif num[j] - num[i] > k:
                        break
        return cnt # k < 0 

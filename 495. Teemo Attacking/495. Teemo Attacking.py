class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        if timeSeries == []:
            return 0
        cnt = duration #the last one
        for i in xrange(len(timeSeries) - 1):
            if timeSeries[i] + duration < timeSeries[i + 1]:
                cnt += duration
            else:
                cnt += (timeSeries[i + 1] - timeSeries[i])
        return cnt

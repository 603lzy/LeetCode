class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        https://discuss.leetcode.com/topic/71429/java-easy-solution
        """
        radius = 0
        houses.sort()
        heaters.sort()
        lenhouse = len(houses)
        lenheat = len(heaters)
        i = j = 0
        while i < lenhouse:
            if houses[i] <= heaters[j]: # if house is Located before heater j.
                if not j:
                    radius = max(radius, heaters[j] - houses[i])
                    i += 1
                    continue
            else:
                while j != lenheat - 1 and heaters[j] < houses[i]:
                    j += 1
                if not j or heaters[j] < houses[i]:
                    radius = max(radius, houses[i] - heaters[j])
                    i += 1
                    continue
            dist = min(houses[i] - heaters[j - 1], heaters[j] - houses[i])
            radius = max(radius, dist)
            i += 1
        return radius

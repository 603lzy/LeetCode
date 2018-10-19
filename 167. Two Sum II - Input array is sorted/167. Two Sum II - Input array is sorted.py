class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        # two pointers and greedy algorithm
        :ref: http://blog.csdn.net/xudli/article/details/42290269
        """
        j = len(numbers) - 1
        i = 0
        ni = numbers[i]
        nj = numbers[j]
        while True:
            x = ni + nj
            if x > target:
                j -= 1
                nj = numbers[j]
            elif x < target:
                i += 1
                ni = numbers[i]
            else:
                return [i+1, j+1]
            
        

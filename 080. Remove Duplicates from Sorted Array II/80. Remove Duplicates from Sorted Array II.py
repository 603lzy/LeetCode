class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        http://blog.csdn.net/feliciafay/article/details/42603555
        """
        lenn = len(nums)
        if lenn <= 2:
            return lenn
        else:
            i = 0
            j = 0
            while i < lenn-1:
                if (nums[i] != nums[i+1]):  
                    nums[j] = nums[i]
                    i += 1
                    j += 1
                else:
                    tmp = nums[i]
                    nums[j] = tmp
                    nums[j+1] = tmp
                    j += 2
                    while (nums[i] == tmp) and (i < lenn - 1):
                        i += 1
            if nums[j-1] != nums[-1]:
                nums[j] = nums[-1]
                return j+1
            else:
                return j
            

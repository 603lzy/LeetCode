# @param {Integer[]} nums
# @return {Integer}
def single_non_duplicate(nums)
    i = 0
    numsSize = nums.size - 1
    while i < numsSize
        if nums[i] != nums[i + 1]
            return nums[i]
        else
            i = i + 2
        end
    end
    return nums.last
end

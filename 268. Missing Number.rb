# @param {Integer[]} nums
# @return {Integer}
def missing_number(nums)
    nums = nums.sort
    for i in 0.. nums.size
        if nums[i] != i 
            return i
        end
    end
    return nums.size
end

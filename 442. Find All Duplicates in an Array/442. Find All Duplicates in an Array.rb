# @param {Integer[]} nums
# @return {Integer[]}
def find_duplicates(nums)
    nums = nums.sort
    repnum = []
    for i in 0..nums.size-1
        if nums[i] == nums[i + 1]
            repnum.push(nums[i])
        end
    end
    return repnum
end

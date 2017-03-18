# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer[]}
def two_sum(nums, target)
    idx = [1, 1]
    i = 0
    while i < nums.length - 1
        j = i + 1
        while j < nums.length
            if nums[i] + nums[j] == target
                idx[0] = i
                idx[1] = j
                return idx
            end
            j += 1
        end
        i += 1
    end
    return idx
end

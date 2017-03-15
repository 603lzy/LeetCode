# @param {Integer[]} nums
# @return {Integer}
def find_max_consecutive_ones(nums)
    cnt = 0
    maxcnt = 0
    for i in 0..nums.size
        if nums[i] == 1
            cnt = cnt + 1
        else
            maxcnt = (maxcnt > cnt ? maxcnt : cnt)
            cnt = 0
        end
    end
    return maxcnt > cnt ? maxcnt : cnt
end

# @param {Integer[]} nums
# @return {Void} Do not return anything, modify nums in-place instead.
def move_zeroes(nums)
    l = nums.length
    nums.delete 0
    while nums.length < l 
        nums.push 0
    end
    return
end

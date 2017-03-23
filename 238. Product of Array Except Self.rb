# @param {Integer[]} nums
# @return {Integer[]}
def product_except_self(nums)
    l = nums.size
    prods = [1] * l
    prodl = prodr = 1
    1.upto(l - 1) { |i|
        prods[i] *= prodl *= nums[i - 1]
        prods[~i] *= prodr *= nums[-i]
    }
    return prods
end

/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function(nums) {
    var l = nums.length
    var prods = new Array(l)
    for (var i = 0, prod = 1; i < l; i++) {
        prods[i] = prod
        prod *= nums[i]
    }
    for (var i = l - 1, prod = 1; i >= 0; i--) {
        prods[i] *= prod
        prod *= nums[i]
    }
    return prods
};

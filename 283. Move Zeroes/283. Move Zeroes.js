/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var moveZeroes = function(nums) {
    var j = 0
    var cnt = 0
    for (var i = 0; i < nums.length; i++) {
        if (nums[i] != 0) {
            nums[j++] = nums[i]
        } else {
            cnt++
        }
    }
    while (cnt > 0) {
        nums[nums.length - cnt--] = 0
    }
    return
};

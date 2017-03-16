/**
 * @param {number[]} nums
 * @return {number}
 */
function compare(a, b) {
    return a - b;
}

var missingNumber = function(nums) {
    nums.sort(compare);
    for (var i = 0; i < nums.length; i++) {
        if (nums[i] != i) {
            return i;
        }
    }
    return nums.length;
};

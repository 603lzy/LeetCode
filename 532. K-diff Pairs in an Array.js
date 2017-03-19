/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var findPairs = function(nums, k) {
    nums.sort(function(a, b) {return a - b})
    var cnt = 0, tmp = nums[0] - 1
    if (k == 0) {
        for (var i = 0; i < nums.length - 1; tmp = nums[i], i++) {
            if (nums[i] == tmp) {
                continue
            }
            if (nums[i + 1] == nums[i]) {
                cnt++
            }
        }
    }
    if (k > 0) {
        for (i = 0, tmp; i < nums.length - 1; tmp = nums[i], i++) {
            if (nums[i] == tmp) {
                continue
            }
            for (var j = 0; j < nums.length; j++) {
                if (nums[j] - nums[i] < k) {
                    continue
                }
                if (nums[j] - nums[i] == k) {
                    cnt++
                    break
                }
                if (nums[j] - nums[i] > k) {
                    break
                }
            }
        }
    }
    return cnt
};

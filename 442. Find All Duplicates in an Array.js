/**
 * @param {number[]} nums
 * @return {number[]}
 */
var findDuplicates = function(nums) {
    nums.sort();
    var repnum = [];
    var j = 0;
    for (var i = 0; i < nums.length - 1; i++) {
        if (nums[i] == nums[i + 1]) {
            repnum[j++] = nums[i];
        }
    }
    return repnum;
};

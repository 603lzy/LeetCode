/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    var idx = new Array(2)
    for (var i = 0; i < nums.length - 1; i++){
        for (var j = i + 1; j < nums.length; j++){
            if (nums[i] + nums[j] == target){
                idx[0] = i
                idx[1] = j
                return idx
            }
        }
    }
    return idx
};

/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNonDuplicate = function(nums) {
    for (var i = 0; i <  nums.length - 2; i += 2){
        if (nums[i] != nums[i + 1])
            return nums[i];
    }
    return nums.pop();
};

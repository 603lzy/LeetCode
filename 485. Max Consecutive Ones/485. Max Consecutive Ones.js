/**
 * @param {number[]} nums
 * @return {number}
 */
var findMaxConsecutiveOnes = function(nums) {
    var cnt = 0, maxcnt = 0, l = nums.length;
    for (var i = 0; i < l; i++){
        if (nums[i] == 1)
            cnt++;
        else{
            maxcnt = (maxcnt > cnt ? maxcnt : cnt);
            cnt = 0;
        }
    }
    return maxcnt > cnt ? maxcnt : cnt;
};

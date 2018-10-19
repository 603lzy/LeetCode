class Solution {
    func moveZeroes(_ nums: inout [Int]) {
        var j = 0
        var cnt = 0
        for num in nums {
            if num != 0 {
                nums[j] = num
                j += 1
            } else {
                cnt += 1
            }
        }
        if (cnt > 0){
           for i in 1 ... cnt{
                nums[nums.count - i] = 0
            } 
        }
        return
    }
}

class Solution {
    func missingNumber(_ nums: [Int]) -> Int {
        var num = nums
        num.sort()
        var i = 0
        while i < num.count{ 
            if num[i] != i {
                return i
            }
            else {
                i += 1
            }
        }
        return nums.count
    }
}

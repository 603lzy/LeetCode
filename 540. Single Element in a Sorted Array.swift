class Solution {
    func singleNonDuplicate(_ nums: [Int]) -> Int {
        var i = 0
        var lengthofArray = nums.count - 1 // get the length of the array
        while i < lengthofArray {
            if nums[i] != nums[i + 1]{
                return nums[i]
            } else {
                i += 2
            }
        }
        return nums[lengthofArray]
    }
}

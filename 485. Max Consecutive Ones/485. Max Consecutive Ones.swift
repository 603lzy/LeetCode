class Solution {
    func findMaxConsecutiveOnes(_ nums: [Int]) -> Int {
        var lengthofArray = nums.count
        var cnt = 0, maxcnt = 0, i = 0
        while i < lengthofArray {
            if nums[i] == 1 {
                cnt += 1
            }
            else {
                maxcnt = maxcnt > cnt ? maxcnt : cnt
                cnt = 0
            }
            i += 1
        }
        return maxcnt > cnt ? maxcnt : cnt
    }
}

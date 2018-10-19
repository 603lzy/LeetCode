class Solution {
    func twoSum(_ nums: [Int], _ target: Int) -> [Int] {
        var idx: [Int] = [1, 3]
        var i = 0, j = 1
        while i < nums.count - 1 {
            j = i + 1
            while j < nums.count {
                if nums[i] + nums[j] == target {
                    idx[0] = i
                    idx[1] = j
                    return idx
                }
                j += 1
            }
            i += 1
        }
        return idx
    }
}

func twoSum(nums []int, target int) []int {
    var idx = []int{1, 1}
    for i := 0; i < len(nums) - 1; i++ {
        for j := i + 1; j < len(nums); j++ {
            if nums[i] + nums[j] == target {
                idx[0] = i
                idx[1] = j
                return idx
            }
        }
    }
    return idx
}

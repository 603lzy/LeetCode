func singleNonDuplicate(nums []int) int {
    var l = len(nums)
    for i := 0; i < l - 2; i = i + 2 {
        if nums[i] != nums[i + 1] {
            return nums[i]
        }
    }
    return nums[l - 1]
}

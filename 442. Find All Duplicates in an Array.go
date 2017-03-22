func findDuplicates(nums []int) []int {
    var rep []int
    sort.Ints(nums)
    for i := 0; i < len(nums) - 1; i++ {
        if nums[i] == nums[i + 1] {
            rep = append(rep, nums[i])
        }
    }
    return rep
}

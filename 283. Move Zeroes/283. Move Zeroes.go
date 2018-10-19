func moveZeroes(nums []int)  {
    var cnt = 0
    var j = 0
    for i := 0; i < len(nums); i++ {
        if nums[i] != 0 {
            nums[j] = nums[i]
            j++
        } else {
            cnt++
        }
    }
    for ; cnt > 0; cnt-- {
        nums[len(nums) - cnt] = 0
    }
    return
}

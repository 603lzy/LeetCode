func findMaxConsecutiveOnes(nums []int) int {
    var cnt = 0
    var maxcnt = 0
    var l = len(nums)
    for i := 0; i < l; i++ {
        if nums[i] == 1 {
            cnt++
        } else {
            if cnt > maxcnt {
                maxcnt = cnt
            }
            cnt = 0
        }
    }
    if cnt > maxcnt {
        maxcnt = cnt
    }
    return maxcnt
}

func findPoisonedDuration(timeSeries []int, duration int) int {
    if len(timeSeries) == 0 {
        return 0
    }
    var cnt = duration
    for i := 0; i < len(timeSeries) - 1; i++ {
        if timeSeries[i] + duration < timeSeries[i + 1] {
            cnt += duration
        } else {
            cnt += (timeSeries[i + 1] - timeSeries[i])
        }
    }
    return cnt
}

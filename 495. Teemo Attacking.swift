class Solution {
    func findPoisonedDuration(_ timeSeries: [Int], _ duration: Int) -> Int {
        var i = 0, l = timeSeries.count - 1, cnt = duration
        if l == -1 {
            return 0
        }
        while i < l {
            if timeSeries[i] + duration < timeSeries[i + 1] {
                cnt += duration
            } else {
                cnt += (timeSeries[i + 1] - timeSeries[i])
            }
            i += 1
        }
        return cnt
    }
}

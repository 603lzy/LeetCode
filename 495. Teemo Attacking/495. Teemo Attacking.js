/**
 * @param {number[]} timeSeries
 * @param {number} duration
 * @return {number}
 */
var findPoisonedDuration = function(timeSeries, duration) {
    var cnt = duration
    var l = timeSeries.length - 1
    if (l == -1) {
        return 0
    }
    for (var i = 0; i < l; i++) {
        if (timeSeries[i] + duration < timeSeries[i + 1]) {
            cnt += duration
        } else {
            cnt += (timeSeries[i + 1] - timeSeries[i])
        }
    }
    return cnt
};

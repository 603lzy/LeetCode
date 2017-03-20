public class Solution {
    public int FindPoisonedDuration(int[] timeSeries, int duration) {
        int cnt = duration, l = timeSeries.Length - 1;
        if (l == -1) {
            return 0;
        }
        for (int i = 0; i < l; i++) {
            if (timeSeries[i] + duration < timeSeries[i + 1]) {
                cnt += duration;
            } else {
                cnt += (timeSeries[i + 1] - timeSeries[i]);
            }
        }
        return cnt;
    }
}

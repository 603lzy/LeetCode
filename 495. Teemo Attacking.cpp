class Solution {
public:
    int findPoisonedDuration(vector<int>& timeSeries, int duration) {
        if (timeSeries.empty()) {
            return 0;
        }
        int cnt = duration;
        for (int i = 0; i < timeSeries.size() - 1; i++) {
            if (timeSeries[i] + duration < timeSeries[i + 1]) {
                cnt += duration;
            } else {
                cnt += (timeSeries[i + 1] - timeSeries[i]);
            }
        }
        return cnt;
    }
};

int findPoisonedDuration(int* timeSeries, int timeSeriesSize, int duration) {
    if (timeSeriesSize == 0) {
        return 0;
    }
    int cnt = duration;
    for (int i = 0; i < timeSeriesSize - 1; i++) {
        if (timeSeries[i] + duration < timeSeries[i + 1]) {
            cnt += duration;
        } else {
            cnt += (timeSeries[i + 1] - timeSeries[i]);
        }
    }
    return cnt;
}

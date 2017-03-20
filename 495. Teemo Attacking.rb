# @param {Integer[]} time_series
# @param {Integer} duration
# @return {Integer}
def find_poisoned_duration(time_series, duration)
    cnt = duration
    l = time_series.length - 1
    i = 0
    if l == -1
        return 0
    end
    while i < l
        if time_series[i] + duration < time_series[i + 1]
            cnt += duration
        else
            cnt += (time_series[i + 1] - time_series[i])
        end
        i += 1
    end
    return cnt
end

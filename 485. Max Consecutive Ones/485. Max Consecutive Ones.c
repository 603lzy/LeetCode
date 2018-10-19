int findMaxConsecutiveOnes(int* nums, int numsSize) {
    int cnt = 0, maxcnt = 0, i = 0;
    for (i = 0; i < numsSize; i++)
        if (nums[i] == 1)
            cnt++;
        else{
            maxcnt = (maxcnt > cnt ? maxcnt : cnt);
            cnt = 0;
        }
    return maxcnt > cnt ? maxcnt : cnt;
}

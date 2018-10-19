int maxSubArray(int* nums, int numsSize) {
    int s1 = 0, s2 = 0;
    int i;
    int maxnums = nums[0];
    
    for (i = 0; i < numsSize; i++){
        if (*(nums+i) + s1 < 0)
            s1 = 0;
        else
            s1 = *(nums+i) + s1;
        if (s1 > s2)
            s2 = s1;
        if (maxnums < *(nums+i))
            maxnums = *(nums+i);
    }
    if (s2 == 0)
        return maxnums;
    else
        return s2;
}

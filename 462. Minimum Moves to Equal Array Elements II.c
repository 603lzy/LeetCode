int cmp(const void *a, const void *b){
    return (*(int *)b - *(int *)a);
}
//https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/
int minMoves2(int* nums, int numsSize) {
    int i, median, ret = 0;
    if (numsSize != 0){
        qsort(nums, numsSize, sizeof(nums[0]), cmp);
        median = (numsSize % 2 == 0) ? nums[numsSize/2] : nums[(numsSize - 1) / 2];
        for (i = 0; i < numsSize; i++)
            ret += abs(nums[i] - median);
    }
    return ret;
}

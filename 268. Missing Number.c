int compInc(const void *a, const void *b) {
    return *(int *)a - *(int *)b;    
}

int missingNumber(int* nums, int numsSize) {
    qsort(nums, numsSize, sizeof(nums[0]), compInc);
    int i = 0;
    for (i = 0; i < numsSize; i++) {
        if (nums[i] != i){
            return i;
        }
    }
    return numsSize;  // final value is numsSize
}

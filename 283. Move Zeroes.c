void moveZeroes(int* nums, int numsSize) {
    // use two pointers
    int i = 0, j = 0, cnt = 0;
    while (i < numsSize) {
        if (nums[i] != 0) {
            nums[j++] = nums[i++]; // copy number
        } else {
            i++;
            cnt++;
        }
    }
    i = 0;
    while (i < cnt) {
        nums[numsSize - i - 1] = 0;
        i++;
    }
    return;
}

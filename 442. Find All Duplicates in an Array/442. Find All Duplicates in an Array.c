/**
 * Return an array of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */
int compInc(const void *a, const void *b) {
    return *(int*)a - *(int*)b;
}

int* findDuplicates(int* nums, int numsSize, int* returnSize) {
    qsort(nums, numsSize, sizeof(nums[0]), compInc);
    int* disnum = malloc(sizeof(int) * numsSize);
    int i = 0, j = 0, num = 1, cnt = 0;
    for (i = 0; i < numsSize - 1; i++) {
        if (nums[i] == nums[i + 1]) {
            *(disnum + j) = nums[i];
            j++;
        }
    }
    *returnSize = j;
    return disnum;
}

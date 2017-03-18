int cmp(const void *i, const void *j) {
    return (*(int *)i - *(int *)j);
}

int findPairs(int* nums, int numsSize, int k) {
    qsort(nums, numsSize, sizeof(nums[0]), cmp); //sort the array
    int cnt = 0, tmp = nums[0] - 1;
    if (k == 0) {
        for (int i = 0; i < numsSize - 1; tmp = nums[i], i++) {
            if (nums[i] == tmp) {
                continue;  // this number has been counted
            }
            if (nums[i + 1] == nums[i]) {
                cnt++;
            }
        }
    }
    if (k > 0){
        for (int i = 0; i < numsSize - 1; tmp = nums[i], i++) {
            if (tmp == nums[i]) {
                continue;
            }
            for (int j = i + 1; j < numsSize; j++) {
                if (nums[j] - nums[i] < k) {
                    continue;
                }
                if (nums[j] - nums[i] == k) {
                    cnt++;
                    break;
                }
                if (nums[j] - nums[i] > k) {
                    break;
                }
            }
        }
    }
    return cnt; // include k < 0
}

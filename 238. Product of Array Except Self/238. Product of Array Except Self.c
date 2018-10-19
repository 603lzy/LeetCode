/**
 * Return an array of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* productExceptSelf(int* nums, int numsSize, int* returnSize) {
    int* prods = (int *)malloc(sizeof(int) * numsSize);
    int i = 0, prod;
    // calculate the products by two sides
    for (i = 0, prod = 1; i < numsSize; i++) {
        prods[i] = prod;
        prod *= nums[i];
    }
    for (i = numsSize - 1, prod = 1; i >= 0; i--) {
        prods[i] *= prod;
        prod *= nums[i];
    }
    *returnSize = numsSize;
    return prods;
}

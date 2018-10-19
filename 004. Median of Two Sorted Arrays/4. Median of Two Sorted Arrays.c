int compInc(const void *a, const void *b) {  
    return *(int *)a - *(int *)b;  
}  

double findMedianSortedArrays(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    int* nums = (int *) malloc(sizeof(int) * (nums1Size + nums2Size)), i;
    for (i = 0; i < nums1Size; i++)
        nums[i] = nums1[i];  // save nums1 to nums
    for (; i < nums1Size + nums2Size; i++)
        nums[i] = nums2[i - nums1Size];  // save nums2 to nums
    qsort(nums, nums1Size + nums2Size, sizeof(nums[0]), compInc);  // sort nums
    return (nums1Size + nums2Size) % 2 ? (double)(nums[(nums1Size + nums2Size - 1)/2]) : (double)(nums[(nums1Size + nums2Size)/2] + nums[(nums1Size + nums2Size)/2-1])/2.0;
}

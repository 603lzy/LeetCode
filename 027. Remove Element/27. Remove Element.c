int removeElement(int* nums, int numsSize, int val) {
    int *p = nums, i = -1, orinumsSize = numsSize; // two pointers point to the array
    while (++i < orinumsSize)
        if (*(nums + i) != val)
            *p++ = *(nums + i);
        else 
            numsSize--;
    return numsSize;
}

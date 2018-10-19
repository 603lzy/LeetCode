int singleNonDuplicate(int* nums, int numsSize) {
    int i = 0;
    while (i < numsSize - 2){
        if (*(nums + i) !=  *(nums + i + 1)){
            return *(nums + i);
        }else {
            i += 2;
        }
    }
    return *(nums + numsSize - 1);
}

int minMoves(int* nums, int numsSize) {
    int i = 0, sum = 0, min = nums[0];
    while(i < numsSize){
        sum += nums[i];
        min = nums[i] < min ? nums[i] : min;
        
    }
    return sum - min * numsSize;
}

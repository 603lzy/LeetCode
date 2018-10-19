public class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] idx = new int[2];
        int i, j;
        for (i = 0; i < nums.length - 1; i++){
            for (j = i + 1; j < nums.length; j++){
                if (nums[i] + nums[j] == target){
                    idx[0] = i;
                    idx[1] = j;
                    return idx;
                }
            }
        }
        return idx;
    }
}

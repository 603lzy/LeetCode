public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        int[] idx = new int[2];
        int i = 0, j;
        for (i = 0; i < nums.Length - 1; i++){
            for (j = i + 1; j < nums.Length; j++){
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

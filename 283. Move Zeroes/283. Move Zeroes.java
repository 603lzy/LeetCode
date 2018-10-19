public class Solution {
    public void moveZeroes(int[] nums) {
        int j = 0, cnt = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != 0) {
                nums[j++] = nums[i];
            } else {
                cnt++;
            }
        }
        if (cnt > 0){
            Arrays.fill(nums, nums.length - cnt, nums.length, 0);
        }
        return;
    }
}

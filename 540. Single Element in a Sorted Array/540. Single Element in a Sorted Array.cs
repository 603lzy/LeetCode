public class Solution {
    public int SingleNonDuplicate(int[] nums) {
        for (int i = 0; i < nums.Length - 2; i += 2){
            if (nums[i] != nums[i + 1])
                return nums[i];
        }
        return nums[nums.Length - 1];
    }
}

public class Solution {
    public void MoveZeroes(int[] nums) {
        int j = 0, cnt = 0;
        foreach (int num in nums) {
            if (num != 0) {
                nums[j++] = num;
            } else {
                cnt++;
            }
        }
        while (cnt > 0) {
            nums[nums.Length - cnt--] = 0;
        }
        return;
    }
}

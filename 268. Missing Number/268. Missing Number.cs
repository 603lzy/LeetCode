public class Solution {
    public int MissingNumber(int[] nums) {
        Array.Sort(nums); // sort the array
        for (int i = 0; i < nums.Length; i++) {
            if (nums[i] != i) {
                return i;
            }
        }
        return nums.Length;
    }
}

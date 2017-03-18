public class Solution {
    public int FindPairs(int[] nums, int k) {
        if (nums.Length == 0) {
            return 0;
        }
        Array.Sort(nums);
        int cnt = 0, tmp = nums[0] - 1;
        if (k == 0) {
            for (int i = 0; i < nums.Length - 1; tmp = nums[i], i++) {
                if (nums[i] == tmp) {
                    continue;
                }
                if (nums[i + 1] == nums[i]) {
                    cnt++;
                }
            }
        }
        if (k > 0) {
            for (int i = 0; i < nums.Length - 1; tmp = nums[i], i++) {
                if (tmp == nums[i]) {
                    continue;
                }
                for (int j = i + 1; j < nums.Length; j++) {
                    if (nums[j] - nums[i] < k) {
                        continue;
                    }
                    if (nums[j] - nums[i] == k) {
                        cnt++;
                        break;
                    }
                    if (nums[j] - nums[i] > k) {
                        break;
                    }
                }
            }
        }
        return cnt;
    }
}

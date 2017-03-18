public class Solution {
    public int findPairs(int[] nums, int k) {
        if (nums.length == 0) {
            return 0;
        }
        Arrays.sort(nums);
        int cnt = 0, tmp = nums[0] - 1;
        if (k == 0) {
            for (int i = 0; i < nums.length - 1; tmp = nums[i], i++) {
                if (nums[i] == tmp) {
                    continue;
                }
                if (nums[i + 1] == nums[i]) {
                    cnt++;
                }
            }
        }
        if (k > 0) {
            for (int i = 0; i < nums.length - 1; tmp = nums[i], i++){
                if (tmp == nums[i]) {
                    continue;
                }
                for (int j = i + 1; j < nums.length; j++) {
                    if (tmp == nums[i]) {
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

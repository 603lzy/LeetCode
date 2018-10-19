public class Solution {
    public List<Integer> findDuplicates(int[] nums) {
        Arrays.sort(nums);
        List<Integer> repnums = new ArrayList<Integer>();
        int l = nums.length - 1;
        for (int i = 0; i < l; i++) {
            if (nums[i] == nums[i + 1]) {
                repnums.add(nums[i]);
            }
        }
        return repnums;
    }
}

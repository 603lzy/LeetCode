public class Solution {
    public int FindMaxConsecutiveOnes(int[] nums) {
        int cnt = 0, maxcnt = 0, i = 0, l = nums.Length;
        for (i = 0; i < l; i++){
            if (nums[i] == 1)
                cnt++;
            else{
                maxcnt = (maxcnt > cnt ? maxcnt : cnt);
                cnt = 0;
            }
        }
        return maxcnt > cnt ? maxcnt : cnt;
    }
}

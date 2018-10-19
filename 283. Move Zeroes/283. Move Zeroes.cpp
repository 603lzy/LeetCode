class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int i = -1, j = 0, cnt = 0;
        while (++i < nums.size()) {
            if (nums[i] != 0) {
                nums[j++] = nums[i];
            } else {
                cnt++;
            }
        }
        while (cnt > 0) {
            nums[nums.size() - cnt--] = 0;
        }
        return;
    }
};

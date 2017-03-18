class Solution {
public:
    int findPairs(vector<int>& nums, int k) {
        if (nums.empty()) {
            return 0;
        }
        sort(nums.begin(), nums.end()); // sort the array
        int cnt = 0, tmp = nums[0] - 1;
        if (k == 0) {
            for (int i = 0; i < nums.size(); tmp = nums[i], i++) {
                if (nums[i] == tmp) {
                    continue;
                }
                if (nums[i + 1] == nums[i]) {
                    cnt++;
                }
            }
        }
        if (k > 0) {
            for (int i = 0; i < nums.size() - 1; tmp = nums[i], i++) {
                if (nums[i] == tmp) {
                    continue;
                }
                for (int j = i + 1; j < nums.size(); j++) {
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
        return cnt; // include k < 0
    }
};

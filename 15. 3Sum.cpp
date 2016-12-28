class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<vector<int>> idx;
        int numsLen = nums.size();
        for (int pl = 0; pl < numsLen; pl++){
            if (pl > 0 && nums[pl] == nums[pl - 1])
                continue;  // jump duplicate number from left
            int pm = pl + 1, pr = numsLen - 1;
            while (pm < pr){
                int sum = nums[pl] + nums[pm] + nums[pr];
                if (sum > 0)
                    pr--;  // get a smaller number
                else if (sum < 0)
                    pm++;  // get a bigger number
                else{
                    idx.push_back(vector<int> {nums[pl], nums[pm], nums[pr]});
                    while (pm + 1 < pr && nums[pm] == nums[pm + 1]) pm++;  // pass dup
                    while (pr - 1 < pm && nums[pr] == nums[pr - 1]) pr--;
                    pm++;
                    pr--;
                }
            }
        }
        return idx;
    }
};

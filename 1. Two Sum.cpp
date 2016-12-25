class Solution { 
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int i = 0, n = nums.size();
        unordered_map<int, int> idx; 
        while (i < n && idx.find(target - nums[i]) == idx.end()) { // find the other number and not same with the current number
            idx[nums[i++]] = i;
        }
    return {idx[target - nums[i]] - 1, i};
    }
};

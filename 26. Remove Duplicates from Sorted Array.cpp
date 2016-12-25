class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int i = 0, n = nums.size();
        for (int j = 1; j < n; j++)
            if (nums[i] != nums[j])
                nums[++i] = nums[j];
        return n <= 1 ? n : i + 1;
    }
};

class Solution {
public:
    int singleNonDuplicate(vector<int>& nums) {
        int i = 0;
        while (i < nums.size() - 2){
            if (nums[i] != nums[i + 1]){
                return nums[i];
            } else {
                i += 2;
            }
        }
        return nums.back();
    }
};

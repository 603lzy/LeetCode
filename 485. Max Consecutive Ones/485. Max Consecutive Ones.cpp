class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int i, cnt = 0, maxcnt = 0;
        for (i = 0; i < nums.size(); i++)
            if (nums[i] == 1){
                cnt++;
            } else {
                maxcnt = max(cnt, maxcnt);
                cnt = 0;
            }
        return max(cnt, maxcnt);
    }
};

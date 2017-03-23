class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int l = nums.size();
        vector<int> prods(l);
        for (int i = 0, prod = 1; i < l; i++) {
            prods[i] = prod;
            prod *= nums[i];
        }
        for (int i = l - 1, prod = 1; i >= 0; i--) {
            prods[i] *= prod;
            prod *= nums[i];
        }
        return prods;
    }
};

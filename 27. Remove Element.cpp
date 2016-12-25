class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        vector<int>::iterator n;
        for (n = nums.begin(); n != nums.end();)
            if (*n == val)
                n = nums.erase(n); // del the element and return to the next position of deleted element
            else
                n++;
        return nums.size();
    }
};

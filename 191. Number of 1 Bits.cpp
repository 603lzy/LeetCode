class Solution {
public:
    int hammingWeight(uint32_t n) {
        int cnt = 1; //cnt count of 1
        while (n > 1){
            cnt +=  (n % 2);
            n /= 2;
        }
        return cnt * n; // n = 0, return 0
    }
};
